<template>
  <div id="stage" class="mb-8">
    <v-row>
      <v-col lg="3" cols="12">
        <RecipeIngredientList :ingredients="ingredients" :stageLabel="stageLabel"/>
      </v-col>
      <v-col lg="9" cols="12">
        <v-divider/>
        <RecipeStepList :stageContent="stageContent" :stageLabel="stageLabel"/>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import RecipeIngredientList from './Recipe-IngredientList.vue'
import RecipeStepList from './Recipe-StepList.vue'
export default {
  props:['ingredients', 'stageContent', 'stageLabel'],
  components: { RecipeIngredientList, RecipeStepList },
}
</script>

<style>

</style>