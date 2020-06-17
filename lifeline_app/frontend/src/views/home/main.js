import "../../assets/libs/moment/moment";
import "../../assets/libs/jquery-ui/jquery-ui.min";
import "../../assets/libs/fullcalendar/fullcalendar.min"
import Vue from "vue";
import home from "./home";
import axios from 'axios';
import BootstrapVue from 'bootstrap-vue';
import $ from "jquery";
import 'bootstrap';

Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.prototype.$ajax=axios;
axios.defaults.baseURL='http://127.0.0.1:8000/';
Vue.config.productionTip = false;

new Vue({
  render: h => h(home)
}).$mount("#home");