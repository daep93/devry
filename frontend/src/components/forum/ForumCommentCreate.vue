<template>
  <div class="row col-12">
    <div class="row col-12 q-mt-md q-pr-md">
      <div class="row col-2"></div>
      <div class="row col-8 q-pr-xl">
        <div class="text-h6 text-weight-bold q-mb-md">댓글 작성하기</div>
        <v-md-editor
          v-model="content"
          height="300px"
          left-toolbar="undo redo clear | h bold italic strikethrough quote | ul ol table hr | link image code video "
          :disabled-menus="[]"
          :toolbar="toolbar"
          @upload-image="handleUploadImage"
        >
        </v-md-editor>
      </div>
      <div class="row col-2"></div>

      <!-- 제출 버튼 -->
      <div class="row col-9 q-mt-sm q-pl-xl">
        <div class="row col-3"></div>
        <div class="row col-9">
          <div class="row col-12 q-mb-xl justify-center">
            <div>
              <q-btn
                no-caps
                color="primary"
                label="댓글 작성하기"
                style="width: 200px"
                class="q-mb-xl q-mt-lg"
                @click="createBigComment"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
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
