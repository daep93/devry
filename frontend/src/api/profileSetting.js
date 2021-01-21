import { instance } from '@/api';
function updateProfile() {
  return instance.put('profile/setting/save');
}
function loadProfile() {
  return instance.get('profile/setting/load');
}

export { updateProfile, loadProfile };