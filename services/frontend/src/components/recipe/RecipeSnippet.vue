<template>
  <v-card class="recipe-snippet" :to="`/recipes/${recipe.id}`">
    <v-img
      class="recipe-image"
      :src="recipe.image_url"
    ></v-img>
    <v-card-title>{{ recipe.title }}</v-card-title>
    <v-card-subtitle>{{ `${recipe.owner.first_name} ${recipe.owner.last_name}` }}</v-card-subtitle>
    <v-card-text>
      <v-row align="center" class="mx-0 my-0">
        <v-rating
          :value="recipe.rating"
          background-color="amber"
          color="amber"
          dense
          readonly
          half-increments
        ></v-rating>
        <span class="grey--text ms-4">{{ recipe.rating_count ? `(${recipe.rating_count})` : '' }}</span>
      </v-row>
      <span class="recipe-desc">{{ recipe.description }}</span>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "RecipeSnippet",
  props: {
    "recipe": Object
  },
};
</script>

<style scoped>
.recipe-snippet {
  text-align: left;
  max-width: 250px;
}
.recipe-image {
  max-height: 150px;
  max-width: 250px;
}
.recipe-desc {
  text-align: justify;
  margin-top: 16px;

  /* magical incantations to make the text cut off after 2 lines */
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
