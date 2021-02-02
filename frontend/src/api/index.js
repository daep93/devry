import axios from 'axios';
import { setInterceptors } from '@/api/common/interceptors';
function createInstance() {
  return axios.create({
    baseURL: process.env.VUE_APP_SERVER_API_URL,
  });
}
function createInstanceWithAuth(url) {
  const instance = axios.create({
    baseURL: `${process.env.VUE_APP_SERVER_API_URL}${url}`,
  });
  return setInterceptors(instance);
}
const instance = createInstance();
const follower = createInstanceWithAuth('follower/');
const followee = createInstanceWithAuth('followee/');
const profileSetting = createInstanceWithAuth('profile/setting');
const board = createInstanceWithAuth('board/');
export { instance, follower, followee, profileSetting, board };
