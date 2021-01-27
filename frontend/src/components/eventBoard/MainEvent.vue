<template>
  <div style="clear: both; margin-bottom: 50px;">
    <q-carousel
      animated
      v-model="slide"
      navigation
      infinite
      :autoplay="autoplay"
      arrows
      transition-prev="slide-right"
      transition-next="slide-left"
      @mouseenter="autoplay = false"
      @mouseleave="autoplay = true"
      style="height: 300px;"
    >
      <q-carousel-slide :name="1" style="background-color: black; border-radius: 10px;" @click="moveToDetailPage">
        <div style="margin: 50px 0px 0px 50px;">
          <div class="text-h5 text-white">For Developer vol.1</div>
          <div class="text-h4 text-teal-8 text-weight-bolder">2021 Vue.js Online</div>
        </div>
        <q-btn outline class="absolute-bottom-right" color="white" text-color="white" label="바로가기" style="margin: 50px;"/>
      </q-carousel-slide>
      <q-carousel-slide :name="2" style="background-color: #213186; border-radius: 10px;">
        <div style="position: absolute; top: 9%; left: 29%;">
          <img src="@/assets/hackathon.png" alt="AI hackathon" style="height: 240px; width: 60%;">
        </div>
        <!-- <q-btn outline class="absolute-bottom-right" color="white" text-color="white" label="바로가기" style="margin: 50px;"/> -->
      </q-carousel-slide>
      <q-carousel-slide :name="3" img-src="https://cdn.quasar.dev/img/parallax2.jpg" style="border-radius: 10px;">
        <q-btn outline class="absolute-bottom-right" color="white" text-color="white" label="바로가기" style="margin: 50px;"/>
      </q-carousel-slide>
      <q-carousel-slide :name="4" img-src="https://cdn.quasar.dev/img/quasar.jpg" style="border-radius: 10px;">
        <q-btn outline  class="absolute-bottom-right" color="white" text-color="white" label="바로가기" style="margin: 50px;"/>
      </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script>
export default {
  data () {
    return {
      slide: 1,
      autoplay: true
    }
  },
  methods: {
    moveToDetailPage: function() {
      this.$router.push({ path: '/event-detail'})
    }
  }
}
</script>

<style>

</style>