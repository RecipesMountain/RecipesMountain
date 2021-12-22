<template>
    <v-app>
      <router-view/>
      <Footer/>
    </v-app>
</template>

<script>
import Footer from "@/components/layout/Footer.vue"
import router from './router'

export default {
  name: 'App',
  components: {
    Footer,
  },
  async mounted() {
    await this.$store.dispatch("actionCheckLoggedIn")
        if(this.$store.getters["isLoggedIn"]){
      router.push(`/app`)
  }
  }
};
</script>


<style>

</style>
