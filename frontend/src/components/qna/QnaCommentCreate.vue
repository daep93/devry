<template>
  <div class="row col-12">
    <div class="row col-2">a</div>
    <div class="row col-10">
      <div class="row col-9">
        <div class="q-ml-md row col-12 q-my-sm">
          <div style="color: blue">@작성자</div>
          <span class="q-ml-sm text-caption" style="color: gray;">
            {{ info.title }}
          </span>
        </div>
        <div class="q-ml-md row col-12">
          <v-md-editor
            v-model="content"
            height="800px"
            left-toolbar="undo redo clear | h bold italic strikethrough quote | ul ol table hr | link image code video "
            :disabled-menus="[]"
            :toolbar="toolbar"
            @upload-image="handleUploadImage"
          >
          </v-md-editor>
        </div>
      </div>
    </div>

    <!-- 제출 버튼 -->
    <div class="row col-9 q-mt-lg q-pl-xl">
      <div class="row col-3"></div>
      <div class="row col-9">
        <div class="row col-12">
          <div style="margin:0 auto;">
            <q-btn
              no-caps
              color="primary"
              id="follow-btn"
              label="답변 작성하기"
              style="width: 200px"
              class="q-mb-xl"
              @click="createBigComment"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { createQnaBigComment } from '@/api/qna';

export default {
  props: {
    info: Object,
  },
  data() {
    return {
      content: '',
    };
  },
  methods: {
    async createBigComment() {
      if (this.content === '') {
        alert('댓글 내용을 작성해주세요.');
      }
      try {
        console.log(this.info.post_id);
        this.$q.loading.show();
        await createQnaBigComment({
          // 넘길 데이터
          user: this.$store.state.id,
          content: this.content,
          qna: this.info.post_id,
        });
        location.reload();
        // QnA 게시판으로 이동
        // this.$router.push({ path: `/qna-detail/${this.info.post_id}` });
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
};
</script>

<style scoped></style>
