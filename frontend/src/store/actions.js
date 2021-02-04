import { loginUser, logoutUser } from '@/api/auth';
import {
  saveAuthToCookie,
  saveUserIdToCookie,
  saveUserNicknameToCookie,
} from '@/utils/cookies';

export default {
  async CHANGEPWD(context, userData) {
    const { data } = await loginUser(userData);
    return data;
  },
  async LOGIN({ commit }, userData) {
    const { data } = await loginUser(userData);
    // store에 저장
    commit('setToken', data.token);
    commit('setUserid', data.user.id);
    commit('setUsername', data.user.username);

    // 쿠키에 저장
    saveAuthToCookie(data.token);
    saveUserIdToCookie(data.user.id);
    saveUserNicknameToCookie(data.user.username);
    return data;
  },
  async LOGOUT({ commit }) {
    const { data } = await logoutUser();
    commit('setToken', '');
    commit('setUserid', '');
    commit('setUsername', '');
    saveAuthToCookie('');
    saveUserIdToCookie('');
    saveUserNicknameToCookie('');
    return data;
  },
};
