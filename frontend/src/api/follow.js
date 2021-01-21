import { follower, followee } from '@/api';
//// 팔로워
// 팔로워 목록 불러오기
function getFollower(unitData) {
  return follower.get('/', unitData);
}
// 팔로워 팔로잉하기
function followFollower() {
  return follower.put('following/:id/');
}
// 팔로워 팔로잉 해제하기
function unfollowFollower() {
  return follower.put('unfollowing/:id/');
}

//// 팔로이 (내가 팔로우 하는 사람)
// 팔로이 목록 불러오기
function getFollowee(unitData) {
  return followee.get('/', unitData);
}
// 팔로이 해제하기
function unfollowFollowee() {
  return followee.put('/unfollowing/:id/');
}
// 팔로잉하기
function followingUser() {
  return followee.put('/following/:id/');
}

export {
  getFollower,
  followFollower,
  unfollowFollower,
  getFollowee,
  unfollowFollowee,
  followingUser,
};
