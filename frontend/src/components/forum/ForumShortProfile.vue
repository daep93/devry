<template>
  <div>
    <q-card flat bordered class="my-card row col-12 q-pa-sm q-mb-sm">
      <q-card-section>
        <div class="row col-12">
          <div class="row col-2">
            <span class="q-mt-xs">
              <q-avatar
                style="width: 35px; height: 35px;"
                class="cursor-pointer"
                ><img :src="profile_img" />
              </q-avatar>
            </span>
          </div>
          <div class="row col-10">
            <div class="row col-12">
              <div
                class="q-pl-lg"
                style="font-size: 15px; color: #464646"
                @click="goToProfile"
              >
                <b class="cursor-pointer">유저이름</b>
                <div class="text-caption row">
                  글 0 · 팔로워 0
                </div>
              </div>
            </div>
          </div>
        </div>
      </q-card-section>
      <div class="q-px-md q-pb-md row col-12">
        <div class="text-body2">
          상태메시지
        </div>
      </div>
      <div class="row col-12 justify-center">
        <template v-if="follow">
          <q-btn
            no-caps
            color="primary"
            id="follow-btn"
            label="Follow"
            @click="checkFollow"
            class="q-mb-sm row col-10"
          />
        </template>
        <template v-else>
          <q-btn
            no-caps
            outline
            color="primary"
            label="Following"
            @click="checkFollow"
            class="q-mb-sm row col-10"
          />
        </template>
      </div>
    </q-card>
    <q-card flat bordered class="my-card row col-12 q-pa-lg">
      <div class="q-mb-md">
        <span class="text-weight-bold cursor-pointer" style="color: #598FFC"
          >유저이름</span
        >
        <span>님의 글 더 보기</span>
      </div>
      <template>
        <q-separator />
        <div class="q-mt-md">
          제목
        </div>
      </template>
    </q-card>
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
