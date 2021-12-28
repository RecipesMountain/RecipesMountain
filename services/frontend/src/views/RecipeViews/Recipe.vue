<template>
  <div>
    <!-- <RecipeLayout>
          te sloty powinny byc w recipeLayout
          <div slot="info">
              <RecipeInformations />
          </div>
          <div slot="stages"> TRELO test</div>
          <div slot="tags"> TRELO test</div>
          <div slot="comments"> TRELO test</div>
      </RecipeLayout> -->
    <div id="recipe">
      <v-main id="recipe">
        <v-container fluid>
          <v-row align-content="center">
            <v-col sm="1" class="d-none d-lg-block"></v-col>

            <v-col lg="10" sm="12">
              <v-sheet
                min-height="100vh"
                min-width="200px"
                shaped
                class="mx-4 pa-6"
                elevation="5"
                outlined
                color="transparent"
              >
                <RecipeInformations />
                <v-row
                  ><v-col sm="12" class="d-none d-lg-block"> </v-col
                ></v-row>
                <!-- stages start -->
                <v-row
                  v-for="stage in stages"
                  :key="stage.name"
                  class="flex-column"
                >
                  <v-col>
                    <RecipeStage :ingredients="stage.ingredients" :steps="stage.steps" :stageLabel="stage.label"/>
                  </v-col>
                </v-row>
                <!-- stages end -->
                <v-row id="tags" justify="start" class="flex-column">
                  <v-col class="">
                    <v-divider />
                    <p class="text-overline text-left mb-n3">Tags:</p>
                    <v-chip-group column>
                      <v-chip
                        v-for="tag in tags"
                        :key="tag.id"
                        pill
                        small
                        color="#e0bd70"
                        class="text-body-2 text-left px-2"
                      >
                        {{ tag.label }}
                      </v-chip>
                    </v-chip-group>
                  </v-col>
                </v-row>
                <v-row id="comments" justify="start" class="flex-column">
                  <v-col class="">
                    <v-divider />
                    <div class="justify-space-between d-flex flex-row">
                      <p class="text-left text-h4 ont-weight-bold">Comments:</p>
                      <v-btn icon>
                        <v-icon size="35">mdi-plus</v-icon>
                      </v-btn>
                    </div>
                    //TODO comments
                  </v-col>
                </v-row>
              </v-sheet>
            </v-col>
            <v-col sm="1" class="d-none d-lg-block"></v-col>
          </v-row>
        </v-container>
      </v-main>
    </div>
  </div>
</template>

<script>
import RecipeInformations from "@/components/recipe/Recipe-Informations.vue";
import RecipeStage from "@/components/recipe/Recipe-Stage.vue";

export default {
  components: { RecipeInformations, RecipeStage},
  data() {
    return {
      tags: this.$store.getters["tags"],
      stages: this.$store.getters["stages"],
      comments: []
    };
  },
  async mounted() {

    this.$store.dispatch("actionGetRecipe", this.$route.params.id)
  }
};
</script>

<style scoped>
#recipe {
  /* background-color: #fff8e8; */
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
.theme--light.v-sheet--outlined {
  border: thin solid #fff8e8;
}
</style>
