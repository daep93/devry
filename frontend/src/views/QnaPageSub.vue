<template>
  <div class="q-pa-lg q-mt-sm row justify-center">
    <div class="q-pa-sm" style="width: 80vw;">
      <!-- 타이틀 -->
      <div class="q-mb-md">
        <span class="text-h4 text-weight-bolder">QnA Registration</span>
        <p class="text-subtitle2 q-mt-md q-mb-xl">
          궁금하신 점을 질문해보세요:)
        </p>
      </div>
      <!-- QnA 입력 폼 -->
      <qna-create
        @addTagItem="addOneTag"
        @removeTagItem="removeOneTag"
        :propsTagData="tags"
      ></qna-create>
      <!-- buttons -->
      <div class="q-mb-xl q-mt-xl" style="text-align: center;">
        <q-btn
          outline
          color="blue-12"
          class="text-weight-bold q-px-xl q-py-sm q-mr-md"
          label="임시저장"
          size="md"
        />
        <q-btn
          color="blue-12"
          class="text-weight-bold q-px-xl q-py-sm"
          label="작성하기"
          size="md"
        />
      </div>
    </div>
  </div>
</template>

<script>
import QnaCreate from '@/components/qna/QnaCreate';
export default {
  components: {
    QnaCreate,
  },
  data() {
    return {
      tags: ['Vue', 'UX/UI', 'Python'],
    };
  },
  methods: {
    addOneTag(tagItem) {
      this.tags.push(tagItem);
    },
    removeOneTag(tag, index) {
      this.tags.splice(index, 1);
    },
  },
};
</script>

<style></style>
