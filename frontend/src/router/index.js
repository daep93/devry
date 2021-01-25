import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    redirect: '/main',
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
    path: '*',
    component: () => import('@/views/NotFoundPage.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
