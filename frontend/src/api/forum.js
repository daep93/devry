import { instance } from '@/api';
import { setInterceptors } from '@/api/common/interceptors';

// forum 글 등록하기
function createForumItem(postData) {
  return setInterceptors(instance).post('forum/', postData);
}

// forum 특정 글 불러오기
function loadForumItem(post_pk) {
  return instance.get(`forum/${post_pk}/`);
}
// forum 글 수정하기
function updateForumItem(postId, postData) {
  return setInterceptors(instance).put(`forum/${postId}/`, postData);
}

// forum  글 삭제하기
function deleteForumItem(postId) {
  return instance.delete(`forum/${postId}/`);
}

// forum 글 좋아요 토글하기
function toggleForumLike(post_pk) {
  return instance.post(`forum_like/${post_pk}/`);
}

// forum 글 pinned 하기
function pinnedForum(post_pk) {
  return instance.post(`forum_pinned/${post_pk}/`);
}

// forum 댓글 목록 불러오기
function getForumComment() {
  return instance.get('comment/');
}

// forum 댓글 등록하기
function createForumComment(postData) {
  return instance.post('comment/', postData);
}

// forum 큰 댓글 수정하기
function updateForumComment(comment_pk, putData) {
  return instance.put(`comment/${comment_pk}/`, putData);
}

// forum 큰 댓글 삭제하기
function deleteForumComment(comment_pk) {
  return instance.delete(`comment/${comment_pk}/`);
}

// forum 큰 댓글 멘션 get
function getForumMentioned(comment_pk) {
  return instance.get(`comment/${comment_pk}/mentioned/`);
}

// forum 큰 댓글 멘션 post
function postForumMentioned(comment_pk) {
  return instance.post(`comment/${comment_pk}/mentioned/`);
}

// forum 큰 댓글 좋아요 토글하기
function toggleForumCommentLike(comment_pk) {
  return instance.post(`comment_like/${comment_pk}/`);
}

// forum 게시물 북마크하기
function toggleforumBookmark(post_pk) {
  return instance.post(`forum_bookmark/${post_pk}/`);
}

export {
  loadForumItem,
  createForumItem,
  updateForumItem,
  deleteForumItem,
  toggleForumLike,
  getForumComment,
  createForumComment,
  updateForumComment,
  deleteForumComment,
  getForumMentioned,
  postForumMentioned,
  toggleForumCommentLike,
  toggleforumBookmark,
  pinnedForum,
};
