<template>
  <div id="steps-list" class="flex-columns">
    <v-divider />
    <v-lazy
      v-model="isActive"
      :options="{
        threshold: 0.7,
      }"
      transition="scroll-x-transition"
      class="fill-height"
      min-height="300px"
    >
      <v-card color="transparent" flat>
        <div id="stage-title" v-if="steps.length > 0">
          <p class="text-h6 text-left font-weight-medium">
            Opis przygotowanie - {{ stageLabel }}
          </p>
          <p
            class="text-subtitle-1 text-left px-2"
            v-for="(step, index) in steps"
            :key="index"
          >
            <v-icon class="mx-0" color="lighten--black"
              >mdi-square-medium</v-icon
            >
            {{ step.content }}
          </p>
        </div>
      </v-card>
    </v-lazy>
  </div>
</template>

<script>
export default {
  props: ["stageLabel", "steps"],

  data() {
    return {
      isActive: false,
    };
  },
};
</script>

<style>
</style>
