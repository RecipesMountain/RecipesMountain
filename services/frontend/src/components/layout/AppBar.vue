<template>
  <v-app-bar app absolute color="rgb(255, 202, 137)" elevate-on-scroll>
    <v-tooltip bottom>
      <template v-slot:activator="{ on, attrs }">
        <v-img
          v-bind="attrs"
          v-on="on"
          @click="goToHome"
          lazy-src="https://picsum.photos/id/11/10/6"
          max-height="50"
          max-width="100"
          src="https://picsum.photos/id/11/500/300"
        ></v-img>
      </template>
      <span>Go to main page</span>
    </v-tooltip>

    <v-spacer></v-spacer>

    <v-autocomplete
      label="Search recpies"
      v-model="keyword"
      :items="items"
      :loading="isLoading"
      :search-input.sync="search"
      item-text="title"
      item-value="title"
      clearable
      filled
      rounded
      class="vertical-center"
    ></v-autocomplete>

    <v-tooltip bottom>
      <template v-slot:activator="{ on, attrs }">
        <v-btn 
          icon 
          @click="goToSearch"
          v-bind="attrs"
          v-on="on">
          <v-icon>mdi-book-search-outline</v-icon>
        </v-btn>
      </template>
      <span>Search</span>
    </v-tooltip>
    
    <v-spacer></v-spacer>

    <v-tooltip bottom>
      <template v-slot:activator="{ on, attrs }">
        <v-btn 
          icon 
          @click="goToSearch"
          v-bind="attrs"
          v-on="on">
            <v-icon>mdi-food-variant</v-icon>
        </v-btn>
      </template>
      <span>Your Recpies</span>
    </v-tooltip>
    

    <v-tooltip bottom>
      <template v-slot:activator="{ on, attrs }">
        <v-btn 
          icon 
          @click="goToAddRecipe"
          v-bind="attrs"
          v-on="on">
          <v-icon>mdi-chef-hat</v-icon>
        </v-btn>
      </template>
      <span>Add a recpie</span>
    </v-tooltip>

    <v-divider vertical></v-divider>

    <template  v-if="!isLoggedIn">
      <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn 
            icon 
            @click="login"
            v-bind="attrs"
            v-on="on">
            <v-icon>mdi-login</v-icon>
          </v-btn>
        </template>
        <span>Login</span>
      </v-tooltip>

      <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn 
            icon 
            @click="register"
            v-bind="attrs"
            v-on="on">
            <v-icon>mdi-account-plus-outline</v-icon>
          </v-btn>
        </template>
        <span>Register</span>
      </v-tooltip>
      
    </template>
    <template  v-else-if="isLoggedIn">
      <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn 
            icon 
            @click="logout"
            v-bind="attrs"
            v-on="on">
            <v-icon>mdi-logout</v-icon>
          </v-btn>
        </template>
        <span>Logout</span>
      </v-tooltip>

      <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-avatar v-on="on" v-bind="attrs" @click="goToAccount" color="primary" size="56">PW</v-avatar>
        </template>
        <span>User Profile</span>
      </v-tooltip>
      
    </template>

    
  </v-app-bar>
</template>

<script>
  import { api } from '@/api';
  import { mover } from "@/mover";

export default {
  
  name: "AppBar",
  data() {
    return {
      keyword: null,
      recpies: [],
      isLoading: false,
      search: null,
      sortBy: "popular",
    }
  },
  mounted(){
    this.$store.dispatch("actionCheckLoggedIn")
  },
  computed: {
      items() {
          return this.recpies
      },
      isLoggedIn() {
        return this.$store.getters["isLoggedIn"]
      }
  },
  watch: {
      async search (val) {

        // Items have already been requested
        if (this.isLoading) return

        this.isLoading = true

        let payload = {
            skip: 0,
            limit: 6, 
            keyword: val,
            tags: [],
            sort: this.sortBy,       
        }

        try {
          let response = await api.search(this.$store.getters["token"], payload.keyword, payload.tags, payload.sort, payload.skip, payload.limit);
          this.recpies = response.data
        } catch (error) {
          this.$store.commit("openSnackbar", "There has been an error with getting results from the server\n You can go over to search page and try again, or contact adminstator")
        }
        
        this.isLoading = false
    },
  },
  methods: {
    async logout() {
      await this.$store.dispatch("actionLogOut")
      mover.goToHome()
    },
    login() {
      mover.goToLogin()
    },
    register() {
      mover.goToRegister()
    },
    goToAccount(){
      mover.goToAccount()
    },
    goToAddRecipe() {
      mover.goToAddRecipe()
    },
    goToHome() {
      mover.goToHome()
    },
    async goToSearch() {
      this.$store.commit("setKeyword", this.keyword)
      this.$store.dispatch("searchWithKeywordInState")
      mover.goToSearch()
    }
  }
};
</script>

<style>
.vertical-center {
  top: 23%;
}
</style>