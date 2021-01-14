import { instance } from '@/api';
function registerUser(userData) {
  return instance.post('api/register/', userData);
}
function loginUser(userData) {
  return instance.post('login', userData);
}

export { registerUser, loginUser };
