<template>
  <q-form @submit.prevent="submitForm" style="width:400px; height:665px; margin: 0 auto;">
    <q-icon
      @click="offModal"
      :name="$i.ionCloseOutline"
      class="close-button"
      style="width:30px; height:30px; margin-left: 370px"
    >
    </q-icon>
    <div class="title text-h6 text-weight-bold">Create new password</div>
    <q-input
      class="input"
      v-model="newPwd"
      type="password"
      label="password"
      label-slot
      placeholder="6-12자 이내의 새로운 비밀번호를 입력해주세요"
      style="width:400px;"
      stack-label
      :dense="dense"
      :error="!isValidPwd"
    >
      <template v-slot:label>
        <h5 class="text-primary">새 비밀번호</h5>
        <br />
      </template>
      <template v-slot:error>
        <div class="text-red-8" v-if="newPwd.length < 6">
          6자 이상의 비밀번호를 입력해주세요
        </div>
        <div class="text-red-8" v-else-if="newPwd.length > 12">
          12자 이하의 비밀번호를 입력해주세요
        </div>
        <div class="text-red-8" v-else-if="newPwd === password">
          이전의 비밀번호와 다른 비밀번호를 입력해주세요
        </div>
        <div class="text-red-8" v-else>
          특수문자를 제외하고 입력해주세요
        </div>
      </template>
    </q-input>
    <q-input
      class="input"
      v-model="confirmNewPwd"
      type="password"
      label="confirm password"
      placeholder="비밀번호를 다시 한 번 입력해주세요"
      style="width:400px;"
      stack-label
      :dense="dense"
      :error="!isValidPwdConfirm"
      error-message="비밀번호를 다시 확인해주세요"
    >
      <template v-slot:label>
        <h5 class="text-primary">비밀번호 확인</h5>
        <br />
      </template>
    </q-input>
    <q-btn
      :disabled="!checkForm"
      class="save-button"
      color="primary"
      label="SAVE"
      style="width:400px; height:50px;"
      type="submit"
    />
  </q-form>
</template>

<script>
import { changePwdUser } from '@/api/auth';
import { validatePwd } from '@/utils/validation';
export default {
  data() {
    return {
      password: '12345678',
      jwt: this.$route.query.jwt,
      newPwd: '',
      confirmNewPwd: '',
      dense: false,
      login: false
    }
  },
  computed: {
    isValidPwd() {
      return (
        (this.newPwd === '' || validatePwd(this.newPwd)) &&
        this.newPwd !== this.password
      );  
    },
    isValidPwdConfirm() {
      return this.confirmNewPwd === '' || this.newPwd === this.confirmNewPwd;
    },
    checkForm() {
      return (
        validatePwd(this.newPwd) &&
        this.newPwd === this.confirmNewPwd &&
        this.newPwd !== this.password
      );
    },
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
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    async submitForm() {
      const config = this.setToken()
      try {
        // await changePwdUser({
        //   password: this.newPwd,
        // });
        console.log(this.password)
        this.password = this.newPwd
        console.log(this.password)
        alert('비밀번호 변경에 성공하였습니다!')
      } catch (error) {
        console.log(error);
        console.log('error발생')
        // console.log(old_password)
      }
    }
  },
  created() {
    // 로그인 되어있는 상태인지 확인
    const token = localStorage.getItem('jwt')
    if (token) {
      this.login = true
    }
  }
}
</script>

<style scoped>
.title {
  margin-bottom: 30px;
  padding-top: 30%;
}

.close-button {
  padding-top: 30px;
}

.input {
  margin-bottom: 25px;
}

.save-button {
  margin-top: 50px;
}

</style>
