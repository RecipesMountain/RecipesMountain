import { createLocalVue, mount } from '@vue/test-utils'
import HelloWorld from '@/components/HelloWorld.vue'
import App from '@/App.vue'
import Vuetify from 'vuetify'
import Vue from 'vue'
import VueRouter from 'vue-router'

// describe('HelloWorld.vue', () => {
//   it('renders props.msg when passed', () => {
//     const msg = 'new message'
//     const wrapper = mount(HelloWorld, {
//       propsData: { msg: msg }
//     })
//     expect(wrapper.text()).toContain(msg)
//   })
// })


describe('App mount layout', () => {
    const localVue = createLocalVue()
    let vuetify
    let router

    beforeEach(() => {
      vuetify = new Vuetify()
      router = new VueRouter()
      
    })

    it('mount basic layout', () => {
      const wrapper = mount(App, {
        localVue,
        vuetify,
        router,
      })
      const AppBar = wrapper.findComponent({name: 'AppBar'})
      expect(AppBar.exists()).toBe(true)
    })
})