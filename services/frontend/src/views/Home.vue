
<template>
  <div >
      Home page fssssss
      email: {{ email }} fullname: {{ fullName }}
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
    email: this.$store.getters["email"],
    fullName: this.$store.getters["fullName"],
    }
  }
}
</script>

<style scoped>
.bg {
  background-color: black;
}
</style>
