<template>
  <div>
    <v-parallax
      height="300"
      src="main-page-background.jpg"
    >
      <v-row
        align="center"
        justify="center"
      >
        <h1 class="text-h1">Welcome to RecipeMountain</h1>
      </v-row>
    </v-parallax>
    <v-container>
      <div v-for="(name, i) in ['Popular', 'Best']" :key="i">
        <v-row>
          <router-link
            class="text-h5 text-decoration-none grey--text text--darken-3 mt-8 mb-4 arrow-link"
            :to="`/explore/${name.toLowerCase()}`"
          >
            {{ name }} <v-icon class="grey--text text--darken-3 arrow">mdi-arrow-right</v-icon>
          </router-link>
        </v-row>
        <v-row>
          <div class="horiz-scroll">
            <RecipeSnippet
                class="card ma-4"
                v-for="(recipe, i) in $store.getters[`${name.toLowerCase()}Recipes`]"
                :key="i"
                :recipe="recipe"
            ></RecipeSnippet>
          </div>
        </v-row>
      </div>
    </v-container>
  </div>
</template>

<script>
import RecipeSnippet from '@/components/recipe/RecipeSnippet.vue';

export default {
  name: 'Home',
  components: {
    RecipeSnippet
  },
  created: function() {
    this.$store.dispatch("getPopularRecipes", { limit: 10 });
    this.$store.dispatch("getBestRecipes", { limit: 10 });
  }
}
</script>

<style scoped>
.arrow-link > .arrow {
  margin-left: 0;
  transition: margin-left 300ms;
}

.arrow-link:hover > .arrow {
  margin-left: 8px;
}

.horiz-scroll {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
}

.horiz-scroll > .card {
  flex: 0 0 auto;
}
</style>
