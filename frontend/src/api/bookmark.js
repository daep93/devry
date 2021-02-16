import { instance } from '@/api';

// QnA 북마크 리스트 가져오기
function getQnaBookmarkList() {
  return instance.get(`qna/mybookmark/`);
}

// Event 북마크 리스트 가져오기
function getEventBookmarkList() {
  return instance.get(`event/mybookmark/`);
}

export { getQnaBookmarkList, getEventBookmarkList };
