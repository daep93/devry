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
            <div class="row col-10">
              <div class="q-ml-md row col-12">
                <span
                  class="text-body1 text-weight-bold"
                  style="color: #585858"
                >
                  @{{ data.user.username }}
                </span>
                <span
                  class="q-ml-sm text-caption"
                  style="color: gray; margin-top: 2px"
                >
                  {{ data.written_time | moment('YYYY/MM/DD HH:mm') }}
                  <!-- 답변 채택 버튼 -->
                  <span v-if="$store.state.id == author" class="q-ml-sm">
                    <q-icon
                      :name="$i.ionCheckmarkCircleOutline"
                      :style="{ color: data.assisted ? 'blue' : '#B7B7B7' }"
                      class="cursor-pointer"
                      size="sm"
                      @click="chooseComment(index)"
                    ></q-icon>
                    <!-- <q-icon
                      :name="$i.ionRibbonOutline"
                      :style="{ color: data.assisted ? 'blue' : '#727272' }"
                      class="cursor-pointer"
                      size="sm"
                      @click="chooseComment(index)"
                    ></q-icon> -->
                  </span>
                  <span v-else-if="data.assisted" class="q-ml-sm">
                    <q-icon
                      :name="$i.ionCheckmarkCircleOutline"
                      style="color: blue"
                      size="sm"
                    ></q-icon>
                  </span>
                </span>
              </div>
            </div>

            <div class="row col-2 justify-end">
              <div v-if="data.user.id == $store.state.id">
                <q-btn flat round dense icon="more_vert">
                  <q-menu>
                    <q-list style="min-width: 100px">
                      <q-item
                        clickable
                        v-close-popup
                        @click="editerOpen(index)"
                      >
                        <q-item-section>수정하기</q-item-section>
                      </q-item>
                      <q-item
                        clickable
                        v-close-popup
                        @click="updateQnaComment(index)"
                      >
                        <q-item-section>수정 적용</q-item-section>
                      </q-item>
                      <q-item
                        clickable
                        v-close-popup
                        @click="deleteQnaComment(index)"
                      >
                        <q-item-section>삭제하기</q-item-section>
                      </q-item>
                      <q-separator />
                    </q-list>
                  </q-menu>
                </q-btn>
              </div>
            </div>

            <div class="row col-12">
              <v-md-editor v-model="data.content" :mode="modes[index]">
              </v-md-editor>
              <!-- <q-btn @click="updateQnaComment(index)">수정 적용</q-btn> -->
            </div>

            <div class="q-ml-md row col-12">
              <q-card-section class="row col-12">
                <q-markdown :src="info.contents"> </q-markdown>
              </q-card-section>
            </div>

            <q-separator />
            <!-- 큰 댓글의 작은 댓글 -->
            <!-- <qna-recomment></qna-recomment> -->
            <div class="q-mt-sm q-px-md row col-12">
              <div class="row col-11">
                <q-input
                  borderless
                  v-model="text"
                  autogrow
                  placeholder="댓글을 입력해주세요"
                  class="full-width"
                />
              </div>
              <div class="row col-1">
                <div class="q-mt-sm ">
                  <q-btn color="primary" label="등록" size="13px" />
                </div>
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
// import QnaRecomment from '@/components/qna/QnaRecomment';
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
    const res = [];
    for (const i in this.info) res.push('preview');
    this.modes = res;
    return {
      text: '',
      follow: true,
      contents: '',
      content: '',
      qna: null,
      author: null,
      modes: res,
      ans_pk: null,
    };
  },
  methods: {
    editerOpen(index) {
      this.modes[index] = 'editable';
      this.modes = [...this.modes];
    },
    async updateQnaComment(index) {
      if (this.contents === '') {
        alert('내용은 필수 입력항목 입니다');
      }
      try {
        const ans_pk = this.info[index].id;
        const qnaId = this.info[index].qna;
        this.modes[index] = 'preview';
        this.modes = [...this.modes];
        this.$q.loading.show();
        await updateQnaBigComment(ans_pk, {
          content: this.info[index].content,
          qna: qnaId,
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
        const ans_pk = this.info[index].id;
        console.log(ans_pk);
        await deleteQnaBigComment(ans_pk);
        location.reload();
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    async chooseComment(index) {
      try {
        for (let check of this.info) {
          if (check.assisted == true && !this.info[index].assisted) {
            check.assisted = false;
            await toggleQnaCommentChoose(check.id);
          }
        }
        const ans_pk = this.info[index].id;
        await toggleQnaCommentChoose(ans_pk);
        this.info[index].assisted = !this.info[index].assisted;
      } catch (error) {
        console.log(error);
      }
    },
    // async chooseComment(index) {
    //   try {
    //     const ans_pk = this.info[index].id;
    //     await toggleQnaCommentChoose(ans_pk);
    //     this.info[index].assisted = !this.info[index].assisted;
    //   } catch (error) {
    //     console.log(error);
    //   }
    // },
  },
  async created() {
    const index = this.$route.params.id;
    try {
      const { data } = await loadQnaItem(index);
      this.contents = data;
      this.author = data.user.id;
    } catch (error) {
      console.log(error);
    }
  },
};
</script>

<style scoped></style>
