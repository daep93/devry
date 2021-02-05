import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueMoment from 'vue-moment';
import './quasar';
Vue.use(VueMoment);
Vue.config.productionTip = false;

import Plugin from '@quasar/quasar-ui-qmarkdown';
import '@quasar/quasar-ui-qmarkdown/dist/index.css';

Vue.use(Plugin);

// import {
//   Quasar,
//   Notify
// } from 'quasar'

// Vue.use(Quasar, {
//   plugins: {
//     Notify
//   },
//   config: {
//     notify: { /* look at QUASARCONFOPTIONS from the API card (bottom of page) */ }
//   }
// })

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
