<template>
  <div id="addForm">
    <v-main id="addRecipe">
      <v-container fluid>
        <v-row justify="center">
          <v-col cols="10">
            <p class="text-h3 text-left">Add new recipe</p>
            <RecipeForm
              :isForEdit="false"
              :tags="allTags"
              :products="allProducts"
            />
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </div>
</template>

<script>
import RecipeForm from "../../components/recipe/Recipe-Form.vue";
export default {
  components: { RecipeForm },

  created: function () {
    this.$store.dispatch("actionGetTags");
    this.$store.dispatch("actionGetProducts");
  },
  computed: {
    allTags() {
      return this.$store.getters["allTags"];
    },
    allProducts() {
      return this.$store.getters["allProducts"];
    },
  },
};
</script>

<style scoped>
#addForm {
  background-image: linear-gradient(
    to bottom,
    #ffe6cf,
    #ffdfc9,
    #ffd8c3,
    #ffd1be,
    #ffcabb,
    #ffc2b5,
    #ffbbb0,
    #ffb3ab,
    #ffa9a1,
    #ff9e97,
    #ff948d,
    #ff8984
  );
}
</style>