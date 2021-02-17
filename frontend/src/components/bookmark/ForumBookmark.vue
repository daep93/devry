<template>
  <div class="row col-12 justify-center">
    <div
      class="row col-12 q-mb-md text-h6 text-weight-bold"
      style="color: #545454"
    >
      Forum bookmark
    </div>
    <template v-if="ForumBookmarkList.length > 0">
      북마크 내역 출력
    </template>
    <template v-else>
      아직 북마크한 내역이 없습니다.
    </template>
  </div>
</template>

<script>
export default {
  data() {
    return {
      ForumBookmarkList: [],
    };
  },
};
</script>

<style scoped></style>
