<template>
  <v-app>
    <AppBar/>
    <v-main>
      <v-sheet
      class="overflow-y-auto"
      >
      <router-link to="/">Main</router-link> |
      <router-link to="/about">About</router-link>
      <router-view/>
      </v-sheet>
    </v-main>
    <Footer/>
  </v-app>
</template>

<script>
import Footer from "@/components/layout/Footer.vue"
import AppBar from "@/components/layout/AppBar.vue"

export default {
  name: 'App',
  components: {
    Footer,
    AppBar
  },
  mounted() {
    this.$store.dispatch("actionCheckLoggedIn")
  }
};
</script>


<style scoped>
.logout {
  display: flex;
  flex-flow: column;
  height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
