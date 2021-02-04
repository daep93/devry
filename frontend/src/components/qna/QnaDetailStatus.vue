<template>
  <div class="q-pl-md">
    <q-card flat bordered style="width: 40px; height: 245px;">
      <div style="margin:0 auto; text-align:center" class="q-pt-sm">
        <template v-if="writer_info.liked">
          <q-icon
            :name="$i.ionHeartOutline"
            style="color:#727272"
            size="17px"
            class="cursor-pointer"
            @click="checkLiked"
          ></q-icon>
        </template>
        <template v-else>
          <q-icon
            :name="$i.ionHeart"
            color="red"
            size="17px"
            class="cursor-pointer"
            @click="checkLiked"
          ></q-icon>
        </template>
        <br />
        <span>{{ info.like_num }}</span>
        <br />
        <br />
        <q-icon
          :name="$i.ionChatboxEllipsesOutline"
          style="color:#727272"
          size="17px"
        ></q-icon>
        <br />
        <span>{{ info.comment_num.length }}</span>
        <br />
        <br />
        <q-icon :name="$i.ionEyeOutline" color="grey-6" size="17px"></q-icon>
        <br />
        <span>{{ info.viewed_num }}</span>
        <br />
        <br />
        <q-icon
          :name="$i.ionBookmarkOutline"
          color="grey-6"
          size="17px"
          class="cursor-pointer"
        ></q-icon>
        <br />
        <span>{{ info.bookmark_num }}</span>
      </div>
    </q-card>
  </div>
</template>

<script>
export default {
  props: {
    info: Object,
  },
  data() {
    return {
      writer_info: {
        userid: 1,
        username: 'fe-master',
        profile_img: null,
        post_num: 27,
        follower_num: 57,
        bio: '소개입니다.',
        pinned: [
          {
            title: 'pinned 1 title',
            post_id: 3,
          },
        ],
        liked: true,
        is_following: false,
      },
      quest_post: {
        title: 'How can I use axios in Vue.js?',
        written_time: '2021-01-24T02:02',
        ref_tags: ['vue', 'javascript'],
        solved: true,
        like_num: 3,
        comment_num: 2,
        viewed_num: 300,
        bookmarked_num: 6,
        contents:
          'One of the most essential parts of frontend development is communication with the backend by making HTTP requests. There are a few ways how we can make API calls in Javascript asynchronously.',
      },
    };
  },
  methods: {
    checkLiked() {
      this.writer_info.liked = !this.writer_info.liked;
      if (this.writer_info.liked) {
        this.quest_post.like_num = this.quest_post.like_num - 1;
      } else {
        this.quest_post.like_num = this.quest_post.like_num + 1;
      }
    },
  },
};
</script>

<style scoped></style>
