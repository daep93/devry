<template>
  <div class="row col-12">
    <div class="row col-12">
      <div class="row col-12">
        <q-separator />
        <div
          class="row col-12 q-py-sm"
          v-for="(data, index) in comments"
          :key="index"
        >
          <div class="row col-12 justify-between">
            <div class="row col-10">
              <span class="q-mr-xs">{{ index + 1 }}</span>
              <span class="q-mr-sm" style="color: blue">
                @{{ data.user.username }}
              </span>
              <span class="text-caption" style="color: gray">
                {{ data.written_time | moment('YYYY/MM/DD HH:mm') }}
              </span>
            </div>
          </div>
          <div class="q-ml-lg q-py-xs row col-12">
            {{ data.content }}
          </div>
          <q-btn @click="qnaSmallCommentDelete(index)">삭제하기</q-btn>
          <q-btn @click="qnaSmallCommentUpdate(index)">수정하기</q-btn>
        </div>
      </div>
    </div>
    <q-separator />
    <div class="q-mt-sm row col-12">
      <q-input
        borderless
        v-model="text"
        placeholder="댓글을 입력해주세요"
        class="full-width"
      />
    </div>
    <div class="row col-12">
      <div class="row col-10"></div>
      <div class="row col-2 q-pl-xl q-mb-lg">
        <q-btn
          color="primary"
          label="댓글 추가"
          size="md"
          @click="setSmallAnswer"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { getRecomment } from '@/api/qna';

export default {
  methods: {
    async reloadSmallAns() {
      try {
        this.comments = await getRecomment(this.info.post_id);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped></style>
