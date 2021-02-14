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
          class="rounded-borders q-ml-xl col-6">
          <q-badge v-if="bookmarked === false" @click="checkbookmarked" class="q-ma-xs" float-left>
            <q-icon size="sm" name="turned_in_not" />
          </q-badge>
          <q-badge v-else @click="checkbookmarked" class="q-ma-xs" float-left>
            <q-icon size="sm" name="turned_in" />
          </q-badge>
        </q-img>    
        <!-- 이벤트 소개 -->
        <div class="col-4 q-ml-xl q-mb-lg">
          <div class="row q-my-md">
            <q-badge class="q-mr-sm" color="orange">
              {{ state }}
            </q-badge>
            <q-badge class="q-px-sm" color="purple">
              {{ category }}
            </q-badge>
          </div>
          <div class="text-h4 text-weight-bold q-mb-lg">{{ title }}</div>
          <div class="q-mb-md">
            <span class="text-h6 text-weight-bold q-mr-md">장소</span>
            <span class="text-h7">{{ place }}</span>
          </div>
          <div class="row q-mb-md">
            <div class="col-2 text-h6 text-weight-bold">일시</div>
            <div class="col q-ml-xs">
              <div class="text-h7 q-mb-sm">{{ start }} - {{ end }}</div>
              <div class="text-h7">{{ start }} - {{ end }}</div>
            </div>
          </div>
          <div class="q-mb-md">
            <span class="text-h6 text-weight-bold q-mr-md">주최</span>
            <span class="text-h7">{{ host_name }}</span>
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
          <p><q-icon size="xs" name="bookmarks" /> {{ bookmark_num }}건의 북마크 </p>
          <p><q-icon size="xs" name="calendar_today" /> 신청기간 : ~ {{ start }} 까지 </p>
        </div>
        <q-btn
          @click="register"
          color="blue-12"
          class="col-4 rounded-borders q-ml-xl"
          label="참가 신청"
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
              :src="profile_img"
              class="col-6 float-left q-mr-md rounded-borders"
              style="width: 70px; height: 50px;"
            >
            <div class="col-6 q-pt-sm text-h6 text-weight-bold">{{ host_name }}</div>
          </div>
        </div>
        <!-- 관련 태그 -->
        <div class="q-mb-xl q-ml-xl">
          <div class="text-h6 text-weight-bold q-mb-md">관련 태그</div>
          <ul class="row q-gutter-sm">
            <li
              v-for="(tag, index) in ref_tags"
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
        <!-- 수정하기 버튼 -->
        <div class="row q-mb-md q-mt-md float-right" style="margin-bottom: 150px;">
          <q-btn
            outline
            color="blue-12"
            class="text-weight-bold q-px-xl q-py-sm q-mr-md"
            label="수정하기"
            size="md"
            @click="updateEvent"
          />
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import { getEvent, toggleEventBookmark } from '@/api/event';
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
      place: 'Online',
      category: '컨퍼런스',
      start: '2021/02/11',
      end: '2021/02/13',
      cost: '무료',
      participation: '개발자 혹은 개발에 관심있는 누구나',
      introduction: '프론트엔드 개발을 위한 Vue.js 컨퍼런스입니다.',
      schedule: '1. 주최자 소개 | 2. 컨퍼런스 소개 | 3. 프론트엔드 프레임워크 소개',
      host_name: 'Eddie',
      profile_img: 'https://cdn.quasar.dev/img/parallax1.jpg',
      register_url: 'https://google.com',
      ref_tags: ['Vue.js', 'Python', 'JavaScript', 'React'],
      bookmarked: false,
      bookmark_num: 159,
    }
  },
  methods: {
    updateEvent() {
      const post_id = this.$route.params.id;
      // 이벤트 등록 수정하기 페이지로 이동
      this.$router.push({ path: `/event-registration/${post_id}` });
      // this.$router.push({ path: '/event-registration/:id' });
    },
    // 북마크 토글하기
    async checkbookmarked() {
      if (!this.$store.getters.isLogined) {
        alert('로그인이 필요합니다');
        return
      }
      const post_id = this.$route.params.id;
      try {
        const { data } = await toggleEventBookmark(post_id); 
        // 넘겨줄 데이터
        this.bookmarked = !this.bookmarked
        if(this.bookmarked) {
          this.bookmark_num = this.bookmark_num + 1
        }else {
          this.bookmark_num = this.bookmark_num - 1
        }
      } catch (error) {
        console.log(error);
      }
    },
    register() {
      window.open(this.register_url, "_blank");  
    },
    tagColor(tag) {
      return colorSoloMapper(tag, 0.5);
    },
  },
  async created() {
    this.$store.commit('offLeft');
    // id 가져오기
    try {
      const post_id = this.$route.params.id;
      this.$q.loading.show();
      const { data } = await getEvent(post_id);
      // 가져올 데이터 목록
      this.state = data.state;
      this.thumnail = data.thumnail;
      this.title = data.title;
      this.place = data.place;
      this.category = data.category;
      this.start = data.start;
      this.end = data.end;
      this.cost = data.cost;
      this.participation = data.participation;
      this.introduction = data.introduction;
      this.schedule = data.schedule;
      this.host_name = data.host_name;
      this.profile_img = data.profile_img;
      this.register_url = data.register_url;
      this.ref_tags = data.ref_tags;
      this.bookmarked = data.bookmarked;
      this.bookmark_num = data.bookmark_num;
    } catch (error) {
      console.log(error);
      // alert('에러가 발생했습니다.)
    } finally {
      this.$q.loading.hide();
    }
  },
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>