import { instance } from '@/api';

// QnA 글 불러오기
function loadQnaItem(postId) {
  return instance.get(`qna/${postId}/`);
}
// QnA 글 등록하기
function createQnaItem(postData) {
  return instance.post('qna/', postData);
}
// QnA 글 수정하기
function updateQnaItem(postId, postData) {
  return instance.put(`qna/${postId}/`, postData);
}
// QnA  글 삭제하기
function deleteQnaItem(postId) {
  return instance.delete(`qna/${postId}/`);
}
// QnA 작은 댓글 등록하기
function registerSmallAnswer(ansData) {
  return instance.post(`qna_small/`, ansData);
}
// QnA 작은 댓글들 불러오기
function getSmallAnswers(postId) {
  return instance.get(`qna_small/${postId}/`);
}
// QnA 글 좋아요 토글하기
function toggleQnaLike(postId) {
  return instance.post(`qna_like/${postId}/`);
}
export {
  registerSmallAnswer,
  getSmallAnswers,
  toggleQnaLike,
  loadQnaItem,
  createQnaItem,
  updateQnaItem,
  deleteQnaItem,
};
