<template>
  <div class="row full-width">
    <q-card
      flat
      bordered
      class="q-px-lg row col-12 q-pt-xs my-card"
      style="min-height: 300px;"
    >
      <div class="row col-12 justify-end">
        <span v-if="info.user.id == $store.state.id">
          <q-btn flat round dense icon="more_vert" class="q-mt-md">
            <q-menu>
              <q-list style="min-width: 100px">
                <q-item clickable v-close-popup>
                  <q-item-section>수정하기</q-item-section>
                </q-item>
                <q-item clickable v-close-popup>
                  <q-item-section>삭제하기</q-item-section>
                </q-item>
                <q-separator />
              </q-list>
            </q-menu>
          </q-btn>
        </span>
        <span v-else class="q-mt-xl"></span>
      </div>
      <q-card-section class="row col-12 q-py-none">
        <div class="row col-12 text-weight-bold q-mb-md text-h4">
          <span>{{ info.title }}</span>
        </div>
        <div class="text-subtitle2 text-grey-6 q-mb-md">
          {{ info.written_time | moment('YYYY/MM/DD HH:mm') }}
        </div>
      </q-card-section>
      <q-card-section class="q-pa-none full-width">
        <div class="q-ml-sm">
          <span v-for="tag in info.ref_tags" :key="tag" class="q-px-xs">
            <q-badge
              class="q-pa-sm text-black"
              :style="{ 'background-color': tagColor(tag, 0.5) }"
              style="font-size:1em; border-radius:3pt;"
            >
              # {{ tag }}
            </q-badge>
          </span>
        </div>
      </q-card-section>
      <div
        class="row col-12 q-px-md q-mt-md q-mb-xl"
        style="min-height: 120px;"
      >
        <div class="q-mt-lg">
          {{ info.content }}
        </div>
        <!-- <v-md-editor v-model="content" mode="preview"> </v-md-editor> -->
      </div>
    </q-card>
  </div>
</template>

<script>
import { colorSoloMapper } from '@/utils/tagColorMapper';

export default {
  props: {
    info: Object,
  },
  data() {
    return {
      title: this.info.title,
      tags: ['Javascript', 'Vue.js'],
    };
  },
  methods: {
    tagColor(tag, alpha) {
      return colorSoloMapper(tag, alpha);
    },
  },
};
</script>

<style scoped></style>
