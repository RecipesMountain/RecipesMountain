<template>
  <v-row align="center" justify="center">
      <v-col v-bind:key="recpie.id" v-for="recpie in recpies" align="center" justify="center" > 
        <v-card
            color="rgb(25, 202, 137)"
            elevation="9"
            rounded
            shaped
            class="recpie-card"
        >
            {{recpie.title}}
            <v-img
            lazy-src="http://t0.gstatic.com/licensed-image?q=tbn:ANd9GcSt6XaVwRYuoMvrzqceIm8UTAReg9pkdrytNvTXFz9QXdEbUgdmTDESypOL-8ln9DnwVjORUyBHqntjNHYUAro"
            max-height="400"
            max-width="400"
            src="http://t0.gstatic.com/licensed-image?q=tbn:ANd9GcSt6XaVwRYuoMvrzqceIm8UTAReg9pkdrytNvTXFz9QXdEbUgdmTDESypOL-8ln9DnwVjORUyBHqntjNHYUAro"
            ></v-img>
        </v-card>
      </v-col>
  </v-row>
</template>

<script>
export default {
    computed: {
        recpies() {
            return this.$store.getters["getRecipes"]
        }
    }
}
</script>

<style>

.recpie-card {
    max-height: 400px;
    max-width: 400px;
}

</style>