<template>
  <div>
    <q-input
      v-model="email"
      clearable
      :clear-icon="$i.ionCloseOutline"
      stack-label
      label-slot
      :input-style="{ width: '350px' }"
      hint="이메일을 입력해주세요"
      placeholder="ssafyPark@edu.ssafy.com"
    >
      <template v-slot:label>
        <h5 class="text-primary">이메일</h5>
        <br />
      </template>
    </q-input>
    <br />
    <br />
    <q-input
      v-model="password1"
      clearable
      :clear-icon="$i.ionCloseOutline"
      stack-label
      label-slot
      hint="8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요."
      placeholder="*************"
      type="password"
    >
      <template v-slot:label>
        <h5 class="text-primary">비밀번호</h5>
        <br />
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
      placeholder="*************"
      hint="비밀번호를 다시 적어주세요"
      type="password"
    >
      <template v-slot:label>
        <h5 class="text-primary">비밀번호 확인</h5>
        <br />
      </template>
    </q-input>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password1: '',
      password2: '',
    };
  },
  methods: {},
};
</script>

<style scoped></style>
