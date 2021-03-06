import Vue from 'vue';
import '@quasar/extras/material-icons/material-icons.css';
import '@quasar/extras/ionicons-v4/ionicons-v4.css';
import 'quasar/dist/quasar.css';
import { Quasar, Loading, QSpinner, Dialog } from 'quasar';
import * as iconSet from '@quasar/extras/ionicons-v5';
Vue.prototype.$i = iconSet;

import '@quasar/extras/material-icons/material-icons.css';
import '@quasar/extras/ionicons-v4/ionicons-v4.css';

Vue.use(Quasar, {
  config: {
    // Quasar Spinning 파트 참조
    loading: {
      spinner: QSpinner,
      spinnerColor: 'teal-10',
      messageColor: 'white',
      message: '<b>Loading...</b>',
    },
    animations: ['backInLeft', 'backOutLeft', 'fadeIn', 'fadeOut'],
  },
  plugins: { Loading, Dialog },
});
