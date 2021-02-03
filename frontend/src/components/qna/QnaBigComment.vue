<template>
  <div class="row col-12">
    <!-- 첫 번째 댓글 -->
    <div class="row col-12">
      <!-- 댓글 좋아요 수, 댓글 수, 북마크 수 -->
      <div class="row col-2">
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
                  @Hello
                </div>
                <span class="q-ml-sm text-caption" style="color: gray;">
                  50분 전
                </span>
              </div>
            </div>
            <div v-if="!blueModel" class="row col-2">
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
            <div v-else class="row col-2"></div>
            <div class="row col-1 q-mb-sm q-pl-sm">
              <q-toggle
                :label="채택하기"
                :true-value="false"
                :false-value="true"
                v-model="blueModel"
              />
            </div>
            <div class="q-ml-md row col-12">
              <div class="q-mr-md q-pb-lg">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Exercitationem quidem, iure eveniet praesentium repudiandae
                necessitatibus delectus explicabo repellat id eligendi corrupti.
                Dolorem harum, nihil ipsum accusantium delectus labore dolorum,
                illo
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
            <div v-if="!blueModel" class="row col-2">
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
            <div v-else class="row col-2"></div>
            <div class="row col-1 q-mb-sm q-pl-sm">
              <q-toggle
                :label="채택하기"
                :true-value="false"
                :false-value="true"
                v-model="blueModel"
              />
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
