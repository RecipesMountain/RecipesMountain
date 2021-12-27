
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/UserViews/Login.vue'
import Register from '@/views/UserViews/Register.vue'
import SearchRecipe from "@/views/RecipeViews/SearchRecipes.vue"
import MyAccount from "@/views/UserViews/MyAccount.vue"
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
    path: '/user/',
    name: 'MyAccount',
    component: MyAccount,
    beforeEnter: (to, from, next) => {
      if(!store.getters["isLoggedIn"]){
        next({ name: "Home"  })
      } else next()
    },
    children: [
      {//duplicate to shot how to do sup routures 
        path: '/account',
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
