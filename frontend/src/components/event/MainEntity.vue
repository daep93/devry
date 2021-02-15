<template>
  <q-carousel-slide
    :name="this.num"
    style="background-color: #1E1B39; border-radius: 10px;"
    class="overflow-hidden"
    @click="goToDetail"
  >
    <div class="row justify-center overflow-hidden">
      <img
        :src="entity.thumnail"
        style="height:230px; width:70%;"
      />
    </div>
  </q-carousel-slide>
</template>

<script>
export default {
  props: {
    entity: Object,
  },
  data() {
    return {
      num: 1,
    }
  },
  methods: {
    goToDetail() {
      this.$router.push(`/event-detail/${this.entity.id}`);
    }
  },
}
</script>

<style>

</style>