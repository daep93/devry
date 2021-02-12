<template>
  <div class="row q-pa-md justify-center q-mt-md">
    <div class="col-7">
      <!-- 이벤트 메인 -->
      <div class="row full-width">
        <!-- 이벤트 썸네일 이미지 -->
        <q-img
            :src="thumnail"
            spinner-color="white"
            style="max-width: 450px; height:330px;"
            class="rounded-borders q-ml-xl col-6"
          />
        <!-- 이벤트 소개 -->
        <div class="col-4 q-ml-xl q-mb-lg">
          <div class="text-caption text-primary q-my-md">{{ state }}</div>
          <div class="text-h4 text-weight-bold q-mb-lg">{{ title }}</div>
          <div class="q-mb-md">
            <span class="text-h6 text-weight-bold q-mr-md">장소</span>
            <span class="text-h7">{{ location }}</span>
          </div>
          <div class="row q-mb-md">
            <div class="col-2 text-h6 text-weight-bold">일시</div>
            <div class="col q-ml-xs">
              <div class="text-h7 q-mb-sm">{{ sdata }} ~ {{ edata }}</div>
              <div class="text-h7">{{ stime }} ~ {{ etime }}</div>
            </div>
          </div>
          <div class="q-mb-md">
            <span class="text-h6 text-weight-bold q-mr-md">주최</span>
            <span class="text-h7">{{ hostInfo.host_name }}</span>
          </div>
          <div class="q-mb-md">
            <span class="text-h6 text-weight-bold q-mr-md">비용</span>
            <span class="text-h7">{{ cost }}</span>
          </div>
        </div>
      </div>
      <hr>
      <!-- 이벤트 신청 -->
      <div class="row full-width q-pt-md q-my-lg q-ml-xl">
        <div class="col-6 q-ml-xl">
          <!-- <p><q-icon size="xs" name="group" /> {{ applicant }}명 신청중</p> -->
          <p><q-icon size="xs" name="calendar_today" /> 신청기간 : {{ period }}</p>
        </div>
        <q-btn
          v-if="registerState === false"
          @click="register"
          color="blue-12"
          class="col-4 rounded-borders q-ml-xl"
          label="참가 신청"
          style="max-width:300px; height:50px;"
        />
        <q-btn
          v-else
          @click="register"
          color="grey-7"
          class="col-4 rounded-borders q-ml-xl"
          label="신청 취소"
          style="max-width:300px; height:50px;"
        />
      </div>
      <hr>
      <!-- 이벤트 상세 정보 -->
      <div class="full-width q-mt-lg q-ml-xl">
        <!-- 참가대상 -->
        <div class="q-mt-md q-ml-xl">
          <div class="text-h6 text-weight-bold q-mb-md">Event 참가대상</div>
          <div>{{ participation }}</div>
        </div>
          <!-- 소개 -->
        <div class="q-mt-lg q-ml-xl">
          <div class="text-h6 text-weight-bold q-mb-md">Event 소개</div>
          <div>{{ introduction }}</div>
        </div>
          <!-- 스케쥴 -->
          <div class="q-mt-lg q-ml-xl">
          <div class="text-h6 text-weight-bold q-mb-md">Event 스케쥴</div>
          <div>{{ schedule }}</div>
          </div>
          <!-- 주최자 정보 -->
        <div class="q-my-lg q-ml-xl">
          <div class="text-h6 text-weight-bold q-mb-md">주최자 정보</div>
          <div class="row">
            <img
              :src="hostInfo.hostImg"
              class="col-6 float-left q-mr-md rounded-borders"
              style="width: 70px; height: 50px;"
            >
            <div class="col-6 q-pt-sm text-h6 text-weight-bold">{{ hostInfo.hostName }}</div>
          </div>
        </div>
        <!-- 관련 태그 -->
        <div class="q-mb-xl q-ml-xl">
          <div class="text-h6 text-weight-bold q-mb-md">관련 태그</div>
          <ul class="row q-gutter-sm">
            <li
              v-for="(tag, index) in tags"
              :key="index"
              class="cursor-pointer"
            >
              <q-badge
                class="text-black q-pa-sm q-mr-sm shadow-3"
                :style="{
                  'background-color': tagColor(tag),
                }"
              >
                # {{ tag }}
              </q-badge>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import {
  colorSoloMapper,
  // matchingColorSoloMapper,
} from '@/utils/tagColorMapper';

export default {
  data() {
    return {
      state: 'ready',
      thumnail: 'https://placeimg.com/500/300/nature',
      title: 'Vue.js 컨퍼런스',
      location: 'Online',
      catetory: '',
      sdata: '2021-02-11',
      edata: '2021-02-13',
      stime: '18:00',
      etime: '19:30',
      cost: '무료',
      participation: '개발자 혹은 개발에 관심있는 누구나',
      introduction: '프론트엔드 개발을 위한 Vue.js 컨퍼런스입니다.',
      schedule: '1. 주최자 소개 | 2. 컨퍼런스 소개 | 3. 프론트엔드 프레임워크 소개',
      hostInfo: {
        host_name: 'Eddie',
        profile_img: 'https://cdn.quasar.dev/img/parallax1.jpg',
      },
      ref_tags: ['Vue.js', 'Python', 'JavaScript', 'React'],
      registerState : false
    }
  },
  methods: {
    register: function() {
      this.registerState = !this.registerState
      // if(this.registerState) {
      //   this.applicant = this.applicant + 1
      // }else {
      //   this.applicant = this.applicant - 1
      // }
    },
    tagColor(tag) {
      return colorSoloMapper(tag, 0.5);
    },
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>