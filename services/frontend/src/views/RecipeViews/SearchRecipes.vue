<template>
    <v-card
    color="grey lighten-4"
    flat
    >
    <div class="spacer"/> 
      <v-row
      align="center"
      justify="center"
      >
        <SearchBar class="center search-bar"/>
      </v-row>
      <div class="spacerBig"/> 
      <v-row align="center" justify="center" >
        <SearchRes class="center search-bar" />
      </v-row>
      <v-row align="center" justify="center" >
        <v-btn @click="previosPage" v-if="hasPreviousPage" >
          Go Back
        </v-btn>
        <v-btn @click="nextPage" v-if="hasNextPage">
          Next Page
        </v-btn>
      </v-row>
    </v-card>
</template>

<script>
import SearchBar from "@/components/search/searchBar.vue"
import SearchRes from "@/components/search/searchRes.vue"
export default {
  components: {SearchBar, SearchRes},
  methods: {
    nextPage() {
      this.$store.dispatch("nextPage")
    },
    previosPage() {
      this.$store.dispatch("previousPage")
    }
  },
  computed:{
    hasPreviousPage() {
      return this.$store.getters['hasPreviousPage']
    },
    hasNextPage() {
      return this.$store.getters['hasNextPage']
    }
  }
}
</script>

<style>

.spacer {
  height: 30px;
}

.spacerBig {
  height: 40px;
}

.search-bar {
  width: 80%;
}

</style>