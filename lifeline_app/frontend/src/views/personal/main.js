import Vue from "vue";
import personal from "./personal";
import ViewUI from "view-design";
import "../../assets/css/font.css"
import "view-design/dist/styles/iview.css";
import BootstrapVue from "bootstrap-vue";
import axios from 'axios';
import "../../components/template/_globals";

Vue.config.productionTip = false;
Vue.use(ViewUI);
Vue.use(BootstrapVue);

Vue.prototype.$ajax=axios;
axios.defaults.baseURL='http://127.0.0.1:8000/';

/* eslint-disable no-new */
new Vue({
  render: (h) => h(personal),
}).$mount("#personal");
