<template>
  <div style="clear: both; " class="q-mb-xl">
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
      height="270px"
    >
      <q-carousel-slide
        :name="1"
        class="bg-black"
        style="border-radius: 10px;"
        @click="moveToDetailPage"
      >
        <div class="q-mt-lg q-ml-lg">
          <div class="text-h5 text-white">For Developer vol.1</div>
          <div class="text-h4 text-teal-8 text-weight-bolder">
            2021 Vue.js Online
          </div>
        </div>
        <q-btn
          outline
          class="absolute-bottom-right q-ma-xl"
          color="white"
          text-color="white"
          label="바로가기"
        />
      </q-carousel-slide>
      <q-carousel-slide
        :name="2"
        style="background-color: #213186; border-radius: 10px;"
        class="overflow-hidden"
      >
        <div class="row justify-center overflow-hidden">
          <img
            src="@/assets/hackathon.png"
            alt="AI hackathon"
            style="height:250px;width:40%"
          />
        </div>
      </q-carousel-slide>
      <q-carousel-slide
        :name="3"
        img-src="https://cdn.quasar.dev/img/parallax2.jpg"
        style="border-radius: 10px;"
      >
        <q-btn
          outline
          class="absolute-bottom-right q-ma-xl"
          color="white"
          text-color="white"
          label="바로가기"
        />
      </q-carousel-slide>
      <q-carousel-slide
        :name="4"
        img-src="https://cdn.quasar.dev/img/quasar.jpg"
        style="border-radius: 10px;"
      >
        <q-btn
          outline
          class="absolute-bottom-right q-ma-xl"
          color="white"
          text-color="white"
          label="바로가기"
        />
      </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script>
export default {
  data() {
    return {
      autoplay: true,
      slide: 1,
    };
  },
  methods: {
    moveToDetailPage: function() {
      this.$router.push({ path: '/event-detail' });
    },
  },
};
</script>

<style></style>
