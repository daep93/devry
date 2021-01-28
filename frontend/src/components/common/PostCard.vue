<template>
  <div class="row q-mb-sm post-card-frame">
    <div class="col-2">
      <q-img
        src="https://source.unsplash.com/random"
        alt="change-password"
        class="post-thumbnail"
      ></q-img>
    </div>
    <div class="col-10 q-pl-sm row content-between wrap" style="height:100%">
      <div class="row justify-between q-pt-xs q-mb-sm col-12">
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
      <div class="row text-bold col-12 q-px-md q-mb-xs" style="font-size:14pt">
        {{ detail.title }}
      </div>
      <div class="row justify-end items-end col-12">
        <span
          v-for="(tag, index) in detail.tags"
          class="q-mr-sm q-mb-sm q-px-xs tag-color"
          :style="{ 'background-color': tagColors[index] }"
          :key="tag"
          >#{{ tag }}</span
        >
      </div>
    </div>
  </div>
</template>

<script>
import { colorListMapper } from '@/utils/tagColorMapper';
export default {
  props: {
    detail: Object,
  },
  computed: {
    tagColors() {
      return colorListMapper(this.detail.tags);
    },
  },
};
</script>

<style scoped>
.post-card-frame {
  width: 100%;
  border: 1px solid #c1b9b9;
  border-radius: 8px;
}
.post-thumbnail {
  height: 130px;
  clip: inherit;
}
.tag-color {
  font-size: 10pt;
  border-radius: 5pt;
}
</style>
