<template>
  <div style="height:50%">
    <div class="row justify-start items-end" style="height:50%">
      <p class="text-h3 text-weight-bolder">
        계정 생성 성공!
      </p>
    </div>
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
