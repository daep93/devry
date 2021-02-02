<template>
  <div class="row col-12">
    <div class="row col-2"></div>
    <div class="row col-10">
      <div class="row col-9">
        <q-card flat bordered class="my-card q-pa-lg q-mt-lg row col-12">
          <div class="row col-12">
            <!-- 답변 상태 표기 -->
            <div
              class="row col-2 q-pl-md q-pb-xs"
              v-for="(color, msg) in {
                '답변 완료': '#1976D2',
              }"
              :key="msg"
            >
              <div
                class="row col-12 shadow-1 overflow-hidden"
                style="border-radius:5px; max-width: 100px;"
              >
                <div class="col-2" :style="{ 'background-color': color }"></div>
                <div class="col-10 text-center">{{ msg }}</div>
              </div>
            </div>
          </div>

          <div class="row col-9">
            <div class="q-ml-md row col-12 q-my-sm">
              <div style="color: blue">
                @채택된유저
              </div>
              <span class="q-ml-md text-caption" style="color: gray;">
                50분 전
              </span>
            </div>
          </div>
          <div class="row col-2 q-pl-xl">
            <div class="icon-position q-mb-xs row items-center">
              <div class="q-mr-xs">
                <q-icon
                  :name="$i.ionHeartOutline"
                  style="color:#727272"
                  size="17px"
                ></q-icon>
              </div>
              <div class="q-mr-md" style=" font-size: 10pt;">
                2
              </div>
              <div class="q-mr-sm">
                <q-icon
                  :name="$i.ionChatboxEllipsesOutline"
                  style="color:#727272"
                  size="17px"
                ></q-icon>
              </div>
              <span style="font-size: 10pt;">3</span>
            </div>
          </div>
          <div class="row col-1 q-mb-sm">
            <q-toggle
              :label="채택하기"
              :true-value="false"
              :false-value="true"
              v-model="blueModel"
            />
          </div>
          <div class="q-ml-md row col-12">
            <div class="q-mr-md q-pb-md">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet
              accusantium quam laudantium fugiat sequi, soluta cupiditate fugit
              delectus minima cumque quos eius ad debitis molestias laborum
              suscipit nesciunt? Quis, libero.
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
        </q-card>
        <q-card flat bordered class="my-card q-pa-lg q-mt-lg row col-12">
          <!-- <div class="row col-11 q-pl-lg"></div> -->

          <div class="row col-9">
            <div class="q-ml-md row col-12 q-my-sm">
              <div style="color: blue">
                @채택된유저
              </div>
              <span class="q-ml-md text-caption" style="color: gray;">
                50분 전
              </span>
            </div>
          </div>
          <div class="row col-2 q-pl-xl">
            <div class="icon-position q-mb-xs row items-center">
              <div class="q-mr-xs">
                <q-icon
                  :name="$i.ionHeartOutline"
                  style="color:#727272"
                  size="17px"
                ></q-icon>
              </div>
              <div class="q-mr-md" style=" font-size: 10pt;">
                2
              </div>
              <div class="q-mr-sm">
                <q-icon
                  :name="$i.ionChatboxEllipsesOutline"
                  style="color:#727272"
                  size="17px"
                ></q-icon>
              </div>
              <span style="font-size: 10pt;">3</span>
            </div>
          </div>
          <div class="row col-1 q-mb-sm">
            <q-toggle
              :label="채택하기"
              :true-value="false"
              :false-value="true"
              v-model="blueModel"
            />
          </div>
          <div class="q-ml-md row col-12">
            <div class="q-mr-md q-pb-lg">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet
              accusantium quam laudantium fugiat sequi, soluta cupiditate fugit
              delectus minima cumque quos eius ad debitis molestias laborum
              suscipit nesciunt? Quis, libero.
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
        </q-card>
      </div>
      <!-- 채택 댓글 프로필 -->
      <div v-if="!blueModel">
        <qna-comment-selected></qna-comment-selected>
      </div>
    </div>
  </div>
</template>

<script>
import QnaCommentSelected from '@/components/qna/QnaCommentSelected';

export default {
  components: {
    QnaCommentSelected,
  },
  data() {
    return {
      title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      username: 'Test User',
      profile_img: 'https://cdn.quasar.dev/img/avatar.png',
      follow: true,
      blueModel: true,
    };
  },
};
</script>

<style scoped></style>
