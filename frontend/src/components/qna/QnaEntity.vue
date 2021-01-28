<template>
  <div class="row col-12 " style="border: 1px solid #eaebef;">
    <div class="row col-8">
      <div
        class="full-height"
        :style="{
          'background-color': entity.solved ? '#1976D2' : '#C8DAFE',
          width: '25px',
        }"
      ></div>
      <div class="row col-11 q-pl-sm q-pt-xs">
        <div class="row text-weight-bold qna-title col-12 q-mb-xs">
          <span class="text-weight-thin text-grey-8"
            >#{{ entity.questId }}</span
          >
          {{ entity.title }}
        </div>

        <div class="row q-mr-xs q-gutter-sm q-mb-sm col-12">
          <span
            v-for="tag in entity.refTags"
            :key="tag"
            :style="{ 'background-color': tagColor(tag, 0.5) }"
            style="font-size:0.8em; border-radius:3pt;"
            class="q-px-xs"
            >#{{ tag.charAt(0).toUpperCase() + tag.slice(1) }}</span
          >
        </div>
      </div>
    </div>
    <div class="row col-4 q-pl-sm">
      <div class="row col-2 items-center">
        <q-icon :name="$i.ionHeartOutline" size="sm" color="grey-6"></q-icon>
        <span class="q-pl-xs text-grey-8" style="font-size:1.2em;">{{
          entity.likeNum
        }}</span>
      </div>
      <div class="row col-2 items-center">
        <q-icon
          :name="$i.ionChatboxEllipsesOutline"
          size="sm"
          color="grey-6"
        ></q-icon>
        <span class="q-pl-xs text-grey-8" style="font-size:1.2em;">{{
          entity.commentNum
        }}</span>
      </div>
      <div class="row col-2  items-center justify-center">
        <q-icon :name="$i.ionEyeOutline" size="sm" color="grey-6"></q-icon>
        <span class="q-pl-xs text-grey-8" style="font-size:1.2em;">{{
          entity.viewedNum
        }}</span>
      </div>
      <div class="row col-6 items-center justify-center q-py-xs ">
        <div class="">
          <q-avatar style="border: 1px solid #ECEFF1" size="2.8em">
            <q-img :src="require('@/assets/keyboard.png')" />
          </q-avatar>
        </div>
        <div class="q-pl-sm">
          <div class="text-weight-regular col-12 text-primary">
            {{ entity.userInfo.username }}
          </div>
          <div class="text-weight-thin col-12" style="font-size:8pt">
            {{ entity.writtenTime | moment('YYYY/MM/DD HH:mm') }}
          </div>
        </div>
      </div>
    </div>
  </div>
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
  },
};
</script>

<style scoped>
.qna-title {
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
