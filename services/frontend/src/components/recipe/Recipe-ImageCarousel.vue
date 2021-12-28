<template>
  <div id="image-carousel">
    <v-carousel
      mx-4
      hide-delimiter-background
      hide-delimiters
      light
      vertical
      continuous
      show-arrows-on-hover
      class="rounded-l-lg"
    >
      <v-carousel-item
        v-for="(item, i) in images"
        :key="i"
        :src="item.src"
        reverse-transition="fade-transition"
        transition="hide-delimiters"
        ripple
      >
      </v-carousel-item>
    </v-carousel>
    <!-- {{ id }} -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: this.$route.params.id,
      images: this.$store.getters["images"],
    };
  },
};
</script>

<style>
</style>