<template>
  <div class="q-pa-lg q-mt-sm row justify-center">
    <div class="q-pa-sm" style="width: 80vw;">
      <!-- 타이틀 -->
      <div class="q-mb-md">
        <span class="text-h4 text-weight-bolder">QnA Registration</span>
        <p class="text-subtitle2 q-mt-md q-mb-xl">
          궁금하신 점을 질문해보세요:)
        </p>
      </div>
      <!-- QnA 입력 폼 -->
      <div class="q-pa-md q-gutter-sm row">
        <q-card flat bordered>
          <!-- 제목 입력 -->

          <q-input
            v-model="contents"
            min-height="50rem"
            placeholder="내용을 입력해주세요"
            type="textarea"
          >
          </q-input>
        </q-card>
        <!-- 미리보기 화면 -->
        <q-card flat filled class="col bg-grey-3 full-width row">
          <q-card-section class="row col-12">
            <q-markdown :src="contents" class="full-width"> </q-markdown>
          </q-card-section>
        </q-card>
      </div>
      <!-- buttons -->
      <div class="q-mb-xl q-mt-xl" style="text-align: center;">
        <q-btn
          outline
          color="blue-12"
          class="text-weight-bold q-px-xl q-py-sm q-mr-md"
          label="임시저장"
          size="md"
        />
        <q-btn
          color="blue-12"
          class="text-weight-bold q-px-xl q-py-sm"
          label="작성하기"
          size="md"
          @click="submitQna"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { Notify } from 'quasar';

// Notify.create({
//   message: 'Danger, Will Robinson! Danger!'
// })

export default {
  data() {
    return {
      title: '',
      tagItem: '',
      contents: '',
      ref_tags: [
        // 'Vue', 'UX/UI', 'Python'
      ],
    };
  },
  methods: {
    logging() {
      console.log(this.contents);
    },
    createTag(tagItem) {
      if (this.tagItem !== '') {
        console.log(this.tagItem);
        this.ref_tags.push(this.tagItem);
        this.tagItem = '';
      }
    },
    removeTag(tag, index) {
      this.ref_tags.splice(index, 1);
    },
    // TODO : api 수정하기
    // qna 게시글 생성하기
    async submitQna() {
      if (this.title === '') {
        //   this.$q.notify({
        //   message: '제목을 입력해주세요',
        //   color: 'primary',
        // })
        alert('제목은 필수 입력 항목입니다');
      }
      if (this.ref_tags.length === 0) {
        alert('태그를 하나이상 입력해주세요');
      }
      if (this.contents === '') {
        alert('내용은 필수 입력항목 입니다');
      }
      try {
        console.log('성공!');
        // post_id 넘겨주기
        const post_id = this.$route.parmas.id;
        this.$q.loading.show();
        await createQnaItem(post_id, {
          // 넘길 데이터 적어주기
          title: this.title,
          contents: this.contents,
          ref_tags: this.tags,
        });
        // 이동 시킬 페이지 적어주기(이전 페이지로 이동)
        this.$router.go(-1);
      } catch (error) {
        // alert('에러가 발생했습니다!')
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  // qna 게시글 수정하기(기존 정보 가져오기)
  async created() {
    // id 가져오기
    const post_id = this.$route.params.id;
    try {
      this.$q.loading.show();
      await updateQnaItem(post_id, {
        title: this.title,
        contents: this.contents,
        ref_tags: this.tags,
      });
    } catch (error) {
      // alert('에러가 발생했습니다.)
    } finally {
      this.$q.loading.hide();
    }
  },
  computed: {
    isValid() {
      return this.tagItem === '' || this.ref_tags.length > 0;
    },
    // isValidContent () {
    //   return this.content.length > 0
    // }
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>
