import { instance } from '@/api';
function getProfile(userid) {
  return instance.get(`profiles/${userid}`);
}
export { getProfile };
