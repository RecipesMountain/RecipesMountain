<template>
  <v-container class="login-card">
    <v-alert
      dense
      outlined
      type="error"
      v-if="error"
    >
      There was a problem with loging in 
    </v-alert>
    <v-alert
      dense
      outlined
      type="error"
      v-if="wrongPass"
    >
      Wrong credentians
    </v-alert>
        <v-card >
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
            <v-btn color="success" outlined @click="submitLogIn"
              >Login</v-btn
            >
            <v-spacer></v-spacer>
            <router-link to="/register">
              <v-btn color="orange" outlined>Register</v-btn>
            </router-link>
          </v-card-actions>
        </v-card>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    passwordVisible: false,
    username: "",
    password: "",
    error: false,
    wrongPass: false,
  }),
  methods: {
    async submitLogIn() {
      console.log("Login", this.username, this.password);
      let payload = {
        username: this.username,
        password: this.password,
      }
      await this.$store.dispatch("actionLogIn", payload);
      if(this.$store.getters["isLoggedIn"])
        this.$router.push("/app")
      else if(this.$store.getters["loginError"])
        this.error = true;
      else this.wrongPass = true;
    },
  },
};
</script>

<style scoped>

.login-card {
  max-width: 400px;
}

</style>