import { instance, instanceAuth } from '@/api';
function registerUser(userData) {
  return instance.post('signup/', userData);
}
function loginUser(userData) {
  return instance.post('login/', userData);
}
function checkUser(userData) {
  return instance.post('password_reset/', userData);
}
function changePwdUser(userData) {
  return instance.put('change_password/', userData);
}
function logoutUser() {
  return instanceAuth.post('logout/');
}
export { registerUser, loginUser, checkUser, changePwdUser, logoutUser };
