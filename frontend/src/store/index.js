import Vue from 'vue';
import Vuex from 'vuex';
import { loginUser } from '@/api/auth';
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
    id: getUserIdFromCookie() || '',
    token: getAuthFromCookie() || '',
    nickname: getUserNicknameFromCookie() || '',
    accountModal: false,
    accountModalType: 'login',
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
    offAccountModal(state) {
      state.accountModal = false;
    },
    setAccountModalType(state, type) {
      state.accountModalType = type;
    },
    setUserid(state, id) {
      state.id = id;
    },
    setUsername(state, nickname) {
      state.nickname = nickname;
    },
    setToken(state, token) {
      state.token = token;
    },
    clearUserInfo(state) {
      state.id = '';
      state.nickname = '';
      state.token = '';
    },
  },
  actions: {
    async LOGIN({ commit }, userData) {
      const { data } = await loginUser(userData);
      // store에 저장
      commit('setToken', data.token);
      commit('setUserid', data.user.username);
      commit('setUsername', data.user.nickname);

      // 쿠키에 저장
      saveAuthToCookie(data.token);
      saveUserIdToCookie(data.user.username);
      saveUserNicknameToCookie(data.user.nickname);
      return data;
    },
  },
  modules: {},
});
