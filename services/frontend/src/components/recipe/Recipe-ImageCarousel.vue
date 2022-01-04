<template>
  <div id="image-carousel">
    <v-carousel
      hide-delimiter-background
      hide-delimiters
      vertical
      continuous
      class="rounded-l-lg"
      :prev-icon="false"
      :next-icon="false"
    >
      <!-- Possible place for multiple pictures -->
      <v-carousel-item
        :src="image"
        reverse-transition="fade-transition"
        transition="hide-delimiters"
        :ripple="false"
      >
      </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
export default {
  props:["image"],
};
</script>

<style>
</style>