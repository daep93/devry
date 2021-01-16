<template>
  <div>
    <div class="row justify-start " style="height:10%">
      <p class="text-h5 text-weight-bolder">
        Signup
      </p>
    </div>
    <div class="row" style="height:55%">
      <signup-form @signupSuccess="$emit('signupSuccess')"></signup-form>
    </div>
    <!-- 로그인 이동 -->
    <div class="row justify-center text-grey-6" style=" width:400px;">
      <span>이미 계정이 있으신가요?</span>
      <span
        @click="moveToLogin"
        class="text-light-blue-13 q-ml-sm"
        style="cursor:pointer"
        >로그인하기</span
      >
    </div>
    <!-- SNS로 가입하기 -->
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
import SignupForm from '@/components/signup/SignupForm.vue';
export default {
  components: {
    SignupForm,
  },
  methods: {
    moveToLogin() {
      this.$store.commit('setAccountModalType', 'login');
    },
  },
};
</script>

<style scoped></style>
