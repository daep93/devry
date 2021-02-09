<template>
  <div class="row shadow-2">
    <div class="row full-width">
      <q-btn :icon="$i.ionHeart" flat padding="5px" size="sm"></q-btn>
      <q-btn></q-btn>
      <q-btn></q-btn>
    </div>
    <q-card flat bordered class="col-6">
      <!-- 제목 입력 -->
      <q-input
        v-model="contents"
        placeholder="내용을 입력해주세요"
        type="textarea"
        input-style="height:70vh; padding: 0; line-height:1.5"
        square
        borderless
      />
    </q-card>
    <!-- 미리보기 화면 -->
    <q-card flat class="col-6 bg-grey-3 row scroll-y" style="height:70vh; ">
      <q-markdown :src="contents" class="full-width bg-white" style="">
      </q-markdown>
    </q-card>
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

<style scoped></style>
