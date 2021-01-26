<template>
  <div>
    <div
      class="justify-center"
      style="width: 900px; height: 600px; margin:0 auto;"
    >
      <!-- 탭 시작 -->
      <div class="q-pa-md">
        <div class="q-gutter-y-md">
          <q-tabs
            v-model="tab"
            no-caps
            dense
            class="text-grey"
            active-color="primary"
            indicator-color="primary"
            narrow-indicator
            style="max-width: 150px;"
          >
            <q-tab name="feed" label="Feed" />
            <q-tab name="latest" label="Latest" />
          </q-tabs>

          <q-tab-panels v-model="tab" animated>
            <q-tab-panel name="feed">
              <!-- 피드 리스트 -->
              <div v-for="n in 5" :key="n">
                <q-card flat bordered class="my-card" style="width: 800px;">
                  <q-item class="col-align">
                    <!-- 썸네일 -->
                    <div>
                      <q-item-section avatar>
                        <q-avatar
                          rounded
                          style="width: 100px; height: 100px; margin-right: 5px;"
                        >
                          <img src="https://cdn.quasar.dev/img/mountains.jpg" />
                        </q-avatar>
                      </q-item-section>
                    </div>
                    <!-- 프로필 -->
                    <div style="width: 650px; padding-top: 20px;">
                      <span style="cursor: pointer;">
                        <q-avatar
                          @click="goToProfile"
                          style="width: 35px; height: 35px;"
                          ><img :src="profile_img" />
                        </q-avatar>
                      </span>

                      <span style="margin-left: 15px; font-size: 20px;">{{
                        username
                      }}</span>
                      <span style="font-size: 10px; margin-left: 7px;">
                        7시간 전</span
                      >
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
                        <span style="margin-right: 20px;">2 comments</span>
                      </div>
                      <div
                        style="margin-top: 10px; cursor:pointer"
                        @click="goToDetail"
                      >
                        <p style="font-size: 20px;">
                          <b>{{ title }}</b>
                        </p>
                      </div>

                      <!-- 태그 -->
                      <div v-for="i in 3" :key="i">
                        <span class="icon-position" style="margin-left: 10px;">
                          <q-badge color="blue">
                            # Vue
                          </q-badge>
                        </span>
                      </div>
                    </div>
                  </q-item>
                </q-card>
                <br />
              </div>
            </q-tab-panel>

            <q-tab-panel name="latest">
              <div>최신순</div>
              최신순 정렬 내용 위치
            </q-tab-panel>
          </q-tab-panels>
        </div>
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
      title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      username: 'test user',
      profile_img: 'https://cdn.quasar.dev/img/avatar.png',
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
</style>
