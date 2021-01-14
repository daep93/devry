<template>
  <account-modal>
    <div class="q-pa-md row">
      <!-- 로그인 이미지 -->
      <div
        class="col-6 row justify-center"
        style="display: flex; align-items: center;"
      >
        <q-img
          :src="require('@/assets/login.png')"
          alt="login"
          style="width:552px; heigth:680px; vertical-align:middle;"
        />
      </div>
      <!-- 로그인 컨텐츠 -->
      <div class="col-6">
        <login-form></login-form>
      </div>
    </div>
  </account-modal>
</template>

<script>
import AccountModal from '@/components/common/AccountModal';
import LoginForm from './LoginForm.vue';
export default {
  components: { AccountModal, LoginForm }
};
</script>

<style scoped></style>
