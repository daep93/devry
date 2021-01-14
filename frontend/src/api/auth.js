import { instance } from '@/api';
function registerUser(userData) {
  return instance.post('register/', userData);
}
function loginUser(userData) {
  return instance.post('login', userData);
}

export { registerUser, loginUser };
