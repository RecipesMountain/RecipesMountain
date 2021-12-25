import Vue from 'vue'
import Vuex from 'vuex'
import { userModule } from "./user";
import { api } from '../api';

Vue.use(Vuex)

const state = { 
  search: {
    recipes: [],
    tags: [],
    keyword: null,
  },
}

export const mutations = {
      //synchros
      setRecipes(state, newRecipes) {
        state.search.recipes = newRecipes
      },
      setTags(state, newTags) {
        state.search.tags = newTags
      },
      setKeyword(state, keyword) {
        state.search.keyword = keyword
      }
}

export const actions = {
 async search(context, payload) {
   try {
      let response = await api.search(context.state.user.token, payload.keyword, payload.tags, payload.sort, payload.skip, payload.limit);
      console.log(response)
      let recipes = response.data
      context.commit("setRecipes", recipes)
      console.log(recipes)
      let tags = []
      for(let recipe of recipes){
        for(let tag of recipe.tags) {
          if(!tags.includes(tag))
            tags.push(tag)
        }
      }

      context.commit("setTags", tags)
   } catch (error) {
     //TODO handle error correctly
     console.log(error)
   }
  }
}

export const getters = {
  getRecipes: (state) => state.search.recipes,
  getTags: (state) => state.search.tags,
  getKeyword: (state) => state.search.keyword,
}

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters,
  modules: {
    user: userModule,
  }
})