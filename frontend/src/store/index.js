import Vue from 'vue';
import Vuex from 'vuex';

// import {
//   saveAuthToCookie,
//   saveUserIdToCookie,
//   saveUserNicknameToCookie,
//   getAuthFromCookie,
//   getUserIdFromCookie,
//   getUserNicknameFromCookie,
// } from '@/utils/cookies';
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    accountModal: false,
    accountModalType: 'login',
  },
  getters: {
    getAccountModal(state) {
      return state.accountModal;
    },
    getAccountModalType(state) {
      return state.accountModalType;
    },
  },
  mutations: {
    onAccountModal(state) {
      state.accountModal = true;
    },
    offAccounModal(state) {
      state.accountModal = false;
    },
    setAccountModalType(state, type) {
      state.accountModalType = type;
    },
  },
  actions: {},
  modules: {},
});
