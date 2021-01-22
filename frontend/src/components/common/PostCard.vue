<template>
  <div
    class="row q-mb-sm"
    style="width:100%; border: 1px solid #C1B9B9; border-radius: 8px"
  >
    <div class="col-2">
      <q-img
        :src="require('@/assets/keyboard.png')"
        alt="change-password"
        style="height:120px; clip: inherit;"
      ></q-img>
    </div>
    <div class="col-10 q-pl-sm">
      <div class="row justify-between q-pt-xs q-mb-sm">
        <div class="row items-baseline q-mb-sm">
          <div class="q-mr-sm text-weight-regular">@{{ detail.username }}</div>
          <div class="text-weight-thin" style="font-size:8pt">
            {{ detail.writtenAt | moment('YYYY/MM/DD') }}
          </div>
        </div>
        <div class="row">
          <div class="row items-center q-mr-sm">
            <q-icon
              :name="$i.ionHeart"
              color="red"
              size="22px"
              class="q-mr-sm"
            ></q-icon>
            <span>{{ detail.likeNum }}</span>
          </div>
          <div class="row items-center q-mr-md">
            <q-icon
              :name="$i.ionChatboxEllipsesOutline"
              style="color:#617E9F"
              size="22px"
              class="q-mr-sm"
            ></q-icon>
            <span>{{ detail.commentNum }}</span>
          </div>
          <div></div>
        </div>
      </div>
      <div class="row text-bold" style="font-size:14pt">
        {{ detail.title }}
      </div>
      <div class="row justify-end items-end">
        <span
          v-for="(tag, index) in detail.tags"
          class="q-mr-sm q-mb-sm q-px-xs"
          :style="{ 'background-color': tagColors[index] }"
          style="font-size:10pt; border-radius:5pt"
          :key="tag"
          >{{ tag }}</span
        >
      </div>
    </div>
  </div>
</template>

<script>
import { colorMapper } from '@/utils/tagColorMapper';
export default {
  props: {
    detail: Object,
  },
  computed: {
    tagColors() {
      return colorMapper(this.detail.tags);
    },
  },
};
</script>

<style scoped></style>
