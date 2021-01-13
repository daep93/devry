<template>
  <q-dialog v-model="$store.state.accountModal">
    <q-card style="min-width:1200px; height:700px">
      <login-modal
        v-if="$store.getters.getAccountModalType === 'login'"
      ></login-modal>
      <signup-modal
        v-else-if="$store.getters.getAccountModalType === 'signup'"
      ></signup-modal>
      <find-pwd-modal v-else></find-pwd-modal>
    </q-card>
  </q-dialog>
</template>

<script>
import LoginModal from '@/components/login/LoginModal';
import SignupModal from '@/components/signup/SignupModal';
import FindPwdModal from '@/components/findPwd/FindPwdModal';
export default {
  components: { LoginModal, SignupModal, FindPwdModal },
};
</script>

<style scoped></style>
