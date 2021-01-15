import { instance } from '@/api';

function loginUser(userData) {
  return instance.post('login/', userData);
}

export { loginUser };
