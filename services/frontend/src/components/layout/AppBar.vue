<template>
  <v-app-bar app absolute color="rgb(255, 202, 137)" elevate-on-scroll>
    <v-img
      lazy-src="https://picsum.photos/id/11/10/6"
      max-height="50"
      max-width="100"
      src="https://picsum.photos/id/11/500/300"
    ></v-img>

    <v-spacer></v-spacer>

    <v-text-field
      class="vertical-center"
      label="Search"
      placeholder="Enter food here"
      filled
      rounded
      dense
    ></v-text-field>

    <v-btn icon @click="search">
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
export default {
  name: "AppBar",
  methods: {
    async logout() {
      await this.$store.dispatch("actionLogOut")
      this.$router.push("/")
    },
    async search() {
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