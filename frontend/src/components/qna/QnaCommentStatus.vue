<template>
  <div class="q-pl-md row col-12">
    <div class="row col-12">
      <!-- <div v-for="(data, index) in info" :key="index" class="row col-12"> -->
      <!-- <div v-for="(data, index) in answer_posts" :key="index" class="row col-12"> -->
      <q-card flat bordered style="width: 40px; height: 125px;">
        <div style="margin:0 auto; text-align:center" class="q-pt-sm">
          <template v-if="liked_ans">
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
          <span>{{ data.like_ans_num }}</span>
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
  props: {
    info: Object,
  },
  data() {
    return {};
  },
  methods: {
    checkLiked(index) {
      for (const heart of this.info) {
        if (this.info.indexOf(heart) === index) {
          heart.liked_ans = !heart.liked_ans;
          if (heart.quest_post.liked) {
            heart.like_ans_num = heart.like_ans_num - 1;
          } else {
            heart.like_ans_num = heart.like_ans_num + 1;
          }
        }
      }
    },
  },
};
</script>

<style scoped></style>
