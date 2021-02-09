<template>
  <div class="row col-12">
    <!-- 댓글 시작 -->
    <div class="row col-12" v-for="(data, index) in info" :key="index">
      <div class="row col-2">
        <!-- 댓글 좋아요 수, 댓글 수, 북마크 수 -->
        <div class="row col-9"></div>
        <div class="row col-3 q-mt-lg">
          <qna-comment-status :info="data"></qna-comment-status>
        </div>
      </div>
      <div class="row col-10">
        <div class="row col-9">
          <q-card flat bordered class="my-card q-pa-lg q-mt-lg row col-12">
            <div class="row col-9">
              <div class="q-ml-md row col-12 q-my-sm">
                <div style="color: blue">@{{ data.user.username }}</div>
                <span class="q-ml-sm text-caption" style="color: gray;">
                  {{ data.written_time | moment('YYYY/MM/DD HH:mm') }}
                </span>
              </div>
              <div class="q-ml-md row col-12">
                <v-md-editor v-model="data.content" mode="preview">
                </v-md-editor>
                <q-card-section
                  class="row col-12 justify-end"
                  v-if="data.user.id == $store.state.id"
                >
                  <q-btn @click="updateQnaComment(index)">수정하기</q-btn>
                </q-card-section>
                <q-btn
                  outline
                  color="red-12"
                  class="text-weight-bold q-px-xl q-py-sm q-mr-md"
                  label="삭제하기"
                  size="md"
                  @click="deleteQnaComment(index)"
                />
              </div>
            </div>
            <div class="row col-3">
              <div class="row col-8" v-if="data.assisted == true">
                <div class="q-pl-xl q-mt-sm">
                  <div
                    class="row col-12 shadow-1 overflow-hidden"
                    style="border-radius:5px; width: 100px; height: 20px;"
                  >
                    <div class="col-2" style="background-color:#1976D2"></div>
                    <div class="col-10 text-center">답변 채택</div>
                  </div>
                </div>
              </div>
              <div
                class="row col-4 q-mb-sm q-pl-sm"
                v-if="$store.state.id == author"
              >
                <q-toggle
                  label="채택하기"
                  :true-value="true"
                  :false-value="false"
                  v-model="data.assisted"
                  @click="chooseBigComment(index)"
                />
              </div>
            </div>
            <div class="q-ml-md row col-12">
              <div class="q-mr-md q-pb-lg">
                <q-card-section class="row col-12">
                  <q-markdown :src="info.contents"> </q-markdown>
                </q-card-section>
              </div>
            </div>
            <div class="row col-12 q-px-md">
              <q-separator />
            </div>
            <div class="q-mt-sm q-px-md row col-12">
              <q-input
                borderless
                v-model="text"
                placeholder="댓글을 입력해주세요"
              />
            </div>
            <div class="row col-12">
              <div class="row col-10"></div>
              <div class="row col-2 q-pl-lg q-mb-sm">
                <span class="q-pl-md"
                  ><q-btn color="primary" label="댓글 추가" size="md"
                /></span>
              </div>
            </div>
          </q-card>
        </div>
        <!-- 채택 댓글 프로필 -->
        <div v-if="data.assisted === true">
          <qna-comment-selected :info="data"></qna-comment-selected>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { toggleQnaCommentChoose } from '@/api/qna';
import QnaCommentSelected from '@/components/qna/QnaCommentSelected';
import QnaCommentStatus from '@/components/qna/QnaCommentStatus';
import {
  loadQnaItem,
  updateQnaBigComment,
  deleteQnaBigComment,
} from '@/api/qna';

export default {
  props: {
    info: Array,
  },
  components: {
    QnaCommentSelected,
    QnaCommentStatus,
  },
  data() {
    return {
      text: '',
      follow: true,
      contents: '',
      content: null,
      qna: null,
      author: null,
    };
  },
  methods: {
    async updateQnaComment(index) {
      if (this.contents === '') {
        alert('내용은 필수 입력항목 입니다');
      }
      try {
        const commentId = this.info[index].id;
        const qnaId = this.info[index].qna;
        this.$q.loading.show();
        await updateQnaBigComment(commentId, {
          qna: qnaId,
          content: this.content,
        });
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    async deleteQnaComment(index) {
      try {
        this.$q.loading.show();
        const commentId = this.info[index].id;
        await deleteQnaBigComment(commentId);
        location.reload();
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  // created() {
  //   this.checkWriter();
  // },
  async created() {
    const index = this.$route.params.id;
    try {
      const { data } = await loadQnaItem(index);
      this.contents = data;
      this.author = data.user.id;
    } catch (error) {
      console.log(error);
    }
    // this.checkWriter();
  },
};
</script>

<style scoped></style>
