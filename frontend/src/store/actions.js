import { loginUser } from '@/api/auth';
import {
  saveAuthToCookie,
  saveUserIdToCookie,
  saveUserNicknameToCookie,
} from '@/utils/cookies';

export default {
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
  async LOGIN({ commit }, userData) {
    const { data } = await loginUser(userData);
    // store에 저장
    commit('setToken', data.token);
    commit('setUserid', data.user.email);
    // commit('setUserid', data.user.username);
    // commit('setUsername', data.user.nickname);

    // 쿠키에 저장
    saveAuthToCookie(data.token);
    saveUserIdToCookie(data.user.email);
    // saveUserIdToCookie(data.user.username);
    saveUserNicknameToCookie(data.user.nickname);
    return data;
  },
};
