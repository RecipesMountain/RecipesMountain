<template>
  <div>
    <v-card flat>
      <v-card-title>
        Stage:
        <v-row class="mx-4">
          <v-text-field
            label="Stage name"
            hint="For example: pastry, glaze ..."
            v-model="stage.name"
          ></v-text-field>
        </v-row>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-form v-model="formStage" ref="stageForm">
            <v-row wrap>
              <v-col md="6" cols="12">
                <v-card outlined flat>
                  <v-subheader>
                    Ingredients in stage<v-spacer></v-spacer>
                    <v-btn icon @click="addIngredient">
                      <v-icon>mdi-plus</v-icon>
                    </v-btn></v-subheader
                  >
                  <v-divider />
                  <v-card-text>
                    <v-container>
                      <v-row
                        wrap
                        dense
                        v-for="product in stage.products"
                        :key="product.no"
                      >
                        <v-col md="4">
                          <RecipeSingleProduct :product="product" :isForEdit="isForEdit"/>
                        </v-col>
                        <v-col md="4">
                          <v-text-field
                            outlined
                            label="Quantity"
                            type="number"
                            v-model="product.amount"
                          ></v-text-field>
                        </v-col>
                        <v-col md="3">
                          <v-select
                            outlined
                            :items="units"
                            label="Units"
                            item-text="label"
                            v-model="product.amount_unit"
                          >
                          </v-select>
                        </v-col>
                        <v-col md="1" class="mt-2 ml-n3">
                          <v-btn icon @click="deleteIngredient(product.no)"><v-icon>mdi-delete</v-icon></v-btn>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card-text>
                </v-card>
              </v-col>
              <v-col md="6" cols="12">
                <v-card outlined flat>
                  <v-subheader> Instructions<v-spacer></v-spacer></v-subheader>
                  <v-divider />
                  <v-card-text>
                    <v-row wrap dense>
                      <v-col md="12">
                        <v-textarea
                          outlined
                          label="Instruction"
                          rows="5"
                          v-model="stage.content"
                        ></v-textarea>
                      </v-col>
                    </v-row>
                  </v-card-text>
                </v-card>
              </v-col>
              <v-spacer></v-spacer>
            </v-row>
          </v-form>
        </v-container>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import RecipeSingleProduct from './Recipe-SingleProduct.vue';
export default {
  components: { RecipeSingleProduct },
  props: ["stage", "products", "isForEdit"],
  data() {
    return {
      formStage: false,
      numberOfIngredients: this.stage.products.length,
      ingredientRules: [
        v => !!v || 'Product is required',
        v => !!(this.stage.products.filter((prod) => prod.product_id == v).length <= 1)  || 'This product have been already used in this stage'
      ],
    };
  },
  methods: {
    addIngredient() {
      this.stage.products.push({
        no: this.numberOfIngredients,
        name: "",
        price: 0,
        product_id: "",
        amount: 1,
        amount_unit: "gram",
      });
      this.numberOfIngredients += 1;
    },
    deleteIngredient(no){
      this.stage.products = this.stage.products.filter(item => item.no != no)
    }
  },
  computed: {
    units() {
      return this.$store.getters["units"];
    },
    productsCopy(){
      return this.products
    }
  },
};
</script>

<style>
</style>