<template>
  <div class="col-7 q-my-lg ">
    <div class="row justify-between q-mb-sm">
      <div class="q-mb-sm row items-center">
        <q-icon
          :name="$i.ionAttachOutline"
          style="color: #B54333"
          size="md"
          class="q-mr-xs"
        ></q-icon>
        <span class="text-h5 text-weight-bold">Pinned</span>
      </div>
      <div>
        <q-tabs v-model="pinned" style="color:#259EC5">
          <q-tab name="forum" label="포럼" />
          <q-tab name="qna" label="질문" />
        </q-tabs>
      </div>
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
          height="180px"
          v-if="info.qnas_pinned.length"
        >
          <q-carousel-slide
            v-for="(post, index) in pinned_post"
            :name="index + 1"
            :key="post.id"
            style="border-radius: 10px;"
            class="row items-center"
          >
            <forum-post-card
              :detail="post"
              v-if="pinned == 'forum'"
            ></forum-post-card>
            <qna-post-card :detail="post" v-else></qna-post-card>
          </q-carousel-slide>
        </q-carousel>
        <div v-else class="full-width text-center text-grey-6">없음</div>
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
          <q-tab name="forum" label="포럼" />
          <q-tab name="qna" label="질문" />
          <q-tab name="comments" label="댓글" />
        </q-tabs>
      </div>
    </div>
    <q-card v-if="post == 'qna'">
      <q-card-section
        style="width:100%;border: 2px solid #2F95B4; border-raidus:5px; "
      >
        <qna-post-card
          v-for="qna in info.qnas"
          :detail="qna"
          :key="qna.id"
        ></qna-post-card>
      </q-card-section>
    </q-card>
    <q-card v-if="post == 'forum'">
      <q-card-section
        style="width:100%;border: 2px solid #2F95B4; border-raidus:5px; "
      >
        <forum-post-card
          v-for="forum in info.forums"
          :detail="forum"
          :key="forum.id"
        ></forum-post-card>
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
import QnaPostCard from '@/components/qna/QnaPostCard';
import ForumPostCard from '@/components/forum/ForumPostCard';
import CommentCard from '@/components/common/CommentCard';
export default {
  props: {
    info: Object,
  },
  components: { QnaPostCard, CommentCard, ForumPostCard },
  data() {
    return {
      autoplay: true,
      slide: 1,
      post: 'forum',
      pinned: 'forum',
      pinned_post: this.info.forums_pinned,
    };
  },
  watch: {
    pinned(newValue) {
      if (newValue === 'forum') this.pinned_post = this.info.forums_pinned;
      else this.pinned_post = this.info.qnas_pinned;
    },
  },
};
</script>

<style scoped></style>
