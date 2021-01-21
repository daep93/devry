<template>
  <div style="width:100%">
    <div class="row back-header justify-center"></div>
    <div class="row justify-center ">
      <header-banner></header-banner>
    </div>
    <div class="row justify-center body-banner">
      <div class="row  justify-between" style="width: 60%;">
        <div style="width:28%">
          <side-banner></side-banner>
        </div>
        <div style="width: 65%">
          <div class="q-mb-sm row items-center">
            <q-icon
              :name="$i.ionAttachOutline"
              style="color: #B54333"
              size="md"
              class="q-mr-xs"
            ></q-icon>
            <span class="text-h5">Pinned</span>
          </div>
          <q-card class="q-mb-lg">
            <q-card-section
              style="width:100%;border: 2px solid #FBAA9F; border-raidus:5px; "
            ></q-card-section>
          </q-card>
          <div class="q-mb-sm row items-center">
            <q-icon
              :name="$i.ionLayersOutline"
              style="color: #259EC5"
              size="md"
              class="q-mr-xs"
            ></q-icon>
            <span class="text-h5">History</span>
          </div>
          <q-card>
            <q-card-section
              style="width:100%;border: 2px solid #2F95B4; border-raidus:5px; "
            >
              <div style=""></div>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderBanner from '@/components/profile/HeaderBanner';
import SideBanner from '@/components/profile/SideBanner';
export default {
  components: {
    HeaderBanner,
    SideBanner,
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
  top: -5vh;
}
.side-banner {
  width: 100%;
}
.contents-banner {
  width: 100%;
}
</style>
