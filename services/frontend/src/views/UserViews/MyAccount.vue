<template>
  <div>
    <v-parallax
      height="300"
      src="user-page-background.jpg"
    >
      <v-row
        align="center"
        justify="center"
      >
        <h1 class="text-h1">Your account</h1>
      </v-row>
    </v-parallax>
    <v-container>
      <div class="flex-row">
        <div class="flex-col-right">
          <v-avatar size="128" color="primary" class="text-h3">{{ initials }}</v-avatar>
        </div>
        <div class="flex-col-left">
          <span class="text-h2">{{ $store.getters.fullName }}</span>
          <br/>
          <a
              class="text--secondary text-decoration-none"
              :href="`mailto:${$store.getters.email}`"
          >{{ $store.getters.email }}</a>
        </div>
      </div>
      <div v-for="([title, name], i) in [['Your Favourites', 'favourite'], ['Authored by You', 'authored'], ['Commented by You', 'commented']]" :key="i">
        <v-row>
          <router-link
            class="text-h5 text-decoration-none grey--text text--darken-3 mt-8 mb-4 arrow-link"
            :to="`/explore/${name}`"
          >
            {{ title }} <v-icon class="grey--text text--darken-3 arrow">mdi-arrow-right</v-icon>
          </router-link>
        </v-row>
        <v-row>
          <div class="horiz-scroll">
            <RecipeSnippet
                class="card ma-4"
                v-for="(recipe, i) in $store.getters[`${name}Recipes`]"
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
import {getInitials} from "@/utils";

export default {
  name: 'User',
  components: {
    RecipeSnippet
  },
  created: function() {
    this.$store.dispatch("getFavouriteRecipes", { limit: 10 });
    this.$store.dispatch("getAuthoredRecipes", { limit: 10 });
    this.$store.dispatch("getCommentedRecipes", { limit: 10 });
  },
  computed: {
    initials: function() {
      return getInitials(this.$store.getters.fullName);
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

.flex-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 48px;
}

.flex-col-left {
  align-items: center;
  justify-content: flex-start;
  flex-direction: column;
}

.flex-col-right {
  align-items: center;
  justify-content: flex-end;
  flex-direction: column;
}
</style>