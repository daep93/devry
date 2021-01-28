<template>
  <div class="row">
    <!-- 소제목 타이틀 -->
    <div class="row col-12 text-h6 text-weight-bold">Upcoming Events</div>
    <!-- 이벤트 카테고리 -->
    <div class="q-pr-md row col-12 justify-end q-mb-sm">
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
    <!-- 이벤트 목록 -->
    <div class="q-ma-xs row col-12">
      <div class="row justify-center col-12">
        <q-intersection
          v-for="(event, index) in events"
          :key="index"
          transition="scale"
          class="example-item col-4 q-pa-xs"
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
        </q-intersection>
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
          categoryCheck: true,
        },
        {
          eventCategory: 'workshop',
          eventTitle: 'JavaScript Workshop',
          eventTags: ['JavaScript', 'Workshop'],
          eventDate: '2021.03.20',
          eventHostImg:
            'https://img.etoday.co.kr/pto_db/2019/10/600/20191008190706_1374482_584_432.jpg',
          bookmark: false,
          categoryCheck: true,
        },
        {
          eventCategory: 'hackathon',
          eventTitle: 'Bigdata hackathon',
          eventTags: ['Bigdata', 'hackathon'],
          eventDate: '2021.04.20',
          eventHostImg: 'https://cdn.quasar.dev/img/mountains.jpg',
          bookmark: false,
          categoryCheck: true,
        },
        {
          eventCategory: 'conference',
          eventTitle: 'Vue.js Conference',
          eventTags: ['Vue.js', 'Conference'],
          eventDate: '2021.03.15',
          eventHostImg:
            'https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F99E375455D5E2D6A1960E9',
          bookmark: false,
          categoryCheck: true,
        },
        {
          eventCategory: 'workshop',
          eventTitle: 'JavaScript Workshop',
          eventTags: ['JavaScript', 'Workshop'],
          eventDate: '2021.03.20',
          eventHostImg:
            'https://img.etoday.co.kr/pto_db/2019/10/600/20191008190706_1374482_584_432.jpg',
          bookmark: false,
          categoryCheck: true,
        },
        {
          eventCategory: 'hackathon',
          eventTitle: 'Bigdata hackathon',
          eventTags: ['Bigdata', 'hackathon'],
          eventDate: '2021.04.20',
          eventHostImg: 'https://cdn.quasar.dev/img/mountains.jpg',
          bookmark: false,
          categoryCheck: true,
        },
      ],
      categories: ['ALL', 'conference', 'workshop', 'hackathon'],
    };
  },
  methods: {
    checkBookMark: function(index) {
      this.events[index].bookmark = !this.events[index].bookmark;
    },
    onItemClick: function(index) {
      for (const event of this.events) {
        if (index === event.eventCategory) {
          event.categoryCheck = true;
        } else {
          event.categoryCheck = false;
        }
      }
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
</style>
