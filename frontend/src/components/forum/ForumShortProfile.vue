<template>
  <div>
    <div style="margin-top: 16px;">
      <q-card
        flat
        bordered
        class="my-card margin:0 auto;"
        style="padding: 10px; width: 250px; "
      >
        <q-card-section>
          <div class="row">
            <div class="col-2">
              <span style="cursor:pointer;">
                <q-avatar
                  @click="goToProfile"
                  style="width: 35px; height: 35px;"
                  ><img :src="profile_img" />
                </q-avatar>
              </span>
            </div>
            <div class="col-10">
              <div
                style="margin-left: 12px; font-size: 15px; cursor:pointer; height: 17px; color: #464646"
                @click="goToProfile"
              >
                <b>{{ username }}</b>
              </div>
              <span style="font-size: 10px; margin-left: 12px;"
                >글 12 · 팔로워 58</span
              >
            </div>
          </div>
        </q-card-section>
        <div style="margin-left: 15px; margin-right: 12px;">
          <p style="font-size: 13px;">
            FE Engineer for en expensive cars company. Archer at night. Ask me
            about company culture, side projects, performance and Vue.
          </p>
        </div>
        <center>
          <div style="margin-bottom: 10px;">
            <div v-if="follow">
              <q-btn
                no-caps
                color="primary"
                id="follow-btn"
                label="Follow"
                style="width:200px;"
                @click="checkFollow(index)"
              />
            </div>
            <div v-else>
              <q-btn
                no-caps
                outline
                color="primary"
                label="Following"
                style="width:200px;"
                @click="checkFollow(index)"
              />
            </div>
          </div>
        </center>
      </q-card>
    </div>

    <!-- 작성자 글 리스트 -->
    <div style="margin-top: 16px;">
      <q-card flat bordered class="my-card" style="padding: 8px; width: 250px;">
        <q-card-section>
          <span style="color: #598FFC">
            <b>{{ username }}</b></span
          >
          님의 대표글 더 보기
        </q-card-section>
        <q-separator inset />
        <q-card-section>
          <div @click="goToDetail" style="cursor:pointer">
            Products Quantity Counter Using HTML CSS
          </div>
        </q-card-section>
        <q-separator inset />
        <q-card-section>
          <div @click="goToDetail" style="cursor:pointer">
            {{ title }}
          </div>
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      username: 'Test User',
      profile_img: 'https://cdn.quasar.dev/img/avatar.png',
      follow: true,
    };
  },
  methods: {
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
    goToDetail() {
      this.$router.push({ name: 'ForumDetail' });
    },
    checkFollow() {
      this.follow = !this.follow;
    },
  },
};
</script>

<style scoped></style>
