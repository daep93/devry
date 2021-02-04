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
    name: 'Main',
    component: () => import('@/views/MainPage.vue'),
  },
  {
    path: '/profile/:id',
    name: 'Profile',
    component: () => import('@/views/ProfilePage.vue'),
  },
  {
    path: '/profile-setting',
    name: 'ProfileSetting',
    component: () => import('@/views/ProfileSettingPage.vue'),
  },
  {
    path: '/twit',
    name: 'Twit',
    component: () => import('@/views/TwitPage.vue'),
  },
  {
    path: '/qna',
    name: 'QnA',
    component: () => import('@/views/QnaPage.vue'),
  },
  {
    // path: '/qna/:id',
    path: '/qna-detail/:id',
    name: 'QnaDetail',
    component: () => import('@/views/QnaDetailPage.vue'),
  },
  {
    path: '/qna/create',
    name: 'QnACreate',
    component: () => import('@/views/QnaPageCreate.vue'),
  },
  {
    path: '/qna/:id',
    name: 'QnAUpdate',
    component: () => import('@/views/QnaPageUpdate.vue'),
  },
  {
    path: '/forum',
    name: 'Forum',
    component: () => import('@/views/ForumPage.vue'),
  },
  {
    // 추후 id값으로 수정 필요
    path: '/forum/forum-detail',
    name: 'ForumDetail',
    component: () => import('@/views/ForumDetailPage.vue'),
  },
  {
    path: '/event',
    name: 'Event',
    component: () => import('@/views/EventPage.vue'),
  },
  {
    // path: '/event/:id',
    path: '/event-detail',
    name: 'EventDetail',
    component: () => import('@/views/EventDetailPage.vue'),
  },
  {
    path: '/jobs',
    name: 'Jobs',
    component: () => import('@/views/JobsPage.vue'),
  },
  {
    path: '*',
    component: () => import('@/views/NotFoundPage.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
