<template>
  <q-drawer
    v-model="$store.state.tagFilter"
    side="right"
    behavior="desktop"
    bordered
    :width="232"
    overlay
    class="row full-width"
  >
    <q-card>
      <q-card-actions align="center" style="height:40px"> </q-card-actions>
      <q-card-section class="row">
        <q-card
          flag
          class="row full-width justify-center q-my-sm"
          v-for="(flag, tag) in tags"
          :key="tag"
          :style="{
            'background-color': flag ? mainColor(tag) : '#EEF0F1',
            'transition-duration': '0.5s',
            'transition-timing-function': 'ease-in-out',
          }"
          :id="`toggle-${tag}`"
        >
          <q-card-section class="col-12">
            <q-btn
              flat
              class="full-width"
              :style="{
                'background-color': flag ? subColor(tag) : '#acb3b7',
                color: flag ? mainColor(tag) : 'white',
                'transition-duration': '0.5s',
                'transition-timing-function': 'ease-in-out',
              }"
              @click="toggleFollow(tag)"
            >
              <div class="row items-center">
                <div>#{{ tag }}</div>
                <q-icon
                  size="xs"
                  :name="$i.ionCheckmarkOutline"
                  v-if="flag"
                  :style="{
                    color: flag ? mainColor(tag) : 'white',
                    'transition-duration': '0.5s',
                    'transition-timing-function': 'ease-in-out',
                  }"
                ></q-icon>
              </div>
            </q-btn>
          </q-card-section>
        </q-card>
      </q-card-section>

      <q-card-actions align="center" style="height:40px"> </q-card-actions>
    </q-card>
    <!-- 태그 검색 -->
    <q-page-sticky position="top" :offset="[0, -51]" expand class="q-pr-md">
      <q-card class="row full-width justify-center" flat>
        <q-card-actions align="center" class="">
          <q-input
            style="height:40px"
            v-model="searched_tag"
            type="text"
            @keypress.enter="handleScroll(searched_tag)"
            label="태그 검색"
          />
        </q-card-actions>
      </q-card>
    </q-page-sticky>

    <!-- 태그 적용 -->
    <q-page-sticky position="bottom" expand class="q-pr-md">
      <q-card class="row full-width justify-center" flat>
        <q-card-actions align="center">
          <div class="bg-white">
            <q-btn flat color="black" @click="toggleAllTags">
              전체 선택
              <q-icon
                size="xs"
                :name="$i.ionCheckmarkOutline"
                v-if="all_flag"
                :style="{
                  'transition-duration': '0.5s',
                  'transition-timing-function': 'ease-in-out',
                }"
              ></q-icon>
            </q-btn>
            <q-btn
              flat
              label="취소"
              color="red"
              @click="$store.commit('toggleTagFilter')"
            />
            <q-btn
              flat
              label="적용"
              color="primary"
              @click="updateSelectedTags"
            />
          </div>
        </q-card-actions>
      </q-card>
    </q-page-sticky>
  </q-drawer>
</template>

<script>
import {
  colorSoloMapper,
  matchingColorSoloMapper,
} from '@/utils/tagColorMapper';
import { scroll } from 'quasar';
const { getScrollTarget, setScrollPosition } = scroll;
export default {
  data() {
    return {
      searched_tag: '',
      scrollInfo: {},
      tags: { ...this.$store.state.tags_selected },
      all_flag: false,
    };
  },
  methods: {
    // 모든 토글을 선택하거나 해제할 수 있다.
    toggleAllTags() {
      this.all_flag = !this.all_flag;
      for (const tag in this.tags) {
        this.tags[tag] = this.all_flag;
      }
    },

    // 태그를 적을 때 자동으로 부분일치하는 태그를 제시해준다.
    tagAutoComplete(str) {
      const reg = new RegExp(`^${str}`, 'i');
      for (const tag of this.$store.state.all_tag_list) {
        if (tag.match(reg)) return tag;
      }
      return '';
    },
    // 주어진 태그를 찾아서 이동한다.
    handleScroll(str) {
      let tag;
      if (!(tag = this.tagAutoComplete(str))) return;
      const ele = document.getElementById(`toggle-${tag}`);
      const target = getScrollTarget(ele);
      const offset = ele.offsetTop - ele.scrollHeight;
      const duration = 500;
      setScrollPosition(target, offset, duration);
    },
    mainColor(tag) {
      return colorSoloMapper(tag, 1);
    },
    subColor(tag) {
      return matchingColorSoloMapper(tag, 1);
    },
    toggleFollow(tag) {
      this.tags[tag] = !this.tags[tag];
    },
    updateSelectedTags() {
      const selectedTags = [];
      for (const tag in this.tags) {
        if (this.tags[tag]) selectedTags.push(tag);
      }
      this.$store.commit('setSelectedTags', selectedTags);
      this.$store.commit('toggleTagFilter');
    },
  },
  created() {
    if (this.$store.getters.getMyTags.length > 0) {
      for (const tag in this.tags) this.tags[tag] = false;
      for (const tag of this.$store.getters.getMyTags) {
        this.tags[tag] = true;
      }
    }
  },
};
</script>

<style scoped></style>
