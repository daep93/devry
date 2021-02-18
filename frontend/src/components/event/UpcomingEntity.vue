<template>
  <div>
    <q-card style="border-radius: 20px;">
      <q-card-section class="q-px-md q-pt-lg q-pb-none">
        <div class="q-pa-xs row justify-between">
          <div
            class="text-weight-bold text-weight-bold col-10 cursor-pointer"
            style="font-size:1.1em"
            @click="goToDetail"
          >
            {{ entity.title }}
          </div>
          <div class="col-2 row justify-end">
            <q-icon
              class="col cursor-pointer"
              :name="entity.bookmarked ? 'bookmark' : 'bookmark_border'"
              size="sm"
              :color="entity.bookmarked ? 'blue-12' : 'grey-6'"
              @click="checkbookmarked"
            ></q-icon>
            <span class="col q-pl-xs text-grey-8" style="font-size:1.2em;">
              {{ entity.bookmark_num }}
            </span>
          </div>
        </div>
      </q-card-section>
      <q-card-section class="q-px-lg q-pt-sm q-pb-xs">
        <ul class="row q-gutter-sm">
          <li
            v-for="(tag, index) in entity.ref_tags"
            :key="index"
            class="cursor-pointer"
          >
            <q-badge
              class="text-black q-py-xs q-mr-xs shadow-3"
              :style="{
                'background-color': tagColor(tag),
              }"
            >
              # {{ tag }}
            </q-badge>
          </li>
        </ul>
      </q-card-section>
      <q-card-section class="q-px-lg q-pt-sm q-pb-lg">
        <div class="row justify-between items-end">
          <div class="text-subtitle2 text-weight-bold text-primary">
            {{ entity.start | moment('YYYY/MM/DD') }}
          </div>
          <div>
            <img
              :src="
                entity.profile_img
                  ? profile_img
                  : require('@/assets/basic_image.png')
              "
              style="width: 50px; height: 40px;  border-radius: 10px;"
            />
          </div>
        </div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import { toggleEventBookmark } from '@/api/event';
// import { getEventList } from '@/api/board';
import {
  colorSoloMapper,
  // matchingColorSoloMapper,
} from '@/utils/tagColorMapper';

export default {
  props: {
    entity: Object,
  },
  data() {
    return {
      // profile_img: `${process.env.VUE_APP_SERVER_API_URL}${this.entity.profile_img}`,
      profile_img: this.entity.profile_img
    };
  },
  methods: {
    tagColor(tag) {
      return colorSoloMapper(tag, 0.5);
    },
    goToDetail() {
      this.$router.push(`/event-detail/${this.entity.id}`);
    },
    // 북마크 토글하기
    async checkbookmarked() {
      // 로그인 확인
      if (!this.$store.getters.isLogined) {
        alert('로그인이 필요합니다');
        return;
      }
      try {
        await toggleEventBookmark(this.entity.id);
        // 넘겨줄 데이터
        this.entity.bookmarked = !this.entity.bookmarked;
        if (this.entity.bookmarked) {
          this.entity.bookmark_num = this.entity.bookmark_num + 1;
        } else {
          this.entity.bookmark_num = this.entity.bookmark_num - 1;
        }
        // getEventList()
        window.location.reload();
      } catch (error) {
        console.log(error);
      }
    },
  },
  // computed: {
  //   bookmark_data() {
  //     console.log('변화가 있나?')
  //   }
  // }
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>
