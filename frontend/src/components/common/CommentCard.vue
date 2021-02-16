<template>
  <div
    class="row q-mb-sm q-pl-sm"
    style="width:100%; border: 1px solid #C1B9B9; border-radius: 8px"
  >
    <div class="row justify-between q-pt-xs q-mb-xs">
      <div class="row items-center">
        <div class="q-mr-sm">@a{{ detail.username }},</div>
        <div>{{ detail.written_time | moment('YYYY/MM/DD') }}</div>
      </div>
    </div>
    <div class="row text-bold q-mb-sm full-width" style="font-size:14pt;">
      {{ detail.title }}
    </div>
    <div
      class="row text-weight-thin q-mb-sm text-grey-8 q-pr-lg comment-content"
    >
      {{ detail.content }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    detail: Object,
  },
};
</script>

<style scoped>
.comment-content {
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
