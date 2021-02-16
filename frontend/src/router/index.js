import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '@/store/index';
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
    beforeEnter: (to, from, next) => {
      if (!store.getters.isLogined) {
        alert('로그인이 필요합니다');
        return;
      }
      next();
    },
  },
  {
    path: '/qna',
    name: 'QnA',
    component: () => import('@/views/qna/QnaPage.vue'),
  },
  {
    path: '/qna-detail/:id',
    name: 'QnaDetail',
    component: () => import('@/views/qna/QnaDetailPage.vue'),
  },
  {
    path: '/qna/create',
    name: 'QnACreate',
    component: () => import('@/views/common/PostCreatePage.vue'),
    beforeEnter: (to, from, next) => {
      if (!store.getters.isLogined) {
        alert('로그인이 필요합니다');
        return;
      }
      next();
    },
  },
  {
    path: '/qna/:id',
    name: 'QnAUpdate',
    component: () => import('@/views/common/PostUpdatePage.vue'),
    beforeEnter: (to, from, next) => {
      if (!store.getters.isLogined) {
        alert('로그인이 필요합니다');
        return;
      }
      next();
    },
  },
  {
    path: '/forum/create',
    name: 'ForumCreate',
    component: () => import('@/views/forum/ForumCreatePage.vue'),
    beforeEnter: (to, from, next) => {
      if (!store.getters.isLogined) {
        alert('로그인이 필요합니다');
        return;
      }
      next();
    },
  },
  {
    path: '/forum/:id',
    name: 'ForumUpdate',
    component: () => import('@/views/forum/ForumUpdatePage.vue'),
    beforeEnter: (to, from, next) => {
      if (!store.getters.isLogined) {
        alert('로그인이 필요합니다');
        return;
      }
      next();
    },
  },
  {
    path: '/forum',
    name: 'Forum',
    component: () => import('@/views/forum/ForumPage.vue'),
  },
  {
    // 추후 id값으로 수정 필요
    path: '/forum-detail/:id',
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
    path: '/event-detail/:id',
    name: 'EventDetail',
    component: () => import('@/views/event/EventDetailPage.vue'),
  },
  {
    path: '/event-update/:id',
    name: 'EventUpdate',
    component: () => import('@/views/event/EventUpdatePage.vue'),
    beforeEnter: (to, from, next) => {
      if (!store.getters.isLogined && Number(store.state.id) <= 5) {
        alert('관리자만 가능합니다');
        next('/main');
        return;
      }
      next();
    },
  },
  {
    path: '/event-registration/',
    name: 'EventRegistration',
    component: () => import('@/views/event/EventRegistrationPage.vue'),
    beforeEnter: (to, from, next) => {
      if (!store.getters.isLogined && Number(store.state.id) <= 5) {
        alert('관리자만 가능합니다');
        next('/main');
        return;
      }
      next();
    },
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
