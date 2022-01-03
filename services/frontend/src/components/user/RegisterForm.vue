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
          <v-card-title primary-title>
            <p class="h6">Register</p>
          </v-card-title>
          <v-card-text>
            <v-form>
              <v-row>
                <v-col>
                  <v-text-field
                    name="firstName"
                    label="First name"
                    id="id"
                    v-model="firstName"
                  ></v-text-field>
                </v-col>
                <v-col>
                  <v-text-field
                    name="surname"
                    label="Surname"
                    id="id"
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
                    id="id"
                    v-model="email"
                  ></v-text-field>
                </v-col>
              </v-row>

              <v-text-field
                name="password"
                :type="passwordVisible ? 'text' : 'password'"
                label="Password"
                id="id"
                :append-icon="passwordVisible ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="passwordVisible = !passwordVisible"
                v-model="password"
              ></v-text-field>
              <v-text-field
                name="passwordComfirm"
                :type="passwordVisible ? 'text' : 'password'"
                label="Password Comfirm"
                id="id"
                :append-icon="passwordVisible ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="passwordVisible = !passwordVisible"
                v-model="passwordComfirm"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn color="success" outlined v-on:click.prevent="submitRegister">Sign up</v-btn>
            <v-spacer></v-spacer>
            <router-link to="/login">
              <v-btn color="orange" outlined>Back</v-btn>
            </router-link>
          </v-card-actions>
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
  }),
  methods: {
    async submitRegister() {
      let payload = {
        email: this.email,
        password: this.password,
        full_name: this.firstName + ' ' + this.surname,
      }
      // console.log(payload)
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