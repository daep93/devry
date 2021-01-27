<template>
  <div class="q-pa-md">
    <div class="justify-center" style="width: 70%; padding: 50px; margin:0 auto;">
      <!-- 타이틀 -->
      <div style="margin-bottom: 20px;">
        <span class="text-h4 text-weight-bolder">Events </span>
        <p class="text-subtitle2" style="margin-top: 10px;">이벤트 정보를 확인할 수 있는 페이지입니다 :)</p>
      </div>
      <!-- 이벤트 등록 신청 버튼 -->
      <div class="q-mb-md q-mt-md float-right" style="margin-bottom: 30px;">
        <q-btn
          color="blue-12"
          class="text-weight-bold"
          label="이벤트 등록 신청"
          style="width:200px; height:50px; border-radius:5px;"
        />
      </div>
      <main-event></main-event>
      <event-tags></event-tags>
      <recommend-events></recommend-events>
      <upcoming-events></upcoming-events>
    </div>
  </div>
</template>

<script>
import MainEvent from '@/components/eventBoard/MainEvent';
import EventTags from '@/components/eventBoard/EventTags';
import RecommendEvents from '@/components/eventBoard/RecommendEvents';
import UpcomingEvents from '@/components/eventBoard/UpcomingEvents';

export default {
  components: { 
    MainEvent, 
    EventTags, 
    RecommendEvents, 
    UpcomingEvents 
  },
};
</script>

<style scoped>
</style>
