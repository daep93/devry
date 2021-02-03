import { instance } from '@/api';

function loadQnaItem(postId) {
  return instance.get(`qna/${postId}`)
}
function createQnaItem(postData) {
  return instance.post('qna', postData);
}
function updateQnaItem(postId, postData) {
  return instance.put(`qna/${postId}`, postData);
}
export { loadQnaItem, createQnaItem, updateQnaItem };