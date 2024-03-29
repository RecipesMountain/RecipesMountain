<template>
  <div>
    <v-row align-content="start" class="flex-row-reverse">
      <v-col md="5" cols="12">
        <v-row>
          <div id="tags-short" class="mx-2">
            <v-chip-group column>
              <v-chip
                v-for="tag in shortTags"
                :key="tag.id"
                pill
                small
                color="#e0bd70"
                class="text-body-2 text-left px-2"
                :href="'/tags/' + tag.id"
              >
                {{ tag.name }}
              </v-chip>
              <v-btn icon @click="$vuetify.goTo('#tags')">
                <v-icon> mdi-dots-horizontal</v-icon>
              </v-btn>
            </v-chip-group>
          </div>
        </v-row>
        <v-row>
          <v-col cols="12">
            <p class="text-h4 text-left">{{ recipe.title }}</p>
          </v-col>
          <v-col cols="12">
            <p class="text-left text-body-1">{{ recipe.description }}</p>
          </v-col>
          <v-col  v-if="recipe.author != null" cols="12">
            <p class="text-left text-subtitle-2">
              Author: {{ recipe.author.full_name }}
            </p>
          </v-col>
        </v-row>
        <v-row class="flex-column">
          <div id="icon-wrap">
            <v-row justify="space-around" align="center">
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <v-icon size="50" v-if="recipeTimeHours < 2"
                      >mdi-clock-outline</v-icon
                    >
                    <v-icon size="50" v-else>mdi-clock-plus-outline</v-icon>
                    <span class="font-weight-bold">
                      <template v-if="recipeTimeHours < 1">
                        {{ recipeTimeHours * 60 }} min</template
                      >
                      <template v-else> {{ recipeTimeHours }} h</template>
                    </span>
                  </div>
                </template>
                <span class="font-weight-bold">Preparation time</span>
              </v-tooltip>
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <v-icon size="50">mdi-silverware</v-icon>
                    <span class="font-weight-bold">
                      <template v-if="recipeServings % 1 != 0">
                        {{ recipeServings - (recipeServings % 1) }}/{{
                          recipeServings - (recipeServings % 1) + 1
                        }}
                      </template>
                      <template v-else>{{ recipeServings }}</template>
                    </span>
                  </div>
                </template>
                <span class="font-weight-bold">Servings</span>
              </v-tooltip>
              <v-tooltip top class="mx-2">
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <v-icon size="40" class="mr-n2">mdi-fire </v-icon>
                    <span class="font-weight-bold">
                      {{recipe.calories}}kcal
                    </span>
                  </div>
                </template>
                <span class="font-weight-bold">Recipe calories</span>
              </v-tooltip>
              <div id="diff">
                <v-tooltip top class="mx-2">
                  <template v-slot:activator="{ on, attrs }">
                    <div v-bind="attrs" v-on="on">
                      <template v-if="recipeDifficultyLevel == 0">
                        <v-icon size="40" color="success"
                          >mdi-chili-mild</v-icon
                        >
                      </template>
                      <template v-else-if="recipeDifficultyLevel == 1">
                        <v-icon size="40" color="warning" class="mr-n6"
                          >mdi-chili-mild
                        </v-icon>
                        <v-icon size="40" color="warning"
                          >mdi-chili-mild
                        </v-icon>
                      </template>
                      <template v-else>
                        <v-icon size="40" color="error" class="mr-n6"
                          >mdi-chili-mild
                        </v-icon>
                        <v-icon size="40" color="error" class="mr-n6"
                          >mdi-chili-mild
                        </v-icon>
                        <v-icon size="40" color="error">mdi-chili-mild </v-icon>
                      </template>
                    </div>
                  </template>
                  <span class="font-weight-bold"
                    >Recipe difficulty:
                    <template v-if="recipeDifficultyLevel == 0">
                      Easy
                    </template>
                    <template v-else-if="recipeDifficultyLevel == 1">
                      Medium
                    </template>
                    <template v-else> Hard </template>
                  </span>
                </v-tooltip>
              </div>
            </v-row>
            <v-row>
              <v-col>
                <v-divider />
              </v-col>
            </v-row>
            <v-row justify="space-around" align="center">
              <v-rating
                empty-icon="mdi-star-outline"
                full-icon="mdi-star"
                half-icon="mdi-star-half-full"
                hover
                length="5"
                size="40"
                half-increments
                v-model="rating"
                color="secondary"
                background-color="secondary"
                @input="submitRating"
              ></v-rating>
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <v-btn icon @click="()=>{printRecipe();}" plain>
                      <v-icon size="50">mdi-printer</v-icon>
                    </v-btn>
                  </div>
                </template>
                <span class="font-weight-bold">Print</span>
              </v-tooltip>
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <v-btn
                      icon
                      :ripple="false"
                      plain
                      v-on:click="() =>{$vuetify.goTo('#comments'); showAddComment();}"
                    >
                      <v-icon size="50">mdi-comment-outline</v-icon>
                    </v-btn>
                  </div>
                </template>
                <span class="font-weight-bold">Leave comment</span>
              </v-tooltip>
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <v-btn icon :ripple="false" plain @click="likeOrUnlike">
                      <v-icon size="50" v-if="!isLiked">mdi-cards-heart-outline</v-icon>
                      <v-icon size="50" v-else>mdi-cards-heart</v-icon>
                    </v-btn>
                  </div>
                </template>
                <span class="font-weight-bold">Like recipe</span>
              </v-tooltip>
            </v-row>
          </div>
        </v-row>
      </v-col>
      <v-col md="7" cols="12">
        <RecipeImageCarousel :image="recipe.image"/>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import RecipeImageCarousel from "@/components/recipe/Recipe-ImageCarousel.vue";

export default {
  components: { RecipeImageCarousel },
  props: ["recipe", "isLiked", "showAddComment", "printRecipe", "submitRating"],
  computed: {
    shortTags() {

      if (this.recipe.tags.length > 4) {
        return this.recipe.tags.slice(0, 4);
      } else {
        return this.recipe.tags;
      }
    },
    recipeTimeHours() {
      return this.recipe.time / 60;
    },
    recipeDifficultyLevel() {
      if (this.recipe.difficulty == "Easy") {
        return 0;
      } else if (this.recipe.difficulty == "Hard") {
        return 2;
      } else {
        return 1;
      }
    },
    recipeServings() {
      return this.recipe.servings / 2;
    },
    recipeId(){
      return this.recipe.id
    },
    rating: {
      get(){return this.recipe.rating / 10},
      set(e){return e}
    }
  },
  methods:{
    async likeOrUnlike(){
      await this.$store.dispatch("actionLikeUnlikeRecipe", this.recipeId);
    }
  }
};
</script>

<style>
</style>