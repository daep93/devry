<template>
  <div class="row col-12">
    <div class="row col-12">
      <div class="row col-12">
        <q-separator />
        <div
          class="row col-12 q-py-sm"
          v-for="(data, index) in comments"
          :key="index"
        >
          <div class="row col-12 justify-between">
            <div class="row col-10">
              <span class="q-mr-xs">{{ index + 1 }}</span>
              <span class="q-mr-sm" style="color: blue">
                @{{ data.user.username }}
              </span>
              <span class="text-caption" style="color: gray">
                {{ data.written_time | moment('YYYY/MM/DD HH:mm') }}
              </span>
            </div>
          </div>
          <div class="q-ml-lg q-py-xs row col-12">
            {{ data.content }}
          </div>
          <q-btn @click="qnaSmallCommentDelete(index)">삭제하기</q-btn>
          <q-btn @click="qnaSmallCommentUpdate(index)">수정하기</q-btn>
        </div>
      </div>
    </div>
    <q-separator />
    <div class="q-mt-sm row col-12">
      <q-input
        borderless
        v-model="text"
        placeholder="댓글을 입력해주세요"
        class="full-width"
      />
    </div>
    <div class="row col-12">
      <div class="row col-10"></div>
      <div class="row col-2 q-pl-xl q-mb-lg">
        <q-btn
          color="primary"
          label="댓글 추가"
          size="md"
          @click="setSmallAnswer"
        />
      </div>
    </div>
  </div>
</template>

<script>
import {
  registerSmallAnswer,
  deleteSmallAnswers,
  updateSmallAnswers,
} from '@/api/qna';
export default {
  props: {
    comments: Array,
    user_id: Number,
    post_id: Number,
    username: String,
  },
  data: function() {
    return {
      text: '',
      // update: false,
    };
  },
  methods: {
    checkLiked(index) {
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
      const heart = this.comments[index];

      heart.liked = !heart.liked;
      if (heart.liked) {
        heart.like_num = heart.like_num - 1;
      } else {
        heart.like_num = heart.like_num + 1;
      }
    },
    async setSmallAnswer() {
      try {
        this.$q.loading.show();
        const { data } = await registerSmallAnswer({
          qna: this.post_id,
          content: this.text,
          user: this.$store.state.id,
        });
        this.text = '';
        this.$emit('reloadSmallAns');
        location.reload();
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    async qnaSmallCommentDelete(index) {
      try {
        this.$q.loading.show();
        const qnasmall_pk = this.comments[index].id;
        await deleteSmallAnswers(qnasmall_pk);
        location.reload();
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    async qnaSmallCommentUpdate(index) {
      try {
        this.$q.loading.show();
        const qnasmall_pk = this.comments[index].id;
        console.log(qnasmall_pk);
        await updateSmallAnswers(qnasmall_pk, {
          content: this.text,
        });
        // location.reload();
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    // qnaSmallCommentUpdate(index) {
    //   this.update = !this.update;
    //   console.log(this.update);
    //   console.log(index);
    // },
  },
};
</script>

<style scoped></style>
