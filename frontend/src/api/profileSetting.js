import { profileSetting } from '@/api';

function loadProfile(profileId) {
  return profileSetting.get('/load', profileId);
}
function updateProfile(profileId, profileData) {
  return profileSetting.put('/save', profileId, profileData);
}
export { loadProfile, updateProfile };
