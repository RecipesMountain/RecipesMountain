<template>
  <div>
    <v-stepper v-model="formStep" color="red">
      <v-stepper-header>
        <v-stepper-step :complete="formStep > 1" step="1">
          General Informations
        </v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step :complete="formStep > 2" step="2">
          Recipe Stages
        </v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step :complete="formStep > 3" step="3">
          Recipe Tags
        </v-stepper-step>
        <v-col class="d-flex">
          <v-spacer></v-spacer>
          <!-- <v-btn plain>Preview</v-btn> -->
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon>mdi-help-circle-outline</v-icon>
          </v-btn>
        </v-col>
      </v-stepper-header>
      <v-stepper-items>
        <v-stepper-content step="1">
          <v-card color="grey lighten-2">
            <v-card-title>General Informations</v-card-title>
            <v-card-subtitle class="text-left"
              >Basic information about recipe</v-card-subtitle
            >
            <v-divider class="mx-4"></v-divider>
            <v-card-text>
              <v-container>
                <v-form v-model="formOneValid" ref="form">
                  <v-row wrap>
                    <v-col md="6" cols="12">
                      <v-text-field
                        v-model="recipeTitle"
                        :rules="titleRules"
                        label="Recipe title"
                        required
                      >
                      </v-text-field>
                      <!-- <v-text-field
                        label="Calories billans"
                        v-model="caloriesBillans"
                        hint="Insert calories"
                        type="number"
                        :rules="descRules"
                      ></v-text-field> -->
                    </v-col>
                    <v-col md="6" cols="12">
                      <v-img
                        :src="previeImage"
                        contain
                        height="150px"
                        v-if="isImage"
                      >
                      </v-img>
                      <v-img
                        v-else-if="isForEdit"
                        :src="oldImage"
                        contain
                        height="150px"
                      ></v-img>
                      <v-file-input
                        show-size
                        chips
                        label="Select Image"
                        accept="image/*"
                        truncate-length="15"
                        @change="selectImage"
                        :rules="imageRules"
                      ></v-file-input>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="12">
                      <v-subheader
                        >Recipe difficulty:
                        {{ tickDiffLabels[difficulty] }}</v-subheader
                      >
                      <v-slider
                        v-model="difficulty"
                        prepend-icon="mdi-chili-mild"
                        step="1"
                        max="2"
                        thumb-label
                        ticks="always"
                        tick-size="6"
                        thumb-size="25"
                        :tick-labels="tickDiffLabels"
                      >
                        <template v-slot:thumb-label="{ value }">
                          <div v-if="value == 0">
                            <v-icon color="success">mdi-chili-mild </v-icon>
                          </div>
                          <div v-if="value == 1">
                            <v-icon color="warning">mdi-chili-mild </v-icon>
                          </div>
                          <div v-if="value == 2">
                            <v-icon color="error">mdi-chili-mild </v-icon>
                          </div>
                        </template>
                      </v-slider>
                      <v-subheader
                        >Number of servings: {{ servings }}</v-subheader
                      >
                      <v-slider
                        v-model="servings"
                        prepend-icon="mdi-silverware"
                        step="0.5"
                        min="1"
                        max="10"
                        tick-size="6"
                        :tick-labels="tickServLabels"
                      >
                      </v-slider>
                      <v-subheader
                        >Preparation time: {{ preparationTime }}</v-subheader
                      >
                      <v-slider
                        v-model="preparationTime"
                        prepend-icon="mdi-clock-outline"
                        step="1"
                        min="1"
                        max="5"
                        tick-size="6"
                        :tick-labels="tickPrepLabels"
                      >
                      </v-slider>
                    </v-col>
                  </v-row>
                </v-form>
              </v-container>
            </v-card-text>
          </v-card>
          <v-btn color="primary" @click="nextStepper">Next step</v-btn>
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-card color="grey lighten-2">
            <v-card-title class="px-3">
              Recipe Stages
            </v-card-title>
            <v-card-subtitle class="text-left"
              >Each stage can be about another part of a dish</v-card-subtitle
            >

            <v-divider class="mx-4"></v-divider>
            <v-card-text>
              <v-container fluid>
                <v-row wrap>
                  <v-item-group
                    v-model="stageWindow"
                    class="shrink mr-6"
                    mandatory
                  >
                    <v-item
                      v-for="stage in stages"
                      :key="stage.no"
                      v-slot="{ active, toggle }"
                    >
                      <div>
                        <v-btn :input-value="active" icon @click="toggle">
                          <v-icon>mdi-record</v-icon>
                        </v-btn>
                        <v-btn icon @click="deleteStage(stage.no)">
                          <v-icon>mdi-close</v-icon>
                        </v-btn>
                      </div>
                    </v-item>
                    <v-btn class="mt-5" @click="addStage">new</v-btn>
                  </v-item-group>
                  <v-col>
                    <v-window
                      v-model="stageWindow"
                      class="elevation-1"
                      vertical
                    >
                      <v-window-item v-for="stage in stages" :key="stage.no">
                        <RecipeFormStage :stage="stage" :products="products" :ref="'stage'+ stage.no" :isForEdit="isForEdit"/>
                      </v-window-item>
                    </v-window>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-card>
          <v-btn color="primary" @click="nextStepper">Next step</v-btn>
          <v-btn text color="primary" @click="formStep = 1">Back</v-btn>
        </v-stepper-content>

        <v-stepper-content step="3">
          <v-card color="grey lighten-2">
            <v-card-title>Recipe Tags</v-card-title>
            <v-card-subtitle class="text-left">
              Tags are really helpfull while searching recipes. Add as much as
              you can it will help your recipe to be more popular
            </v-card-subtitle>
            <v-divider class="mx-4"></v-divider>
            <v-card-text>
              <v-container fluid>
                <v-row>
                  <v-col md="6" cols="12">
                    <v-autocomplete
                      multiple
                      chips
                      deletable-chips
                      v-model="pickedTags"
                      :items="tags"
                      item-text="name"
                      item-value="id"
                    ></v-autocomplete>
                  </v-col>
                </v-row>
                <v-row wrap> </v-row>
              </v-container>
            </v-card-text>
          </v-card>
          <v-btn color="success" @click="submitRecipe">{{
            submitButtonLabel
          }}</v-btn>
          <v-btn text color="primary" @click="formStep = 2">Back</v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </div>
</template>

<script>
import RecipeFormStage from "./Recipe-FormStage.vue";
export default {
  props: ["isForEdit", "tags", "products"],
  components: { RecipeFormStage },
  data() {
    return {
      oldRecipe: undefined,
      oldImage: "",
      recipeTitle: "",
      recipeDesc: "",
      preparationTime: 0.5,
      difficulty: 0,
      caloriesBillans: 200,
      servings: 4,
      rating: 0,
      stages: [
        {
          no: 0,
          name: "",
          content: "",
          products: [],
        },
      ],
      pickedTags: [],

      formStep: 1,
      formOneValid: false,

      titleRules: [
        (v) => !!v || "Recipe title is required",
        (v) => v.length <= 50 || "Recipe title must be less then 50 characters",
      ],
      imageRules: [
        (v) => !(!v && !this.isForEdit) || "Recipe needs at least one picture",
      ],
      descRules: [],

      isImage: false,
      recipeImage: undefined,
      previeImage: undefined,

      stageNumber: 1,
      stageWindow: 0,

      tickDiffLabels: ["Easy", "Medium", "Hard"],
      tickServLabels: [
        "1",
        "1/2",
        "2",
        "2/3",
        "3",
        "3/4",
        "4",
        "4/5",
        "5",
        "5/6",
        "6",
        "6/7",
        "7",
        "7/8",
        "8",
        "8/9",
        "9",
        "9/10",
        "10",
      ],
      tickPrepLabels: ["30 min", "1 h", "1.5 h", "2 h", "2.5 h"],
    };
  },
  methods: {
    nextStepper() {
      if(this.formStep === 1){
        if(this.$refs.form.validate())
        {
          this.formStep += 1;
        }
      }
      else if(this.formStep === 2){
        let validStages = true;
        this.stages.forEach((stage) => {
          if(!this.$refs[`stage`+stage.no][0].$refs.stageForm.validate())
          {
            validStages = false
          }
        })
        if(validStages){
          this.formStep += 1;
        }
      }
    },
    selectImage(image) {
      if (image == undefined) {
        this.isImage = false;
        this.recipeImage = undefined;
        this.previeImage = undefined;
      } else if (image != undefined) {
        this.isImage = true;
        this.recipeImage = image;
        this.previeImage = URL.createObjectURL(this.recipeImage);
      }
    },
    addStage() {
      this.stages.push({
        no: this.stageNumber,
        name: "",
        content: "",
        products: [],
      });
      this.stageNumber += 1;
    },
    deleteStage(no){
      this.stages = this.stages.filter((stage) => stage.no != no)
    },
    async submitRecipe() {
      let tagList = [];
      this.pickedTags.forEach((element) => {
        tagList.push({
          name: "",
          id: element,
        });
      });
      let stageList = [];
      this.stages.forEach((element) => {
        let productList = [];
        element.products.forEach((product) => {
          productList.push({
            name: product.name,
            price: 0,
            product_id: product.product_id,
            amount: product.amount,
            amount_unit: product.amount_unit,
          });
        });
        stageList.push({
          name: element.name,
          content: element.content,
          products: productList,
        });
      });
      let payload = {
        title: this.recipeTitle,
        cookingTime: this.preparationTime * 30,
        difficulty: this.tickDiffLabels[this.difficulty],
        calories: this.caloriesBillans,
        portion: this.servings * 2,
        rating: this.rating,
        totalViews: 0,
        stages: stageList,
        tags: tagList,
      };
      if (!this.isForEdit) {
        await this.$store.dispatch("actionSubmitRecipe", payload);
        if (this.ErrorStatus) {
          console.log("something went wrong");
        } else {
          let fileData = new FormData();
          fileData.append("image", this.recipeImage);
          await this.$store.dispatch("actionAddRecipeImage", fileData);
          this.$router.push("/recipes/" + this.NewRecipeId);
        }
      }
      if (this.isForEdit) {
        this.$store.commit("setRecipeId", this.$route.params.id);
        await this.$store.dispatch("actionUpdateRecipe", payload);
        if (this.recipeImage != undefined) {
          let fileData = new FormData();
          fileData.append("image", this.recipeImage);
          await this.$store.dispatch("actionAddRecipeImage", fileData);
        }
        this.$router.push("/recipes/" + this.NewRecipeId);
      }
    },
  },
  computed: {
    submitButtonLabel() {
      if (this.isForEdit) return "Update your recipe";
      else return "Submit your recipe";
    },
    ErrorStatus() {
      return this.$store.getters["errorStatus"];
    },
    NewRecipeId() {
      return this.$store.getters["recipeId"];
    },
  },

  async mounted() {
    if (this.isForEdit) {
      await this.$store.dispatch("actionGetRecipe", this.$route.params.id);
      await this.$store.dispatch("actionGetRecipeImg", this.$route.params.id);

      this.oldRecipe = this.$store.getters["recipe"];

      this.oldImage = this.oldRecipe.image;

      this.recipeTitle = this.oldRecipe.title;
      this.preparationTime = this.oldRecipe.time / 30;

      this.difficulty = this.tickDiffLabels.indexOf(this.oldRecipe.difficulty);

      this.caloriesBillans = this.oldRecipe.calories;
      this.servings = this.oldRecipe.servings / 2;

      this.stages = [];
      this.oldRecipe.stages.forEach((stage) => {
        var prod = [];
        var numberOfProducts = 0;
        stage.products.forEach((product) => {
          prod.push({
            no: numberOfProducts,
            name: product.name,
            price: 0,
            product_id: product.product_id,
            amount: product.amount,
            amount_unit: product.amount_unit,
          });
          numberOfProducts += 1;
        });
        this.stages.push({
          no: this.stageNumber,
          name: stage.name,
          content: stage.content,
          products: prod,
        });
        this.stageNumber += 1;
      });
      this.pickedTags = [];
      this.oldRecipe.tags.forEach((tag) => this.pickedTags.push(tag.id));
    }
  },
};
</script>

<style>
</style>