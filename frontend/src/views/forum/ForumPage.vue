<template>
  <div class="row justify-center q-pt-lg ">
    <div class="row col-8 justify-center q-pl-lg">
      <div class="row q-mb-sm col-12 text-h5 text-weight-bold">
        Forum 게시판
      </div>
      <!-- <forum-board></forum-board> -->
      <bulletin-board :origin_board="board">
        <template slot="tab">
          <q-tab name="feed" label="피드" />
          <q-tab name="time" label="최신글" />
        </template>
        <forum-entity
          slot="entity"
          slot-scope="scopeProps"
          :entity="scopeProps.entity"
        ></forum-entity>
      </bulletin-board>
    </div>
  </div>
</template>

<script>
// import ForumBoard from '@/components/forum/ForumBoard';
import BulletinBoard from '@/components/common/BulletinBoard';
import ForumEntity from '@/components/forum/ForumEntity';
import { testCase } from '@/dummy/Forum';
export default {
  components: {
    // ForumBoard,
    BulletinBoard,
    ForumEntity,
  },
  data() {
    return {
      board: [],
    };
  },
  methods: {
    // 게시판의 정보를 서버로부터 받아옴
    async loadBoard() {
      try {
        this.$q.loading.show();
        // const { data } = await getQnaList();
        // this.origin_board = data;
        this.board = testCase;
        this.board = this.board.filter(post => {
          for (const tag of post.ref_tags) {
            if (this.selectedTags.indexOf(tag) >= 0) {
              return true;
            }
          }
          return false;
        });
        this.board.sort((item1, item2) => {
          return (
            this.$moment(item2.written_time) - this.$moment(item1.written_time)
          );
        });
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  async created() {
    // myTags로부터 selectedTags를 받아옴
    this.$store.commit('initSelectedTags');
    // QnA 게시판의 정보를 서버로부터 받아옴
    this.loadBoard();
  },
};
</script>

<style scoped></style>
