<template>
    <v-app>
      <AppBar/>
      <v-main>
        <router-view/>
        <v-snackbar
          v-model="snackbar"
          :multi-line="true"
          >
            {{ text }}

          <template v-slot:action="{ attrs }">
            <v-btn
              color="red"
              text
              v-bind="attrs"
              @click="closeSnackbar"
            >
            Close
            </v-btn>
          </template>
        </v-snackbar>
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
  async beforeMount() {
    await this.$store.dispatch("actionCheckLoggedIn")
  },
  async mounted() {
    if(this.$store.getters["isLoggedIn"])
      this.$store.dispatch("actionGetMe")
  },
  computed: {
    snackbar: {
      get() {return this.$store.getters["isSnackbarOpened"]},
      set() {this.$store.commit('closeSnackbar')}
    },
    text() {
      return this.$store.getters["snackbarText"]
    }
  },
  methods:{
    closeSnackbar() {
      this.$store.commit('closeSnackbar')
    }
  }
};
</script>


<style>

</style>
