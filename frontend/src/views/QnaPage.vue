<template>
  <div class="row justify-center q-pt-xl">
    <div class="row col-8 justify-center">
      <div class="row q-ml-md q-mb-sm items-end col-12">
        <div class="text-h5 text-weight-bold q-mr-sm">태그 필터링</div>
        <div>원하는 검색 키워드 태그들을 선택해주세요.</div>
      </div>
      <div class="row col-12 q-ml-md">
        <q-btn
          v-for="(tag, index) in tags"
          :key="tag"
          :style="{ 'background-color': tagColors[index] }"
          class="q-mr-sm text-weight-bold text-white"
          >{{ tag }}</q-btn
        >
        <q-btn outline class="add-button" color="primary">
          <q-icon :name="$i.ionAddOutline"></q-icon>
        </q-btn>
      </div>
    </div>
    <div class="row col-8 justify-center">QnA 게시판</div>
  </div>
</template>

<script>
import { colorMapper } from '@/utils/tagColorMapper';
export default {
  data() {
    return {
      tags: ['Javascript', 'vue', 'react', 'python'],
    };
  },
  computed: {
    tagColors() {
      return colorMapper(this.tags);
    },
  },
};
</script>

<style scoped>
.add-button >>> .q-btn__wrapper:before {
  border: 1px dashed;
}
</style>
