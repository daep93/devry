import { board } from '@/api';
function getQnaList() {
  return board.get(`qna`);
}

export { getQnaList };
