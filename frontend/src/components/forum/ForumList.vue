<template>
  <div>
    <div class="justify-center" style="width: 1070px; margin:0 auto;">
      <div style="margin-left: 50px; margin-top: 30px; font-size: 30px;">
        <b>Forum 게시판</b>
      </div>
      <div class="row justify-between col-12" style="margin-top: 30px;">
        <!-- tab 라벨 -->
        <q-tabs
          v-model="tab"
          no-caps
          dense
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          narrow-indicator
          style="max-width: 170px; margin-left: 60px; margin-bottom: 0px;"
        >
          <q-tab name="feed" label="Feed" style=" width: 50px;" />
          <q-tab name="latest" label="Latest" />
        </q-tabs>
        <!-- 서치바, 태그 버튼 -->
        <div class="row justify-end q-gutter-lg" style="margin-right: 50px;">
          <q-input v-model="search" type="search" class="q-mb-sm" outlined>
            <template v-slot:append>
              <q-icon :name="$i.ionSearchOutline" />
            </template>
          </q-input>
          <q-btn
            class="tag-filter"
            outline
            color="primary"
            @click="$store.commit('toggleTagFilter')"
            >태그 선택</q-btn
          >
        </div>
      </div>
      <!-- 탭 시작 -->
      <div class="q-pa-md justify-center" style="width: 1065px; margin:0 auto;">
        <div class="q-gutter-y-md"></div>
        <q-tab-panels v-model="tab" animated>
          <q-tab-panel name="feed">
            <!-- 피드 리스트 -->
            <div class="row" style="margin-left: 12px;">
              <div v-for="(data, index) in forumList" :key="index">
                <div
                  class="q-pa-md row items-start q-gutter-md"
                  style="width: 345px;"
                >
                  <!-- 썸네일 -->
                  <q-card class="my-card" style="height: 400px;">
                    <img :src="data.thumnail" style="height: 198px;" />
                    <q-card-section style="margin-bottom: -5px; height: 80px;">
                      <div
                        style="font-size: 18px; cursor: pointer"
                        @click="goToDetail"
                      >
                        <b>{{ data.title }}</b>
                      </div>
                    </q-card-section>

                    <div style="margin-left: 15px;">
                      <span
                        v-for="tag in data.ref_tags"
                        :key="tag"
                        style="margin-right: 5px;"
                      >
                        <q-badge color="blue"> # {{ tag }} </q-badge>
                      </span>
                    </div>

                    <q-card-section style="margin-top: 10px;">
                      <div class="row">
                        <div class="col-0.5">
                          <span style="cursor:pointer; margin-right: 11px;">
                            <q-avatar
                              @click="goToProfile"
                              style="width: 35px; height: 35px;"
                              ><img :src="data.user_info.profile_img" />
                            </q-avatar>
                          </span>
                        </div>
                        <div class="col-11.5">
                          <div
                            style="font-size: 15px; cursor:pointer; height: 17px; color: #464646"
                            @click="goToProfile"
                          >
                            <b>{{ data.user_info.username }}</b>
                          </div>
                          <span style="font-size: 5px; color: #464646">{{
                            data.user_info.written_time
                          }}</span>
                        </div>
                      </div>
                    </q-card-section>
                    <div
                      class="icon-position"
                      style="margin-bottom: 10px; margin-top: -10px;"
                    >
                      <span style=" margin-right: 5px;">
                        <q-icon
                          :name="$i.ionHeartOutline"
                          style="color:#727272"
                          size="18px"
                        ></q-icon
                      ></span>
                      <span style="margin-right: 12px; font-size: 13px;">{{
                        data.like_num
                      }}</span>
                      <span style="margin-right: 5px;">
                        <q-icon
                          :name="$i.ionChatboxEllipsesOutline"
                          style="color:#727272"
                          size="15px"
                        ></q-icon
                      ></span>
                      <span style="margin-right: 15px; font-size: 13px;">{{
                        data.comment_num
                      }}</span>
                    </div>
                  </q-card>
                </div>
              </div>
            </div>
          </q-tab-panel>

          <q-tab-panel name="latest">
            <!-- 최신순 리스트 -->
            <div class="row" style="margin-left: 12px;">
              <div v-for="(data, index) in forumList" :key="index">
                <div
                  class="q-pa-md row items-start q-gutter-md"
                  style="width: 345px;"
                >
                  <!-- 썸네일 -->
                  <q-card class="my-card" style="height: 400px;">
                    <img :src="data.thumnail" style="height: 198px;" />
                    <q-card-section style="margin-bottom: -5px; height: 80px;">
                      <div
                        style="font-size: 18px; cursor: pointer"
                        @click="goToDetail"
                      >
                        <b>{{ data.title }}</b>
                      </div>
                    </q-card-section>

                    <div style="margin-left: 15px;">
                      <span
                        v-for="tag in data.ref_tags"
                        :key="tag"
                        style="margin-right: 5px;"
                      >
                        <q-badge color="blue"> # {{ tag }} </q-badge>
                      </span>
                    </div>

                    <q-card-section style="margin-top: 10px;">
                      <div class="row">
                        <div class="col-0.5">
                          <span style="cursor:pointer; margin-right: 11px;">
                            <q-avatar
                              @click="goToProfile"
                              style="width: 35px; height: 35px;"
                              ><img :src="data.user_info.profile_img" />
                            </q-avatar>
                          </span>
                        </div>
                        <div class="col-11.5">
                          <div
                            style="font-size: 15px; cursor:pointer; height: 17px; color: #464646"
                            @click="goToProfile"
                          >
                            <b>{{ data.user_info.username }}</b>
                          </div>
                          <span style="font-size: 5px; color: #464646">{{
                            data.user_info.written_time
                          }}</span>
                        </div>
                      </div>
                    </q-card-section>
                    <div
                      class="icon-position"
                      style="margin-bottom: 10px; margin-top: -10px;"
                    >
                      <span style=" margin-right: 5px;">
                        <q-icon
                          :name="$i.ionHeartOutline"
                          style="color:#727272"
                          size="18px"
                        ></q-icon
                      ></span>
                      <span style="margin-right: 12px; font-size: 13px;">{{
                        data.like_num
                      }}</span>
                      <span style="margin-right: 5px;">
                        <q-icon
                          :name="$i.ionChatboxEllipsesOutline"
                          style="color:#727272"
                          size="15px"
                        ></q-icon
                      ></span>
                      <span style="margin-right: 15px; font-size: 13px;">{{
                        data.comment_num
                      }}</span>
                    </div>
                  </q-card>
                </div>
              </div>
            </div>
          </q-tab-panel>
        </q-tab-panels>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tab: 'feed',
      // title: 'Add',
      // title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      // username: 'test user',
      // profile_img: 'https://cdn.quasar.dev/img/avatar.png',

      forumList: [
        {
          forum_id: 1,
          title: 'Add a YouTube stats widget to your iPhone with JavaScript',
          thumnail: 'https://cdn.quasar.dev/img/mountains.jpg',
          ref_tags: ['vue', 'django'],
          like_num: 7,
          comment_num: 1,
          viewed_num: 20,
          user_info: {
            // 글 작성자 정보
            user_id: 3,
            username: 'test1',
            written_time: '2021-01-24T02:02',
            profile_img: 'https://cdn.quasar.dev/img/avatar.png',
          },
        },
        {
          forum_id: 2,
          title: '두 번째 글',
          thumnail: 'https://placeimg.com/500/300/nature',
          ref_tags: ['django', 'python'],
          like_num: 10,
          comment_num: 3,
          viewed_num: 10,
          user_info: {
            // 글 작성자 정보
            user_id: 5,
            username: 'user2',
            written_time: '2021-01-24T02:02',
            profile_img: 'https://cdn.quasar.dev/img/mountains.jpg',
          },
        },
      ],
    };
  },
  methods: {
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
    goToDetail() {
      this.$router.push({ name: 'ForumDetail' });
    },
  },
};
</script>

<style scoped>
.col-align {
  display: flex;
  align-items: center;
}

.icon-position {
  float: right;
}
.q-tab >>> .q-tab__label {
  font-size: 13pt;
  font-weight: bold;
}
.q-input >>> .q-icon {
  size: 5px;
}
.q-input >>> .q-field__control {
  height: 40px;
}
.q-input >>> .q-field__append {
  height: 40px;
}
.tag-filter {
  height: 38px;
  margin-left: 15px;
}
</style>
