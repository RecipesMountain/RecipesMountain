import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
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
  },
  mutations: {
    //synchros
    newRecipe (state, newRecipe) {
      state.recipe = newRecipe;
    },
    resetRecipe(state) {
      state.recipe = null;
    },
    setUsers(state, newUsers) {
      state.users = newUsers;
    }
  },
  actions: {
    async getUsers(state) {
       let users = await axios.get("users/?skip=0&limit=100").json();
       console.log(users);
       state.commit("setUsers", users);
    }
  },
  modules: {
  },
  getters: {
    getCurrentRecipe: state => state.recipe ,
    hasRecipe: state => state.recipe === null ? false : true,
    users: state => state.users === undefined ? false : state.users
  }
})