import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'
import store from './store/store.js'

const app = createApp(App).use(router);

app.config.globalProperties.$store = store;

app.mount('#app')
