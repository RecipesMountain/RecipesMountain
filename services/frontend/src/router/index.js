
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Welcome from '@/views/Welcome.vue'
import AppHome from '@/views/AppHome.vue'
import Login from '@/views/UserViews/Login.vue'
import Register from '@/views/UserViews/Register.vue'
import SearchRecipe from "@/views/RecipeViews/SearchRecipes.vue"
import MyAccount from "@/views/UserViews/MyAccount.vue"
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Welcome',
    component: Welcome
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
    path: '/app/',
    name: 'App',
    component: AppHome,
    beforeEnter: (to, from, next) => {
      if(!store.getters["isLoggedIn"]){
        next({ name: "Welcome"  })
      } else next()
    },
    children: [
      {
        path: '/',
        name: 'Home',
        component: Home
      },
      {
        path: 'search',
        name: 'Search',
        component: SearchRecipe
      },
      {
        path: 'account',
        name: 'MyAccount',
        component: MyAccount
      },
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
