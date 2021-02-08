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
            v-model="search"
            type="text"
            @keypress.enter="handleScroll(search)"
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
            <q-btn
              flat
              label="취소"
              color="red"
              @click="$store.commit('toggleTagFilter')"
            />
            <q-btn
              flat
              label="선택 적용"
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
import { all_tag_list } from '@/utils/autoComplete';
import { scroll } from 'quasar';
const { getScrollTarget, setScrollPosition } = scroll;
export default {
  data() {
    return {
      search: '',
      scrollInfo: {},
      tags: {
        frontend: false,
        backend: false,
        angular: false,
        django: false,
        java: false,
        'vue.js': false,
        typescript: false,
        docker: false,
        python3: false,
        react: false,
        javascript: false,
        spring: false,
        html5: false,
        css3: false,
        mysql: false,
        mariadb: false,
        'node.js': false,
      },
    };
  },
  methods: {
    tagAutoComplete(str) {
      const reg = new RegExp(`^${str}`, 'i');
      for (const tag of all_tag_list) {
        if (tag.match(reg)) return tag;
      }
      return '';
    },
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
    for (const tag of this.$store.getters.getMyTags) {
      this.tags[tag.toLowerCase()] = true;
    }
  },
};
</script>

<style scoped></style>
