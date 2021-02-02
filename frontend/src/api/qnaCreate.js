// TODO : api 수정하기
import { qnaCreate } from '@/api';

function createQnaItem(postId) {
  return qnaCreate.post('/qna', postId);
}
function updateQnaItem(postId, postData) {
  return qnaCreate.put(`/qna/${postId}`, postData);
}
export { createQnaItem, updateQnaItem };