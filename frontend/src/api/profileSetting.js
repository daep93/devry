import { profileSetting } from '@/api';

function loadProfile() {
  return profileSetting.get('/');
}
function updateProfile(profileData) {
  return profileSetting.put('/', profileData);
}
function deleteProfile() {
  return profileSetting.delete('/');
}
export { loadProfile, updateProfile, deleteProfile };
