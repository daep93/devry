<template>
  <div>
    <q-card
      flat
      bordered
      class="my-card row col-12 q-pa-sm q-mb-sm"
      style="max-width: 250px; max-height: 280px;"
    >
      <q-card-section>
        <div class="row col-12">
          <div class="row col-2">
            <span class="q-mt-xs">
              <q-avatar
                @click="goToProfile"
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
                <b class="cursor-pointer">{{ username }}</b>
                <div class="text-caption">
                  글 27 · 팔로워 57
                </div>
              </div>
            </div>
          </div>
        </div>
      </q-card-section>
      <div class="q-px-md q-pb-md">
        <div style="font-size: 13px;">
          FE Engineer for en expensive cars company. Archer at night. Ask me
          about company culture, side projects, performance and Vue.
        </div>
      </div>
      <div style="margin:0 auto;">
        <template v-if="follow">
          <q-btn
            no-caps
            color="primary"
            id="follow-btn"
            label="Follow"
            @click="checkFollow"
            style="width: 200px"
            class="q-mb-sm"
          />
        </template>
        <template v-else>
          <q-btn
            no-caps
            outline
            color="primary"
            label="Following"
            @click="checkFollow"
            style="width: 200px"
            class="q-mb-sm"
          />
        </template>
      </div>
    </q-card>
    <q-card
      flat
      bordered
      class="my-card row col-12 q-px-sm q-pt-md"
      style="max-width: 250px; max-height: 280px;"
    >
      <div class="q-px-md q-pb-sm">
        <div style="font-size: 13px;">
          <div class="q-my-sm">
            <span class="text-weight-bold cursor-pointer" style="color: #598FFC"
              >Test User</span
            >
            <span>님의 글 더보기</span>
          </div>
          <q-separator />
          <div class="q-my-sm">
            FE Engineer for en expensive cars company.
          </div>
          <q-separator />
          <div class="q-my-sm">
            Archer at night. Ask me about company culture, side projects,
            performance and Vue.
          </div>
        </div>
      </div>
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
      follow: false,
    };
  },
  methods: {
    checkFollow() {
      this.follow = !this.follow;
      console.log(this.follow);
    },
    goToProfile() {
      console.log('click!');
      this.$router.push({ name: 'Profile' });
    },
  },
};
</script>

<style scoped></style>
