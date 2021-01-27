<template>
<div>
  <!-- 소제목 타이틀 -->
  <div class="text-h6 text-weight-bold">Upcoming Events</div>
  <!-- 이벤트 카테고리 -->
  <div class="q-pa-md float-right">
    <q-btn-dropdown color="black" label="Category" style="width: 100px; height: 30px; font-size: 10px;">
      <q-list v-for="(category, index) in categories" :key="index">
        <q-item clickable v-close-popup @click="onItemClick(category, index)">
          <q-item-section>
            <q-item-label>{{ category }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </div>
  <!-- 이벤트 목록 -->
  <div class="q-ma-sm" style="clear: both;">
    <div class="row justify-center q-gutter-sm">
      <q-intersection
        v-for="(event, index) in events"
        :key="index"
        once
        transition="scale"
        class="example-item"
      >
        <q-card v-if="event.categoryCheck" class="q-ma-sm" style="border-radius: 20px;">
          <q-card-section class="eventCard">
            <div class="q-pa-sm" style="height: 175px;">
              <div class="d-flex">
                <span class="text-weight-bold" style="font-size: 15px; margin-top: 20px; width: 100px; text-overflow: ellipsis; ">{{ event.eventTitle }}</span>
                <!-- <q-btn class="float-right" flat round color="primary" icon="bookmark" style="margin-left: 27px;" /> -->
                <q-btn v-if="event.bookmark" @click="checkBookMark(index)" class="float-right" flat round color="primary" icon="bookmark" style="margin-left: 27px;"/>
                <q-btn v-else @click="checkBookMark(index)" class="float-right" flat round color="primary" icon="bookmark_border" style="margin-left: 27px;"/>
              </div>
              <ul class="row" style="margin-top:0px;">
                <li v-for="(tag, index) in event.eventTags" :key="index">
                  <div class="text-caption float-left" style="margin: 0px 5px 60px 0px;">#{{ tag }}</div>
                </li>
              </ul>
              <div>
                <span class="text-subtitle2 text-weight-bold" style="color: #598FFC;">{{ event.eventDate }}</span>
                <span>
                  <img
                    :src="event.eventHostImg"
                    style="width: 50px; height: 40px; margin-left: 100px; border-radius: 10px;"
                  >
                </span>
              </div>
            </div>
          </q-card-section>
        </q-card>
        <q-card v-else style="display: none;">
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
          eventHostImg: 'https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F99E375455D5E2D6A1960E9',
          bookmark: false,
          categoryCheck: true,
        },
        { 
          eventCategory: 'workshop', 
          eventTitle: 'JavaScript Workshop', 
          eventTags: ['JavaScript', 'Workshop'], 
          eventDate: '2021.03.20', 
          eventHostImg: 'https://img.etoday.co.kr/pto_db/2019/10/600/20191008190706_1374482_584_432.jpg',
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
          eventHostImg: 'https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F99E375455D5E2D6A1960E9',
          bookmark: false,
          categoryCheck: true,
        },
        { 
          eventCategory: 'workshop', 
          eventTitle: 'JavaScript Workshop', 
          eventTags: ['JavaScript', 'Workshop'], 
          eventDate: '2021.03.20', 
          eventHostImg: 'https://img.etoday.co.kr/pto_db/2019/10/600/20191008190706_1374482_584_432.jpg',
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
        }
      ],
      categories : ['ALL', 'conference', 'workshop', 'hackathon']
    }
  },
  methods: {
    checkBookMark: function(index) {
      this.events[index].bookmark = !this.events[index].bookmark
    },
    onItemClick: function(index) {
      for (const event of this.events) {
        if(index === event.eventCategory) {
          event.categoryCheck = true
        }
        else{
          event.categoryCheck = false
        }
      }
    }
  }
}
</script>

<style scoped>
.example-item {
  height: 290px;
  width: 290px;
}

ul {
  list-style-type: none;
  padding-left: 0px;
}

.eventCard:hover {
  background-color: #598FFC;
  color: white;
}
</style>