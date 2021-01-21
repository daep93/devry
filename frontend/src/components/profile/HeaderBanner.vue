<template>
  <q-card class="header-banner">
    <q-card-section>
      <div class="row q-pl-xl">
        <div class="col-2">
          <q-img
            :src="require('@/assets/change_pwd.png')"
            alt="change-password"
            class="profile-picture"
          ></q-img>
        </div>
        <div class="col-9 q-ml-md">
          <div class="row q-mb-sm justify-between">
            <span class="text-h5 q-pl-xs">{{ info.username }}</span>
            <q-btn
              style="background-color:#1595DC;"
              class="text-white text-bold"
              >follow</q-btn
            >
          </div>
          <!-- 사는 곳, 소속, 이메일 정보를 받는 행 -->
          <div class="row q-mb-md">
            <div class="q-mr-md row items-center">
              <q-icon
                :name="$i.ionLocationOutline"
                size="sm"
                class="q-mr-xs"
              ></q-icon>
              <span>{{ info.location }}</span>
            </div>
            <div class="q-mr-md row items-center">
              <q-icon
                :name="$i.ionBriefcaseOutline"
                size="sm"
                class="q-mr-xs"
              ></q-icon>
              <span>{{ info.group }}</span>
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
          <div class="row  q-mb-md">
            <q-icon
              v-for="(url, logo) in info.links"
              :key="logo"
              :name="$i[`ionLogo${logo}`]"
              size="sm"
              color="grey-8"
              class="q-mr-xs"
              @click="linkRedirect(url)"
              style="cursor:pointer"
            ></q-icon>
          </div>
          <!-- 가입날짜와 팔로워/팔로우 수를 표시해주는 행 -->
          <div class="row q-mb-sm justify-between">
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
              <span class="q-mr-md"
                >팔로워: <b>{{ info.followerNum }}</b></span
              >
              <span
                >팔로우: <b>{{ info.followeeNum }}</b></span
              >
            </div>
          </div>
        </div>
      </div>
      <div class="row q-pl-xl q-my-md">
        <p>
          {{ info.introduction }}
        </p>
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
  },
};
</script>

<style scoped>
.header-banner {
  width: 60%;
  position: relative;
  top: -10vh;
  z-index: 1;
}
.profile-picture {
  width: 100%;
  border: 5px solid #ece1e1;
  border-radius: 100px;
}
</style>
