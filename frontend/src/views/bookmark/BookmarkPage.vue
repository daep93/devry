<template>
  <div class="row justify-center q-pt-lg ">
    <div class="row col-8 justify-center q-pl-lg">
      <div class="row q-mb-sm q-mb-lg col-12 text-h5 text-weight-bold">
        <div class="row col-9">
          <span>
            <q-icon :name="$i.ionBookmarkOutline" size="sm"></q-icon
          ></span>
          <span class="text-h5 text-weight-bold q-ml-xs">My Bookmark</span>
        </div>
      </div>
      <div class="row col-12 q-my-lg"><qna-bookmark></qna-bookmark></div>
      <div class="row col-12 q-my-lg"><forum-bookmark></forum-bookmark></div>
      <div class="row col-12 q-my-lg"><event-bookmark></event-bookmark></div>
    </div>
  </div>
</template>

<script>
import QnaBookmark from '@/components/bookmark/QnaBookmark';
import ForumBookmark from '@/components/bookmark/ForumBookmark';
import EventBookmark from '@/components/bookmark/EventBookmark';

export default {
  components: {
    QnaBookmark,
    ForumBookmark,
    EventBookmark,
  },
};
</script>

<style scoped></style>
