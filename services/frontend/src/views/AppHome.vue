<template>
  <v-app>
    <AppBar/>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import AppBar from "@/components/layout/AppBar.vue"

export default {
  name: 'AppHome',
  components: {
    AppBar
  },
  async mounted() {
    this.$store.dispatch("actionGetMe")
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
