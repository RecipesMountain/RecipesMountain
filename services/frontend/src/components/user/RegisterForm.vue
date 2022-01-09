<template>
  <v-container>
      <v-alert
        dense
        outlined
        type="error"
        v-if="error"
      >
        There was a problem with registration
      </v-alert>
        <v-card class="text-center">
          <v-form ref="form" v-model="valid" @submit="(e) => {e.preventDefault(); submitRegister();}" @keyup.enter="submitLogIn">
          <v-card-title primary-title>
            <p class="h6">Register</p>
          </v-card-title>
          <v-card-text>
              <v-row>
                <v-col>
                  <v-text-field
                    name="firstName"
                    label="First name"
                    id="fistName"
                    v-model="firstName"
                    :rules="firstNameRules"
                  ></v-text-field>
                </v-col>
                <v-col>
                  <v-text-field
                    name="surname"
                    label="Surname"
                    id="surName"
                    v-model="surname"
                  ></v-text-field>
                </v-col>
              </v-row>

              <v-row>
                <v-col>
                  <v-text-field
                    name="email"
                    type="email"
                    label="E-mail"
                    id="e-mail"
                    v-model="email"
                    :rules="emailRules"
                  ></v-text-field>
                </v-col>
              </v-row>

              <v-text-field
                name="password"
                :type="passwordVisible ? 'text' : 'password'"
                label="Password"
                :rules="passwordRules"
                id="password"
                :append-icon="passwordVisible ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="passwordVisible = !passwordVisible"
                v-model="password"
              ></v-text-field>
              <v-text-field
                name="passwordConfirm"
                :type="passwordVisible ? 'text' : 'password'"
                label="Password Confirm"
                :rules="passwordRules"
                id="passwordConfirm"
                :append-icon="passwordVisible ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="passwordVisible = !passwordVisible"
                v-model="passwordComfirm"
              ></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-btn class="mr-4" :disabled="!valid" type="submit" color="success" outlined>Sign up</v-btn>
            <v-spacer></v-spacer>
            <router-link to="/login">
              <v-btn color="orange" outlined>Back</v-btn>
            </router-link>
          </v-card-actions>
          </v-form>
        </v-card>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    passwordVisible: false,
    email: "",
    password: "",
    passwordComfirm: "",
    firstName: "",
    surname: "",
    error: false,
    valid: false,
    emailRules: [
      v => !!v || 'E-mail is needed',
      v => /.+@.+\..+/.test(v) || 'E-mail has to be correct',
    ],
    passwordRules: [
        v => !!v || 'Password is needed',
        () => this.password == this.passwordComfirm || "Passwords has to be the same"
    ],
    firstNameRules: [
        v => !!v || 'Fist Name is needed',
    ],
  }),
  methods: {
    async submitRegister() {
      let payload = {
        email: this.email,
        password: this.password,
        full_name: this.firstName + ' ' + this.surname,
      }
      await this.$store.dispatch("actionRegister", payload)
      if(this.$store.getters["registrationSuccess"])
        this.$router.push('/login')
      else if(this.$store.getters["registrationError"])
        this.error = true
    },
  },
};
</script>

<style>
</style>