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
  follow: {
    modal: false,
    tab: 'follow',
  },
  leftDrawal: true,
  tagFilter: false,
  myTags: [
    'javascript',
    'vue.js',
    'python3',
    'backend',
    'frontend',
    'angular',
    'django',
    'java',
    'typescript',
    'docker',
    'react',
  ],
  selectedTags: [],
};
