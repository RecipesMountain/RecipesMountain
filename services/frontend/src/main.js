import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

Vue.config.productionTip = false

axios.defaults.baseURL = 'http://'+ window.location.hostname +':5000/';  // the FastAPI backend

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
