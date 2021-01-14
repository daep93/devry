<template>
  <account-modal>
    <div class="q-pa-md row">
      <!-- 모달 이미지 -->
      <div class="col-6 row justify-center flex items-center">
        <q-img 
          :src="require('@/assets/change_pwd.png')" 
          alt="change-password" 
          style="width:552px; heigth:680px; vertical-align:middle;"
        />
      </div>
      <!-- 모달 컨텐츠 -->
      <div class="col-6">
        <find-pwd-form></find-pwd-form>
      </div>
    </div>
  </account-modal>
</template>

<script>
import AccountModal from '@/components/common/AccountModal';
import FindPwdForm from './FindPwdForm.vue';
export default {
  components: { AccountModal, FindPwdForm },
};
</script>

<style scoped></style>
