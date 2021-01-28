<template>
  <div class="col-12 row" style="margin-bottom: 50px;">
    <!-- 소제목 타이틀 -->
    <div class="text-h6 text-weight-bold col-12">Events for You</div>

    <div class=" row justify-end q-mb-sm q-gutter-lg col-12">
      <!-- 태그 필터링 -->
      <q-btn outline color="primary" @click="$store.commit('toggleTagFilter')"
        >태그 선택</q-btn
      >
      <!-- 이벤트 카테고리 -->
      <q-btn-dropdown outline color="black" label="Category">
        <q-list>
          <q-item clickable v-close-popup @click="onItemClick">
            <q-item-section>
              <q-item-label>ALL</q-item-label>
            </q-item-section>
          </q-item>
          <q-item clickable v-close-popup @click="onItemClick">
            <q-item-section>
              <q-item-label>Conference</q-item-label>
            </q-item-section>
          </q-item>

          <q-item clickable v-close-popup @click="onItemClick">
            <q-item-section>
              <q-item-label>Workshop</q-item-label>
            </q-item-section>
          </q-item>

          <q-item clickable v-close-popup @click="onItemClick">
            <q-item-section>
              <q-item-label>Hackathon</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown>
    </div>
    <div class="row col-12">
      <div class="col-12 row">
        <q-intersection
          transition="scale"
          class="row"
        >
          <q-tabs
            inline-label
            class="bg-white text-black"
            indicator-color="white"
          >
            <div
              v-for="(event, index) in events"
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
                      {{ event.eventTitle }}
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
                      v-for="(tag, index) in event.eventTags"
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
                      {{ event.eventDate }}
                    </div>
                    <div>
                      <img
                        :src="event.eventHostImg"
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
export default {
  data() {
    return {
      events: [
        {
          eventCategory: 'conference',
          eventTitle: 'Vue.js Conference',
          eventTags: ['Vue.js', 'Conference'],
          eventDate: '2021.03.15',
          eventHostImg:
            'https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F99E375455D5E2D6A1960E9',
          bookmark: false,
        },
        {
          eventCategory: 'workshop',
          eventTitle: 'JavaScript Workshop',
          eventTags: ['JavaScript', 'Workshop'],
          eventDate: '2021.03.20',
          eventHostImg:
            'https://img.etoday.co.kr/pto_db/2019/10/600/20191008190706_1374482_584_432.jpg',
          bookmark: false,
        },
        {
          eventCategory: 'hackathon',
          eventTitle: 'Bigdata hackathon',
          eventTags: ['Bigdata', 'hackathon'],
          eventDate: '2021.04.20',
          eventHostImg: 'https://cdn.quasar.dev/img/mountains.jpg',
          bookmark: false,
        },
        {
          eventCategory: 'hackathon',
          eventTitle: 'Bigdata hackathon',
          eventTags: ['Bigdata', 'hackathon'],
          eventDate: '2021.04.20',
          eventHostImg: 'https://cdn.quasar.dev/img/mountains.jpg',
          bookmark: false,
        },
      ],
    };
  },
  methods: {
    checkBookMark: function(index) {
      this.events[index].bookmark = !this.events[index].bookmark;
    },
    onItemClick: function() {},
  },
};
</script>

<style scoped></style>
