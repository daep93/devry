<template>
  <q-layout view="hHh lpR fFf" style="width:100vw">
    <main-header />
    <account-modal></account-modal>
    <follow-modal></follow-modal>
    <side-bar></side-bar>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import MainHeader from '@/components/common/MainHeader';
import SideBar from '@/components/common/SideBar';
import AccountModal from '@/components/common/AccountModal';
import FollowModal from '@/components/follow/FollowModal.vue';
export default {
  components: {
    MainHeader,
    AccountModal,
    FollowModal,
    SideBar,
  },
};
</script>

<style>
a {
  text-decoration: none;
}
</style>
