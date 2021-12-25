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
        <v-btn v-if="this.$store.getters['hasPreviousPage']" >
          Go Back
        </v-btn>
        <v-btn v-if="this.$store.getters['hasNextPage']">
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
  metods: {
    nextPage() {
      this.$store.dispatch("nextPage")
    },
    previosPage() {
      this.$store.dispatch("previousPage")
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