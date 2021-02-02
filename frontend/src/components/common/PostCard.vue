<template>
  <div class="row q-mb-sm post-card-frame">
    <div class="col-2" style="">
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
            {{ detail.written_time | moment('YYYY/MM/DD') }}
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
            <span>{{ detail.like_num }}</span>
          </div>
          <div class="row items-center q-mr-md">
            <q-icon
              :name="$i.ionChatboxEllipsesOutline"
              style="color:#617E9F"
              size="22px"
              class="q-mr-sm"
            ></q-icon>
            <span>{{ detail.comment_num }}</span>
          </div>
          <div></div>
        </div>
      </div>
      <div
        class="row text-bold col-12 q-px-md q-mb-xs"
        style="font-size:14pt; height:80px"
      >
        {{ detail.title }}
      </div>
      <div class="row justify-end items-end col-12">
        <span
          v-for="tag in detail.tags"
          class="q-mr-sm q-mb-sm q-px-xs tag-color"
          :style="{ 'background-color': tagColor(tag) }"
          :key="tag"
          >#{{ tag }}</span
        >
      </div>
    </div>
  </div>
</template>

<script>
import { colorSoloMapper } from '@/utils/tagColorMapper';
export default {
  props: {
    detail: Object,
  },
  methods: {
    tagColor(tag) {
      return colorSoloMapper(tag, 0.2);
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
  height: 150px;
  clip: inherit;
}
.tag-color {
  font-size: 10pt;
  border-radius: 5pt;
}
</style>
