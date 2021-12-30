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
            <RecipeSnippet class="card ma-4" v-for="i in 10" :key="i" :recipe="exampleRecipe"></RecipeSnippet>
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
