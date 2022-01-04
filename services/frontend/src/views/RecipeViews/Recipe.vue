<template>
  <div>
    <div id="recipe">
      <v-main id="recipe">
        <v-container fluid>
          <v-row align-content="center">
            <v-col sm="1" class="d-none d-lg-block"></v-col>
            <v-col lg="10" sm="12">
              <Recipe/>
            </v-col>
            <v-col sm="1" class="d-none d-lg-block"></v-col>
          </v-row>
        </v-container>
      </v-main>
    </div>
  </div>
</template>

<script>
import Recipe from "@/components/recipe/Recipe.vue";

export default {
  components: { Recipe },

  
};
</script>

<style scoped>
#recipe {
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
