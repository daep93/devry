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

export { getQnaList, getEventList, getMainEventList };
