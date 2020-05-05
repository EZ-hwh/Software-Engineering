import Vue from 'vue'
import Router from 'vue-router'
import personal from '../components/personal'
import '../assets/css/bootstrap.min.css'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'personal',
      component: personal
    }
  ]
})
