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
          <v-form ref="form" v-model="valid" @submit="(e) => {e.preventDefault(); submitLogIn();}" @keyup.enter="submitLogIn">
          <v-card-title primary-title>
            <p class="h6">Login</p>
          </v-card-title>
          <v-card-text>
              <v-text-field
                name="email"
                label="E-mail"
                id="e-mail"
                :rules="emailRules"
                prepend-icon="mdi-account-circle"
                v-model="email"
              ></v-text-field>
              <v-text-field
                name="password"
                :type="passwordVisible ? 'text' : 'password'"
                label="Password"
                :rules="passwordRules"
                id="password"
                prepend-icon="mdi-lock"
                :append-icon="passwordVisible ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="passwordVisible = !passwordVisible"
                v-model="password"
              ></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-btn class="mr-4" :disabled="!valid" type="submit" color="success" outlined
              >Login</v-btn
            >
            <v-spacer></v-spacer>
            <router-link to="/register">
              <v-btn color="orange" outlined>Register</v-btn>
            </router-link>
          </v-card-actions>
          </v-form>
        </v-card>
  </v-container>
</template>

<script>
import { mover } from "@/mover";
export default {
  data: () => ({
    passwordVisible: false,
    email: "",
    password: "",
    error: false,
    wrongPass: false,
    valid: false,
    emailRules: [
      v => !!v || 'E-mail is needed',
      v => /.+@.+\..+/.test(v) || 'E-mail has to be correct',
    ],
    passwordRules: [
        v => !!v || 'Password is needed',
    ],
  }),
  methods: {
    async submitLogIn() {
      console.log("Login", this.email, this.password);
      let payload = {
        username: this.email,
        password: this.password,
      }
      await this.$store.dispatch("actionLogIn", payload);
      if(this.$store.getters["isLoggedIn"])
        mover.goToHome()
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