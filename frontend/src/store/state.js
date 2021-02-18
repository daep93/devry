import {
  getAuthFromCookie,
  getUserIdFromCookie,
  getUserNicknameFromCookie,
  getUserMyTagsFromCookie,
} from '@/utils/cookies';

export default {
  id: getUserIdFromCookie() || '',
  token: getAuthFromCookie() || '',
  nickname: getUserNicknameFromCookie() || '',
  myTags: getUserMyTagsFromCookie() ? getUserMyTagsFromCookie() : [],
  liquidTagGuideModal: false,
  accountModal: false,
  accountModalType: 'login',
  follow: {
    modal: false,
    tab: 'follow',
  },
  leftDrawal: true,
  tagFilter: false,
  selectedTags: [],
  tags_selected: {
    Angular: true,
    BackEnd: true,
    CSS3: true,
    Django: true,
    Docker: true,
    FrontEnd: true,
    HTML5: true,
    Java: true,
    JavaScript: true,
    MariaDB: true,
    MySQL: true,
    'Node.js': true,
    Python3: true,
    React: true,
    Spring: true,
    TypeScript: true,
    'Vue.js': true,
  },
  all_tag_list: [
    'Angular',
    'Backend',
    'CSS3',
    'Django',
    'Docker',
    'Frontend',
    'HTML5',
    'Java',
    'JavaScript',
    'MariaDB',
    'MySql',
    'Node.js',
    'Python3',
    'React',
    'Spring',
    'TypeScript',
    'Vue.js',
  ],
};
