import {
  getAuthFromCookie,
  getUserIdFromCookie,
  getUserNicknameFromCookie,
} from '@/utils/cookies';

export default {
  id: getUserIdFromCookie() || '',
  token: getAuthFromCookie() || '',
  nickname: getUserNicknameFromCookie() || '',
  accountModal: false,
  accountModalType: 'login',
  followModal: false,
  leftDrawal: true,
  tagFilter: false,
  myTags: [
    'javascript',
    'vue',
    'python',
    'swift',
    'flutter',
    'angular',
    'django',
    'java',
    'typescript',
    'docker',
    'react',
  ],
  selectedTags: [],
};
