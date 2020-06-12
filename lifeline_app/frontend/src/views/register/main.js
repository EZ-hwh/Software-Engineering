import Vue from "vue";
import Register from "./Register";
import axios from 'axios';
import BootstrapVue from 'bootstrap-vue';


Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.prototype.$ajax=axios;
axios.defaults.baseURL='http://127.0.0.1:8000/';

Vue.config.productionTip = false;

new Vue({
  render: h => h(Register)
}).$mount("#register");