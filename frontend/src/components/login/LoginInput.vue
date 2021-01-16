<template>
  <div style="height:85%">
    <div class="row justify-start " style="height:10%">
      <p class="text-h5 text-weight-bolder">Login</p>
    </div>
    <div class="row" style="height:70%">
      <login-form></login-form>
    </div>
    <!-- 회원가입 이동 -->
    <div class="row justify-center text-grey-6" style=" width:400px;">
      <span>아직 계정이 없으신가요?</span>
      <span
        @click="moveToSignup"
        class="text-light-blue-13 q-ml-sm"
        style="cursor:pointer"
      >
        회원가입하기</span
      >
    </div>

    <!-- SNS 로그인 -->
    <div class="row justify-around q-mt-md" style=" width:400px;">
      <q-btn size="16px" round color="grey-2">
        <q-icon name="img:google.svg"></q-icon>
      </q-btn>
      <q-btn size="16px" round color="black">
        <q-icon name="img:github.svg"></q-icon>
      </q-btn>
      <q-btn size="16px" round style="background-color:#1877F2">
        <q-icon name="img:facebook.svg"></q-icon>
      </q-btn>
      <q-btn size="16px" round color="yellow">
        <q-icon name="img:kakao.svg" size="45px"></q-icon>
      </q-btn>
    </div>
  </div>
</template>

<script>
import LoginForm from '@/components/login/LoginForm';

export default {
  components: { LoginForm },
  methods: {
    moveToSignup() {
      this.$store.commit('setAccountModalType', 'signup');
    },
  },
};
</script>

<style scoped></style>
