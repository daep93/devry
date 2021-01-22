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
          <!-- 커뮤니티 활동 내역 정보가 담긴 배너 -->
          <post-banner></post-banner>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderBanner from '@/components/profile/HeaderBanner';
import SideBanner from '@/components/profile/SideBanner';
import PostBanner from '@/components/profile/PostBanner';
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
        userid: 3,
        email: 'ssafyPark@edu.ssafy.com',
        username: 'Ssafy Park',
        joined: '2013-02-08T09',
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

        skills: ['HTML', 'MongoDB', 'Javascript', 'vue'],
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
      };
    },
    sideInfo() {
      return {
        // TODO : post의 갯수와 comment의 갯수 넘겨줘야함.
        tags: this.fetchedData.tags,
        skills: this.fetchedData.skills,
        projects: this.fetchedData.projects,
      };
    },
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
