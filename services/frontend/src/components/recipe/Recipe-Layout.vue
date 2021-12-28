<template>
  <div id="recipe">
    <v-main id="recipe">
      <v-container fluid>
        <v-row align-content="center">
          <v-col sm="1" class="d-none d-lg-block"></v-col>
          <v-col lg="10" sm="12">
            <v-sheet
              min-height="100vh"
              min-width="200px"
              shaped
              class="mx-4 pa-6"
              elevation="5"
              outlined
              color="transparent"
            >
              <v-row align-content="start">
                <slot name="info"/>
              </v-row>
              <v-row><v-col sm="12" class="d-none d-lg-block"> </v-col></v-row>
              <slot name="stages"/>
              <v-row id="tags" justify="start" class="flex-column">
                <v-col class="">
                  <v-divider />
                  <slot name="tags"/>
                </v-col>
              </v-row>
              <v-row id="comments" justify="start" class="flex-column">
                <v-col class="">
                  <v-divider />
                  <slot name="comments"/>
                </v-col>
              </v-row>
            </v-sheet>
          </v-col>
          <v-col sm="1" class="d-none d-lg-block"></v-col>
        </v-row>
      </v-container>
    </v-main>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
#recipe {
  /* background-color: #fff8e8; */
  background-image: linear-gradient(
    to bottom,
    #ffe6cf,
    #ffdfc9,
    #ffd8c3,
    #ffd1be,
    #ffcabb,
    #ffc2b5,
    #ffbbb0,
    #ffb3ab,
    #ffa9a1,
    #ff9e97,
    #ff948d,
    #ff8984
  );
}
.theme--light.v-sheet--outlined {
  border: thin solid #fff8e8;
}
</style>