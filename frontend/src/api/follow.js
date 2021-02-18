import { instance } from '@/api';
//// 팔로워
// 팔로워 목록 불러오기 (나를 팔로우하는 사람)
function getFollowerList() {
  return instance.get('myfollower/');
}

// 팔로이 목록 불러오기 (내가 팔로우하는 사람)
function getFolloweeList() {
  return instance.get('myfollow/');
}

// 특정 유저 팔로우하기
function followOtherUser(want_pk) {
  return instance.post(`following/${want_pk}/`);
}

export { getFollowerList, getFolloweeList, followOtherUser };
