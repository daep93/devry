<template>
  <div style="clear: both; " class="q-mb-xl">
    <div>
      <div v-for="(event, index) in main_events" :key="index">
        <div>
          {{ event.id }}
        </div>
      </div>
    </div>
    <q-carousel
      animated
      v-model="slide"
      navigation
      infinite
      :autoplay="autoplay"
      arrows
      transition-prev="slide-right"
      transition-next="slide-left"
      @mouseenter="autoplay = false"
      @mouseleave="autoplay = true"
      height="270px"
    >
      <!-- v-for="event in main_events"
      :key="event.eventId" -->
      <!-- <main-entity :entity="event"></main-entity> -->
      <q-carousel-slide
        :name="1"
        style="background-color: #1E1B39; border-radius: 10px;"
        class="overflow-hidden"
        @click="moveToDetailPage"
      >
        <div class="row justify-center overflow-hidden">
          <img
            src="@/assets/game.png"
            alt="game webinar"
            style="height:230px; width:70%;"
          />
        </div>
      </q-carousel-slide>
      <q-carousel-slide
        :name="2"
        style="background-color: #213186; border-radius: 10px;"
        class="overflow-hidden"
        @click="moveToDetailPage"
      >
        <div class="row justify-center overflow-hidden">
          <img
            src="@/assets/hackathon.png"
            alt="AI hackathon"
            style="height:250px;width:40%"
          />
        </div>
      </q-carousel-slide>
      <q-carousel-slide
        :name="3"
        style="background-color: black; border-radius: 10px;"
        class="overflow-hidden"
        @click="moveToDetailPage"
      >
        <div class="row justify-center overflow-hidden">
          <img
            src="@/assets/ifkakao.jpg"
            alt="if kakao"
            style="height:250px;width:70%"
          />
        </div>
      </q-carousel-slide>
      <q-carousel-slide
        :name="4"
        style="background-color: #1A174F; border-radius: 10px;"
        class="overflow-hidden"
        @click="moveToDetailPage"
      >
        <div class="row justify-center overflow-hidden">
          <img
            src="@/assets/tensorFlow.jpg"
            alt="tensorflow"
            style="height:240px; width:100%;"
          />
        </div>
      </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script>
// import MainEntity from '@/components/event/MainEntity.vue';
import { getMainEventList } from '@/api/board';

export default {
  // components: {
  //   MainEntity,
  // },
  data() {
    return {
      autoplay: true,
      slide: 1,
      main_events: [],
    };
  },
  methods: {
    moveToDetailPage: function() {
      const post_id = this.$route.params.id;
      this.$router.push({ path: `/event-detail/${this.name}` });
    },
  },
  async created() {
    try {
      this.$q.loading.show();
      // 가져올 데이터 목록
      const { data } = await getMainEventList();
      this.main_events = data;
      return data;
    } catch (error) {
      console.log(error);
      // alert('에러가 발생했습니다.)
    } finally {
      this.$q.loading.hide();
    }
  }
};
</script>

<style></style>
