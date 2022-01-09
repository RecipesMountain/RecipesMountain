<template>
    <v-card class="comment" color="transparent" elevation="2" >
        <v-card-title class="text-h5"> 
            <div v-if="comment.owner.full_name != null"> <v-avatar color="primary" size="56">PW</v-avatar> {{comment.owner.full_name}} </div>
            <div v-else>Anonymous </div>
        </v-card-title>
        <v-card-text>
            <p>{{comment.content}}</p>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    name: 'comment',
    props: ['comment']
}
</script>

<style>

.comment {
    width: 100%;
}

</style>