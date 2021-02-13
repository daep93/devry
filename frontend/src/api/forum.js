import { instance } from '@/api';
// import { setInterceptors } from '@/api/common/interceptors';

// forum 글 불러오기
function loadForumItem(postId) {
  return instance.get(`forum/${postId}/`);
}

export { loadForumItem };
