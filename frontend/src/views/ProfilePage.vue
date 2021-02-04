<template>
  <div style="width:100%">
    <!-- 백그라운드 파란색 헤더(장식) -->
    <div class="row back-header justify-center"></div>
    <!-- 개인 정보가 담긴 배너 -->
    <div class="row justify-center ">
      <header-banner :info="headerInfo"></header-banner>
    </div>
    <div class="row justify-center">
      <!-- 커뮤니티 활동 성향 관련 정보가 담긴 배너 -->
      <side-banner :info="sideInfo"></side-banner>
      <!-- 글과 댓글 정보가 담긴 배너 -->
      <post-banner :info="postInfo"></post-banner>
    </div>
  </div>
</template>

<script>
import HeaderBanner from '@/components/profile/HeaderBanner';
import SideBanner from '@/components/profile/SideBanner';
import PostBanner from '@/components/profile/PostBanner';
import { getProfile } from '@/api/profile.js';
export default {
  components: {
    HeaderBanner,
    SideBanner,
    PostBanner,
  },
  // 가짜 데이터
  data() {
    return {
      profile: {},
    };
  },
  computed: {
    headerInfo() {
      return {
        username: this.profile.username,
        location: this.profile.location,
        group: this.profile.group,
        email: this.profile.email,
        links: this.profile.links,
        joined: this.profile.joined,
        followerNum: this.profile.follower_num,
        followeeNum: this.profile.followee_num,
        bio: this.profile.bio,
      };
    },
    sideInfo() {
      return {
        // TODO : post의 갯수와 comment의 갯수 넘겨줘야함.
        tags: this.profile.tags,
        skills: this.profile.tech_stacks,
        projects: this.profile.projects,
        postNum: this.profile.posts.length,
        commentNum: this.profile.comments.length,
      };
    },
    postInfo() {
      return {
        posts: this.profile.posts,
        comments: this.profile.comments,
        pinned: this.profile.pinned_posts,
      };
    },
  },
  async created() {
    const id = this.$route.params.id;
    try {
      this.$q.loading.show();
      const { data } = await getProfile(id);
      this.profile = data;
    } catch (error) {
      console.log(error);
    } finally {
      this.$q.loading.hide();
    }
  },
};
</script>

<style scoped>
.back-header {
  height: 15vh;
  background-color: #1595dc;
}
</style>
