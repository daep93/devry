<template>
  <q-card class="col-7 q-mt-xl">
    <q-card-section>
      <div class="row items-center">
        <div class="col-3 row justify-center">
          <div class="col-9">
            <q-img
              :src="info.profileImg ? img : require('@/assets/basic_image.png')"
              alt="change-password"
              class="profile-picture "
              style="width:150px;height:150px"
            ></q-img>
          </div>
        </div>
        <div class="col-9 q-pr-xl">
          <div class="row q-mb-sm justify-between">
            <span class="text-h5  text-indigo-14"> @{{ info.username }}</span>
            <q-btn
              style="background-color:#1595DC;"
              class="text-white text-bold"
              >follow</q-btn
            >
          </div>
          <!-- 사는 곳, 소속, 이메일 정보를 받는 행 -->
          <div class="row q-mb-md full-width">
            <div class="q-mr-md row items-center">
              <q-icon
                :name="$i.ionLocationOutline"
                size="sm"
                class="q-mr-xs"
              ></q-icon>
              <span>{{ info.region ? info.region : '-' }}</span>
            </div>
            <div class="q-mr-md row items-center">
              <q-icon
                :name="$i.ionBriefcaseOutline"
                size="sm"
                class="q-mr-xs"
              ></q-icon>
              <span>{{ info.group ? info.group : '-' }}</span>
            </div>
            <div class="q-mr-md row items-center">
              <q-icon
                :name="$i.ionMailOutline"
                size="sm"
                class="q-mr-xs"
              ></q-icon>
              <span>{{ info.email }}</span>
            </div>
          </div>
          <!-- 등록된 웹싸이트 링크에 맞춰 로고를 보여주는 행-->
          <div class="row  q-mb-md full-width">
            <q-icon
              v-for="link in info.links"
              :key="link.sns_name"
              :name="
                $i[
                  `ionLogo${link.sns_name.charAt(0).toUpperCase() +
                    link.sns_name.slice(1)}`
                ]
              "
              size="sm"
              color="grey-8"
              class="q-mr-xs cursor-pointer"
              @click="linkRedirect(link.sns_url)"
            ></q-icon>
          </div>
          <!-- 가입날짜와 팔로워/팔로우 수를 표시해주는 행 -->
          <div class="row q-mb-sm justify-between full-width">
            <div class="row items-center">
              <q-icon
                :name="$i.ionCalendarClearOutline"
                color="grey-8"
                size="xs"
                class="q-mr-xs"
              ></q-icon>
              <span>joined on {{ info.joined | moment('YYYY/MM/DD') }}</span>
            </div>
            <div>
              <span class="q-mr-md cursor-pointer" @click="onFollow('follow')"
                >팔로워: <b>{{ info.followerNum }}</b></span
              >
              <span class="cursor-pointer" @click="onFollow('following')"
                >팔로우: <b>{{ info.followeeNum }}</b></span
              >
            </div>
          </div>
        </div>
      </div>
      <div class="row q-px-xl q-my-md full-width">
        <div class="full-width">
          {{ info.bio }}
        </div>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  props: {
    info: Object,
  },
  methods: {
    linkRedirect(url) {
      window.open(url);
    },
    onFollow(tab) {
      this.$store.commit('onFollowModal', tab);
    },
  },
  data() {
    return {
      img: `${process.env.VUE_APP_SERVER_API_URL}${this.info.profileImg}`,
    };
  },
};
</script>

<style scoped>
.profile-picture {
  width: 100%;
  border: 5px solid #d1d4f1;
  border-radius: 100px;
}
</style>
