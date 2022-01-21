<template>
  <v-autocomplete
    outlined
    clearable
    label="Product"
    v-model="product.name"
    :loading="isLoading"
    :search-input.sync="search"
    :items="ingredients"
    :rules="ingredientRules"
  ></v-autocomplete>
</template>

<script>
import { api } from '@/api';
export default {
    props: ["product"],
    data() {
    return {
      ingredientRules: [
        v => !!v || 'Product is required',
        // v => !v || v
        // v => !!(this.stage.products.filter((prod) => prod.product_id == v).length <= 1)  || 'This product have been already used in this stage'
      ],
      isLoading: false,
      search: null,
      ingredients: []
    };
  },
  mounted(){
    this.ingredients.push(this.product.name)
  },
  watch: {
    async search (query) {
        if (this.isLoading) return

        this.isLoading = true
        
        let response
        try {
           response = await api.searchProducts(this.$store.getters["token"], query)
          this.ingredients = response.data
        }
        catch(error) {
          console.log(error)
        }
        this.isLoading = false
        console.log(this.product.name)
    }
  }
};
</script>

<style>
</style>