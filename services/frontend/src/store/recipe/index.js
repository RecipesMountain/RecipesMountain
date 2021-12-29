import { api } from "@/api";

const defaultState = {
  error: "",
  errorStatus: false,
  recipe: {
    Id: 0,
    Title: "",
    Description: "",
    Author: "Anonymous",
    AuthorId: 1,
    Time: 0.5,
    Difficulty: "",
    Rating: 4,
    RatingCount: 1000,
    Calories: 200,
    Servings: 3.5,
    Tags: [
      {
        id: 1,
        name: "Pasta",
      },
      {
        id: 2,
        name: "In Oven",
      },
      {
        id: 3,
        name: "Tomatoes",
      },
      {
        id: 4,
        name: "Cheese",
      },
      {
        id: 5,
        name: "Oregano",
      },
      {
        id: 6,
        name: "Onion",
      },
    ],
    Stages: [       
      {
        name: "Zapiekanka",
        content: "",
        ingredients: [
          {
            label: "makaron świderki",
            amount: "100",
            unit: "g",
            unitHint: "grams",
          },
          {
            label: "rosół z kury Knorr",
            amount: "1",
            unit: "pc.",
            unitHint: "piece",
          },
          {
            label: "filet z kurczaka",
            amount: "1",
            unit: "pc.",
            unitHint: "piece",
          },
          {
            label: "pomidor",
            amount: "1",
            unit: "pc.",
            unitHint: "piece",
          },
          {
            label: "przecier pomidorowy",
            amount: "2",
            unit: "tbsp",
            unitHint: "table spoon",
          },
        ],
        steps: [
          {
            content:
              "Cebulę pokrój w piórka, czosnek przeciśnij przez praskę. Podsmaż je na oleju.",
          },
          { content: "Ugotuj makaron na sposób al dente." },
          {
            content:
              "Warzywa pokrój w paski i wraz z kurczakiem dodaj do całości. Duś około 15 minut. Następnie podlej szklanką wody i dodaj kostkę Rosołu z kury Knorr oraz przecier pomidorowy.",
          },
          {
            content:
              "Makaron wyłóż do naczynia żaroodpornego, zalej sosem i posyp startym serem. Włóż do piekarnika nagrzanego do 180 stopni na 20 minut. Następnie podawaj.",
          },
        ],
      },
      {
        name: "Dodatki",
        ingredients: [
          {
            label: "ketchup",
            amount: "100",
            unit: "g",
            unitHint: "grams",
          },
          {
            label: "musztarda",
            amount: "200",
            unit: "g",
            unitHint: "grams",
          },
        ],
        steps: [
            
          ]
      },
    ],
    // TO CHANGE
    ImageUrls: [
      {
        src: "https://s3.przepisy.pl/przepisy3ii/img/variants/800x0/zapiekanka-makaronowa-pychotka.jpg",
      },
    ],
  },
};

export const recipeModule = {
  state: defaultState,
  mutations: {
    setRecipeId(state, payload){
        state.recipe.Id = payload
    },
    setTitle(state, payload) {
        state.recipe.Title = payload
    },
    setDescription(state, payload) {
        state.recipe.Description = payload
    },
    setAuthor(state, payload){
      state.recipe.Author = payload
    },
    setAuthorId(state, payload){
      state.recipe.AuthorId = payload
    },
    setTime(state, payload){
      state.recipe.Time = payload 
    },
    setDifficulty(state, payload){
      state.recipe.Difficulty = payload
    },
    setRating(state, payload){
      state.recipe.Rating = payload
    },
    setRatingCount(state, payload){
      state.recipe.RatingCount = payload
    },
    setCalories(state, payload){
      state.recipe.Calories = payload
    },
    setServings(state, payload){
      state.recipe.Servings = payload
    },
    setTags(state, payload){
      state.recipe.Tags = payload
    },
    setStages(state, payload){
      state.recipe.Stages = payload
    },
    setError(state, payload){
      state.error = payload
    },
    setErrorStatus(state, payload){
      state.errorStatus = payload
    }

    // TODO TAGS AND STAGES
    // set(state, payload){
    //   state.recipe. = payload
    // },

  },
  actions: {
    async actionGetRecipe(context, payload) {
      try {
        const response = await api.getRecipe(payload)
        if (response.data) {
            context.commit("setTags", response.data.tags)
            context.commit("setStages", response.data.stages)
        }
        else {
            console.log("Something gone wrong")
        }      
      } catch (error) {
        context.commit("setErrorStatus", true)
        context.commit("setError", error)
        // await context.dispatch("actionCheckApiError", error);
      }
    },
    async actionGetRecipeInfo(context, payload) {
      try{
        const response = await api.getRecipe(payload)
        if(response.data) {
          console.log(response.data)
          context.commit("setTitle", response.data.title)
          context.commit("setDescription", "")
          context.commit("setTime", response.data.cookingTime)
          context.commit("setDifficulty", response.data.difficulty)
          context.commit("setRating", response.data.rating)
          context.commit("setCalories", response.data.calories)
          context.commit("setServings", response.data.portion)
          context.commit("setTags", response.data.tags)
          
        }
        else {
          console.log("Something gone wrong")
        }
      }
      catch(error) {
        await console.log("error")
        await context.commit("setErrorStatus", true)
        // context.commit("setError", error)
        // await context.dispatch("actionCheckApiError", error);
      }
    }
  },
  getters: {
    title: (state) => state.recipe.Title,
    description: (state) => state.recipe.Description,
    author: (state) => state.recipe.Author,
    authorId: (state) => state.recipe.AuthorId,
    time: (state) => state.recipe.Time,
    difficulty: (state) => state.recipe.Difficulty,
    rating: (state) => state.recipe.Rating,
    ratingCount: (state) => state.recipe.RatingCount,
    calories: (state) => state.recipe.Calories,
    servings: (state) => state.recipe.Servings,
    tags: (state) => state.recipe.Tags,
    stages: (state) => state.recipe.Stages,
    images: (state) => state.recipe.ImageUrls,
    errorStatus: (state) => state.errorStatus,
  },
};
