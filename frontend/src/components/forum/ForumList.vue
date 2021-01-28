<template>
  <div class="row justify-center q-ml-md q-mt-lg">
    <div class="row col-8">
      <div class="text-h4 text-weight-bold q-mb-lg col-12">Forum 게시판</div>
      <div class="row justify-between col-12">
        <!-- tab 라벨 -->
        <q-tabs
          v-model="tab"
          no-caps
          dense
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          narrow-indicator
        >
          <q-tab name="feed" label="Feed" />
          <q-tab name="latest" label="Latest" />
        </q-tabs>
        <!-- 서치바, 태그 버튼 -->
        <div class="row justify-end q-gutter-lg">
          <q-input v-model="search" type="search" outlined>
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
      <div class=" justify-center col-12">
        <q-tab-panels v-model="tab" animated>
          <q-tab-panel :name="tab">
            <!-- 피드 리스트 -->
            <div class="row ">
              <div
                v-for="(data, index) in tab === 'feed'
                  ? forumList
                  : forumListSorted"
                :key="index"
                class="q-pa-sm row col-4"
              >
                <!-- 썸네일 -->
                <q-card class="my-card">
                  <img :src="data.thumnail" style="height: 50%;" />
                  <q-card-section
                    class="q-pa-md cursor-pointer text-weight-bold"
                    style="font-size: 14pt; height: 21%;"
                    @click="goToDetail"
                  >
                    {{ data.title }}
                  </q-card-section>

                  <div
                    class="row  q-px-md q-gutter-xs q-mb-xs"
                    style="height: 10%;"
                  >
                    <span v-for="tag in data.ref_tags" :key="tag">
                      <q-badge class="q-pa-xs" color="blue">
                        # {{ tag }}
                      </q-badge>
                    </span>
                  </div>

                  <q-card-section class="q-px-md">
                    <div class="row">
                      <div class="row col-7 items-center q-gutter-sm">
                        <div class="row justify-center items-center">
                          <q-avatar
                            class="cursor-pointer"
                            @click="goToProfile"
                            style="width: 35px; height: 35px;"
                            ><img :src="data.user_info.profile_img" />
                          </q-avatar>
                        </div>
                        <div>
                          <div
                            class="cursor-pointer"
                            style="color: #464646"
                            @click="goToProfile"
                          >
                            <b>{{ data.user_info.username }}</b>
                          </div>
                          <div style="font-size: 5pt; color: #464646">
                            {{ data.user_info.written_time }}
                          </div>
                        </div>
                      </div>

                      <div class="col-5 row items-end justify-end">
                        <div class="icon-position q-mb-xs row items-center">
                          <div class="q-mr-xs">
                            <q-icon
                              :name="$i.ionHeartOutline"
                              style="color:#727272"
                              size="22px"
                            ></q-icon>
                          </div>
                          <div class="q-mr-md" style=" font-size: 13pt;">
                            {{ data.like_num }}
                          </div>
                          <div class="q-mr-sm">
                            <q-icon
                              :name="$i.ionChatboxEllipsesOutline"
                              style="color:#727272"
                              size="22px"
                            ></q-icon>
                          </div>
                          <span style="font-size: 13pt;">{{
                            data.comment_num
                          }}</span>
                        </div>
                      </div>
                    </div>
                  </q-card-section>
                </q-card>
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
            written_time: '2021-01-25T02:02',
            profile_img: 'https://cdn.quasar.dev/img/mountains.jpg',
          },
        },
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
            written_time: '2021-01-25T04:02',
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
            written_time: '2021-01-23T11:02',
            profile_img: 'https://cdn.quasar.dev/img/mountains.jpg',
          },
        },
      ],
      forumListSorted: [],
    };
  },
  created() {
    this.forumListSorted = this.forumList.slice();
    this.forumListSorted.sort((a, b) => {
      if (this.$moment(a.written_time).isAfter(b.written_time)) {
        return 1;
      } else {
        return -1;
      }
    });
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
