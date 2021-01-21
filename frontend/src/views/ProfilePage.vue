<template>
  <div style="width:100%">
    <div class="row back-header justify-center"></div>
    <div class="row justify-center ">
      <header-banner></header-banner>
    </div>
    <div class="row justify-center body-banner">
      <div class="row  justify-between" style="width: 60%;">
        <div style="width:30%">
          <side-banner></side-banner>
        </div>
        <div style="width: 67%">
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
