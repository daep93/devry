import Vue from 'vue';
import Vuex from 'vuex';

import {
  saveAuthToCookie,
  saveUserIdToCookie,
  saveUserNicknameToCookie,
  getAuthFromCookie,
  getUserIdFromCookie,
  getUserNicknameFromCookie,
} from '@/utils/cookies';
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    accountModal: false,
    accountModalType: 'login',
    id: getUserIdFromCookie() || '',
    token: getAuthFromCookie() || '',
    nickname: getUserNicknameFromCookie() || '',
  },
  getters: {
    isLogined(state) {
      return state.id !== '';
    },
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
    setUsername(state, nickname) {
      state.nickname = nickname;
    },
    setToken(state, token) {
      state.token = token;
    },
    setPassword(state, password) {
      state.password = password;
    }
  },
  actions: {
    async CHANGEPWD({ commit }, userData) {
      const { data } = await loginUser(userData);
      // store에 저장
      commit('setToken', data.token);
      commit('setUserid', data.user.email);
      commit('setPassword', data.user.password);
      commit('setUsername', data.user.nickname);

      // 쿠키에 저장
      saveAuthToCookie(data.token);
      saveUserIdToCookie(data.user.email);
      saveUserIdToCookie(data.user.username);
      saveUserNicknameToCookie(data.user.nickname);
      return data;
    },

  },
  modules: {},
});
