<template>
  <div style="height:100%">
    <div class="row justify-end" style="height:15%">
      <q-icon
        :name="$i.ionClose"
        class="q-ma-lg"
        size="md"
        @click="offModal"
      ></q-icon>
    </div>
    <div class="row justify-start " style="height:10%">
      <p class="text-h4 text-weight-bolder">
        계정 생성
      </p>
    </div>
    <div class="row" style="height:55%">
      <signup-form></signup-form>
    </div>
    <!-- 로그인으로 이동하기 -->
    <div class="row justify-center text-grey-6" style=" width:400px;">
      이미 계정이 있으신가요?&nbsp;&nbsp;
      <a href="#" @click="moveToLogin" class="text-light-blue-13 "
        >로그인하기</a
      >
    </div>
    <!-- SNS로 가입하기 -->
    <div class="row justify-around q-mt-md" style=" width:400px;">
      <q-btn size="16px" round color="blue-8">
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
    offModal() {
      this.$store.commit('offAccountModal');
    },
    moveToLogin() {
      this.$store.commit('setAccountModalType', 'login');
    },
  },
};
</script>

<style scoped></style>
