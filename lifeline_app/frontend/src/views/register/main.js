import Vue from "vue";
import Register from "./Register";
import axios from 'axios';
import BootstrapVue from 'bootstrap-vue';
import "../../assets/css/font.css"
import ViewUI from "view-design";
import "view-design/dist/styles/iview.css";


Vue.use(BootstrapVue)
Vue.use(ViewUI)
Vue.config.productionTip = false
Vue.prototype.$ajax=axios;
axios.defaults.baseURL='http://127.0.0.1:8000/';

Vue.config.productionTip = false;

new Vue({
  render: h => h(Register)
}).$mount("#register");