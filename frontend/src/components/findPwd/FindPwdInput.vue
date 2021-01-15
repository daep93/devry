<template>
  <q-form @submit.prevent="submitForm" style="width:400px; height:665px; margin: 0 auto;">
    <q-icon
      @click="offModal"
      :name="$i.ionCloseOutline"
      class="close-button"
      style="width:30px; height:30px; margin-left: 370px"
    >
    </q-icon>
    <div class="title text-h6 text-weight-bold">Forgot password</div>
    <div class="row" style="width:400px">
      <div class="col-8">
        <q-input
          class="input"
          v-model="email"
          type="email"
          label="email"
          label-slot
          placeholder="이메일을 입력해주세요"
          style="width:250px;"
          stack-label
          :dense="dense"
          :error="!isValidEmail"
        >
          <template v-slot:label>
            <h7>email</h7>
            <br />
          </template>
          <template v-slot:error>
            <div class="text-red-8">
              잘못된 이메일 양식입니다.
            </div>
          </template>
        </q-input>
      </div>  
      <div class="col-1"></div>
      <div class="col-3">
        <q-input
          v-model="nickname"
          clearable
          :clear-icon="$i.ionCloseOutline"
          stack-label
          label-slot
          bottom-slots
        >
          <template v-slot:label>
            <h7>별명</h7>
            <br />
          </template>
        </q-input>
      </div>
    </div>  
    <q-btn
      @click="moveToChangePwd"
      :disabled="!checkForm"
      class="save-button"
      color="primary"
      label="SEND"
      style="width:400px; height:50px;"
      type="submit"
    />
    <!-- @findPwd="emit('findPwd')" -->
  </q-form>
</template>

<script>
import { checkUser } from '@/api/auth';
import { validateEmail } from '@/utils/validation';
export default {
  data() {
    return {
      email: '',
      dense: false,
    }
  },
  computed: {
    isValidEmail() {
      return this.email === '' || validateEmail(this.email);
    },
    checkForm() {
      return (
        validateEmail(this.email)
      );
    },
  },
  methods: {
    offModal() {
      this.$store.commit('offAccountModal');
    },
    async submitForm() {
      try {
        // await checkUser({
        //   email: this.email,
        //   username: this.nickname
        // });
        alert('이메일을 보냈습니다. 비밀번호 변경을 진행해주세요')
        // this.$emit('findPwd');
      } catch (error) {
        alert('에러가 발생했습니다.')
        console.log(error);
        console.log('error발생')
      }
    },
    moveToChangePwd() {
      this.$store.commit('setAccountModalType', '')
    }
  },
  created() {
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
