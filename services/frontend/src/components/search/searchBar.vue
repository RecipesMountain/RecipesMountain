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
                    <v-autocomplete
                        label="Search by tags"
                        v-model="tags"
                        :items="items"
                        :loading="isLoading"
                        :search-input.sync="search"
                        item-text="name"
                        item-value="name"
                        chips
                        clearable
                        filled
                        multiple
                        rounded
                        small-chips
                    ></v-autocomplete>
                </v-col>
            </v-row>
            <v-row no-gutters align="center" justify="center" >
                <v-col no-gutters >
                        Sort By:
                </v-col>
                <v-col no-gutters >
                    <v-checkbox
                        v-model="sortBy"
                        value="popular"
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
                <v-col>
                    <v-checkbox
                        v-model="sortBy"
                        value="nosort"
                        label="No Sorting"
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
            keyword: this.$store.getters["getKeyword"],
            tags: [],
            showMore: false,
            sortBy: "popular",
            tagsPosible: [],
            isLoading: false,
            search: null,
        }
    },
    methods: {
        serach() {
        //TODO, handle skip and limit correctly 
        let payload = {
            skip: 0,
            limit: 20, 
            keyword: this.keyword,
            tags: this.tags,
            sort: this.sortBy,       
        }
        console.log(this.keyword)
        console.log(this.tags)
        console.log(payload)
        this.$store.dispatch("search", payload)
    },
    },
    computed: {
        items() {
            return this.tagsPosible
        }
    },
    watch: {
      async search () {
        // Items have already been loaded
        if (this.tagsPosible.length > 0) return

        // Items have already been requested
        if (this.isLoading) return

        this.isLoading = true

        await this.$store.dispatch("getTags")
        this.tagsPosible = this.$store.getters["getTagsAvailable"]
        console.log(this.tagsPosible)
        //TODO ERROr handling
        this.isLoading = false
      },
}
}
</script>

<style>

.rows {
    width: 95%;
}

</style>