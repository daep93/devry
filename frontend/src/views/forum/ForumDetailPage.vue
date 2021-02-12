<template>
  <div class="row col-12">
    <div class="row col-12">
      <div class="row col-2 q-mt-lg">
        <div class="row col-9"></div>
        <div class="row col-3">
          <forum-detail-status></forum-detail-status>
        </div>
      </div>
      <div class="row col-10 q-mt-lg">
        <div class="col-9">
          <div class="row col-12">
            <forum-detail-content></forum-detail-content>
          </div>
        </div>
        <div class="col-3 q-pl-sm q-pr-xl">
          <forum-short-profile></forum-short-profile>
        </div>
      </div>
    </div>
    <div class="row col-12">
      <forum-comment></forum-comment>
    </div>
    <!-- <div class="row col-12">
      <qna-comment-create :info="createBigComments"></qna-comment-create>
    </div> -->
  </div>
</template>

<script>
import ForumShortProfile from '@/components/forum/ForumShortProfile';
import ForumComment from '@/components/forum/ForumComment';
import ForumDetailStatus from '@/components/forum/ForumDetailStatus';
import ForumDetailContent from '@/components/forum/ForumDetailContent';

export default {
  components: {
    ForumShortProfile,
    ForumComment,
    ForumDetailStatus,
    ForumDetailContent,
  },
  data() {
    return {
      // forumData: {
      //   forum_id: 3,
      //   title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      //   ref_tags: ['javascript', 'vue'],
      //   like_num: 5,
      //   comment_num: 7,
      //   viewed_num: 50,
      //   user_idfo : {
      //     user_id: 3,
      //     username: 'testuser',
      //     written_time: '2021-01-06T02:02',
      //   }
      // }
    };
  },
  methods: {
    // goToProfile() {
    //   this.$router.push({ name: 'Profile' });
    // },
  },
};
</script>

<style scoped></style>
