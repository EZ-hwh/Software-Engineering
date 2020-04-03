import Vue from "vue";
import VueRouter from "vue-router";
import Login from '../views/Login';
import first from "../views/first";
import Register from "../views/Register";
import home from "../views/home";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'first',
    component: first
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path:'/Register',
    name: 'Register',
    component: Register
  },
  {
    path:'/UserHome/:id',
    name: 'UserHome',
    component: home
  }

];

const router = new VueRouter({
  routes
});

export default router;
