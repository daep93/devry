<template>
  <div class="q-pa-md q-gutter-sm row justify-center">
    <div class="q-pa-sm" style="width: 80vw;">
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
// import enUS from '@kangc/v-md-editor/lib/lang/en-US';

// VueMarkdownEditor.lang.use('en-US', enUS);

VMdEditor.use(githubTheme);

Vue.use(VMdEditor);

export default {
  data() {
    return {
      text: '',
    };
  },
  
}
</script>

<style>

</style>