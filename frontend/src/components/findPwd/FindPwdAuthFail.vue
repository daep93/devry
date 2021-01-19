<template>
  <div style="height:50%">
    <div class="row justify-start items-end" style="height:60%">
      <p class="text-h4 text-weight-bolder">
        계정 인증 실패😥
      </p>
    </div>
    <br />
    <br />
    <div class="row justify-start" style="height:55%">
      <q-btn
        color="blue-12"
        class="text-center"
        style="width:330px;height:50px;border-radius:5px;font-size:16pt"
        type="submit"
        @click="backToAuthCheck"
        >뒤로가기</q-btn
      >
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      modalState: 'auth'
    }
  },
  methods: {
    backToAuthCheck() {
      this.$emit('authPwd');
    },
  },
};
</script>

<style scoped></style>