<template>
  <div>
    <!-- TODO : markdown형식으로 입력받고 출력하는 것 연습하기 -->
    <q-markdown>
      # hello
      <!-- <textarea name="" id="" cols="30" rows="10"><q-markdown></q-markdown></textarea> -->
    </q-markdown>
    <!-- <textarea v-model="contents" name="" id="" cols="30" rows="10"></textarea> -->
    <div v-html="contents"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      contents: '',
    };
  },
};
</script>

<style></style>
