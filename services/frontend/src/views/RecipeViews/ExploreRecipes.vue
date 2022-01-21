<template>
  <v-container>
    <h2 class="text-h2 text-left my-8">{{ titleText }}</h2>
    <div class="overflow-list">
      <RecipeSnippet
          class="ma-4"
          v-for="(recipe, i) in recipes"
          :key="i"
          :recipe="recipe"
      ></RecipeSnippet>
    </div>
  </v-container>
</template>

<script>
import RecipeSnippet from "@/components/recipe/RecipeSnippet";
import {capitalize} from "@/utils";

export default {
  name: "ExploreRecipes",
  components: {RecipeSnippet},
  created: function() {
    let sort = this.$route.params.sort;
    let skip = this.$route.params.skip || 0;
    let limit = this.$route.params.limit || 100;

    this.$store.dispatch(`get${capitalize(sort)}Recipes`, { skip: skip, limit: limit });
  },
  computed: {
    titleText: function() {
      return capitalize(this.$route.params.sort) + " recipes";
    },
    recipes: function() {
      return this.$store.getters[`${this.$route.params.sort}Recipes`] || []
    }
  },
}
</script>

<style scoped>
.overflow-list {
  display: flex;
  flex-wrap: wrap;
}
</style>
