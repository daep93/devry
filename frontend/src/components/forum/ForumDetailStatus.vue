<template>
  <div class="q-pl-md">
    <q-card flat bordered style="width: 50px; height: 245px;">
      <div style="margin:0 auto; text-align:center" class="q-pt-sm">
        <template v-if="liked">
          <q-icon
            :name="$i.ionHeart"
            color="red"
            size="17px"
            class="cursor-pointer"
            @click="checkLiked"
          ></q-icon>
        </template>
        <template v-else>
          <q-icon
            :name="$i.ionHeartOutline"
            style="color:#727272"
            size="17px"
            class="cursor-pointer"
            @click="checkLiked"
          ></q-icon>
        </template>
        <br />
        <span>{{ like_num }}</span>
        <br />
        <br />
        <q-icon
          :name="$i.ionChatboxEllipsesOutline"
          style="color:#727272"
          size="17px"
        ></q-icon>
        <br />
        <span>{{ info.comment_count }}</span>
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
import { toggleForumLike } from '@/api/forum';
export default {
  props: {
    info: Object,
  },
  data() {
    return {
      liked: this.info.liked,
      like_num: this.info.like_num,
    };
  },
  watch: {
    info(newValue) {
      (this.liked = newValue.liked), (this.like_num = newValue.like_num);
    },
  },
  methods: {
    async checkLiked() {
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
      try {
        await toggleForumLike(this.info.post_id);
        this.liked = !this.liked;
        if (this.liked) {
          this.like_num = this.like_num + 1;
        } else {
          this.like_num = this.like_num - 1;
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped></style>
