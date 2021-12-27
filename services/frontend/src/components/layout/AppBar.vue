<template>
  <v-app-bar app absolute color="rgb(255, 202, 137)" elevate-on-scroll>
    <v-img
      lazy-src="https://picsum.photos/id/11/10/6"
      max-height="50"
      max-width="100"
      src="https://picsum.photos/id/11/500/300"
    ></v-img>

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

    <v-btn icon @click="goToSearch">
      <v-icon>mdi-book-search-outline</v-icon>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn icon >
      <v-icon>mdi-food-variant</v-icon>
    </v-btn>

    <v-btn icon>
      <v-icon>mdi-chef-hat</v-icon>
    </v-btn>

    <v-divider vertical></v-divider>

      <v-btn icon @click="logout">
        <v-icon>mdi-logout</v-icon>
      </v-btn>

    <v-avatar @click="() => { this.$router.push('/app/account') }" color="primary" size="56">PW</v-avatar>
  </v-app-bar>
</template>

<script>
  import { api } from '@/api';
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
  computed: {
      items() {
          return this.recpies
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

        let response = await api.search(this.$store.getters["token"], payload.keyword, payload.tags, payload.sort, payload.skip, payload.limit);
        console.log(response)  
        this.recpies = response.data
      
        //TODO ERROr handling
        this.isLoading = false
    },
  },
  methods: {
    async logout() {
      await this.$store.dispatch("actionLogOut")
      this.$router.push("/")
    },
    async goToSearch() {
      console.log(this.keyword)
      this.$store.commit("setKeyword", this.keyword)
      this.$store.dispatch("searchWithKeywordInState")
      this.$router.push("/app/search")
    }
  }
};
</script>

<style>
.vertical-center {
  top: 23%;
}
</style>