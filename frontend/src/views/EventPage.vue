<template>
  <div class="q-pa-lg q-mt-sm row justify-center">
    <div class="q-pa-sm" style="width: 60vw; ">
      <!-- 타이틀 -->
      <!-- <div style="margin-bottom: 20px;">
        <span class="text-h4 text-weight-bolder">Events </span>
        <p class="text-subtitle2" style="margin-top: 10px;">이벤트 정보를 확인할 수 있는 페이지입니다 :)</p>
      </div> -->
      <main-event></main-event>
      <recommend-events></recommend-events>
      <upcoming-events></upcoming-events>
      <!-- 이벤트 등록 신청 버튼 -->
      <div class="q-mb-md q-mt-md float-right" style="margin-bottom: 30px;">
        <q-btn
          color="blue-12"
          class="text-weight-bold q-px-md q-py-sm"
          label="이벤트 등록 신청"
          size="md"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MainEvent from '@/components/eventBoard/MainEvent';
import RecommendEvents from '@/components/eventBoard/RecommendEvents';
import UpcomingEvents from '@/components/eventBoard/UpcomingEvents';

export default {
  components: {
    MainEvent,
    RecommendEvents,
    UpcomingEvents,
  },
  created() {
    // 왼쪽 사이드 바 열림
    this.$store.commit('onLeft');
  },
};
</script>

<style scoped></style>
