import { profileSetting } from '@/api';

function loadProfile(profileId) {
  return profileSetting.get(`/${profileId}/`);
}
function updateProfile(profileId, profileData) {
  return profileSetting.put(`/${profileId}/`, profileData);
}
function deleteProfile() {
  return profileSetting.delete('/');
}
export { loadProfile, updateProfile, deleteProfile };
