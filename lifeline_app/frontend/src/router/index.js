import Vue from "vue";
import VueRouter from "vue-router";
import Login from '@/components/Login';
import Helloworld from '@/components/HelloWorld';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Helloworld',
    component: Helloworld
  },
  {
    path: '/a',
    name: 'Login',
    component: Login
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  routes
});

export default router;
