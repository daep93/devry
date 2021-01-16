<template>
  <account-modal>
    <div class="q-pa-md row" style="height:100%">
      <!-- 로그인 이미지 -->
      <div class="col-7 row justify-center items-center" style="height:100%">
        <q-img
          :src="require('@/assets/login.png')"
          style="width: 552px;height:492px"
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
        <login-input></login-input>
      </div>
    </div>
  </account-modal>
</template>

<script>
import AccountModal from '@/components/common/AccountModal';
import LoginInput from '@/components/login/LoginInput';

export default {
  components: { AccountModal, LoginInput },
  methods: {
    offModal() {
      this.$store.commit('offAccountModal');
    },
  },
};
</script>

<style scoped></style>
