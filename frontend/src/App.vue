<template>
  <q-layout view="hHh lpR fFf" class="bg-blue-grey-1">
    <main-header />
    <account-modal></account-modal>
    <follow-modal></follow-modal>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import MainHeader from '@/components/common/MainHeader';
import AccountModal from '@/components/common/AccountModal';
import FollowModal from '@/components/follow/FollowModal.vue';
export default {
  components: {
    MainHeader,
    AccountModal,
    FollowModal,
  },
};
</script>

<style>
a {
  text-decoration: none;
}
</style>
