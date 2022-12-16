import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import * as echarts from 'echarts'
import jQuery from 'jquery'
import axios from 'axios'

const app = createApp(App);

axios.defaults.baseURL = "http://10.181.237.6:8000";
app.config.globalProperties.$http = axios;

app.use(echarts).use(jQuery).use(router).mount('#app');
