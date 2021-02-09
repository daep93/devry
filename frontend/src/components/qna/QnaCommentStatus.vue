<template>
  <div class="q-pl-md row col-12">
    <div class="row col-12">
      <q-card flat bordered style="width: 40px; height: 125px;">
        <div style="margin:0 auto; text-align:center" class="q-pt-sm">
          <template v-if="info.liked_ans">
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
          <span>{{ info.like_ans_num }}</span>
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
import { toggleQnaCommentLike } from '@/api/qna';

export default {
  props: {
    info: Object,
    idx: Number,
  },
  // data() {
  //   return {
  //     liked_ans: this.liked_ans,
  //     like_ans_num: this.like_ans_num,
  //   };
  // },
  methods: {
    // checkLiked(index) {
    //   console.log(this.idx);
    //   console.log(this.info[this.idx]);
    //   for (const heart of this.info) {
    //     if (this.info.indexOf(heart) === index) {
    //       heart.liked_ans = !heart.liked_ans;
    //       if (heart.quest_post.liked) {
    //         heart.like_ans_num = heart.like_ans_num - 1;
    //       } else {
    //         heart.like_ans_num = heart.like_ans_num + 1;
    //       }
    //     }
    //   }
    // },
    async checkLiked() {
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
      try {
        console.log(this.info.liked_ans);
        const commentId = this.info.id;
        const { data } = await toggleQnaCommentLike(commentId);
        this.info.liked_ans = !this.info.liked_ans;
        if (this.info.liked_ans) {
          this.info.like_ans_num = this.info.like_ans_num + 1;
        } else {
          this.info.like_ans_num = this.info.like_ans_num - 1;
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped></style>
