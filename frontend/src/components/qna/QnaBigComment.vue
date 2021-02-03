<template>
  <div class="row col-12">
    <!-- 두 번째 댓글 -->
    <div class="row col-12">
      <div class="row col-2">
        <!-- 댓글 좋아요 수, 댓글 수, 북마크 수 -->
        <div class="row col-9"></div>
        <div class="row col-3 q-mt-lg">
          <qna-comment-status></qna-comment-status>
        </div>
      </div>
      <div class="row col-10">
        <div class="row col-9">
          <q-card flat bordered class="my-card q-pa-lg q-mt-lg row col-12">
            <div class="row col-9">
              <div class="q-ml-md row col-12 q-my-sm">
                <div style="color: blue">
                  @user123
                </div>
                <span class="q-ml-sm text-caption" style="color: gray;">
                  50분 전
                </span>
              </div>
            </div>
            <!-- 토글이 꺼져있으며, 글 작성자가 아닌 경우 -->
            <div v-if="blueModel && !writerStatus" class="row col-3"></div>
            <!-- 토글이 켜져있으며 글 작성자가 아닌 경우 -->
            <div v-else-if="!blueModel && !writerStatus" class="row col-3">
              <div class="row col-3 q-mb-sm q-pl-sm"></div>
              <div class="row col-9">
                <div
                  class="q-pl-xl q-mt-sm"
                  v-for="(color, msg) in {
                    '답변 채택': '#1976D2',
                  }"
                  :key="msg"
                >
                  <div
                    class="row col-12 shadow-1 overflow-hidden"
                    style="border-radius:5px; width: 100px; height: 20px;"
                  >
                    <div
                      class="col-2"
                      :style="{ 'background-color': color }"
                    ></div>
                    <div class="col-10 text-center">{{ msg }}</div>
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
                <div
                  class="q-pl-xl q-mt-sm"
                  v-for="(color, msg) in {
                    '답변 채택': '#1976D2',
                  }"
                  :key="msg"
                >
                  <div
                    class="row col-12 shadow-1 overflow-hidden"
                    style="border-radius:5px; width: 100px; height: 20px;"
                  >
                    <div
                      class="col-2"
                      :style="{ 'background-color': color }"
                    ></div>
                    <div class="col-10 text-center">{{ msg }}</div>
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
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Exercitationem quidem, iure eveniet praesentium repudiandae
                necessitatibus delectus explicabo repellat id eligendi corrupti.
                Dolorem harum, nihil ipsum accusantium delectus labore dolorum,
                illo, autem quas distinctio accusamus tenetur fugiat
                perspiciatis illum dolore! Obcaecati totam laboriosam eaque
                quos. Consequuntur esse veritatis tempora cum earum illum,
                suscipit nobis neque excepturi ducimus sed voluptatum nesciunt
                minus placeat nulla voluptate iste corrupti odit repudiandae
                totam itaque facilis quas non! Eos hic veritatis quas minima
                cupiditate odit dignissimos? Totam asperiores architecto illum
                eum accusantium rerum neque? Officiis ut illo aut minima maiores
                fuga obcaecati animi, veniam facilis distinctio?
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
                  ><q-btn color="primary" label="댓글 추가" size="sm"
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
  components: {
    QnaCommentSelected,
    QnaCommentStatus,
  },
  data() {
    return {
      follow: true,
      blueModel: true,
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
      },
    };
  },
  methods: {
    checkWriter() {
      // 글 작성자 판별
      if (this.$store.state.id === this.QnaDetailData.user_info.userid) {
        this.writerStatus = true;
      }
      // console.log('1번', this.$store.state.id);
      // console.log('2번', this.QnaDetailData.user_info.userid);
    },
  },
};
</script>

<style scoped></style>
