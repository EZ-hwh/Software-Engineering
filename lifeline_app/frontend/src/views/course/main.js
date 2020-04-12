import Vue from "vue";
import course from "./course";
import router from "./router";
import axios from 'axios';
import "../../components/_globals";
import BootstrapVue from "bootstrap-vue";
import ViewUI from "view-design";
import "view-design/dist/styles/iview.css";

Vue.use(BootstrapVue)
Vue.use(ViewUI);

Vue.config.productionTip = false
Vue.prototype.$ajax=axios;
axios.defaults.baseURL='http://127.0.0.1:8000/';

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(course),
}).$mount("#course");


