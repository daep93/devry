<template>
  <div class="row col-12">
    <div class="row justify-between  col-12">
      <!-- tab -->
      <q-tabs
        dens
        v-model="sort"
        style="color:#3B77AF"
        class="row justify-start"
      >
        <slot name="tab"></slot>
      </q-tabs>
      <!-- 검색창 및 태그 필터 선택 -->
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
    <!-- 게시물 목록 -->
    <div class="row q-mt-md col-12">
      <div
        class="row col-4 q-pa-sm"
        v-for="(post, index) in board"
        :key="index"
      >
        <slot name="entity" :entity="post"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    origin_board: Array,
  },
  data() {
    return {
      sort: 'time',
      search: '',
      board: this.origin_board,
    };
  },
  watch: {
    sort(newValue) {
      // sort값이 바뀌면 board의 정렬 순서를 바꾼다.
      if (newValue === 'time') {
        this.board.sort((item1, item2) => {
          return (
            this.$moment(item2.written_time) - this.$moment(item1.written_time)
          );
        });
      } else if (newValue === 'comment') {
        this.board.sort(
          (item1, item2) => item2.comment_num - item1.comment_num,
        );
      } else if (newValue === 'like') {
        this.board.sort((item1, item2) => item2.like_num - item1.like_num);
      } else if (newValue === 'feed') {
        //
      }
    },
    selectedTags(newValue) {
      // store의 selectedTags가 바뀌면 새롭게 개시될 게시물들을 필터링한다.
      this.board = this.origin_board.filter(post => {
        for (const tag of post.ref_tags) {
          if (newValue.indexOf(tag) >= 0) return true;
        }
        return false;
      });
    },
  },
  computed: {
    // watch로 감시하기 위해서 store의 데이터를 selectedTags에 담음.
    selectedTags() {
      return this.$store.getters.getSelectedTags;
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
