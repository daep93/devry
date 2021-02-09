<template>
  <div class="q-pl-md row col-12">
    <div v-for="(data, index) in answer_posts" :key="index" class="row col-12">
      <q-card flat bordered style="width: 40px; height: 125px;">
        <div style="margin:0 auto; text-align:center" class="q-pt-sm">
          <template v-if="data.quest_post.liked">
            <q-icon
              :name="$i.ionHeartOutline"
              style="color:#727272"
              size="17px"
              class="cursor-pointer"
              @click="checkLiked(index)"
            ></q-icon>
          </template>
          <template v-else>
            <q-icon
              :name="$i.ionHeart"
              color="red"
              size="17px"
              class="cursor-pointer"
              @click="checkLiked(index)"
            ></q-icon>
          </template>

          <br />
          <span>{{ data.quest_post.like_num }}</span>
          <br />
          <br />
          <q-icon
            :name="$i.ionChatboxEllipsesOutline"
            style="color:#727272"
            size="17px"
          ></q-icon>
          <br />
          <span>0</span>
          <br />
          <br />
        </div>
      </q-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      answer_posts: [
        {
          user_info: {
            userid: 5,
            username: 'SSAFY ONE',
            written_time: '2021-01-25T05:23',
            profile_img: 'user/5',
            post_num: 3,
            follower_num: 10,
            bio: 'SSAFY is The One!',
          },
          quest_post: {
            title: 'Read vue documentation',
            assisted: true,
            like_num: 30,
            comment_num: 1,
            contents: 'Just Read it plz.',
            answers: [
              {
                contents: 'I agree',
                userid: 2,
                username: 'SSAFY Pro',
                written_time: '2021-01-25T05:26',
              },
            ],
            liked: true,
          },
        },
      ],
    };
  },
  methods: {
    checkLiked(index) {
      for (const heart of this.answer_posts) {
        if (this.answer_posts.indexOf(heart) === index) {
          heart.quest_post.liked = !heart.quest_post.liked;
          if (heart.quest_post.liked) {
            heart.quest_post.like_num = heart.quest_post.like_num - 1;
          } else {
            heart.quest_post.like_num = heart.quest_post.like_num + 1;
          }
        }
      }
    },
  },
};
</script>

<style scoped></style>
