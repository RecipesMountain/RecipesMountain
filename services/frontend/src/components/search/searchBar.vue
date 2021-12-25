<template>
    <v-card
      color="rgb(255, 202, 137)"
      elevation="9"
      rounded
      shaped
    >
        <v-col no-gutters align="center" justify="center">
            <v-row align="center" justify="center" >
                <v-col>
                    <v-text-field
                        label="Search by keyword"
                        placeholder="Enter keyword here"
                        v-model="keyword"
                        filled
                        dense
                        rounded
                    ></v-text-field>
                </v-col>
                <v-col>
                    <v-text-field
                        label="Search by tags"
                        placeholder="Split tags using comma(tag,tag)"
                        v-model="tagsTyped"
                        filled
                        dense
                        rounded
                    ></v-text-field>
                </v-col>
            </v-row>
            <v-row no-gutters align="center" justify="center" >
                <v-col no-gutters >
                        Sort By:
                </v-col>
                <v-col no-gutters >
                    <v-checkbox
                        v-model="sortBy"
                        value="popularity"
                        label="Popularity"
                    ></v-checkbox>
                </v-col>
                <v-col no-gutters >
                    <v-checkbox
                        v-model="sortBy"
                        value="best"
                        label="Best"
                    ></v-checkbox>
                </v-col>
                <v-col>
                    <v-checkbox
                        v-model="sortBy"
                        value="views"
                        label="Most viewed"
                    ></v-checkbox>
                </v-col>
                </v-row>
                <div v-if="!showMore">
                    Tags<a @click="toggleShow">(show more)</a>:
                </div>
                <div v-if="showMore">
                    Tags<a @click="toggleShow">(show less)</a>:
                </div>
                <v-row align="center" justify="center" >
                    <v-col v-for="tag in tagsToShow" v-bind:key="tag" >
                        <v-checkbox
                            v-model="chooseTags"
                            :value="tag"
                            :label="tag"
                        ></v-checkbox>
                    </v-col>
                </v-row>
                <v-row align="center" justify="center" >
                    <v-col>
                        <v-btn
                        block
                        elevation="2"
                        large
                        rounded
                        >Collapse</v-btn>
                    </v-col>
                    <v-col>
                        <v-btn
                        block
                        elevation="2"
                        large
                        rounded
                        @click="serach"
                        >Search</v-btn>
                    </v-col>
                </v-row>
        </v-col>
    </v-card>
</template>

<script>

export default {
    data() {
        return {
            keyword: null,
            tagsTyped: null,
            showMore: false,
            amountTagsLessShow: 8,
            tagsToShow: [],
            tags: ["fast", "easy", "pierogi", "fast2", "easy2", "pierogi2", "fast3", "easy3", "pierogi3", "fast4", "easy4", "pierogi4"],
            sortBy: "popularity",
            chooseTags: []
        }
    },
    methods: {
        toggleShow() {
            this.showMore = !this.showMore
            if(this.showMore) this.showMoreTags()
            else this.showLessTags()
        },
        showMoreTags() {
            this.tagsToShow = this.tags
        },
        showLessTags() {
            this.tagsToShow = this.tags.slice(0, this.amountTagsLessShow)
        },
        serach() {
        //TODO, handle skip and limit correctly 
        let payload = {
            skip: 0,
            limit: 20,   
            keyword: this.keyword,
            tags: this.tagsTyped,
            sort: this.sort,       
        }
        console.log(this.keyword)
        console.log(this.tagsTyped)
        console.log(payload)
        this.$store.dispatch("search", payload)
    },
    },
    mounted() {
        this.tagsToShow = this.tags.slice(0, this.amountTagsLessShow)
    },
}
</script>

<style>

.rows {
    width: 95%;
}

</style>