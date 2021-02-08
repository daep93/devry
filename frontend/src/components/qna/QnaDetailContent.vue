<template>
  <div class="row full-width">
    <q-card flat bordered class="my-card q-px-lg q-pt-xs row col-12">
      <q-card-section class="row full-width q-pb-sm q-px-none justify-end">
        <div class="row col-2 justify-end">
          <div
            class="row col-12 shadow-1 overflow-hidden"
            style="border-radius:5px; height:25px; max-width:100px;"
          >
            <div
              class="col-2"
              :style="{
                'background-color': info.solved ? '#1976D2' : '#C8DAFE',
              }"
            ></div>
            <div class="col-10 text-center row items-center justify-center">
              {{ info.solved ? '답변 완료' : '답변 대기' }}
            </div>
          </div>
        </div>
      </q-card-section>

      <q-card-section class="row col-12 q-py-none q-mb-sm">
        <div class="row col-12 text-h4 text-weight-bold">
          {{ info.title }}
        </div>
        <div class="text-subtitle2 text-grey-6">
          {{ info.written_time | moment('YYYY/MM/DD HH:mm') }}
        </div>
      </q-card-section>
      <q-card-section class="q-pa-none full-width q-mb-sm">
        <div class="q-ml-md">
          <span v-for="tag in info.ref_tags" :key="tag" class="q-px-xs">
            <q-badge
              class="q-pa-sm text-black"
              :style="{ 'background-color': tagColor(tag, 0.5) }"
              style="font-size:1em; border-radius:3pt;"
            >
              # {{ tag }}
            </q-badge>
          </span>
        </div>
      </q-card-section>
      <q-card-section class="row col-12">
        <v-md-editor v-model="content" mode="preview"> </v-md-editor>
      </q-card-section>
      <q-card-section
        class="row col-12 justify-end"
        v-if="info.user_id == $store.state.id"
      >
        <q-btn @click="qnaPostEdit">수정하기</q-btn>
      </q-card-section>
      <q-card-section class="row col-12">
        <qna-small-comment
          :comments="comments"
          :user_id="info.user_id"
          :post_id="info.post_id"
          :username="info.username"
          @reloadSmallAns="reloadSmallAns"
        ></qna-small-comment>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import QnaSmallComment from '@/components/qna/QnaSmallComment';
import { colorSoloMapper } from '@/utils/tagColorMapper';
import { getSmallAnswers } from '@/api/qna';

export default {
  props: {
    info: Object,
  },
  components: {
    QnaSmallComment,
  },
  data: function() {
    return {
      content: this.info.contents,
      msg: true,
      comments: this.info.comments,
      solved: this.info.solved,
      tags: ['Vue', 'Javascript', 'Typescript'],
      writerStatus: false,
    };
  },
  methods: {
    tagColor(tag, alpha) {
      return colorSoloMapper(tag, alpha);
    },
    qnaPostEdit() {
      this.$router.push(`/qna/${this.info.post_id}`);
    },
    async reloadSmallAns() {
      try {
        this.comments = await getSmallAnswers(this.info.post_id);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped>
.icon-position {
  float: right;
}
</style>
