import { instance } from '@/api';
function getProfile(userid) {
  return instance.get(`profile/profilewrite/${userid}`);
}
export { getProfile };
