<template>
  <div class="row justify-center q-pt-lg ">
    <div class="row col-8 justify-center q-pl-lg">
      <div class="row q-mb-sm col-10 text-h5 text-weight-bold">
        QnA 게시판
      </div>
      <div class="row col-2 q-pl-xl q-mb-sm">
        <span class="q-pl-xl q-pb-sm"
          ><q-btn color="primary" label="글 작성" size="sm"
        /></span>
      </div>

      <!-- 게시판 보드 -->
      <qna-board></qna-board>
      <div class="row q-mt-sm col-12 q-mb-xl justify-between">
        <!-- 답변 완료 표기 -->
        <div class="col-9 row q-py-xs">
          <div
            class="row col-2 q-pb-xs q-mr-md"
            v-for="(color, msg) in {
              '답변 완료': '#1976D2',
              '답변 대기': '#C8DAFE',
            }"
            :key="msg"
          >
            <div
              class="row col-12 shadow-1 overflow-hidden"
              style="border-radius:5px;"
            >
              <div class="col-2" :style="{ 'background-color': color }"></div>
              <div class="col-10 text-center">{{ msg }}</div>
            </div>
          </div>
        </div>
        <!-- 페이지네이션 -->
        <div class="col-3 row justify-end">
          <q-pagination
            v-model="current"
            color="grey"
            :max="5"
            :boundary-links="true"
          >
          </q-pagination>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import QnaBoard from '@/components/qna/QnaBoard';
export default {
  components: {
    QnaBoard,
  },
  data() {
    return {
      current: 3,
      tagFilter: false,
    };
  },
};
</script>

<style scoped></style>
