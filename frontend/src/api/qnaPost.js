import { instance } from '@/api';
function registerSmallAnswer(ansData) {
  return instance.post(`qna_small/`, ansData);
}
function getSmallAnswer(postId) {
  return instance.get(`qna_small/${postId}/`);
}
function toggleQnaLike(postId) {
  return instance.post(`qna_like/${postId}/`);
}
export { registerSmallAnswer, getSmallAnswer, toggleQnaLike };
