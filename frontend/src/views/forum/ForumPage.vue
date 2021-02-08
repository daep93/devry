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
        <template slot="entities" slot-scope="scopeProps">
          <div
            class="row col-4 q-pa-sm"
            v-for="(post, index) in scopeProps.entities"
            :key="index"
          >
            <forum-entity :entity="post"></forum-entity>
          </div>
        </template>
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
