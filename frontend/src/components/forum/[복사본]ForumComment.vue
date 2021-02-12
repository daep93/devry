<template>
  <div class="row col-12">
    <!-- 댓글 시작 -->
    <div class="row col-12">
      <!-- <div class="row col-12" v-for="(data, index) in info" :key="index"> -->
      <div class="row col-2">
        <!-- 댓글 좋아요 수, 댓글 수, 북마크 수 -->
        <div class="row col-9"></div>
        <div class="row col-3 q-mt-lg">
          <forum-comment-status></forum-comment-status>
        </div>
      </div>
      <div class="row col-10">
        <div class="row col-9">
          <q-card flat bordered class="my-card q-pa-lg q-mt-lg row col-12">
            TEST
            <!-- <div class="row col-10">
              <div class="q-ml-md row col-12 q-mt-sm">
                <span
                  class="text-body1 text-weight-bold"
                  style="color: #585858"
                >
                  @유저이름
                </span>
                <span
                  class="q-ml-sm text-caption"
                  style="color: gray; margin-top: 2px"
                >
                  작성시각
                  {{ data.written_time | moment('YYYY/MM/DD HH:mm') }}

                </span>
              </div>
            </div> -->

            <!-- <div class="row col-2 justify-end">
              <div>
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
                        @click="deleteQnaComment(index)"
                      >
                        <q-item-section>삭제하기</q-item-section>
                      </q-item>
                      <q-separator />
                    </q-list>
                  </q-menu>
                </q-btn>
              </div>
            </div> -->
            댓글 내용
            <!-- <div class="row col-12 justify-center">
              <v-md-editor
                v-model="data.content"
                :mode="modes[index]"
                class="q-mb-md"
                :style="{
                  height: modes[index] === 'preview' ? 'auto' : '500px',
                }"
              >
              </v-md-editor>
              <q-btn
                @click="updateQnaComment(index)"
                color="primary"
                v-if="modes[index] === 'editable'"
                >수정 완료</q-btn
              >
            </div> -->
            댓글 내용2
            <!-- <div class="q-ml-md row col-12">
              <q-card-section class="row col-12">
                <q-markdown :src="info.contents"> </q-markdown>
              </q-card-section>
            </div> -->

            <!-- <q-card-section class="row col-12">
              <template v-if="data.anssmall_set.length">
                <q-separator />
              </template>
              큰 댓글의 작은 댓글
              <qna-recomment
                :ans_id="data.id"
                :recomments="data.anssmall_set"
                @reloadRecomment="reloadRecomment(index)"
              ></qna-recomment>
            </q-card-section> -->
          </q-card>
        </div>
      </div>
    </div>
  </div>
  <!-- <div>
    <q-card flat bordered class="my-card" style="padding: 40px; width: 800px;">
      <div class="q-pt-none row">
        <div class="col-2" style="width: 50px; margin-right: 5px;">
          <span style="cursor: pointer;">
            <q-avatar @click="goToProfile" style="width: 35px; height: 35px;"
              ><img src="https://cdn.quasar.dev/img/avatar.png" />
            </q-avatar>
          </span>
        </div>
        <div class="col-10">
          <span>
            <q-input
              outlined
              v-model="text"
              :dense="dense"
              style="width: 660px;"
              placeholder="댓글을 입력해주세요"
            />
          </span>
        </div>
      </div>
      <q-card-section style="margin-right: -12px;">
        <div class="icon-position">
          <q-btn
            no-caps
            color="grey"
            id="follow-btn"
            label="Cancel"
            style="width:85px;"
          />
          <q-btn
            no-caps
            color="primary"
            id="follow-btn"
            label="Submit"
            style="width:85px; margin-left: 10px;"
          />
        </div>
      </q-card-section>
      <div style="margin-top: 50px;">
        <div class="q-pt-none row" v-for="n in 3" :key="n">
          <div class="col-2" style="width: 50px; margin-right: 5px;">
            <span style="cursor: pointer;">
              <q-avatar @click="goToProfile" style="width: 35px; height: 35px;"
                ><img :src="profile_img" />
              </q-avatar>
            </span>
          </div>
          <div class="col-10">
            <span>
              <q-card
                flat
                bordered
                class="my-card"
                style="width: 660px; height: 100px; padding: 18px;"
              >
                <span>{{ username }}</span>
                <span style="margin-left: 10px; font-size: 5px;">7분 전</span>
                <div class="icon-position">
                  <q-icon
                    :name="$i.ionHeartOutline"
                    style="color:#727272"
                    size="22px"
                    class="q-mr-sm"
                  ></q-icon>
                  <span style="margin-right: 20px;">17 likes</span>
                  <q-icon
                    :name="$i.ionChatboxEllipsesOutline"
                    style="color:#727272"
                    size="22px"
                    class="q-mr-sm"
                  ></q-icon>
                  <span style="margin-right: 20px;">Reply</span>
                </div>
                <div style="padding-top: 5px;">댓글 내용</div>
              </q-card>
              <br />
            </span>
          </div>
        </div>
      </div>
    </q-card>
  </div> -->
</template>

<script>
import ForumCommentStatus from '@/components/forum/ForumCommentStatus';

export default {
  components: {
    ForumCommentStatus,
  },
  data() {
    return {
      title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      username: 'test user',
      profile_img: 'https://cdn.quasar.dev/img/mountains.jpg',
    };
  },
  methods: {
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
  },
};
</script>

<style scoped>
.icon-position {
  float: right;
}
</style>
