<template>
  <v-container>
    <h2 class="text-h2 text-left my-8">{{ titleText }}</h2>
    <div class="overflow-list">
      <RecipeSnippet class="ma-4" v-for="i in 20" :key="i" :recipe="exampleRecipe"></RecipeSnippet>
    </div>
  </v-container>
</template>

<script>
import RecipeSnippet from "@/components/recipe/RecipeSnippet";

export default {
  name: "ExploreRecipes",
  components: {RecipeSnippet},
  computed: {
    titleText: function() {
      return this.$route.params.sort.charAt(0).toUpperCase() + this.$route.params.sort.substring(1) + " recipes";
    }
  },
  data() {
    return {
      exampleRecipe: {
        id: "465038e4-2b5e-492b-83d7-61397fa483ad",
        image_url: "https://cdn.pixabay.com/photo/2017/09/16/19/21/salad-2756467_960_720.jpg",
        title: "Recipe",
        description: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam purus erat, ultricies in urna vitae, lobortis semper erat. Nullam vestibulum libero sed vulputate sodales. Maecenas at velit a sapien venenatis tempor a sit amet orci.`,
        rating: 3.5,
        rating_count: undefined,
        owner: {
          first_name: "John",
          last_name: "Smith"
        }
      }
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
