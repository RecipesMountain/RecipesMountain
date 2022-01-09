<template>
  <v-col justify="center"  >
    <v-row v-bind:key="comment.id" v-for="comment in comments">
        <Comment :comment="comment"/>
    </v-row>
  </v-col>
</template>

<script>
import Comment from './Comment.vue'

export default {
    name: 'CommentsList',
    props: ["comments"],
    components: {Comment}
}
</script>

<style>

</style>