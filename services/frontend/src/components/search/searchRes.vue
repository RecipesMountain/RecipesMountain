<template>
  <v-row align="center" justify="center">
      <v-col v-bind:key="recipe.id" v-for="recipe in recpies" align="center" justify="center" > 
        <RecpieSnippet class="ma-4" v-bind:recipe="recipe" />
      </v-col>
  </v-row>
</template>

<script>
import RecpieSnippet from "@/components/recipe/RecipeSnippet.vue"

export default {
    components: {RecpieSnippet},
    computed: {
        recpies() {
            return this.$store.getters["getRecipes"]
        }
    }
}
</script>

<style>

.recipe-card {
    max-height: 400px;
    max-width: 400px;
}

</style>