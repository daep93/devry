import Vue from 'vue';

import 'quasar/dist/quasar.css';
import '@quasar/extras/ionicons-v4/ionicons-v4.css';
import { Quasar, Loading, QSpinner } from 'quasar';
import * as iconSet from '@quasar/extras/ionicons-v5';
Vue.prototype.$i = iconSet;

Vue.use(Quasar, {
  config: {
    loading: {
      spinner: QSpinner,
      spinnerColor: 'teal-10',
      messageColor: 'white',
      message: '<b>Loading...</b>',
    },
    animations: ['backInLeft', 'backOutLeft'],
  },
  plugins: { Loading },
});
