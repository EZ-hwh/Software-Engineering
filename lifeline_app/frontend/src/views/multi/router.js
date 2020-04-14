import Vue from "vue";
import VueRouter from "vue-router";
import Login from "../login/Login";
import first from "../first/first";
import Register from "../register/Register";

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
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
