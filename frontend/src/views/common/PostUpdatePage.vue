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
        <ul class="row">
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
          color="red-12"
          class="text-weight-bold q-px-xl q-py-sm q-mr-md"
          label="삭제하기"
          size="md"
          @click="deleteQna"
        />
        <q-btn
          color="blue-12"
          class="text-weight-bold q-px-xl q-py-sm"
          label="작성하기"
          size="md"
          @click="updateQna"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { loadQnaItem, updateQnaItem, deleteQnaItem } from '@/api/qna';

import Vue from 'vue';
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
import koKR from '@kangc/v-md-editor/lib/lang/ko-KR';
import { filtered_tags, all_tags } from '@/utils/autoComplete';
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
    };
    return {
      index,
      user: '',
      profile: '',
      title: '',
      tagItem: '',
      content: '',
      ref_tags: [],
      tags: all_tags,
    };
  },
  methods: {
    createTag() {
      if (this.tagItem !== '') {
        console.log(this.tagItem);
        this.ref_tags.push(this.tagItem);
        this.tagItem = '';
      }
    },
    autoCreateTag(tag) {
      this.ref_tags.push(tag);
      this.tagItem = '';
    },
    removeTag(tag, index) {
      this.ref_tags.splice(index, 1);
    },
    // qna 게시글 수정하기
    async updateQna() {
      if (this.title === '') {
        alert('제목은 필수 입력 항목입니다');
      }
      if (this.ref_tags.length === 0) {
        alert('태그를 하나이상 입력해주세요');
      }
      if (this.contents === '') {
        alert('내용은 필수 입력항목 입니다');
      }
      try {
        // post_id 넘겨주기
        const post_id = this.$route.params.id;
        this.$q.loading.show();
        await updateQnaItem(post_id, {
          // 넘길 데이터 적어주기
          title: this.title,
          user: this.user.id,
          content: this.content,
          ref_tags: this.ref_tags,
        });
        // 이동 시킬 페이지 적어주기(QnA 게시판으로 이동)
        this.$router.push({ path: '/qna' });
      } catch (error) {
        console.log(error);
        // alert('에러가 발생했습니다!')
      } finally {
        this.$q.loading.hide();
      }
    },
    async deleteQna() {
      try {
        const post_id = this.$route.params.id;
        this.$q.loading.show();
        await deleteQnaItem(post_id);
        // 이동 시킬 페이지 적어주기(QnA 게시판으로 이동)
        this.$router.push({ path: '/qna' });
      } catch (error) {
        console.log(error);
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
      const { data } = await loadQnaItem(post_id);
      this.user = data.user;
      this.profile = data.profile;
      this.title = data.title;
      this.content = data.content;
      this.ref_tags = data.ref_tags;
    } catch (error) {
      console.log(error);
      // alert('에러가 발생했습니다.)
    } finally {
      this.$q.loading.hide();
    }
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
