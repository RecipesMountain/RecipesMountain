// import { api } from '@/api';


const defaultState = {
    recipe: {
        Title: "Recipe Title",
        Description: "Recipe Description",
        Author: "Magda Krzesler",
        AuthorId: 1,
        Time: 1.5,
        Rating: 4.5,
        RatingCount: 1000,
        Tags:[
            {
                id: 1,
                label: "Pasta"
            },
            {
                id: 2,
                label: "In Oven"
            },
            {
                id: 3,
                label: "Tomatoes"
            },
            {
                id: 4,
                label: "Cheese"
            }
        ],
        Stages: [
            {
                label: "Zapiekanka"
            },
            {
                label: "Dodatki"
            }

        ]
    }
}

export const recipeModule = {
    state: defaultState,
    mutations: {

    },
    actions:{

    },
    getters: {

    }
}