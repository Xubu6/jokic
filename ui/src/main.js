import { createApp } from 'vue'
import { Quasar } from 'quasar'

// Import icon libraries
import '@quasar/extras/roboto-font/roboto-font.css'
import '@quasar/extras/material-icons/material-icons.css'

// Import Quasar css
import 'quasar/src/css/index.sass'

import App from './App.vue'
import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8080/api';

const rootApp = createApp(App);
rootApp.use(Quasar, {
    plugins: {},
})

rootApp.mount('#app')
