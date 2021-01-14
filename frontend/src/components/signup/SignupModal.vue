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
        <q-form @submit.prevent="" style="height:60%">
          <div class="row" style="height:80%">
            <!-- 회원가입 입력 form -->
            <signup-form></signup-form>
          </div>
          <!-- Signup 버튼  -->
          <div class="row" style="height:20%">
            <q-btn
              color="blue-12"
              class="text-center"
              style="width:400px;height:50px;border-radius:5px;font-size:16pt"
              type="submit"
              >회원가입</q-btn
            >
          </div>
        </q-form>
        <!-- SNS로 가입하기 -->
        <div class="row justify-around " style=" width:400px">
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
    </div>
  </account-modal>
</template>

<script>
import AccountModal from '@/components/common/AccountModal.vue';
import SignupForm from '@/components/signup/SignupForm.vue';
export default {
  components: { AccountModal, SignupForm },
  methods: {
    offModal() {
      this.$store.commit('offAccountModal');
    },
  },
  computed: {},
};
</script>

<style scoped></style>
