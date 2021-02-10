<template>
  <div class="q-pa-md q-gutter-sm row justify-center">
    <div class="q-pa-sm" style="width: 85vw;">
      <div class="q-pa-md q-gutter-sm">
        <!-- 제목 입력 -->
        <q-input
          class="q-mx-md q-my-md text-h3 text-weight-bold"
          borderless
          v-model="title"
          placeholder="제목을 입력해주세요"
        />
        <!-- 태그 입력 -->
        <q-input
          class="q-mx-md"
          borderless
          v-model="tagItem"
          placeholder="태그를 하나 이상 입력해주세요"
          TODO
          @keypress.enter="createTag"
        >
        </q-input>
        <!-- 자동완성 -->
        <div class="row col-12">
          <div
            class="row col-3 bg-light-blue-1"
            style="position: absolute; z-index:999; border-radius: 5px;"
          >
            <div
              v-for="tag in suggests"
              class="col-12 q-py-md q-px-md"
              :class="{ 'bg-blue-3': tags[tag] }"
              :key="tag"
              @click="autoCreateTag(tag)"
              @mouseover="tags[tag] = true"
              @mouseout="tags[tag] = false"
            >
              {{ tag }}
            </div>
          </div>
        </div>
        <!-- 태그 보여주기 -->
        <ul class="row relative-position" style="">
          <li
            class="q-mb-xs cursor-pointer"
            v-for="(tag, index) in ref_tags"
            :key="index"
          >
            <q-chip outline square color="primary">
              <div @click="removeTag(tag, index)">{{ tag }}</div>
            </q-chip>
          </li>
        </ul>
        <!-- 마크다운 에디터 -->
        <form method="post" action="/qna/" enctype="multipart/form-data">
          <v-md-editor
            v-model="content"
            height="800px"
            left-toolbar="undo redo clear | h bold italic strikethrough quote | ul ol table hr | link image code video "
            :disabled-menus="[]"
            :toolbar="toolbar"
            @upload-image="handleUploadImage"
          >
          </v-md-editor>
        </form>
      </div>
      <!-- 버튼 -->
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
          @click="createQna"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { filtered_tags, first_matched_tag } from '@/utils/autoComplete';

import { createQnaItem, saveQnaImage, loadQnaImage } from '@/api/qna';

export default {
  data() {
    const index = this.$route.params.id;
    return {
      index,
      profile: '',
      title: '',
      tagItem: '',
      content: '',
      ref_tags: [],
      tags: { ...this.$store.state.tags_selected },
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
      img: [],
      imgUrl: '',
    };
  },
  methods: {
    createTag() {
      if (this.tagItem !== '') {
        const str = first_matched_tag(this.tagItem);
        if (str && this.ref_tags.indexOf(str) < 0) {
          this.ref_tags.push(str);
          this.tagItem = '';
        }
      }
    },
    autoCreateTag(tag) {
      if (tag && this.ref_tags.indexOf(tag) < 0) {
        this.ref_tags.push(tag);
        this.tagItem = '';
      }
    },
    removeTag(tag, index) {
      this.ref_tags.splice(index, 1);
    },
    // 게시글 생성하기
    async createQna() {
      if (this.title === '') {
        alert('제목은 필수 입력 항목입니다');
      }
      if (this.ref_tags.length === 0) {
        alert('태그를 하나이상 입력해주세요');
      }
      if (this.content === '') {
        alert('내용은 필수 입력항목 입니다');
      }
      try {
        if (this.img.length === 0) {
          this.img = null;
        }
        console.log(this.$store.state.id);
        console.log(this.$store.state);
        console.log(this.img);
        console.log(this.img);
        console.log('여기..?');

        this.$q.loading.show();
        await createQnaItem({
          // 넘길 데이터 적어주기
          title: this.title,
          user: this.$store.state.id,
          content: this.content,
          img: this.img,
          ref_tags: this.ref_tags,
        });
        console.log('페이지 이동 전까지 성공?');
        // 이동 시킬 페이지 적어주기(QnA 게시판으로 이동)
        this.$router.push({ path: '/qna' });
      } catch (error) {
        console.log(error);
        // alert('에러가 발생했습니다!')
      } finally {
        this.$q.loading.hide();
      }
    },
    async handleUploadImage(event, insertImage, files) {
      console.log(files);
      const file = event.target.files[0];
      console.log(file);
      this.img.push(file);
      // 파일 임시 서버에 저장하기
      try {
        await saveQnaImage({
          // 이미지 formData 서버에 넘겨주기
          img: this.img,
        });
        console.log('성공?');
        console.log(this.img);
        // 이미지 url 받아오기
        const { data } = await loadQnaImage();
        this.imgUrl = data.imgUrl;
      } catch (error) {
        console.log(error);
      }
      // Here is just an example
      insertImage({
        // 1. blob 데이터 출력하기
        // url : URL.createObjectURL(file),
        // 2. 서버에서 받아온 이미지 url 출력하기
        url: this.imgUrl,
        // 3. 파일명 출력하기
        // url : file.name,
        // 4. base64 출력하기
        // url: localStorage.getItem('imgUrl'),
        desc: '글 작성 시 ' + file.name + ' 이미지가 출력됩니다.',
        responseType: 'blob',
      });
    },
  },
  computed: {
    isValid() {
      return this.tagItem === '' || this.ref_tags.length > 0;
    },
    suggests() {
      return filtered_tags(this.tagItem);
    },
  },
  created() {
    this.$store.commit('offLeft');
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>
