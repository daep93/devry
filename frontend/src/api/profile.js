import { instance } from '@/api';
function getProfile(userid) {
  return instance.get(`profile/${userid}`);
}
export { getProfile };
