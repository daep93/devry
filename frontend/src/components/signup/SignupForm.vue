<template>
  <div>
    <div class="row" style="width:400px">
      <div class="col-8">
        <q-input
          v-model="email"
          clearable
          :clear-icon="$i.ionCloseOutline"
          stack-label
          label-slot
          :input-style="{ width: '180px' }"
          bottom-slots
          placeholder="ssafyPark@edu.ssafy.com"
          :error="!isValidEmail"
        >
          <template v-slot:label>
            <h5 class="text-primary">이메일</h5>
            <br />
          </template>
          <template v-slot:error>
            <div class="text-red-8">잘못된 이메일 양식입니다</div>
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
          :input-style="{ width: '110px' }"
          bottom-slots
        >
          <template v-slot:label>
            <h5 class="text-primary">별명</h5>
            <br />
          </template>
        </q-input>
      </div>
    </div>
    <br />
    <br />
    <q-input
      v-model="password1"
      clearable
      :clear-icon="$i.ionCloseOutline"
      stack-label
      label-slot
      placeholder="6~12자 영문 대 소문자, 숫자를 사용하세요"
      type="password"
      :error="!isValidPwd"
    >
      <template v-slot:label>
        <h5 class="text-primary">비밀번호</h5>
        <br />
      </template>
      <template v-slot:error>
        <div class="text-red-8" v-if="password1.length < 6">
          6자 이상의 비밀번호를 입력해주세요
        </div>
        <div class="text-red-8" v-else-if="password1.length > 12">
          12자 이하의 비밀번호를 입력해주세요
        </div>
        <div class="text-red-8" v-else>
          특수문자를 제외하고 입력해주세요
        </div>
      </template>
    </q-input>
    <br />
    <br />
    <q-input
      v-model="password2"
      clearable
      :clear-icon="$i.ionCloseOutline"
      stack-label
      label-slot
      placeholder="다시 한번 비밀번호를 입력해주세요"
      type="password"
      :error="!isValidPwdConfirm"
      error-message="다시 비밀번호를 확인해주세요"
    >
      <template v-slot:label>
        <h5 class="text-primary">비밀번호 확인</h5>
        <br />
      </template>
    </q-input>
  </div>
</template>

<script>
import { validateEmail, validatePwd } from '@/utils/validation';
export default {
  data() {
    return {
      email: '',
      nickname: '',
      password1: '',
      password2: '',
    };
  },
  computed: {
    isValidEmail() {
      return this.email === '' || validateEmail(this.email);
    },
    isValidPwd() {
      return this.password1 === '' || validatePwd(this.password1);
    },
    isValidPwdConfirm() {
      return this.password2 === '' || this.password1 === this.password2;
    },
  },
};
</script>

<style scoped></style>
