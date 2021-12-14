import { mutations } from '@/store'


describe('basic store test ', () => {
  
  const { newRecipe, resetRecipe } = mutations 

  const recipe = {
    Title: "Pierogi",
    Category: "Polish",
    Description: "MM  pankcakes good",
    Rating: 4.5,
    RatingCount: 400,
    steps: [
      { number: 1, title: "Step one", description: "pour milk into bowl"},
      { number: 2, title: "Step tow", description: "pour more milk into bowl"}
    ]
}

  it('new recipe set ', () => {
    
    const state = { 
      recipe: {
        Title: "Pancakes",
        Category: "Polish",
        Description: "MM  pankcakes good",
        Rating: 4.5,
        RatingCount: 400,
        steps: [
          { number: 1, title: "Step one", description: "pour milk into bowl"},
          { number: 2, title: "Step tow", description: "pour more milk into bowl"}
        ]
    }
    }

    newRecipe(state, recipe)
    
    expect(state.recipe).toBe(recipe)

  })

  it('recpie reset ', () => {
    
    const state = { 
      recipe: {
        Title: "Pancakes",
        Category: "Polish",
        Description: "MM  pankcakes good",
        Rating: 4.5,
        RatingCount: 400,
        steps: [
          { number: 1, title: "Step one", description: "pour milk into bowl"},
          { number: 2, title: "Step tow", description: "pour more milk into bowl"}
        ]
    }
    }

    newRecipe(state, recipe)
    resetRecipe(state)

    expect(state.recipe).toBe(null)

  })
})

