<template>
  <div class="row col-12">
    <!-- 댓글 시작 -->
    <div class="row col-12" v-for="data in info" :key="data">
      <!-- <div class="row col-12" v-for="data in info.content" :key="data"> -->
      <div class="row col-2">
        <!-- 댓글 좋아요 수, 댓글 수, 북마크 수 -->
        <div class="row col-9"></div>
        <div class="row col-3 q-mt-lg">
          <qna-comment-status :info="bigCommentsStatus"></qna-comment-status>
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
                {{ data.content }}
              </div>
            </div>
            <!-- 토글이 꺼져있으며, 글 작성자가 아닌 경우 -->
            <div v-if="blueModel && !writerStatus" class="row col-3"></div>
            <!-- 토글이 켜져있으며 글 작성자가 아닌 경우 -->
            <div v-else-if="!blueModel && !writerStatus" class="row col-3">
              <div class="row col-3 q-mb-sm q-pl-sm"></div>
              <div class="row col-9">
                <div class="q-pl-xl q-mt-sm">
                  <div
                    class="row col-12 shadow-1 overflow-hidden"
                    style="border-radius:5px; width: 100px; height: 20px;"
                  >
                    <div class="col-2" style="background-color: #1976D2"></div>
                    <div class="col-10 text-center">답변 채택</div>
                  </div>
                </div>
              </div>
            </div>
            <!-- 토글이 꺼져있으며 글 작성자가 맞는 경우 -->
            <div v-else-if="blueModel && writerStatus" class="row col-3">
              <div class="row col-8"></div>
              <div class="row col-4 q-mb-sm q-pl-sm">
                <q-toggle
                  :label="채택하기"
                  :true-value="false"
                  :false-value="true"
                  v-model="blueModel"
                />
              </div>
            </div>
            <!-- 토글이 켜져있으며, 글 작성자가 맞는 경우 -->
            <div v-else-if="!blueModel && writerStatus" class="row col-3">
              <div class="row col-8">
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
              <div class="row col-4 q-mb-sm q-pl-sm">
                <q-toggle
                  :label="채택하기"
                  :true-value="false"
                  :false-value="true"
                  v-model="blueModel"
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
        <div v-if="!blueModel">
          <qna-comment-selected></qna-comment-selected>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import QnaCommentSelected from '@/components/qna/QnaCommentSelected';
import QnaCommentStatus from '@/components/qna/QnaCommentStatus';

export default {
  props: {
    info: Object,
  },
  components: {
    QnaCommentSelected,
    QnaCommentStatus,
  },
  data() {
    return {
      text: '',
      follow: true,
      blueModel: true,
      writerStatus: false,
      contents: '',
    };
  },
  methods: {
    checkWriter() {
      // 글 작성자 판별
      if (this.$store.state.id === this.QnaDetailData.user_info.userid) {
        this.writerStatus = true;
      }
    },
  },
  computed: {
    bigCommentsStatus() {
      return this.contents.ans_set;
    },
    // bigCommentsStatus() {
    //   for (let data of this.contents.ans_set) {
    //     return {
    //       liked_ans: data.liked_ans,
    //       like_ans_num: data.like_ans_num,
    //     };
    //   }
    // },
  },
  created() {
    this.checkWriter();
  },
};
</script>

<style scoped></style>
