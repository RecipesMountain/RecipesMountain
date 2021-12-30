import { api } from "@/api";

const defaultState = {
  error: "",
  errorStatus: false,
  submitStatus: false,
  units: [
    {
      label: "gram",
      shortcut: "g",
    },
    {
      label: "kilogram",
      shortcut: "kg",
    },
    {
      label: "piece",
      shortcut: "pc.",
    },
    {
      label: "pinch",
      shortcut: "pinch",
    },
    {
      label: "tablespoon",
      shortcut: "tbsp.",
    },
    {
      label: "teaspoon",
      shortcut: "tsp.",
    },
    {
      label: "cup",
      shortcut: "cup",
    },
    {
      label: "decagram",
      shortcut: "dag",
    },
    {
      label: "litre",
      shortcut: "l",
    },
    {
      label: "pack",
      shortcut: "pack",
    },
    {
      label: "millilitre",
      shortcut: "ml",
    },
  ],
  recipe: {
    Id: "0",
    Title: "",
    Description: "",
    Author: "Anonymous",
    AuthorId: 0,
    Time: 0,
    Difficulty: "",
    Rating: 0,
    RatingCount: 0,
    Calories: 0,
    Servings: 0,
    Tags: [],
    Stages: [],
    Image: "https://s3.przepisy.pl/przepisy3ii/img/variants/800x0/zapiekanka-makaronowa-pychotka.jpg",

  },
  allProducts: [],
  allTags: [],
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
    },
    setImage(state, payload){
      state.recipe.Image = payload
    },
    setAllTags(state, payload){
      state.allTags = payload
    },
    setAllProducts(state, payload){
      state.allProducts = payload
    },
     setSubmitStatus(state, payload){
       state.submitStatus = payload
     }
  },
  actions: {

    async actionGetProducts(context){
      try{
        const response = await api.getProducts()
        if(response.data){
          console.log(response.data)
          context.commit("setAllProducts", response.data)
        }
        else {
          console.log("Something gone wrong")
      } 
      }
      catch(error){
        context.commit("setErrorStatus", true)
        context.commit("setError", error)
      }
    },
    async actionGetTags(context){
      try{
        const response = await api.getTags()
        if(response.data){
          context.commit("setAllTags", response.data)
        }
        else {
          console.log("Something gone wrong")
      } 
      }
      catch(error){
        context.commit("setErrorStatus", true)
        context.commit("setError", error)
      }
    },
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
    },
    async actionGetRecipeImg(context, payload){
      try{
        const imageLink = await api.getRecipeImage(payload)
        
        context.commit("setImage", imageLink)
        
      }
      catch(error){
        console.log(error)
      }
    },
    async actionSubmitRecipe(context, payload){
      try {
        const response = await api.createRecipe(context.rootState.user.token, payload)
        console.log(response)
        if(response.status == 200)
        {
          console.log("success")
          context.commit("setSubmitStatus", true)
          context.commit("setRecipeId", response.data.id)
        }
        else{
          context.commit("setSubmitStatus", false)
          context.commit("setErrorStatus", true)
        }
      }
      catch(error){
        console.log(error)
      }
    },
    async actionAddRecipeImage(context, payload)
    {
      try{
        // console.log(context.state)
        const response = await api.sendImage(context.rootState.user.token, payload, context.state.recipe.Id)
        if(response.status == 200)
        {
          console.log("success")
          context.commit("setSubmitStatus", true)
        }
        else{
          context.commit("setSubmitStatus", false)
          context.commit("setErrorStatus", true)
        }
      }
      catch(error){
        console.log(error)
      }
    }

  },
  getters: {
    recipeId: (state) => state.recipe.Id,
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
    errorStatus: (state) => state.errorStatus,

    imageLink: (state) => state.recipe.Image,

    units: (state) => state.units,
    allTags: (state) => state.allTags,
    allProducts: (state) => state.allProducts,
  },
};
