<template>
  <div class="col-12" style="margin-bottom: 50px;">
    <!-- 소제목 타이틀 -->
    <div class="text-h6 text-weight-bold">Events for You</div>
    <!-- 이벤트 카테고리 -->
    <div class="q-pa-md float-right q-gutter-lg">
      <q-btn outline color="primary" @click="$store.commit('toggleTagFilter')"
        >태그 선택</q-btn
      >
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
    <div class="q-pa-md" style="clear: both;">
      <div class="q-gutter-y-md" style="max-width: 1500px">
        <q-tabs inline-label class="bg-white text-black">
          <q-tab>
            <q-intersection
              v-for="(event, index) in events"
              :key="index"
              once
              transition="scale"
            >
              <q-card class="q-ma-sm" style="border-radius: 20px;">
                <q-card-section>
                  <div
                    class="q-pa-sm d-flex"
                    style="height: 180px; justify-content: space-between;"
                  >
                    <span
                      class="text-weight-bold"
                      style="font-size: 15px; margin-top: 20px;"
                      >{{ event.eventTitle }}</span
                    >
                    <q-btn
                      v-if="event.bookmark"
                      @click="checkBookMark(index)"
                      flat
                      round
                      color="primary"
                      icon="bookmark"
                      style="margin-left: 40px;"
                    />
                    <q-btn
                      v-else
                      @click="checkBookMark(index)"
                      flat
                      round
                      color="primary"
                      icon="bookmark_border"
                      style="margin-left: 40px;"
                    />
                    <ul class="row" style="margin-top:0px;">
                      <li v-for="(tag, index) in event.eventTags" :key="index">
                        <div
                          class="text-caption float-left"
                          style="margin: 0px 5px 40px 0px;"
                        >
                          #{{ tag }}
                        </div>
                      </li>
                    </ul>
                    <div
                      class="d-flex"
                      style="clear: both; justify-content: space-between"
                    >
                      <span
                        class="text-subtitle2 text-weight-bold text-primary"
                        >{{ event.eventDate }}</span
                      >
                      <span>
                        <img
                          :src="event.eventHostImg"
                          style="width: 50px; height: 40px; margin-left: 130px; border-radius: 10px;"
                        />
                      </span>
                    </div>
                  </div>
                </q-card-section>
              </q-card>
            </q-intersection>
          </q-tab>
        </q-tabs>
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

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>
