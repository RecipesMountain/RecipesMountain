
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/UserViews/Login.vue'
import Register from '@/views/UserViews/Register.vue'
import ExploreRecipes from "@/views/RecipeViews/ExploreRecipes.vue"
import SearchRecipe from "@/views/RecipeViews/SearchRecipes.vue"
import MyAccount from "@/views/UserViews/MyAccount.vue"
import Comment from "@/components/comment/Comment.vue"
import Recipe from "@/views/RecipeViews/Recipe.vue"
import AddRecipe from "@/views/RecipeViews/AddRecipe.vue"
import EditRecipe from "@/views/RecipeViews/EditRecipe.vue"

import store from '@/store'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/search',
    name: 'Search',
    component: SearchRecipe
  },
  {
    path: "/explore/:sort",
    name: "ExploreRecipes",
    component: ExploreRecipes
  },
  {
    path: '/recipes/:id',
    name: 'Recipe',
    component: Recipe
  },
  {
    path: '/addRecipe',
    name: 'AddRecipe',
    component: AddRecipe,
    beforeEnter: (to, from, next) => {
      if(!store.getters["isLoggedIn"]){
        next({ name: "Home"  })
      } else next()
    },
  },
  {
    path: '/editRecipe/:id?',
    name: 'EditRecipe',
    component: EditRecipe,
    beforeEnter: (to, from, next) => {
      if(!store.getters["isLoggedIn"]){
        next({ name: "Home"  })
      } else next()
    },
  },
  {
    path: '/comment',
    name: 'comment',
    component: Comment,
  },
  {
    path: '/user/',
    name: 'MyAccount',
    component: MyAccount,
    beforeEnter: async (to, from, next) => {
      await store.dispatch("actionCheckLoggedIn")
      if (!store.getters["isLoggedIn"]) {
        next({ name: "Home" })
      } else next()
    },
    children: []
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router
