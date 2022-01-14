<template>
  <v-sheet
    min-height="100vh"
    min-width="200px"
    shaped
    class="mx-4 pa-6"
    elevation="5"
    outlined
    color="transparent"
  >
  <div id="RecipeToPrint">
    <RecipeInformations :submitRating="submitRating" :printRecipe="printRecipe"  :showAddComment="showAddComment" :isLiked="isLiked" :recipe="recipe" />
    <v-row><v-col sm="12" class="d-none d-lg-block"> </v-col></v-row>
    <v-row v-for="(stage, index) in recipe.stages" :key="index" class="flex-column">
      <v-col>
        <RecipeStage
          :ingredients="stage.products"
          :stageContent="stage.content"
          :stageLabel="stage.name"
        />
      </v-col>
    </v-row>
    <v-row id="tags" justify="start" class="flex-column">
      <v-col class="">
        <v-divider />
        <p class="text-overline text-left mb-n3">Tags:</p>
        <v-chip-group column>
          <v-chip
            v-for="tag in recipe.tags"
            :key="tag.id"
            pill
            small
            color="#e0bd70"
            class="text-body-2 text-left px-2"
          >
            {{ tag.name }}
          </v-chip>
        </v-chip-group>
      </v-col>
    </v-row>
  </div>
    <v-row id="comments" justify="start" class="flex-column">
      <v-col class="">
        <v-divider />
        <div class="justify-space-between d-flex flex-row">
          <p class="text-left text-h4 ont-weight-bold">Comments:</p>
          <v-btn icon @click="showAddComment">
            <v-icon size="35">mdi-plus</v-icon>
          </v-btn>
        </div>
          <NewComment v-if="addComment" :commentAdded="commentAdded" :recpie_id="this.$route.params.id"/>
        <CommentList :deleteComment="deleteComment" :comments="comments"/>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
import RecipeInformations from "@/components/recipe/Recipe-Informations.vue";
import RecipeStage from "@/components/recipe/Recipe-Stage.vue";
import CommentList from "@/components/comment/CommentsList.vue";
import NewComment from "@/components/comment/CommentAdd.vue";
import { mover } from "@/mover";
import { api } from '@/api';
// import print from 'print-js'

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

export default {
  components: { RecipeInformations, RecipeStage, CommentList, NewComment },
  data() {
    return {
      comments: [],
      props: ["recipe"],
      addComment: false,
      justSubmitedRating: false,
    };
  },
  async mounted() {
    await this.$store.dispatch("actionGetRecipe", this.$route.params.id);
    await this.$store.dispatch("actionGetRecipeImg", this.$route.params.id);
    if (this.error) {
      mover.goToHome();
    }
    this.getComments();
  },
  computed: {
    recipe() {
      return this.$store.getters["recipe"];
    },
    error() {
      return this.$store.getters["errorStatus"];
    },
    isLiked(){
      return this.$store.getters["isLiked"]
    }
  },
  methods: {
    showAddComment() {
      if(this.$store.getters["isLoggedIn"])
        this.addComment = true
      else
        this.$store.commit("openSnackbar", "Must be logged in to add a comment");
    },
    commentAdded() {
      this.addComment = false
      this.getComments()
    },
    async printRecipe() {

        // wait for tooltip to disapear 
        await sleep(1000);

        const prtHtml = document.getElementById('RecipeToPrint').innerHTML;
        // Get all stylesheets HTML
        let stylesHtml = '';
        console.log(document.querySelectorAll('link[rel="stylesheet"], style'))
        for (const node of [...document.querySelectorAll('link[rel="stylesheet"], style')]) {
          stylesHtml += node.outerHTML;
        }

        console.log(prtHtml)
        console.log(stylesHtml)

        print({
          printable: 'RecipeToPrint',
          type: "html",
          style: stylesHtml,
          ignoreElements: ["comments", "image-carousel"]
        })

    },
    async submitRating(rating) {
      if(!this.justSubmitedRating) {
        if(this.$store.getters["isLoggedIn"]) {
          try {
            const response = await api.submitRating(this.$store.getters["token"], this.$route.params.id, rating*10)
            this.$store.commit("setRating", response.data)
            this.$store.commit("openSnackbar", "Rated succefuly!");
          } catch (e) {
            this.$store.commit("openSnackbar", "Something went wrong");
          }
        }
        else
          this.$store.commit("openSnackbar", "Must be logged in add a rating");
      }
      this.justSubmitedRating = !this.justSubmitedRating
    },
    async getComments() {
      try {
        const respone = await api.getComments(this.$route.params.id);
        this.comments = respone.data;
      } catch (e) {
        this.$store.commit("openSnackbar", "Error while getting comments");
      }
    },
    async deleteComment(comment) {
      try { 
        const respone = await api.deleteComment(this.$store.getters["token"],this.$route.params.id, comment.id)
        if(respone.data == true) {
          this.$store.commit("openSnackbar", "Comment deleted successfully");
        }
        this.getComments()
      } catch (e) {
        this.$store.commit("openSnackbar", "There has been en error while deleting comment");
      }
    }
  }
};
</script>

<style>
</style>