<template>
  <v-container>
    <v-row justify="center" class="">
      <v-col cols="5">
        <v-card class="text-center">
          <v-card-title primary-title>
            <p class="h6">Login</p>
          </v-card-title>
          <v-card-text>
            <v-form @keyup.enter="submitLogIn">
              <v-text-field
                name="username"
                label="Username"
                id="id"
                prepend-icon="mdi-account-circle"
                v-model="username"
              ></v-text-field>
              <v-text-field
                name="password"
                :type="passwordVisible ? 'text' : 'password'"
                label="Password"
                id="id"
                prepend-icon="mdi-lock"
                :append-icon="passwordVisible ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="passwordVisible = !passwordVisible"
                v-model="password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn color="success" outlined v-on:click.prevent="submitLogIn"
              >Login</v-btn
            >
            <v-spacer></v-spacer>
            <router-link to="/register">
              <v-btn color="orange" outlined>Register</v-btn>
            </router-link>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    passwordVisible: false,
    username: "",
    password: "",
  }),
  methods: {
    async submitLogIn() {
      console.log("Login", this.username, this.password);
      let payload = {
        username: this.username,
        password: this.password,
      }
      await this.$store.dispatch("actionLogIn", payload);
      this.$router.push("/app")
    },
  },
  mounted() {
    this.$store.commit('setToken', 'xxx')
    console.log(this.$store.getters['token']) 
  }
};
</script>

<style>
</style>