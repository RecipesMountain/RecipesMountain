<template>
  <div class="center">
      <LoginForm/>
  </div>
</template>

<script>
import LoginForm from '@/components/user/LoginForm.vue'

export default {
  components: { LoginForm },

}
</script>

<style>

.center {
  display: flex;
  align-items: center;
}


</style>