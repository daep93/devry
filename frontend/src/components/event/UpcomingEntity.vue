<template>
  <div>
    <q-card style="border-radius: 20px;">
      <q-card-section class="q-px-md q-pt-lg q-pb-none">
        <div class="q-pa-xs row justify-between">
          <div
            class="text-weight-bold text-weight-bold col-10 cursor-pointer"
            style="font-size:1.1em"
            @click="goToDetail"
          >
            {{ entity.title }}
          </div>
          <div class="col-2 row justify-end">
            <q-icon
              class="col"
              :name="entity.bookmarked ? 'bookmark' : 'bookmark_border'"
              size="sm"
              :color="entity.bookmarked ? 'blue-12' : 'grey-6'"
            ></q-icon>
            <span class="col q-pl-xs text-grey-8" style="font-size:1.2em;">
              {{ entity.bookmark_num }}
            </span>
          </div>
        </div>
      </q-card-section>
      <q-card-section class="q-px-lg q-pt-sm q-pb-xs">
        <ul class="row q-gutter-sm">
          <li
            v-for="(tag, index) in entity.ref_tags"
            :key="index"
            class="cursor-pointer"
          >
            <q-badge
              class="text-black q-py-xs q-mr-xs shadow-3"
              :style="{
                'background-color': tagColor(tag),
              }"
            >
              # {{ tag }}
            </q-badge>
          </li>
        </ul>
      </q-card-section>
      <q-card-section class="q-px-lg q-pt-sm q-pb-lg">
        <div class="row justify-between items-end">
          <div class="text-subtitle2 text-weight-bold text-primary">
            {{ entity.start | moment('YYYY/MM/DD') }}
          </div>
          <div>
            <img
              :src="entity.profile_img"
              style="width: 50px; height: 40px;  border-radius: 10px;"
            />
          </div>
        </div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import { 
  colorSoloMapper,
  // matchingColorSoloMapper,
} from '@/utils/tagColorMapper';

export default {
  props: {
    entity: Object,
  },
  methods: {
    tagColor(tag) {
      return colorSoloMapper(tag, 0.5);
    },
    goToDetail() {
      this.$router.push(`/event-detail/${this.entity.id}`);
    }
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>