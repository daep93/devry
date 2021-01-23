<template>
  <div style="width:100%">
    <!-- 백그라운드 파란색 헤더(장식) -->
    <div class="row back-header justify-center"></div>
    <!-- 개인 정보가 담긴 배너 -->
    <div class="row justify-center ">
      <header-banner :info="headerInfo"></header-banner>
    </div>
    <div class="row justify-center body-banner">
      <div class="row  justify-between" style="width: 60%;">
        <div style="width:30%">
          <!-- 커뮤니티 활동 성향 관련 정보가 담긴 배너 -->
          <side-banner :info="sideInfo"></side-banner>
        </div>
        <div style="width: 67%">
          <!-- 글과 댓글 정보가 담긴 배너 -->
          <post-banner :info="postInfo"></post-banner>
        </div>
      </div>
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
      // TODO : 사진을 어떻게 받을지 고민...
      fetchedData: {
        email: 'ssafyPark@edu.ssafy.com',
        username: 'Ssafy Park',
        joined: '2013-02-08',
        followerNum: 4301,
        followeeNum: 392,
        region: 'Daejeon',
        group: 'Multi Campus',
        bio: `Jumped into web development 1st of January 2020 and I'm completely in
            love. I have little experience as a blogger but practice makes
            perfect! 🤖🦾`,
        links: {
          Github: 'https://github.com/daep93/',
          Gitlab: 'https://lab.ssafy.com/',
          Facebook: 'https://www.facebook.com/groups/vuejs.korea/',
          Linkedin:
            'https://www.linkedin.com/in/%EB%8C%80%ED%98%84-%EB%B0%95-001319202/',
        },

        tech_stacks: ['HTML', 'MongoDB', 'Javascript', 'vue'],
        projects: {
          'ssafy-common': 'https://lab.ssafy.com/',
          'ssafy-special': 'https://lab.ssafy.com/',
          'ssafy-complete': 'https://lab.ssafy.com/',
        },
        tags: {
          Vue: 8,
          React: 12,
          Angular: 3,
          Javascript: 24,
        },
        // TODO : 이미지를 어떻게 받을지 고민을 해야함.
        pinnedPosts: [
          {
            id: 1,
            username: 'Go SSAFY',
            writtenAt: '2021-01-03T09',
            likeNum: 30,
            commentNum: 5,
            title: 'Vue interview questions and answers for js developers',
            tags: ['Vue', 'Javascript', 'React', 'Angular'],
          },
          {
            id: 2,
            username: 'Go SSAFY',
            writtenAt: '2021-01-03T09',
            likeNum: 13,
            commentNum: 1,
            title: 'Useful Markup skills 5',
            tags: ['Vue', 'Javascript', 'React', 'Angular'],
          },
        ],
        posts: [
          {
            id: '1',
            username: 'Go SSAFY',
            writtenAt: '2021-01-03T09',
            likeNum: 30,
            commentNum: 5,
            title: 'Vue interview questions and answers for js developers',
            tags: ['Vue', 'Javascript', 'React', 'Angular'],
          },
          {
            id: '2',
            username: 'Go SSAFY',
            writtenAt: '2021-01-03T09',
            likeNum: 13,
            commentNum: 1,
            title: 'Useful Markup skills 5',
            tags: ['Vue', 'Javascript', 'React', 'Angular'],
          },
          {
            id: '3',
            username: 'Go SSAFY',
            writtenAt: '2021-01-03T09',
            likeNum: 13,
            commentNum: 1,
            title: 'Useful Markup skills 5',
            tags: ['Vue', 'Javascript', 'React', 'Angular'],
          },
        ],
        comments: [
          {
            id: 1,
            postId: 1,
            username: 'Go SSAFY',
            writtenAt: '2021-01-03T09',
            title: 'Vue interview questions and answers for js developers',
            comment:
              'Hope this has been helpful and will give you ideas for your future.',
          },
          {
            id: 2,
            postId: 1,
            username: 'Go SSAFY',
            writtenAt: '2021-01-03T09',
            title: 'Vue interview questions and answers for js developers',
            comment:
              'Hope this has been helpful and will give you ideas for your future.Hope this has been helpful and will give you ideas for your future.Hope this has been helpful and will give you ideas for your future.',
          },
        ],
      },
    };
  },
  computed: {
    headerInfo() {
      return {
        username: this.fetchedData.username,
        location: this.fetchedData.location,
        group: this.fetchedData.group,
        email: this.fetchedData.email,
        links: this.fetchedData.links,
        joined: this.fetchedData.joined,
        followerNum: this.fetchedData.followerNum,
        followeeNum: this.fetchedData.followeeNum,
        introduction: this.fetchedData.introduction,
        bio: this.fetchedData.bio,
      };
    },
    sideInfo() {
      return {
        // TODO : post의 갯수와 comment의 갯수 넘겨줘야함.
        tags: this.fetchedData.tags,
        skills: this.fetchedData.tech_stacks,
        projects: this.fetchedData.projects,
      };
    },
    postInfo() {
      return {
        posts: this.fetchedData.posts,
        comments: this.fetchedData.comments,
        pinned: this.fetchedData.pinnedPosts,
      };
    },
  },
  async created() {
    const id = this.$route.params.id;
    try {
      this.$q.loading.show();
      const { data } = await getProfile(id);
      // this.fetchedData = data;
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
.body-banner {
  position: relative;
  top: -6vh;
}
.side-banner {
  width: 100%;
}
.contents-banner {
  width: 100%;
}
</style>
