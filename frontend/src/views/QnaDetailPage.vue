<template>
  <div class="row col-12">
    <div class="row col-12">
      <div class="row col-2 q-mt-lg">
        <div class="row col-9"></div>
        <div class="row col-3">
          <qna-detail-status></qna-detail-status>
        </div>
      </div>
      <div class="row col-10 q-mt-lg ">
        <div class="row col-9">
          <div class="row col-12">
            <qna-detail-content></qna-detail-content>
          </div>
        </div>
        <div class="row col-3 q-pl-lg q-pr-xl">
          <qna-short-profile></qna-short-profile>
        </div>
      </div>
    </div>
    <div class="row col-12">
      <qna-big-comment></qna-big-comment>
    </div>

    <div class="row col-9 q-mt-lg q-pl-xl">
      <div class="row col-3"></div>
      <div class="row col-9">
        <div class="row col-12">
          <div style="margin:0 auto;">
            <q-btn
              no-caps
              color="primary"
              id="follow-btn"
              label="답변 작성하기"
              @click="checkFollow(index)"
              style="width: 200px"
              class="q-mb-xl"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="row col-3 q-mt-sm q-pl-lg q-pr-xl"></div>
  </div>
</template>

<script>
import QnaDetailContent from '@/components/qna/QnaDetailContent';
import QnaShortProfile from '@/components/qna/QnaShortProfile';
import QnaBigComment from '@/components/qna/QnaBigComment';
import QnaDetailStatus from '@/components/qna/QnaDetailStatus';

export default {
  components: {
    QnaDetailContent,
    QnaShortProfile,
    QnaBigComment,
    QnaDetailStatus,
  },
  data() {
    return {
      title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      username: 'test user',
      profile_img: 'https://cdn.quasar.dev/img/avatar.png',
    };
  },
  methods: {
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
  },
};
</script>

<style scoped>
.icon-position {
  float: right;
}
</style>
