<template>
  <div>
    <ForumTags></ForumTags>
    <ForumList></ForumList>
  </div>
</template>

<script>
import ForumList from '@/components/forum/ForumList';
import ForumTags from '@/components/forum/ForumTags';

export default {
  components: {
    ForumList,
    ForumTags,
  },
};
</script>

<style scoped></style>
