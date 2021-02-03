<template>
  <div class="q-pa-md q-gutter-sm row justify-center">
    <div class="q-pa-sm" style="width: 80vw;">
      <!-- 타이틀 -->
      <div class="q-mb-md">
        <span class="text-h4 text-weight-bolder">QnA Registration</span>
        <p class="text-subtitle2 q-mt-md q-mb-xl">
          궁금하신 점을 질문해보세요:)
        </p>
      </div>
      <!-- 마크다운 에디터 -->
      <v-md-editor v-model="text" height="400px"></v-md-editor>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
import koKR from '@kangc/v-md-editor/lib/lang/ko-KR';

VMdEditor.lang.use('ko-KR', koKR);

VMdEditor.use(githubTheme);

Vue.use(VMdEditor);

export default {
  data() {
    return {
      text: '',
    };
  },
};
</script>

<style></style>
