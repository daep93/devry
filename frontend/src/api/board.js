import { board } from '@/api';
function getQnaList() {
  return board.get(`qna`);
}

// forum list 불러오기
function getForumList() {
  return board.get(`forum/`);
}

export { getQnaList, getForumList };
