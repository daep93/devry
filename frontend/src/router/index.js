import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    redirect: '/forum',
  },
  {
    path: '/main',
    redirect: '/forum',
    // name: 'Main',
    // component: () => import('@/views/MainPage.vue'),
  },
  {
    path: '/profile/:id',
    name: 'Profile',
    component: () => import('@/views/profile/ProfilePage.vue'),
  },
  {
    path: '/profile-setting',
    name: 'ProfileSetting',
    component: () => import('@/views/profile/ProfileSettingPage.vue'),
  },
  {
    path: '/twit',
    name: 'Twit',
    component: () => import('@/views/TwitPage.vue'),
  },
  {
    path: '/qna',
    name: 'QnA',
    component: () => import('@/views/qna/QnaPage.vue'),
  },
  {
    // path: '/qna/:id',
    path: '/qna-detail/:id',
    name: 'QnaDetail',
    component: () => import('@/views/qna/QnaDetailPage.vue'),
  },
  {
    path: '/qna/create',
    name: 'QnACreate',
    component: () => import('@/views/common/PostCreatePage.vue'),
  },
  {
    path: '/qna/:id',
    name: 'QnAUpdate',
    component: () => import('@/views/common/PostUpdatePage.vue'),
  },
  {
    path: '/forum',
    name: 'Forum',
    component: () => import('@/views/forum/ForumPage.vue'),
  },
  {
    // 추후 id값으로 수정 필요
    path: '/forum/forum-detail',
    name: 'ForumDetail',
    component: () => import('@/views/forum/ForumDetailPage.vue'),
  },
  {
    path: '/event',
    name: 'Event',
    component: () => import('@/views/event/EventPage.vue'),
  },
  {
    // path: '/event/:id',
    path: '/event-detail',
    name: 'EventDetail',
    component: () => import('@/views/event/EventDetailPage.vue'),
  },
  {
    path: '/jobs',
    name: 'Jobs',
    component: () => import('@/views/JobsPage.vue'),
  },
  {
    path: '*',
    component: () => import('@/views/common/NotFoundPage.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
