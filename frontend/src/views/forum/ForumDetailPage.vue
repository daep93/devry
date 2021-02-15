<template>
  <div class="row col-12">
    <div class="row col-12">
      <div class="row col-2 q-mt-lg">
        <div class="row col-9"></div>
        <div class="row col-3">
          <forum-detail-status :info="status"></forum-detail-status>
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
        like_num: this.contents.like_num,
        liked: this.contents.liked,
        bookmarked: this.contents.bookmarked,
        bookmark_num: this.contents.bookmark_num,
        viewed_num: this.contents.viewed_num,
        post_id: this.contents.id,
        comment_count: this.contents.comment_count,
      };
    },
    forumBody() {
      return {
        title: this.contents.title,
        ref_tags: this.contents.ref_tags,
        content: this.contents.content,
        written_time: this.contents.written_time,
        post_id: this.contents.id,
        user: this.contents.user,
      };
    },
    comments() {
      return this.contents.comment_set;
    },
    createComments() {
      return {
        post_id: this.contents.id,
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
      // console.log(this.contents);
    } catch (error) {
      console.log(error);
    }
    this.$store.commit('offLeft');
  },
};
</script>

<style scoped></style>
