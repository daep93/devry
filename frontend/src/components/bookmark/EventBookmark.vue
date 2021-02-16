<template>
  <div class="row col-12">
    <div
      class="row col-12 q-mb-md text-h6 text-weight-bold"
      style="color: #545454"
    >
      Event bookmark
    </div>
    <div
      v-for="(data, index) in EventBookmarkList"
      key="data"
      class="row col-9 q-mb-sm"
    >
      <q-card class="row full-width q-pa-md" flat bordered>
        <div class="row col-12">
          <div class="row col-9">
            <div class="row col-12 q-mb-sm">
              <span class="text-body1">{{ data.title }}</span>
            </div>
            <div class="row col-12">
              <span
                v-for="tag in data.ref_tags"
                :key="tag"
                :style="{ 'background-color': tagColor(tag, 0.5) }"
                style="font-size:0.8em; border-radius:3pt;"
                class="q-px-xs q-mr-sm"
                >#{{ tag.charAt(0).toUpperCase() + tag.slice(1) }}</span
              >
            </div>
          </div>
          <div class="row col-2">
            <div class="row col-12">@{{ data.user.username }}</div>
            <div class="row col-12 text-caption">
              {{ data.start | moment('YYYY/MM/DD') }}
            </div>
          </div>
          <div class="row col-1 justify-end">
            <q-icon
              :name="$i.ionBookmark"
              :style="{ color: '#598FFC' }"
              size="xs"
              class="cursor-pointer"
              @click="cancelBookmark(index)"
            ></q-icon>
          </div>
        </div>
      </q-card>
    </div>
  </div>
</template>

<script>
import { getEventBookmarkList } from '@/api/bookmark';
import { toggleEventBookmark } from '@/api/event';
import { colorSoloMapper } from '@/utils/tagColorMapper';

export default {
  data() {
    return {
      EventBookmarkList: [],
    };
  },
  methods: {
    tagColor(tag, alpha) {
      return colorSoloMapper(tag, alpha);
    },
    async getEventBookmark() {
      try {
        this.$q.loading.show();
        const { data } = await getEventBookmarkList();
        this.EventBookmarkList = data;
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    async cancelBookmark(index) {
      try {
        this.$q.loading.show();
        const eventId = this.EventBookmarkList[index].id;
        await toggleEventBookmark(eventId);
        this.getEventBookmark();
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  async created() {
    try {
      this.getEventBookmark();
    } catch (error) {
      console.log(error);
    }
  },
};
</script>

<style scoped></style>
