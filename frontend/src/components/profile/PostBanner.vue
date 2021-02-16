<template>
  <div class="col-7 q-my-lg ">
    <div class="q-mb-sm row items-center">
      <q-icon
        :name="$i.ionAttachOutline"
        style="color: #B54333"
        size="md"
        class="q-mr-xs"
      ></q-icon>
      <span class="text-h5 text-weight-bold">Pinned</span>
    </div>
    <q-card class="q-mb-lg">
      <q-card-section
        style="width:100%;border: 2px solid #FBAA9F; border-raidus:5px; "
      >
        <q-carousel
          v-model="slide"
          transition-prev="slide-right"
          transition-next="slide-left"
          swipeable
          animated
          infinite
          control-color="black"
          padding
          arrows
          :autoplay="autoplay"
          @mouseenter="autoplay = false"
          @mouseleave="autoplay = true"
          height="170px"
        >
          <q-carousel-slide
            v-for="(post, index) in info.pinned"
            :name="index"
            :key="post.id"
            style="border-radius: 10px;"
          >
            <post-card :detail="info.pinned[0]"></post-card>
          </q-carousel-slide>
        </q-carousel>
      </q-card-section>
    </q-card>
    <div class="row justify-between q-mb-sm">
      <div class="q-mb-sm row items-center">
        <q-icon
          :name="$i.ionLayersOutline"
          style="color: #259EC5"
          size="md"
          class="q-mr-xs"
        ></q-icon>
        <span class="text-h5 text-weight-bold">History</span>
      </div>
      <div>
        <q-tabs v-model="post" style="color:#259EC5">
          <q-tab name="posts" label="posts" class="qtab" />
          <q-tab name="comments" label="comments" />
        </q-tabs>
      </div>
    </div>
    <q-card v-if="post == 'posts'">
      <q-card-section
        style="width:100%;border: 2px solid #2F95B4; border-raidus:5px; "
      >
        <post-card
          v-for="post in info.posts"
          :detail="post"
          :key="post.id"
        ></post-card>
      </q-card-section>
    </q-card>
    <q-card v-if="post == 'comments'">
      <q-card-section
        style="width:100%;border: 2px solid #2F95B4; border-raidus:5px; "
      >
        <comment-card
          v-for="comment in info.comments"
          :detail="comment"
          :key="comment.id"
        ></comment-card>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import PostCard from '@/components/common/PostCard';
import CommentCard from '@/components/common/CommentCard';
export default {
  props: {
    info: Object,
  },
  components: { PostCard, CommentCard },
  data() {
    return {
      autoplay: true,
      slide: 1,
      post: 'posts',
    };
  },
};
</script>

<style scoped></style>
