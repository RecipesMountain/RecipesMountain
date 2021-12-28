import { api } from "@/api";

const defaultState = {
  recipe: {
    Title: "Recipe Title",
    Description: "Recipe Description",
    Author: "Magda Krzesler",
    AuthorId: 1,
    Time: 0.5,
    Difficulty: 0,
    Rating: 1,
    RatingCount: 1000,
    Calories: 200,
    Servings: 3.5,
    Tags: [
      {
        id: 1,
        label: "Pasta",
      },
      {
        id: 2,
        label: "In Oven",
      },
      {
        id: 3,
        label: "Tomatoes",
      },
      {
        id: 4,
        label: "Cheese",
      },
      {
        id: 5,
        label: "Oregano",
      },
      {
        id: 6,
        label: "Onion",
      },
    ],
    Stages: [
      {
        label: "Zapiekanka",
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
        label: "Dodatki",
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
  mutations: {},
  actions: {
    async actionGetRecipe(context) {
      try {
        const response = await api.getMe(
          context.state.token,
          context.state.userID
        );
        if (response.data) {
          console.log("Yest");
        }
      } catch (error) {
        await context.dispatch("actionCheckApiError", error);
      }
    },
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
  },
};
