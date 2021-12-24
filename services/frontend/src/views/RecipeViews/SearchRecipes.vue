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
    </v-card>
</template>

<script>
import SearchBar from "@/components/search/searchBar.vue"

export default {
  components: {SearchBar}
}
</script>

<style>

.spacer {
  height: 30px;
}

.search-bar {
  max-width: 80%;
  min-width: 80%;
}

</style>