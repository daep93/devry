<template>
  <q-drawer
    v-model="$store.state.tagFilter"
    side="right"
    behavior="desktop"
    bordered
    :width="230"
    overlay
  >
    <q-card>
      <q-card-section class="q-gutter-md">
        <q-card
          flag
          v-for="(flag, tag) in tags"
          :key="tag"
          :style="{
            'background-color': flag ? mainColor(tag) : '#EEF0F1',
            'transition-duration': '0.5s',
            'transition-timing-function': 'ease-in-out',
          }"
        >
          <q-card-section
            :style="{
              color: flag ? subColor(tag) : 'black',
              'font-size': '1.2em',
              'transition-duration': '0.5s',
              'transition-timing-function': 'ease-in-out',
            }"
          >
            #{{ tag }}
          </q-card-section>

          <q-card-section>
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
                <q-icon
                  :name="$i.ionCheckmarkOutline"
                  v-if="flag"
                  :style="{
                    color: flag ? mainColor(tag) : 'white',
                    'transition-duration': '0.5s',
                    'transition-timing-function': 'ease-in-out',
                  }"
                ></q-icon>
                <div>{{ flag ? 'checked' : 'check' }}</div>
              </div>
            </q-btn>
          </q-card-section>
        </q-card>
      </q-card-section>

      <q-separator />

      <q-card-actions align="center">
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
      </q-card-actions>
    </q-card>
  </q-drawer>
</template>

<script>
import {
  colorSoloMapper,
  matchingColorSoloMapper,
} from '@/utils/tagColorMapper';
export default {
  data() {
    return {
      tags: {
        swift: false,
        flutter: false,
        angular: false,
        django: false,
        java: false,
        vue: true,
        typescript: false,
        docker: false,
        python: true,
        react: false,
        javascript: true,
      },
    };
  },
  methods: {
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
};
</script>

<style scoped></style>
