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
      min-height="120px"
    >
      <v-card color="transparent" flat>
        <p class="text-h6 text-left font-weight-medium">
          Preparation - {{ stageLabel }}
        </p>
        <p class="text-subtitle-1 text-left px-2">{{ stageContent }}</p>
      </v-card>
    </v-lazy>
  </div>
</template>

<script>
export default {
  props: ["stageLabel", "stageContent"],

  data() {
    return {
      isActive: false,
    };
  },
};
</script>

<style>
</style>
