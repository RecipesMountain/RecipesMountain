import { api } from "@/api";

const defaultState = {
  error: "",
  errorStatus: false,
  submitStatus: false,
  recipe: {
    id: "0",
    title: "",
    description: "",
    author: "Anonymous",
    authorId: 0,
    time: 0,
    difficulty: "",
    rating: 0,
    ratingCount: 0,
    calories: 0,
    servings: 0,
    tags: [],
    stages: [],
    image: "https://s3.przepisy.pl/przepisy3ii/img/variants/800x0/zapiekanka-makaronowa-pychotka.jpg",

  },
  isLiked: false,
  allProducts: [],
  allTags: [],
  units: [
    {
      label: "ounce",
      shortcut: "oz",
    },
    {
      label: "gram",
      shortcut: "g",
    },
    {
      label: "pound",
      shortcut: "pd",
    },
    {
      label: "kilogram",
      shortcut: "kg",
    },
    {
      label: "liter",
      shortcut: "l",
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
      label: "milliliter",
      shortcut: "ml",
    },
  ],
  // units: [
  //   {
  //     label: "gram",
  //     shortcut: "g",
  //   },
  //   {
  //     label: "kilogram",
  //     shortcut: "kg",
  //   },
  //   {
  //     label: "piece",
  //     shortcut: "pc.",
  //   },
  //   {
  //     label: "pinch",
  //     shortcut: "pinch",
  //   },
  //   {
  //     label: "tablespoon",
  //     shortcut: "tbsp.",
  //   },
  //   {
  //     label: "teaspoon",
  //     shortcut: "tsp.",
  //   },
  //   {
  //     label: "cup",
  //     shortcut: "cup",
  //   },
  //   {
  //     label: "decagram",
  //     shortcut: "dag",
  //   },
  //   {
  //     label: "liter",
  //     shortcut: "l",
  //   },
  //   {
  //     label: "pack",
  //     shortcut: "pack",
  //   },
  //   {
  //     label: "milliliter",
  //     shortcut: "ml",
  //   },
  // ],
};

export const recipeModule = {
  state: defaultState,
  mutations: {
    setRecipeId(state, payload){
        state.recipe.id = payload
    },
    setTitle(state, payload) {
        state.recipe.title = payload
    },
    setDescription(state, payload) {
        state.recipe.description = payload
    },
    setAuthor(state, payload){
      state.recipe.author = payload
    },
    setAuthorId(state, payload){
      state.recipe.authorId = payload
    },
    setTime(state, payload){
      state.recipe.time = payload 
    },
    setDifficulty(state, payload){
      state.recipe.difficulty = payload
    },
    setRating(state, payload){
      state.recipe.rating = payload
    },
    setRatingCount(state, payload){
      state.recipe.ratingCount = payload
    },
    setCalories(state, payload){
      state.recipe.calories = payload
    },
    setServings(state, payload){
      state.recipe.servings = payload
    },
    setTags(state, payload){
      state.recipe.tags = payload
    },
    setStages(state, payload){
      state.recipe.stages = payload
    },
    setError(state, payload){
      state.error = payload
    },
    setErrorStatus(state, payload){
      state.errorStatus = payload
    },
    setImage(state, payload){
      state.recipe.image = payload
    },
    setAllTags(state, payload){
      state.allTags = payload
    },
    setAllProducts(state, payload){
      state.allProducts = payload
    },
     setSubmitStatus(state, payload){
       state.submitStatus = payload
     },
     setIsLiked(state, payload){
       state.isLiked = payload
     }
  },
  actions: {

    async actionGetProducts(context){
      try{
        const response = await api.getProducts()
        if(response.data){
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
        if(context.rootState.user.isLoggedIn){
          const likeResponse = await api.getIsLiked(context.rootState.user.token, payload)
          context.commit("setIsLiked", likeResponse.data)
        }
        if (response.data) {
          context.commit("setRecipeId", response.data.id)
          context.commit("setAuthor", response.data.owner)
          context.commit("setTitle", response.data.title)
          context.commit("setDescription", "")
          context.commit("setTime", response.data.cookingTime)
          context.commit("setDifficulty", response.data.difficulty)
          context.commit("setRating", response.data.rating)
          context.commit("setCalories", response.data.calories)
          context.commit("setServings", response.data.portion)
          context.commit("setTags", response.data.tags)
          context.commit("setTags", response.data.tags)
          context.commit("setStages", response.data.stages)
          context.commit("setErrorStatus", false)
        }
        else {
            context.commit("openSnackbar", "Something gone wrong")
            console.log("Something gone wrong")
        }      
      } catch (error) {
        context.commit("setErrorStatus", true)
        context.commit("setError", error)
        context.commit("openSnackbar", "Recipe not found")
      }
    },
    async actionGetRecipeImg(context, payload){
      try{
        const imageLink = await api.getRecipeImage(payload)        
        context.commit("setImage", imageLink.request.responseURL)
        
      }
      catch(error){
        console.log(error)
      }
    },
    async actionSubmitRecipe(context, payload){
      try {
        const response = await api.createRecipe(context.rootState.user.token, payload)

        if(response.status == 200)
        {
          context.commit("setSubmitStatus", true)
          context.commit("setRecipeId", response.data.id)
          context.commit("openSnackbar", "Succesfully added new recipe")
          context.commit("setErrorStatus", false)
        }
        else{
          context.commit("setSubmitStatus", false)
          context.commit("setErrorStatus", true)
          context.commit("openSnackbar", "Something went wrong")
        }
      }
      catch(error){
        console.log(error)
        context.commit("openSnackbar", "Server error")
      }
    },
    async actionUpdateRecipe(context, payload){
      try{
        const response  = await api.updateRecipe(context.rootState.user.token, payload, context.state.recipe.id)
        if(response.status == 200){
          context.commit("setSubmitStatus", true)
          context.commit("setRecipeId", response.data.id)
          context.commit("openSnackbar", "Succesfully updated recipe")

        }
        else{
          console.log("something went wrong")
          context.commit("setErrorStatus", true)
          context.commit("openSnackbar", "Something went wrong")
        }
      }
      catch(error){
        console.log(error)
        context.commit("openSnackbar", "Server error")
      }
    },
    async actionAddRecipeImage(context, payload)
    {
      try{
        const response = await api.sendImage(context.rootState.user.token, payload, context.state.recipe.id)
        if(response.status == 200)
        {
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
    },
    async actionLikeUnlikeRecipe(context, payload){
      try{
        if(!context.rootState.user.isLoggedIn){
          context.commit("openSnackbar", "To like recipe you have to be logged in!")
        }
        else{
          const response = await api.updateLikeStatus(context.rootState.user.token, payload)
          context.commit("setIsLiked", response.data)
          if(response.data){
            context.commit("openSnackbar", "Liked")
          }
          else{
            context.commit("openSnackbar", "Disliked")
          }

        }
      }
      catch(error){
        console.log(error)
        console.log("error",error.response)
        context.commit("openSnackbar", "Server error")
      }
    }

  },
  getters: {
    recipe: (state) => state.recipe,
    recipeId: (state) => state.recipe.id,
    title: (state) => state.recipe.title,
    description: (state) => state.recipe.description,
    author: (state) => state.recipe.author,
    authorId: (state) => state.recipe.authorId,
    time: (state) => state.recipe.time,
    difficulty: (state) => state.recipe.difficulty,
    rating: (state) => state.recipe.rating,
    ratingCount: (state) => state.recipe.ratingCount,
    calories: (state) => state.recipe.calories,
    servings: (state) => state.recipe.servings,
    tags: (state) => state.recipe.tags,
    stages: (state) => state.recipe.stages,
    errorStatus: (state) => state.errorStatus,
    imageLink: (state) => state.recipe.image,
    units: (state) => state.units,
    allTags: (state) => state.allTags,
    allProducts: (state) => state.allProducts,
    isLiked: (state) => state.isLiked,
  },
};
