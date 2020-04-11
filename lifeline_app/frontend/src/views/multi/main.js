import Vue from "vue";
import App from "./App";
import router from "./router";
import axios from 'axios';
import BootstrapVue from 'bootstrap-vue';


Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.prototype.$ajax = axios;
axios.defaults.baseURL = "http://127.0.0.1:8000/";

Vue.config.productionTip = false;

new Vue({
    router,
    render: h => h(App)
}).$mount("#multi");