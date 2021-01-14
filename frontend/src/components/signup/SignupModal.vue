<template>
  <account-modal>
    <div class="row" style="height:100%">
      <!-- 회원가입 이미지 -->
      <div class="col-7 ">
        <div class="row justify-center items-center" style="height:100%">
          <q-img
            :src="require('@/assets/signup.jpg')"
            style="width: 552px;height:492px"
          />
        </div>
      </div>
      <div class="col-5">
        <signup-input></signup-input>
      </div>
    </div>
  </account-modal>
</template>

<script>
import AccountModal from '@/components/common/AccountModal.vue';
import SignupInput from '@/components/signup/SignupInput.vue';

export default {
  components: { AccountModal, SignupInput },
  computed: {},
};
</script>

<style scoped></style>
