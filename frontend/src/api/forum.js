import { instance } from '@/api';
// import { setInterceptors } from '@/api/common/interceptors';

// forum 글 불러오기
function loadForumItem(post_pk) {
  return instance.get(`forum/${post_pk}/`);
}

// forum 글 좋아요 토글하기
function toggleForumLike(post_pk) {
  return instance.post(`forum_like/${post_pk}/`);
}

// forum 댓글 등록하기
function createForumComment(postData) {
  return instance.post('comment/', postData);
}

// QnA 큰 댓글 수정하기
function updateForumComment(comment_pk, putData) {
  return instance.put(`comment/${comment_pk}/`, putData);
}

// QnA 큰 댓글 삭제하기
function deleteForumComment(comment_pk) {
  return instance.delete(`comment/${comment_pk}/`);
}

// QnA 큰 댓글 좋아요 토글하기
function toggleForumCommentLike(comment_pk) {
  return instance.post(`comment_like/${comment_pk}/`);
}

export {
  loadForumItem,
  toggleForumLike,
  createForumComment,
  updateForumComment,
  deleteForumComment,
  toggleForumCommentLike,
};
