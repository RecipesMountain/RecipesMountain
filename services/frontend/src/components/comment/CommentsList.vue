<template>
  <v-col justify="center"  >
    <v-row v-bind:key="comment.id" v-for="comment in comments">
        <Comment class="commend-card" :userID="userID" :delete="deleteComment" :comment="comment"/>
    </v-row>
  </v-col>
</template>

<script>
import Comment from './Comment.vue'

export default {
    name: 'CommentsList',
    props: ["comments", "deleteComment"],
    components: {Comment},
    computed: {
      userID() {
        return this.$store.getters["userID"]
      }
    },
}
</script>

<style>

.commend-card {
  margin: 4px;
}

</style>