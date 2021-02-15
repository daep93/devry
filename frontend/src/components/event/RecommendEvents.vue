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
        :options="['ALL', 'Conference', 'Workshop', 'Hackathon', 'Competition', 'Meeting']"
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
              v-for="event in categorySortedList"
              :key="event.eventId"
              class="col-4 q-pa-xs"
            >
              <recommend-entity 
                :entity="event"
              ></recommend-entity>
            </div>
          </q-tabs>
        </q-intersection>
      </div>
    </div>
  </div>
</template>

<script>
// import { testCase } from '@/dummy/Events.js';
import RecommendEntity from '@/components/event/RecommendEntity.vue';
import { getEventList } from '@/api/board';

export default {
  components: {
    RecommendEntity,
  },
  data() {
    return {
      category: 'ALL',
      recommend_events: [],
      origin_event: [],
    };
  },
  async created() {
    // myTags로부터 selectedTags를 받아옴
    this.$store.commit('initSelectedTags');
    // QnA 게시판의 정보를 서버로부터 받아옴
    this.loadBoard();
  },
  watch: {
    selectedTags(newValue) {
      // store의 selectedTags가 바뀌면 새로운 게시판의 정보를 서버로부터 받아옴
      this.recommend_events = this.origin_event.filter(post => {
        for (const tag of post.ref_tags) {
          if (newValue.indexOf(tag) >= 0) return true;
        }
        return false;
      });
    },
  },
  methods: {
    // checkBookMark: function(index) {
    //   this.categorySortedList[index].bookmark = !this.categorySortedList[index]
    //     .bookmark;
    // },
    async loadBoard() {
      try {
        this.$q.loading.show();
        // 가져올 데이터 목록
        const { data } = await getEventList();
        this.origin_event = data;
        // this.recommend_events = data;
        this.recommend_events = this.origin_event.filter(post => {
          for (const tag of post.ref_tags) {
            if (this.selectedTags.indexOf(tag) >= 0) {
              return true;
            }
          }
          return false;
        });
      } catch (error) {
      console.log(error);
      // alert('에러가 발생했습니다.)
      } finally {
        this.$q.loading.hide();
      }
    }
  },
  // created() {
  //   this.$store.commit('initSelectedTags');
  // },
  computed: {
    selectedTags() {
      return this.$store.getters.getSelectedTags;
    },
    // tagFilteredList() {
    //   return this.recommend_events.filter(article => {
    //     for (const tag of article.tags) {
    //       for (const selected of this.$store.getters.getSelectedTags) {
    //         if (tag.toLowerCase() === selected) return true;
    //       }
    //     }
    //     return false;
    //   });
    // },
    categorySortedList() {
      return this.recommend_events.filter(article => {
      // return this.tagFilteredList.filter(article => {
        if (this.category === 'ALL') return true;
        if (article.category === this.category) return true;
        return false;
      });
    },
  },
  // async created() {
  //   try {
  //     this.$q.loading.show();
  //     // myTags로 부터 태그 정보 가져오기
  //     this.$store.commit('initSelectedTags');
  //     // 가져올 데이터 목록
  //     const { data } = await getEventList();
  //     this.recommend_events = data;
  //     // this.origin_event = data;
  //     // this.recommend_events = this.origin_event.filter(post => {
  //     //   for (const tag of post.ref_tags) {
  //     //     if (this.selectedTags.indexOf(tag) >= 0) {
  //     //       return true;
  //     //     }
  //     //   }
  //     //   return false;
  //     // });
  //     return data;
  //   } catch (error) {
  //     console.log(error);
  //     // alert('에러가 발생했습니다.)
  //   } finally {
  //     this.$q.loading.hide();
  //   }
  // }
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
