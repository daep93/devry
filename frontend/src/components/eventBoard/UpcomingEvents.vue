<template>
  <div class="row">
    <!-- 소제목 타이틀 -->
    <div class="row col-12 text-h6 text-weight-bold">Upcoming Events</div>
    <!-- 이벤트 카테고리 -->
    <div class="row col-12 justify-end q-mb-sm">
      <!-- <q-btn-dropdown
        color="black"
        label="Category"
        style="width: 100px; height: 30px; font-size: 10px;"
      >
        <q-list v-for="(category, index) in categories" :key="index">
          <q-item clickable v-close-popup @click="onItemClick(category, index)">
            <q-item-section>
              <q-item-label>{{ category }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown> -->
      <q-select
        outlined
        v-model="category"
        :options="['ALL', 'conference', 'workshop', 'hackathon']"
        style="width:140px;"
      />
    </div>
    <!-- 이벤트 목록 -->
    <div class="q-ma-xs row col-12">
      <div class="row col-12">
        <q-intersection
          v-for="(event, index) in categorySortedList"
          :key="index"
          transition="scale"
          class=" col-4 q-pa-xs"
        >
          <q-card style="border-radius: 20px;">
            <q-card-section class="q-px-md q-pt-lg q-pb-none">
              <div class="q-pa-xs row justify-between">
                <div
                  class="text-weight-bold text-weight-bold col-10"
                  style="font-size:1.1em"
                >
                  {{ event.title }}
                </div>
                <div class="col-2 row justify-end">
                  <q-btn
                    padding="0"
                    @click="checkBookMark(index)"
                    flat
                    round
                    color="primary"
                    :icon="event.bookmark ? 'bookmark' : 'bookmark_border'"
                    style="margin-left: 40px;"
                  />
                </div>
              </div>
            </q-card-section>
            <q-card-section class="q-px-lg q-pt-sm q-pb-xs">
              <div class="row q-gutter-sm">
                <div
                  v-for="(tag, index) in event.tags"
                  :key="index"
                  style="font-size:0.9em"
                >
                  #{{ tag }}
                </div>
              </div>
            </q-card-section>
            <q-card-section class="q-px-lg q-pt-sm q-pb-lg">
              <div class="row justify-between items-end">
                <div class="text-subtitle2 text-weight-bold text-primary">
                  {{ event.date }}
                </div>
                <div>
                  <img
                    :src="event.host_info.profile_img"
                    style="width: 50px; height: 40px;  border-radius: 10px;"
                  />
                </div>
              </div>
            </q-card-section>
          </q-card>
        </q-intersection>
      </div>
    </div>
  </div>
</template>

<script>
import { testCase } from '@/dummy/Events.js';
export default {
  data() {
    return {
      category: 'ALL',
    };
  },
  methods: {
    checkBookMark: function(index) {
      this.categorySortedList[index].bookmark = !this.categorySortedList[index]
        .bookmark;
    },
  },
  computed: {
    categorySortedList() {
      return testCase.filter(article => {
        if (this.category === 'ALL') return true;
        if (article.category === this.category) return true;
        return false;
      });
    },
  },
};
</script>

<style scoped>
/* ul {
  list-style-type: none;
  padding-left: 0px;
} */

/* .eventCard:hover {
  background-color: #598FFC;
  color: white;
} */
.q-select >>> .q-field--auto-height {
  min-height: 40px;
}
.q-select >>> .q-field__native {
  min-height: 40px;
  height: 40px;
}
.q-select >>> .q-field__append {
  min-height: 40px;
  height: 40px;
}
.q-select >>> .q-field__marginal {
  min-height: 40px;
}
.q-select >>> .q-field__control {
  min-height: 40px;
}
.q-select >>> .q-field__control-container {
  height: inherit;
}
.q-intersection > div {
  width: 100%;
}
</style>
