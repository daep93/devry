import axios from 'axios';
// import { setInterceptors } from '@/api/common/interceptors';
function createInstance() {
  return axios.create({
    baseURL: process.env.VUE_APP_SERVER_API_URL,
  });
}
const instance = createInstance();

export { instance };