<template>
  <div class="row col-12">
    <div class="row col-12 q-mt-md q-pr-md">
      <div class="row col-2"></div>
      <div class="row col-8 q-pr-xl">
        <div class="text-h6 text-weight-bold q-mb-sm">댓글 작성하기</div>

        <q-input
          outlined
          flat
          v-model="newComment"
          type="textarea"
          placeholder="댓글을 입력해주세요"
          class="full-width"
          @input="getContents"
        />

        <!-- <markdown-editor
          @input="getContents"
          :height="'400px'"
        ></markdown-editor> -->
      </div>
      <div class="row col-2"></div>

      <!-- 제출 버튼 -->
      <div class="row col-9 q-mt-sm q-pl-xl">
        <div class="row col-3"></div>
        <div class="row col-9">
          <div class="row col-12 justify-center">
            <div>
              <q-btn
                no-caps
                color="primary"
                label="댓글 작성하기"
                style="width: 200px"
                class="q-mb-md q-mt-lg"
                @click="createComment"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { createForumComment } from '@/api/forum';
// import MarkdownEditor from '@/components/common/MarkdownEditor';

export default {
  // components: { MarkdownEditor },
  props: {
    info: Object,
  },
  data() {
    return {
      content: '',
    };
  },
  methods: {
    getContents(data) {
      this.content = data;
    },
    async createComment() {
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
      if (this.content === '') {
        alert('댓글 내용을 작성해주세요.');
        return;
      }
      try {
        this.$q.loading.show();
        await createForumComment({
          // 넘길 데이터
          user: this.$store.state.id,
          comment_content: this.content,
          post: this.info.post_id,
        });
        location.reload();
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
