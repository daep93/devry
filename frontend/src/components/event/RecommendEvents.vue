<template>
  <div class="row q-mb-xl">
    <!-- 소제목 타이틀 -->
    <div class="row col-12 text-h6 text-weight-bold ">Events for You</div>

    <div class=" row q-mb-sm justify-end col-12">
      <!-- 태그 필터링 -->
      <q-btn
        outline
        color="primary"
        @click="$store.commit('toggleTagFilter')"
        class="q-mr-sm"
        style="height:40px"
        >태그 선택</q-btn
      >
      <!-- 이벤트 카테고리 -->
      <q-select
        outlined
        v-model="category"
        :options="['ALL', 'conference', 'workshop', 'hackathon']"
        style="width:140px;"
      />
    </div>
    <div class="row col-12 " style="height:30vh">
      <div class="col-12 row">
        <q-intersection transition="scale" class="col-12">
          <q-tabs
            inline-label
            class="bg-white text-black col-12"
            indicator-color="white"
          >
            <div
              v-for="(event, index) in categorySortedList"
              :key="index"
              class="col-4 q-pa-xs"
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
            </div>
          </q-tabs>
        </q-intersection>
        <!-- <q-intersection
          v-for="(event, index) in events"
          :key="index"
          once
          transition="scale"
          class=" row"
        >
         
        </q-intersection> -->
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
  created() {
    this.$store.commit('initSelectedTags');
  },
  computed: {
    tagFilteredList() {
      return testCase.filter(article => {
        for (const tag of article.tags) {
          for (const selected of this.$store.getters.getSelectedTags) {
            if (tag.toLowerCase() === selected) return true;
          }
        }
        return false;
      });
    },
    categorySortedList() {
      // return testCase.filter(article => {
      return this.tagFilteredList.filter(article => {
        if (this.category === 'ALL') return true;
        if (article.category === this.category) return true;
        return false;
      });
    },
  },
};
</script>

<style scoped>
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
