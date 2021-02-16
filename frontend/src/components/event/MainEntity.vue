<template>
  <div class="row justify-center overflow-hidden" @click="goToDetail">
    <img
      src="@/assets/tensorFlow.jpg"
      alt="tensorflow"
      style="height:240px; width:100%;"
      
    />
    <!-- {{ entity.thumnail }} -->
    <!-- {{ this.address }}
    <img
      src="address"
      style="height:240px; width:100%;"
    /> -->
  </div>
</template>

<script>
export default {
  props: {
    entity: Object,
  },
  data() {
    return {
      num: '',
      address: `https://devry.kr${this.entity.thumnail}`
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