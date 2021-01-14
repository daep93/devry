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
      <q-form @submit.prevent="submitLoginForm">
        <q-input
          v-model="email"
          clearables
          :clear-icon="$i.ionCloseOutline"
          stack-label
          placeholder="이메일 주소를 입력해주세요"
          type="email"
          label="e-mail"
          style="width:400px;"
          autocapitalize="none"
          :dense="dense"
          :error="!isEmailValid"
        >
        <!-- TODO: [디자인] 타이틀 lable 없음 (글씨 크기 다름) -->
          <template v-slot:error>
            <div class="text-red-8">잘못된 이메일 양식입니다</div>
          </template>
        </q-input>

        <!-- TODO: [로직] X 아이콘 -->
        <q-input
          v-model="password"
          clearable
          :clear-icon="$i.ionCloseOutline"
          stack-label
          bottom-slots
          placeholder="6~12자 영문 대 소문자, 숫자를 사용하세요"
          type="password"
          label="password"
          style="width:400px'"
          :dense="dense"
          :error="!isValidPwd"
        >
          <template v-slot:error>
            <div class="text-red-8" v-if="password.length < 6">
              6자 이상의 비밀번호를 입력해주세요
            </div>
            <div class="text-red-8" v-else-if="password.length > 12">
              12자 이하의 비밀번호를 입력해주세요
            </div>
            <div class="text-red-8" v-else>
              특수문자를 제외하고 입력해주세요
            </div>
          </template>
        </q-input>

        <!-- 비밀번호 찾기 이동 -->
        <div
          @click="fingPwdModal"
          class="password-info text-right"
          style="font-size:3px"
        >
          비밀번호를 잊으셨나요?
        </div>

        <!-- TODO: [디자인] 버튼 색상, 글씨 크기 -->
        <q-btn
          color="primary"
          label="SIGN IN"
          style="width:400px; height:50px; border-radius:5px;"
          :disabled="!checkForm"
          type="submit"
          @click="login"
        />
      </q-form>

      <!-- 회원가입 이동 -->
      <div class="no-account text-center" style="font-size:3px;">
        아직 계정이 없으신가요?
        <span @click="signupModal" class="text-primary">회원가입</span>
      </div>
    </div>

    <!-- SNS 로그인 -->
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
import { validateEmail, validatePwd } from '@/utils/validation';
// import axios from 'axios'

export default {
  data() {
    return {
      email: '',
      password: '',
      dense: false,
    };
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
    async submitLoginForm() {
      try {
        // this.$q.loading.show();
        await this.$store.dispatch('LOGIN', {
          username: this.email,
          password: this.password,
        },
          console.log('로그인 성공'),
          console.log(this.username),
          console.log(this.password),
        );
      } catch (error) {
        console.log('로그인 실패'),
        console.log(error);
      }
      // finally {
      //   this.$q.loading.hide();
      // }
    },
    // login({email, password}) {
    //   const username = this.email
    //   axios.post('http://127.0.0.1:8000/api/login/', {username, password})
    //     .then(res => {
    //       console.log(res)
    //       console.log('111')
    //       console.log('확인')
    //     })
    //     .catch(error => {
    //       console.log(error)
    //       console.log('222')
    //     })
    // }
  },
  computed: {
    isEmailValid() {
      return this.email === '' || validateEmail(this.email);
    },
    isValidPwd() {
      return this.password === '' || validatePwd(this.password);
    },
    checkForm() {
      console.log(validateEmail(this.email))
      return validateEmail(this.email) && validatePwd(this.password);
    },
  },
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
