import { instance } from '@/api';
function registerSmallAnswer(ansData) {
  return instance.post(`qna_small/`, ansData);
}
function getSmallAnswer(postId) {
  return instance.get(`qna_small/${postId}`);
}
export { registerSmallAnswer, getSmallAnswer };
