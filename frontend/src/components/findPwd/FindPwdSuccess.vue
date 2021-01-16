<template>
  <div style="height:50%">
    <div class="row justify-start items-end" style="height:60%">
      <p class="text-h4 text-weight-bolder">
        비밀번호 변경 성공!
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
        @click="offModal"
        >돌아가기</q-btn
      >
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    offModal() {
      this.$store.commit('offAccountModal');
    },
  },
};
</script>

<style scoped></style>
