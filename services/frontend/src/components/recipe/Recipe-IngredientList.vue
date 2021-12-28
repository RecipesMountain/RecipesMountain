<template>
  <div id="ingredients">
    <v-lazy
      v-model="isActive"
      :options="{
        threshold: 0.7,
      }"
      transition="scroll-y-transition"
      class="fill-height"
      min-height="300px"
    >
      <v-card  color="rgba(0, 0, 0, 0.06)" shaped>
        <v-list dense color="transparent">
          <v-list-item >
            <v-list-item-title class="text-left subtitle-1 font-weight-black">
                <!-- Ingredients:  -  -->
              {{ stageLabel }}
            </v-list-item-title>
          </v-list-item>
          <v-list-item
            v-for="ingredient in ingredients"
            :key="ingredient.label"
          >
            <v-list-item-content>
              <v-list-item-title
                class="text-wrap text-left body-1 font-weight-medium"
              >
                <v-icon class="mx-n2" color="black">mdi-circle-small</v-icon>
                {{ ingredient.label }}
              </v-list-item-title>
            </v-list-item-content>
            <v-tooltip right>
              <template v-slot:activator="{ on }">
                <v-list-item-content>
                  <v-list-item-subtitle
                    v-on="on"
                    class="text-right body-1 font-weight-black"
                  >
                    {{ ingredient.amount }} {{ ingredient.unit }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </template>
              {{ ingredient.unitHint }}
            </v-tooltip>
          </v-list-item>
        </v-list>
      </v-card>
    </v-lazy>
  </div>
</template>

<script>
export default {
    props:  ['stageLabel', 'ingredients'],
  data() {
    return {
      isActive: false,
    };
  },
};
</script>

<style scoped>
</style>