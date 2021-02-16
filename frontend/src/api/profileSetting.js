import { profileSetting } from '@/api';

function loadProfile(profileId) {
  return profileSetting.get(`/${profileId}/`);
}
function updateProfile(profileId, profileData) {
  return profileSetting.put(`/${profileId}/`, profileData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
}
function deleteProfile() {
  return profileSetting.delete('/');
}
export { loadProfile, updateProfile, deleteProfile };
