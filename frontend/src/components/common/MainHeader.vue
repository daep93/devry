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
              DEVRY
            </router-link>
          </span>
        </div>
      </q-toolbar-title>
      <q-tabs align="left">
        <!-- 로그인 하기 이전 보여지는 버튼 구현 -->
        <q-btn-dropdown label="Before Login">
          <q-list bordered>
            <q-item @click="loginModal" clickable>
              <q-item-section avatar>
                <q-icon :name="$i.ionPersonCircleOutline"></q-icon>
              </q-item-section>
              <q-item-section>
                로그인
              </q-item-section>
            </q-item>
            <q-item @click="signupModal" clickable>
              <q-item-section avatar>
                <q-icon :name="$i.ionPersonAddOutline"></q-icon>
              </q-item-section>
              <q-item-section>
                회원가입
              </q-item-section>
            </q-item>
          </q-list>
        </q-btn-dropdown>
        <!-- 로그인 이후 보여지는 버튼 구현 -->
        <q-btn-dropdown label="After Login">
          <q-list bordered>
            <q-item @click="moveToProfilePage" clickable>
              <q-item-section avatar>
                <q-icon :name="$i.ionHappyOutline"></q-icon>
              </q-item-section>
              <q-item-section>
                프로필
              </q-item-section>
            </q-item>
            <q-item @click="moveToProfileSettingPage" clickable>
              <q-item-section avatar>
                <q-icon :name="$i.ionColorWandOutline"></q-icon>
              </q-item-section>
              <q-item-section>
                프로필 설정
              </q-item-section>
            </q-item>
            <q-item @click="followModal" clickable>
              <q-item-section avatar>
                <q-icon :name="$i.ionPeopleCircleOutline"></q-icon>
              </q-item-section>
              <q-item-section>
                팔로워/팔로우
              </q-item-section>
            </q-item>
          </q-list>
        </q-btn-dropdown>
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
    followModal() {
      this.$store.commit('onFollowModal');
    },
    moveToProfilePage() {
      this.$router.push(`/profile/${this.$store.getters.getAccountId}`);
    },
    moveToProfileSettingPage() {
      this.$router.push(`/profile-setting/${this.$store.getters.getAccountId}`);
    },
  },
};
</script>

<style scoped>
a {
  color: white;
}
</style>
