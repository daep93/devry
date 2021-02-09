<template>
  <div class="q-pl-md row col-12">
    <div class="row col-12">
      <q-card flat bordered style="width: 40px; height: 125px;">
        <div style="margin:0 auto; text-align:center" class="q-pt-sm">
          <template v-if="info.liked_ans">
            <q-icon
              :name="$i.ionHeart"
              color="red"
              size="17px"
              class="cursor-pointer"
              @click="checkLiked(index)"
            ></q-icon>
          </template>
          <template v-else>
            <q-icon
              :name="$i.ionHeartOutline"
              style="color:#727272"
              size="17px"
              class="cursor-pointer"
              @click="checkLiked(index)"
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
// import { toggleQnaCommentLike } from '@/api/qna';

export default {
  props: {
    info: Object,
  },
  methods: {
    async checkLiked() {
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
    },
  },
};
</script>

<style scoped></style>
