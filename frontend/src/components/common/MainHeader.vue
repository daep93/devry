<template>
  <q-header reveal elevated class="bg-primary text-white" height-hint="98">
    <q-toolbar>
      <router-link :to="logolink">
        <q-btn flat round dense :icon="$i.ionPricetags" color="white" />
      </router-link>
      <q-toolbar-title>
        <div class="text-white q-ma-none text-h4">
          <span>
            <router-link :to="logolink">
              StackHub
            </router-link>
          </span>
        </div>
      </q-toolbar-title>
      <q-tabs align="left">
        <q-btn
          :icon="$i.ionPersonCircleOutline"
          label="로그인"
          @click="loginModal"
        ></q-btn>
        <q-btn
          :icon="$i.ionPersonAddOutline"
          label="회원가입"
          @click="signupModal"
        >
        </q-btn>
        <q-btn
          :icon="$i.ionHelpOutline"
          label="비밀번호 찾기"
          @click="fingPwdModal"
        >
        </q-btn>
      </q-tabs>
    </q-toolbar>
  </q-header>
</template>

<script>
export default {
  computed: {
    logolink() {
      return '/main';
    },
  },
  methods: {
    loginModal() {
      this.$store.commit('setAccountModalType', 'login');
      this.$store.commit('onAccountModal');
    },
    signupModal() {
      this.$store.commit('setAccountModalType', 'signup');
      this.$store.commit('onAccountModal');
    },
    fingPwdModal() {
      this.$store.commit('setAccountModalType', 'findPwd');
      this.$store.commit('onAccountModal');
    },
  },
};
</script>

<style scoped>
a {
  color: white;
}
</style>
