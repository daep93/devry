<template>
  <div class="row full-width">
    <q-card flat bordered class="my-card q-px-lg q-pt-xs row col-12">
      <q-card-section class="row full-width q-pb-sm q-px-none justify-end">
        <div class="row col-2 justify-end">
          <div
            class="row col-12 shadow-1 overflow-hidden"
            style="border-radius:5px; height:25px; max-width:100px;"
          >
            <div
              class="col-2"
              :style="{
                'background-color': info.solved ? '#1976D2' : '#C8DAFE',
              }"
            ></div>
            <div class="col-10 text-center row items-center justify-center">
              {{ info.solved ? '답변 완료' : '답변 대기' }}
            </div>
          </div>
        </div>
      </q-card-section>

      <q-card-section class="row col-12 q-py-none q-mb-sm">
        <div class="row col-12 text-h4 text-weight-bold">
          {{ info.title }}
        </div>
        <div class="text-subtitle2 text-grey-6">
          {{ info.written_time | moment('YYYY/MM/DD HH:mm') }}
        </div>
      </q-card-section>
      <q-card-section class="q-pa-none full-width q-mb-sm">
        <div class="q-ml-md">
          <span v-for="tag in info.ref_tags" :key="tag" class="q-px-xs">
            <q-badge
              class="q-pa-sm text-black"
              :style="{ 'background-color': tagColor(tag, 0.5) }"
              style="font-size:1em; border-radius:3pt;"
            >
              # {{ tag }}
            </q-badge>
          </span>
        </div>
      </q-card-section>
      <q-card-section class="row col-12">
        <q-markdown :src="info.contents"> </q-markdown>
      </q-card-section>
      <q-card-section
        class="row col-12 justify-end"
        v-if="info.user_id == $store.state.id"
      >
        <q-btn @click="qnaPostEdit">수정하기</q-btn>
      </q-card-section>
      <q-card-section class="row col-12">
        <qna-small-comment
          :comments="comments"
          :user_id="info.user_id"
          :post_id="info.post_id"
          :usernmae="info.username"
          @reloadSmallAns="reloadSmallAns"
        ></qna-small-comment>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import QnaSmallComment from '@/components/qna/QnaSmallComment';
import { colorSoloMapper } from '@/utils/tagColorMapper';
import { getSmallAnswers } from '@/api/qna';

export default {
  props: {
    info: Object,
  },
  components: {
    QnaSmallComment,
  },
  data: function() {
    return {
      msg: true,
      comments: this.info.comments,
      solved: this.info.solved,
      tags: ['Vue', 'Javascript', 'Typescript'],
      writerStatus: false,
      QnaDetailData: {
        user_info: {
          userid: 1,
          username: 'SSAFY PARK',
          profile_img: 'user/1',
          post_num: 5,
          follower_num: 3,
          bio: 'Hello DEVRY! Nice Day!!',
          pinned: [
            {
              title: '2021 Awesome Tech Top 5',
              post_id: 310,
            },
            {
              title: '2020 Awesome Tech Top 3', // pinned한 게시글의 제목
              post_id: 4, // pinned한 게시글의 번호
            },
            {
              title: 'How to test your project efficiently', // pinned한 게시글의 제목
              post_id: 203, // pinned한 게시글의 번호
            },
          ],
          liked: true,
          is_following: true,
        },
        quest_post: {
          title: 'How can I use axios in Vue.js?', // 질문 제목
          written_time: '2021-01-24T02:02', // 글 작성시간
          ref_tags: ['vue', 'javascript'], // 참조한 태그들
          solved: true, // 해결 여부
          like_num: 3, // 좋아요 횟수
          comment_num: 2, // 댓글 갯수
          viewed_num: 300, // 조회 수
          bookmarked_num: 1, // 북마크된 횟수
          contents:
            'One of the most essential parts of frontend development is communication with the backend by making HTTP requests. There are a few ways how we can make API calls in Javascript asynchronously.', // 질문 글 (우선은 단순 string으로 취급)
          answers: [
            {
              // 작은 댓글들 (시간순으로 배열에 저장됨)
              contents:
                'Vue.js in the official docs indirectly explains the mechanism of the key special attribute in vue.', // 답변 글(단순 string)
              userid: 45, // 댓글 작성자 id 번호
              username: 'SSAFY MAN', // 댓글 작성자 닉네임
              written_time: '2021-01-25T03:02', // 댓글 작성시간
            },
            {
              // 작은 댓글들 (시간순으로 배열에 저장됨)
              contents:
                'Good Sunday, welcome to my series about destructuring one of those frequently shared JavaScript quizzes on Twitter.', // 답변 글(단순 string)
              userid: 265, // 댓글 작성자 id 번호
              username: 'Newbie in SSAFY', // 댓글 작성자 닉네임
              written_time: '2021-01-25T05:23', // 댓글 작성시간
            },
          ],
        },
        answer_posts: [
          {
            user_info: {
              // 큰 댓글 작성자 정보
              userid: 5, // id 번호
              username: 'SSAFY ONE', // 닉네임
              written_time: '2021-01-25T05:23', // 글 작성 시간
              profile_img: 'user/5', // 프로필 사진 url
              post_num: 3, // 작성한 포스트 횟수
              follower_num: 10, // 팔로워 수
              bio: 'SSAFY is The One!', // 유저 소개
            },
            quest_post: {
              title: 'Read vue documentation', // 질문 제목
              assisted: true, // 답변 채택 여부
              like_num: 300, // 좋아요 횟수
              comment_num: 1, // 댓글 갯수
              contents: 'Just Read it plz.', // 질문 글
              answers: [
                {
                  // 작은 댓글들 (시간순으로 배열에 저장됨)
                  contents: 'I agree', // 답변 글(단순 string)
                  userid: 2, // 댓글 작성자 id 번호
                  username: 'SSAFY Pro', // 댓글 작성자 닉네임
                  written_time: '2021-01-25T05:26', // 댓글 작성시간
                },
              ],
            },
          },
        ],
      },
    };
  },
  methods: {
    tagColor(tag, alpha) {
      return colorSoloMapper(tag, alpha);
    },
    qnaPostEdit() {
      this.$router.push(`/qna/${this.info.post_id}`);
    },
    async reloadSmallAns() {
      try {
        this.comments = await getSmallAnswers(this.info.post_id);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped>
.icon-position {
  float: right;
}
</style>
