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
                        filled
                        dense
                        rounded
                    ></v-text-field>
                </v-col>
                <v-col>
                    <v-text-field
                        label="Search by tags"
                        placeholder="Split tags using comma(tag,tag)"
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
                Tags:
                <v-row align="center" justify="center" >
                    <v-col v-for="tag in tags" :key="tag" >
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
            tags: ["fast", "easy", "pierogi"],
            sortBy: "popularity",
            chooseTags: []
        }
    }
}
</script>

<style>

.rows {
    width: 95%;
}

</style>