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
            class="row col-3 bg-blue-1"
            style="position: absolute; z-index:999; border-radius: 5px;"
          >
            <div
              v-for="item in suggests"
              class="col-12 q-py-md q-px-md"
              :key="item"
            >
              {{ item }}
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
        <v-md-editor
          v-model="content"
          height="800px"
          left-toolbar="undo redo clear | h bold italic strikethrough quote ul ol table hr link image imageLink uploadImage video code save"
          :toolbar="toolbar"
        >
        </v-md-editor>
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
import { createQnaItem } from '@/api/qnaCreate';

import Vue from 'vue';
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
import koKR from '@kangc/v-md-editor/lib/lang/ko-KR';
import { filtered_tags } from '@/utils/autoComplete';
VMdEditor.lang.use('ko-KR', koKR);

VMdEditor.use(githubTheme);

Vue.use(VMdEditor);

export default {
  data() {
    const index = this.$route.params.id;
    this.toolbar = {
      video: {
        title: '비디오',
        // TODO : icon 변경하기
        icon: 'v-md-icon-tip',
        action(editor) {
          editor.insert(function(selected) {
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
    };
    return {
      index,
      profile: '',
      title: '',
      tagItem: '',
      content: '',
      ref_tags: [],
    };
  },
  methods: {
    createTag() {
      if (this.tagItem !== '') {
        const str =
          this.tagItem.charAt(0).toUpperCase() + this.tagItem.slice(1);
        this.ref_tags.push(str);
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
        console.log(this.$store.state.id);
        console.log(this.$store.state);

        this.$q.loading.show();
        await createQnaItem({
          // 넘길 데이터 적어주기
          title: this.title,
          user: this.$store.state.id,
          content: this.content,
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
  },
  computed: {
    isValid() {
      return this.tagItem === '' || this.ref_tags.length > 0;
    },
    suggests() {
      return filtered_tags(this.tagItem);
    },
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>
