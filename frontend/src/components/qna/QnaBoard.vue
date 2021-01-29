<template>
  <div class="row col-12">
    <div class="row justify-between  col-12">
      <q-tabs
        dens
        v-model="sort"
        style="color:#3B77AF"
        class="row justify-start"
      >
        <q-tab name="latest" label="최신순" />
        <q-tab name="orderByComment" label="댓글순" />
        <q-tab name="orderByLike" label="추천순" />
      </q-tabs>
      <div class="row justify-end q-gutter-lg">
        <q-input v-model="search" type="search" class="q-mb-sm" outlined>
          <template v-slot:append>
            <q-icon :name="$i.ionSearchOutline" />
          </template>
        </q-input>
        <q-btn
          class="tag-filter"
          outline
          color="primary"
          @click="$store.commit('toggleTagFilter')"
          >태그 선택</q-btn
        >
      </div>
    </div>
    <div class="row q-mt-md col-12">
      <qna-entity
        v-for="quest in refinedQuest"
        :key="quest.questId"
        :entity="quest"
      ></qna-entity>
    </div>
  </div>
</template>

<script>
import QnaEntity from '@/components/qna/QnaEntity.vue';
import { testCase } from '@/dummy/Questions.js';
export default {
  components: {
    QnaEntity,
  },
  data() {
    return {
      sort: 'latest',
      search: '',
    };
  },
  created() {
    this.$store.commit('initSelectedTags');
  },
  computed: {
    refinedQuest() {
      if (this.sort === 'latest') return this.timeSortedList;
      else if (this.sort == 'orderByComment') return this.commentSortedList;
      else return this.likeSortedList;
    },
    tagFilteredList() {
      return testCase.filter(article => {
        for (const tag of article.refTags) {
          for (const selected of this.$store.getters.getSelectedTags) {
            if (tag === selected) return true;
          }
        }
        return false;
      });
    },
    timeSortedList() {
      const list = this.tagFilteredList.slice();
      return list.sort(
        (a, b) =>
          this.$moment(b.userInfo.writtenTime) -
          this.$moment(a.userInfo.writtenTime),
      );
    },
    commentSortedList() {
      const list = this.tagFilteredList.slice();
      return list.sort(
        (a, b) => this.$moment(b.commentNum) - this.$moment(a.commentNum),
      );
    },
    likeSortedList() {
      const list = this.tagFilteredList.slice();
      return list.sort(
        (a, b) => this.$moment(b.likeNum) - this.$moment(a.likeNum),
      );
    },
  },
};
</script>

<style scoped>
.q-input >>> .q-field__control {
  height: 40px;
}
.q-input >>> .q-field__append {
  height: 40px;
}
.tag-filter {
  height: 40px;
}
</style>
