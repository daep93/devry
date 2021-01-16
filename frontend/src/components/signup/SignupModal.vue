<template>
  <account-modal>
    <div class="q-pa-md row" style="height:100%">
      <!-- 회원가입 이미지 -->
      <div class="col-7 ">
        <div class="row justify-center items-center" style="height:100%">
          <q-img
            :src="require('@/assets/signup.jpg')"
            style="width: 552px;height:492px"
          />
        </div>
      </div>
      <div class="col-5" style="height:100%">
        <div class="row justify-end" style="height:15%">
          <q-icon
            :name="$i.ionClose"
            class="q-ma-lg"
            size="md"
            @click="offModal"
          ></q-icon>
        </div>
        <signup-input
          @signupSuccess="modalState = 'success'"
          v-if="modalState === 'input'"
        ></signup-input>
        <signup-success v-else-if="modalState === 'success'"></signup-success>
      </div>
    </div>
  </account-modal>
</template>

<script>
import AccountModal from '@/components/common/AccountModal';
import SignupInput from '@/components/signup/SignupInput';
import SignupSuccess from '@/components/signup/SignupSuccess';

export default {
  components: { AccountModal, SignupInput, SignupSuccess },
  data() {
    return {
      modalState: 'input',
    };
  },
  computed: {},
  methods: {
    offModal() {
      this.$store.commit('offAccountModal');
    },
  },
};
</script>

<style scoped></style>
