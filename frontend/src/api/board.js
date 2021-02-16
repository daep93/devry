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

// forum list 불러오기
function getForumList() {
  return board.get(`forum/`);
}

export { getQnaList, getForumList, getEventList, getMainEventList };
