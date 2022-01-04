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
    <RecipeInformations :recipe="recipe" />
    <v-row><v-col sm="12" class="d-none d-lg-block"> </v-col></v-row>
    <v-row v-for="stage in recipe.stages" :key="stage.name" class="flex-column">
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
    <v-row id="comments" justify="start" class="flex-column">
      <v-col class="">
        <v-divider />
        <div class="justify-space-between d-flex flex-row">
          <p class="text-left text-h4 ont-weight-bold">Comments:</p>
          <v-btn icon>
            <v-icon size="35">mdi-plus</v-icon>
          </v-btn>
        </div>
        //TODO comments
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
import RecipeInformations from "@/components/recipe/Recipe-Informations.vue";
import RecipeStage from "@/components/recipe/Recipe-Stage.vue";
export default {
  components: { RecipeInformations, RecipeStage },
  data() {
    return {
      comments: [],
    };
  },
  async mounted() {
    await this.$store.dispatch("actionGetRecipe", this.$route.params.id);
    await this.$store.dispatch("actionGetRecipeImg", this.$route.params.id);
    if (this.error) {
      console.log("error", "pushing");
      this.$router.push("/");
    }
  },
  computed: {
    recipe() {
      return this.$store.getters["recipe"];
    },
    error() {
      return this.$store.getters["errorStatus"];
    },
  },
};
</script>

<style>
</style>