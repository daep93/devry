import { instance } from '@/api';

function loginUser(userData) {
  return instance.post('api/login/', userData);
}

export { loginUser };
