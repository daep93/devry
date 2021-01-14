import { instance } from '@/api';
function registerUser(userData) {
  return instance.post('api/register/', userData);
}
function loginUser(userData) {
  return instance.post('login', userData);
}
function changePwdUser(userData) {
  return instance.get('api/change_password/', userData);
}

export { registerUser, loginUser, changePwdUser }