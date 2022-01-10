<template>
  <v-col justify="center"  >
    <v-row v-bind:key="comment.id" v-for="comment in comments">
        <Comment :userID="userID" :delete="deleteComment" :comment="comment"/>
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

</style>