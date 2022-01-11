<template>
    <v-card class="comment" color="transparent" elevation="2" >
        <v-card-title class="text-h5"> 
            <div v-if="comment.owner.full_name != null"> <v-avatar color="primary" size="50">{{ initials }}</v-avatar> {{comment.owner.full_name}} </div>
            <div v-else>Anonymous </div>
            <v-spacer></v-spacer>
            <v-btn v-if="comment.owner.id == userID" icon @click="deleteComment">
                <v-icon size="25">mdi-delete-forever</v-icon>
            </v-btn>
        </v-card-title>
        <v-card-text>
            <p>{{comment.content}}</p>
        </v-card-text>
    </v-card>
</template>

<script>
import { getInitials } from "@/utils";

export default {
    name: 'comment',
    props: ['comment', "userID", "delete"],
    mounted() {
        console.log(this.comment)
        console.log(this.userID)
    },
    methods: {
        deleteComment() {
            this.delete(this.comment)
        }
    },
    computed: {
       initials(){
        if(this.comment.owner != null)
            return getInitials(this.comment.owner.full_name)
        return "PW"
      }
    }

}
</script>

<style>

.comment {
    width: 100%;
}

</style>