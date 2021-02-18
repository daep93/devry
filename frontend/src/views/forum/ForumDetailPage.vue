<template>
  <div class="row col-12">
    <div class="row col-12">
      <div class="row col-2 q-mt-lg">
        <div class="row col-9"></div>
        <div class="row col-3">
          <!-- <forum-detail-status></forum-detail-status> -->
          <!-- <forum-detail-status :info="status"></forum-detail-status> -->
        </div>
      </div>
      <div class="row col-10 q-mt-lg">
        <div class="col-9">
          <div class="row col-12">
            <forum-detail-content :info="forumBody"></forum-detail-content>
          </div>
        </div>
        <div class="col-3 q-pl-sm q-pr-xl">
          <forum-short-profile :info="shortProfile"></forum-short-profile>
        </div>
      </div>
    </div>
    <div class="row col-12">
      <forum-comment :info="comments"></forum-comment>
    </div>
    <div class="row col-12 q-my-xl">
      <forum-comment-create :info="createComments"></forum-comment-create>
    </div>
  </div>
</template>

<script>
import ForumShortProfile from '@/components/forum/ForumShortProfile';
import ForumComment from '@/components/forum/ForumComment';
import ForumDetailStatus from '@/components/forum/ForumDetailStatus';
import ForumDetailContent from '@/components/forum/ForumDetailContent';
import ForumCommentCreate from '@/components/forum/ForumCommentCreate';
import { loadForumItem } from '@/api/forum';

export default {
  components: {
    ForumShortProfile,
    ForumComment,
    ForumDetailStatus,
    ForumDetailContent,
    ForumCommentCreate,
  },
  data() {
    return {
      contents: '',
    };
  },
  computed: {
    status() {
      return {
        like_num: this.contents.forum_post[0].like_num,
        liked: this.contents.forum_post[0].liked,
        bookmarked: this.contents.forum_post[0].bookmarked,
        bookmark_num: this.contents.forum_post[0].bookmark_num,
        viewed_num: this.contents.forum_post[0].viewed_num,
        post_id: this.contents.forum_post[0].id,
        comment_count: this.contents.forum_post[0].comment_num,
      };
    },
    forumBody() {
      return {
        title: this.contents.forum_post[0].title,
        ref_tags: this.contents.forum_post[0].ref_tags,
        content: this.contents.forum_post[0].content,
        written_time: this.contents.forum_post[0].written_time,
        post_id: this.contents.forum_post[0].id,
        user: this.contents.writer_info[0].user,
      };
    },
    comments() {
      return this.contents.comment_set;
    },
    createComments() {
      return {
        post_id: this.contents.forum_post[0].id,
      };
    },
    shortProfile() {
      return {
        profile: this.contents.profile,
        user: this.contents.user,
      };
    },
  },
  async created() {
    const index = this.$route.params.id;
    try {
      const { data } = await loadForumItem(index);
      this.contents = data;
    } catch (error) {
      console.log(error);
    }
    this.$store.commit('offLeft');
  },
};
</script>

<style scoped></style>
