<template>
  <div>
    <v-row align-content="start">
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
            <p class="text-h4 text-left">{{ recipeTitle }}</p>
          </v-col>
          <v-col cols="12">
            <p class="text-left text-body-1">{{ recipeDesc }}</p>
          </v-col>
          <v-col cols="12">
            <p class="text-left text-subtitle-2">Author: {{ recipeAuthor.full_name }}</p>
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
                      {{ recipeCalories }}kcal
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
                v-model="recipeRating"
                color="secondary"
                background-color="secondary"
              ></v-rating>
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <v-btn icon plain>
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
                      v-on:click="$vuetify.goTo('#comments')"
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
                    <v-btn icon :ripple="false" plain>
                      <v-icon size="50">mdi-cards-heart-outline</v-icon>
                    </v-btn>
                    <!-- <v-icon size="50">mdi-cards-heart</v-icon> -->
                  </div>
                </template>
                <span class="font-weight-bold">Like recipe</span>
              </v-tooltip>
            </v-row>
          </div>
        </v-row>
      </v-col>
      <v-col md="7" cols="12">
        <RecipeImageCarousel />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import RecipeImageCarousel from "@/components/recipe/Recipe-ImageCarousel.vue";

export default {
  components: { RecipeImageCarousel },
  props: [],
  computed: {
    shortTags() {
      if (this.tags.length > 4) {
        return this.tags.slice(0, 4);
      } else {
        return this.tags;
      }
    },
    recipeTitle() {
      return this.$store.getters["title"];
    },
    recipeDesc() {
      return this.$store.getters["description"];
    },
    recipeAuthor() {
      return this.$store.getters["author"];
    },
    recipeAuthorId() {
      return this.$store.getters["authorId"];
    },
    recipeTime() {
      return this.$store.getters["time"];
    },
    recipeDifficulty() {
      return this.$store.getters["difficulty"];
    },
    recipeRating() {
      return this.$store.getters["rating"] / 2;
    },
    recipeRatingCount() {
      return this.$store.getters["ratingCount"];
    },
    recipeCalories() {
      return this.$store.getters["calories"];
    },
    recipeServings() {
      return this.$store.getters["servings"] / 2;
    },
    recipeTimeHours() {
      return this.recipeTime / 60;
    },
    recipeDifficultyLevel() {
      if (this.recipeDifficulty == "Easy") {
        return 0;
      } else if (this.recipeDifficulty == "Hard") {
        return 2;
      } else {
        return 1;
      }
    },
    tags() {
      return this.$store.getters["tags"];
    },
  },
};
</script>

<style>
</style>