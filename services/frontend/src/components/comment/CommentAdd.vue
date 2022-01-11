<template>
<div>
    <v-card  shaped color="transparent" elevation="4" >
        <v-card-title class="text-h5">
            Add New Comment
        </v-card-title>
        <v-textarea
          filled
          auto-grow
          label="Comment text"
          rows="2"
          row-height="20"
          v-model="comment"
        ></v-textarea>
        <v-card-actions>
           <v-btn block rounded color="transparent" @click="submintComment">
            Submit you comment
           </v-btn>
        </v-card-actions>
    </v-card>
</div>
</template>

<script>
import { api } from '@/api';

export default {
    name: 'NewComment',
    props: ["recpie_id", "commentAdded"],
    data() {
        return {
            comment: null,
        }
    },
    methods: {
        async submintComment() {
            try {
                let comment = {
                    content: this.comment
                }
                await api.createComment(this.$store.getters["token"], this.recpie_id, comment);
            } catch (e) {
                this.$store.commit("openSnackbar", "Error while adding comment");
            }

            this.commentAdded()
        }
    }
}
</script>

<style>

</style>