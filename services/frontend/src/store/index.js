import Vue from 'vue'
import Vuex from 'vuex'
import { userModule } from "./user";
import { api } from '../api';

Vue.use(Vuex)

const state = { 
  search: {
    recipes: [],
    nextRecipes: [],
    tags: "",
    keyword: null,
    sort: "popularity",
    page: 1,
    perPage: 20,
  },
}

export const mutations = {
      //synchros
      setRecipes(state, newRecipes) {
        state.search.recipes = newRecipes
      },
      setNextRecipes(state, newRecipes) {
        state.search.nextRecipes = newRecipes
      },
      setTags(state, newTags) {
        state.search.tags = newTags
      },
      setKeyword(state, keyword) {
        state.search.keyword = keyword
      },
      setPage(state, newPage) {
        state.search.page = newPage
      },
      setSort(state, newSort) {
        state.search.sort = newSort
      }
}

export const actions = {
 async search(context, payload) {
   try {
      context.commit("setKeyword", payload.keyword)
      context.commit("setTags", payload.tags)
      context.commit("setSort", payload.sort)

      let recipes = await doSearch(context);
      getNextPage(context);
      console.log(recipes)
   } catch (error) {
     //TODO handle error correctly
     console.log(error)
   }
  },
  async nextPage(context) {
    try {
      context.commit("setPage", context.state.search.page + 1)
      context.commit("setRecipes", context.state.search.nextRecipes)
      getNextPage(context);
    } catch (error) {
     //TODO handle error correctly
     console.log(error)
    }
  },
  async previousPage(context) {
    try {
      context.commit("setPage", context.state.search.page - 1)
      context.commit("setNextRecipes", context.state.search.recipes)
      await doSearch(context);
    } catch (error) {
     //TODO handle error correctly
     console.log(error)
    }
  },
}

export const getters = {
  getRecipes: (state) => state.search.recipes,
  hasNextPage: (state) => (state.search.nextRecipes.length == 0) ? false : true,
  hasPreviousPage: (state) => (state.search.page != 1) ? true : false,
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

async function doSearch(context) {
  let skip = (context.state.search.page - 1) * context.state.search.perPage;
  let limit = context.state.search.page * context.state.search.perPage;
  let response = await api.search(context.state.user.token, context.state.search.keyword, context.state.search.tags, context.state.search.sort, skip, limit);
  let recipes = response.data;
  context.commit("setRecipes", recipes);
  return recipes;
}

async function getNextPage(context) {
  let skip = context.state.search.page * context.state.search.perPage;
  let limit = (context.state.search.page + 1) * context.state.search.perPage;
  let response = await api.search(context.state.user.token, context.state.search.keyword, context.state.search.tags, context.state.search.sort, skip, limit);
  let recipes = response.data;
  context.commit("setNextRecipes", recipes);
  return recipes;
}

