<template>
  <div id="stage" class="mb-8">
    <v-row>
      <v-col lg="3" cols="12">
        <RecipeIngredientList :ingredients="ingredients" :stageLabel="stageLabel"/>
      </v-col>
      <v-col lg="9" cols="12">
        <v-divider/>
        <RecipeStepList :steps="steps" :stageLabel="stageLabel"/>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import RecipeIngredientList from './Recipe-IngredientList.vue'
import RecipeStepList from './Recipe-StepList.vue'
export default {
    props:['ingredients', 'steps', 'stageLabel'],
  components: { RecipeIngredientList, RecipeStepList },
  data(){
    return{
      id: this.$route.params.id
    }
  }
}
</script>

<style>

</style>