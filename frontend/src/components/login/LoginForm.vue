<template>
  <div style="width:400px; height:665px; margin: 0 auto;">
    <q-icon
      @click="offModal"
      :name="$i.ionCloseOutline"
      class="close-button"
      style="width:30px; height:30px; margin-left: 370px"
    >
    </q-icon>
    <div class="title text-h6 text-weight-bold">Sign in</div>
    <div>
      <form @submit="checkForm" method="post" novalidate="true">
        <!-- <p v-if="errors.length">
          <b>[ 오류 ]</b>
          <li v-for="(error, idx) in errors" :key="idx">{{ error }}</li>
        </p> -->
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
        <div v-if="emailErrors.length" style="font-size:3px">
          <span v-for="(error, idx) in emailErrors" :key="idx">{{ error }}</span>
        </div>

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
        <div v-if="passwordErrors.length" style="font-size:3px">
          <span v-for="(error, idx) in passwordErrors" :key="idx">{{ error }}</span>
        </div>

        <div
          @click="fingPwdModal"
          class="password-info text-right"
          style="font-size:3px"
        >
          비밀번호를 잊으셨나요?
        </div>
        <q-btn
          @click="goToMain"
          color="primary"
          label="SIGN IN"
          style="width:400px; height:50px;"
          type="submit"
        />
      </form>
      <!-- :disabled="password.length > 15 || password.length < 6" -->
      <div class="no-account text-center" style="font-size:3px;">
        아직 계정이 없으신가요?
        <span @click="signupModal" class="text-primary">회원가입</span>
      </div>
    </div>
    <div class="row justify-around">
      <q-btn size="18px" round color="white">
        <q-icon name="img:google.svg" size="45px"></q-icon>
      </q-btn>  
      <q-btn size="18px" round color="white">
        <q-icon name="img:github.svg" size="45px"></q-icon>
      </q-btn>
      <q-btn size="18px" round color="white">
        <q-icon name="img:facebook.svg" size="45px"></q-icon>
      </q-btn>
      <q-btn size="18px" round color="white">
        <q-icon name="img:kakao.svg" size="45px"></q-icon>
      </q-btn>
    </div>
  </div>
</template>

<script>
// import { validateEmail } from '@/utils/validation';
export default {
  data() {
    return {
      email: '',
      password: '',
      dense: false,
      // errors: [],
      emailErrors: [],
      passwordErrors: [],
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
    offModal() {
      this.$store.commit('offAccountModal');
    },
    checkForm(e) {
      e.preventDefault();
      this.errors = [];
      if (!this.email) {
        this.emailErrors.push('이메일은 필수입니다.');
        // this.errors.push('이메일은 필수입니다.');
      } else if (!this.validEmail(this.email)) {
        this.emailErrors.push('이메일 형식을 다시 확인해주세요.');
        // this.errors.push('이메일 형식을 다시 확인해주세요.');
      }
      if (!this.password) {
        this.passwordErrors.push('비밀번호는 필수입니다.');
        // this.errors.push('비밀번호는 필수입니다.');
      }
      if (this.password.length < 6) {
        this.passwordErrors.push('비밀번호는 6글자 이상입니다.');
        // this.errors.push('비밀번호는 6글자 이상입니다.');
      } else if (this.password.length > 15) {
        this.passwordErrors.push('비밀번호는 15글자 이하입니다.');
        // this.errors.push('비밀번호는 15글자 이하입니다.');
      }
      // if (!this.emailErrors.length || !this.passwordErrors.length) return true;
      // if (!this.errors.length) return true;
    },
    validEmail(email) {
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
  },
  // computed: {
  //   isEmailValid() {
  //     return validateEmail(this.email);
  //   },
  // },
}
</script>

<style scoped>
.title {
  margin-bottom: 30px;
  padding-top: 20%;
}

.close-button {
  padding-top: 30px;
}

.input {
  margin-bottom: 25px;
}

.password-info {
  margin-bottom: 40px;
}

.no-account {
  margin-top: 10px;
  margin-bottom: 20px;
}
</style>
