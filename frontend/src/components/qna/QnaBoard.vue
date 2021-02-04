<template>
  <div class="row col-12">
    <div class="row justify-between  col-12">
      <q-tabs
        dens
        v-model="sort"
        style="color:#3B77AF"
        class="row justify-start"
      >
        <q-tab name="time" label="최신순" />
        <q-tab name="comment" label="댓글순" />
        <q-tab name="like" label="추천순" />
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
        v-for="quest in board"
        :key="quest.questId"
        :entity="quest"
      ></qna-entity>
    </div>
  </div>
</template>

<script>
import QnaEntity from '@/components/qna/QnaEntity.vue';
import { getQnaList } from '@/api/board';
export default {
  components: {
    QnaEntity,
  },
  data() {
    return {
      sort: 'time',
      search: '',
      board: [],
      origin_board: [],
    };
  },
  async created() {
    // myTags로부터 selectedTags를 받아옴
    this.$store.commit('initSelectedTags');
    // QnA 게시판의 정보를 서버로부터 받아옴
    this.loadBoard();
  },
  watch: {
    sort(newValue) {
      // sort를 감시해서 바뀌면 새로운 게시판의 정보를 서버로부터 받아옴
      // this.loadBoard();
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
      } else {
        this.board.sort((item1, item2) => item2.like_num - item1.like_num);
      }
    },
    selectedTags(newValue) {
      // store의 selectedTags가 바뀌면 새로운 게시판의 정보를 서버로부터 받아옴
      // this.loadBoard();
      console.log(newValue);
      this.board = this.origin_board.filter(post => {
        for (const tag of post.ref_tags) {
          if (newValue.indexOf(tag.toLowerCase()) >= 0) return true;
        }
        return false;
      });
    },
  },
  methods: {
    // 게시판의 정보를 서버로부터 받아옴
    async loadBoard() {
      try {
        this.$q.loading.show();
        // const { data } = await getQnaList({
        //   tags_filter: this.selectedTags,
        //   tab: this.sort,
        // });
        const { data } = await getQnaList();
        this.origin_board = data;
        this.board = data;
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
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
