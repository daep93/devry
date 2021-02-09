<template>
  <div class="row col-12">
    <div class="row col-2"></div>
    <div class="row col-10">
      <div class="row col-9">
        <div class="q-ml-md row col-12">
          <v-md-editor
            v-model="content"
            height="400px"
            left-toolbar="undo redo clear | h bold italic strikethrough quote | ul ol table hr | link image code video "
            :disabled-menus="[]"
            :toolbar="toolbar"
            @upload-image="handleUploadImage"
          >
          </v-md-editor>
        </div>
      </div>
    </div>

    <!-- 제출 버튼 -->
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
              style="width: 200px"
              class="q-mb-xl"
              @click="createBigComment"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { createQnaBigComment } from '@/api/qna';

export default {
  props: {
    info: Object,
  },
  data() {
    return {
      content: '',
      toolbar: {
        video: {
          title: '비디오',
          // TODO : icon 변경하기
          icon: 'v-md-icon-toc',
          action(editor) {
            editor.insert(function() {
              const imagetxt = 'Image text';
              const image = 'Screenshot image URL';
              const youtube = 'Youtube Link';

              return {
                text: `[![${imagetxt}](${image})](${youtube})`,
                selected: imagetxt,
              };
            });
          },
        },
      },
    };
  },
  methods: {
    async createBigComment() {
      if (this.content === '') {
        alert('댓글 내용을 작성해주세요.');
      }
      try {
        this.$q.loading.show();
        await createQnaBigComment({
          // 넘길 데이터
          user: this.$store.state.id,
          content: this.content,
          qna: this.info.post_id,
        });
        location.reload();
        // QnA 게시판으로 이동
        // this.$router.push({ path: `/qna-detail/${this.info.post_id}` });
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    handleUploadImage(event, insertImage, files) {
      // Get the files and upload them to the file server, then insert the corresponding content into the editor
      console.log(files);
      console.log(insertImage);
      // Here is just an example
      insertImage({
        url: URL.createObjectURL(files[0]),
        desc: 'desc',
        // width: 'auto',
        // height: 'auto',
      });
    },
  },
};
</script>

<style scoped></style>
