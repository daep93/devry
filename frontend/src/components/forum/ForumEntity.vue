<template>
  <q-card class="row full-width" style="height:300px">
    <!-- 썸네일 -->
    <!-- <q-img
      class="row full-width"
      :src="require('@/assets/keyboard.png')"
      style="height:50%"
    /> -->
    <img :src="entity.thumnail" style="height: 50%;" />
    <!-- 타이틀 -->
    <div
      class="row full-width q-px-sm q-py-sm cursor-pointer text-weight-bold forum-title"
      style="font-size: 1.1em;height:19%"
      @click="goToDetail"
    >
      {{ entity.title }}
    </div>
    <!-- 태그 -->
    <div
      class="row full-width q-px-sm  q-py-sm cursor-pointer"
      style="height:10%"
    >
      <div
        v-for="(tag, index) in entity.ref_tags"
        :key="index"
        :style="{ 'background-color': tagColor(tag, 0.3) }"
        style="font-size:0.8em; border-radius:3pt ;"
        class="q-pa-xs q-mr-xs  "
      >
        # {{ tag }}
      </div>
    </div>
    <div class="row full-width  q-px-sm q-py-sm " style="height:20%">
      <div class="row col-12">
        <div class="row col-7 items-center q-gutter-sm">
          <div class="row justify-center items-center">
            <q-avatar
              class="cursor-pointer"
              @click="goToProfile"
              style="width: 35px; height: 35px;"
            >
              <q-img :src="require('@/assets/keyboard.png')" />
              <!-- <img :src="data.user_info.profile_img" /> -->
            </q-avatar>
          </div>
          <div class="row items-center">
            <div
              class="cursor-pointer"
              style="color: #464646"
              @click="goToProfile"
            >
              <b>{{ entity.user.username }}</b>
            </div>
            <div style="font-size: 5pt; color: #464646">
              {{ entity.written_time | moment('YYYY/MM/DD hh:mm') }}
            </div>
          </div>
        </div>

        <div class="col-5 row items-end justify-end items-md-baseline">
          <div class="icon-position q-mb-xs row items-center">
            <div class="q-mr-xs">
              <q-icon
                :name="$i.ionHeartOutline"
                style="color:#727272"
                size="22px"
              ></q-icon>
            </div>
            <div class="q-mr-md" style=" font-size: 13pt;">
              {{ entity.like_num }}
            </div>
            <div class="q-mr-sm">
              <q-icon
                :name="$i.ionChatboxEllipsesOutline"
                style="color:#727272"
                size="22px"
              ></q-icon>
            </div>
            <span style="font-size: 13pt;">{{ entity.comment_count }}</span>
          </div>
        </div>
      </div>
    </div>
  </q-card>
</template>

<script>
import { colorSoloMapper } from '@/utils/tagColorMapper';
export default {
  props: {
    entity: Object,
  },
  methods: {
    tagColor(tag, alpha) {
      return colorSoloMapper(tag, alpha);
    },
    // TODO: 추후 연결 페이지 수정 필요
    goToDetail() {
      this.$router.push(`/forum-detail/${this.entity.id}`);
    },
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
  },
};
</script>

<style scoped>
.forum-title {
  line-height: 1.6;
  max-height: 3.2em;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
</style>
