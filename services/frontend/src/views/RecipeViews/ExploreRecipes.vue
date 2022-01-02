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

export default {
  name: "ExploreRecipes",
  components: {RecipeSnippet},
  created: function() {
    let sort = this.$route.params.sort;

    if (sort === "popular") {
      this.$store.dispatch("getPopularRecipes", { limit: 20 });
    } else if (sort === "best") {
      this.$store.dispatch("getBestRecipes", { limit: 20 });
    }
  },
  computed: {
    titleText: function() {
      let sort = this.$route.params.sort
      return sort.charAt(0).toUpperCase() + sort.substring(1) + " recipes";
    },
    recipes: function() {
      let sort = this.$route.params.sort
      return sort === "popular" ? this.$store.getters.popularRecipes : (sort === "best" ? this.$store.getters.bestRecipes : []);
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
