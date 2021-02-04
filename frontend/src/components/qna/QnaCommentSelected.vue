<template>
  <!-- 채택 댓글 프로필 -->
  <div class="row cal-3 q-pt-lg q-ml-sm">
    <q-card
      flat
      bordered
      class="my-card row col-12 q-pa-sm"
      style="max-width: 250px; max-height: 280px;"
    >
      <q-card-section>
        <div class="row col-12">
          <div class="row col-2">
            <span style="cursor:pointer;" class="q-mt-xs">
              <q-avatar @click="goToProfile" style="width: 35px; height: 35px;"
                ><img :src="profile_img" />
              </q-avatar>
            </span>
          </div>
          <div class="row col-10">
            <div class="row col-12">
              <div
                class="q-pl-lg"
                style="font-size: 15px; cursor:pointer; color: #464646"
                @click="goToProfile"
              >
                <b>{{ username }}</b>
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
        <div v-if="follow">
          <q-btn
            no-caps
            color="primary"
            id="follow-btn"
            label="Follow"
            @click="checkFollow(index)"
            style="width: 200px"
            class="q-mb-sm"
          />
        </div>
        <div v-else>
          <q-btn
            no-caps
            outline
            color="primary"
            label="Following"
            @click="checkFollow(index)"
            style="width: 220px"
            class="q-mb-sm"
          />
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
      follow: true,
    };
  },
};
</script>

<style scoped></style>
