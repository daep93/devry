import { instance } from '@/api';

// Event 내용 불러오기
function getEvent(postId) {
  return instance.get(`event/${postid}/`);
}

// Event 북마크 토글하기
function toggleEventBookmark(postId) {
  return instance.post(`event_bookmark/${postId}/`);
}

export { getEvent, toggleEventBookmark };