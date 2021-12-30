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
        :src="imageUrl"
        reverse-transition="fade-transition"
        transition="hide-delimiters"
        ripple
      >
      </v-carousel-item>
    </v-carousel>
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
  async mounted(){
    await this.$store.dispatch("actionGetRecipeImg", this.$route.params.id)
  },
  computed:{
    imageUrl(){
      return this.$store.getters["imageLink"]
    }
  }
};
</script>

<style>
</style>