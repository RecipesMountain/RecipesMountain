<template>
  <div id="editForm">
    <v-main>
      <v-container fluid>
        <v-row justify="center">
          <v-col cols="10">
            <p class="text-h3 text-left">Edit recipe - {{recipeTitle}}</p>
            <RecipeForm :isForEdit="true"/>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </div>
</template>

<script>
import RecipeForm from "@/components/recipe/Recipe-Form.vue";
export default {
  components: { RecipeForm },
  computed:{
      recipeTitle(){
          return this.$store.getters["title"]
      }
  }
};
</script>

<style scoped>
#editForm {
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