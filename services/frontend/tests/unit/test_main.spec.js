import { createLocalVue, mount } from '@vue/test-utils'
import App from '@/App.vue'
import AppBar from '@/components/layout/AppBar.vue'
import Vuetify from 'vuetify'
import VueRouter from 'vue-router'
import s from '@/store'

describe('App mount layout', () => {
    const localVue = createLocalVue()
    let vuetify
    let router

    beforeEach(() => {
      vuetify = new Vuetify()
      router = new VueRouter()
      
    })

    const $store = s;

    it('mount basic layout', () => {
      const wrapper = mount(App, {
        localVue,
        vuetify,
        router,
        mocks: {
          $store
        }
      })
      const AppBar = wrapper.findComponent({name: 'AppBar'})
      const Footer = wrapper.findComponent({name: 'AppFooter'})
      expect(AppBar.exists()).toBe(true)
      expect(Footer.exists()).toBe(true)
    })

    it('appbar proper mount', () => {
      const wrapper = mount(AppBar, {
        localVue,
        vuetify,
        router,
        mocks: {
          $store
        }
      })
      const searchBar = wrapper.find('.v-text-field')
      const avatar = wrapper.find('.v-avatar')
      const buttons = wrapper.findAll('.v-btn')
      
      expect(searchBar.exists()).toBe(true)
      expect(avatar.exists()).toBe(true)
      expect(buttons.length).toBe(4)

    })

    // it('appbar mount', () => {
    //   const wrapper = mount(AppBar, {
    //     localVue,
    //     vuetify,
    //     router,
    //   })
    //   const searchBar = wrapper.find('.v-text-field')
    //   expect(AppBar.exists()).toBe(true)
    //   expect(Footer.exists()).toBe(true)
    // })
})