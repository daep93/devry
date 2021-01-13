<template>
  <div style="width:400px; height:665px; margin: 0 auto;">
    <q-icon 
      :name="$i.ionCloseOutline" 
      class="close-button"
      style="width:30px; height:30px; margin-left: 370px">
    </q-icon>
    <div class="title text-h6 text-weight-bold">Sign in</div>
    <div>
      <q-input 
        class="input"
        v-model="email" 
        type="email" 
        label="e-mail" 
        placeholder="이메일 주소를 입력해주세요" 
        style="width:400px;" 
        stack-label 
        :dense="dense" 
      />
      <q-input 
        class="input"
        v-model="password" 
        type="password" 
        label="password" 
        placeholder="비밀번호를 입력해주세요" 
        style="width:400px'" 
        stack-label 
        :dense="dense" 
      />
      <div 
        @click="fingPwdModal" 
        class="password-info text-right" 
        style="font-size:3px">
        비밀번호를 잊으셨나요?
      </div>
      <q-btn 
        @click="goToMain"
        :disabled="password.length > 15 || password.length < 6"
        color="primary" 
        label="SIGN IN" 
        style="width:400px; height:50px;"
        />
      <div class="no-account text-center" style="font-size:3px;">
        아직 계정이 없으신가요? 
        <span @click="signupModal" class="text-primary">회원가입</span>
      </div>
    </div>
    <div class="q-pa-md row justify-center items-start">
      <q-img 
        :src="require('@/assets/google.png')" 
        alt="google" 
        style="width:62px; heigth:62px;"
      />
      <q-img 
        :src="require('@/assets/github.png')" 
        alt="google" 
        style="width:62px; heigth:62px;"
      />
      <q-img 
        :src="require('@/assets/facebook.png')" 
        alt="google" 
        style="width:62px; heigth:62px;"
      />
      <q-img 
        :src="require('@/assets/kakao.png')" 
        alt="google" 
        style="width:62px; heigth:62px;"
      />
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      email: '',
      password: '',
      dense: false
    }
  },
  methods: {
    signupModal() {
      this.$store.commit('setAccountModalType', 'signup');
      this.$store.commit('onAccountModal');
    },
    fingPwdModal() {
      this.$store.commit('setAccountModalType', 'findPwd');
      this.$store.commit('onAccountModal');
    },
    // goToMain() {
    //   this.$router.push({ path: '/main' })
    // }
  }
}
</script>

<style scoped>
  .title{
    margin-bottom: 30px;
    padding-top: 20%;
  }

  .close-button{
    padding-top: 30px;
  }

  .input{
    margin-bottom: 25px;
  }

  .password-info{
    margin-bottom: 40px;
  }

  .no-account{
    margin-top: 10px;
    margin-bottom: 20px;
  }
</style>

