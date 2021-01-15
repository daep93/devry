<template>
  <account-modal>
    <div class="q-pa-md row" style="height:100%">
      <!-- 모달 이미지 -->
      <div
        class="col-7 row justify-center flex items-center"
        style="height:100%"
      >
        <q-img
          :src="require('@/assets/change_pwd.png')"
          alt="change-password"
          style="width:552px; height:492px"
        />
      </div>
      <!-- 모달 컨텐츠 -->
      <div class="col-5" style="height:100%">
        <div class="row justify-end" style="height:15%">
          <q-icon
            :name="$i.ionClose"
            class="q-ma-lg"
            size="md"
            @click="offModal"
          ></q-icon>
        </div>
        <find-pwd-auth
          v-if="modalState === 'auth'"
          @authPwdSuccess="modalState = 'reset'"
        ></find-pwd-auth>
        <find-pwd-reset
          v-else-if="modalState === 'reset'"
          @resetPwdSuccess="modalState = 'success'"
        ></find-pwd-reset>
        <find-pwd-success v-else></find-pwd-success>
      </div>
    </div>
  </account-modal>
</template>

<script>
import AccountModal from '@/components/common/AccountModal';
import FindPwdAuth from '@/components/findPwd/FindPwdAuth';
import FindPwdReset from '@/components/findPwd/FindPwdReset';
import FindPwdSuccess from '@/components/findPwd/FindPwdSuccess';
// import FindPwdForm from './FindPwdForm.vue';

export default {
  components: { AccountModal, FindPwdAuth, FindPwdReset, FindPwdSuccess },
  data() {
    return {
      modalState: 'auth',
    };
  },
  methods: {
    offModal() {
      this.$store.commit('offAccountModal');
    },
  },
};
</script>

<style scoped></style>
