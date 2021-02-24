import { instance } from '@/api';
function getProfile(userid) {
  return instance.get(`profiles/${userid}`);
}
function getProfiles() {
  return instance.get('profiles/');
}
export { getProfile, getProfiles };
