import { board } from '@/api';
function getQnaList() {
  return board.get(`qna`);
}

function getEventList() {
  return board.get(`event`);
}

function getMainEventList() {
  return board.get(`event/main`);
}

// // forum list 불러오기
// function getForumList() {
//   return board.get(`forum/`);
// }

// forum board - 최신순 리스트 불러오기
function loadForumNew() {
  return board.get(`forumno`);
}
// // forum board - 최신순 리스트 불러오기
// function loadForumNew() {
//   return board.get(`forum/new`);
// }
// forum board - 좋아요 높은순 리스트 불러오기
function loadForumLike() {
  return board.get(`forum/new`);
}
// forum board - 피드 리스트 불러오기
function loadForumFeed() {
  return board.get(`forum/feed`);
}

// forum board - 추천 글 리스트 불러오기
// API 요청으로 사용자를 한정할 수 없는 경우(토큰이 없는 경우),
// 가입은 되어있지만 아무도 팔로우하지 않아 피드 기능을 이용할 수 없는 경우
function loadForumRecommend() {
  return board.get(`forum/recommend`);
}

export {
  getQnaList,
  getEventList,
  getMainEventList,
  loadForumNew,
  loadForumLike,
  loadForumFeed,
  loadForumRecommend,
};
