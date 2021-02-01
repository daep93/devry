<template>
  <div class="q-pa-md q-gutter-sm row">
    <q-card flat bordered class="col">
      <!-- 제목 입력 -->
      <q-input 
        class="q-mx-md q-my-md text-h4 text-weight-bold" 
        borderless 
        v-model="title" 
        placeholder="제목을 입력해주세요"  
        :rules="[ val => val && val.length > 0 || '제목은 필수항목 입니다']"
      />
      <!-- 태그 입력 -->
      <q-input
        class="q-mx-md"
        borderless 
        v-model="tagItem"
        placeholder="태그를 하나 이상 입력해주세요" 
        TODO
        :rules="[ propsTagData.length > 0 || '반드시 하나 이상의 태그를 입력해주세요']"
        @keypress.enter="createTag"
      />
      <ul class="row">
        <li class="q-ml-sm cursor-pointer" v-for="(tag, index) in propsTagData" :key="index">
          <q-chip outline square color="primary">
            <div @click="removeTag(tag, index)">{{ tag }}</div>
          </q-chip>
        </li>
      </ul>  
      <!-- 입력 폼 -->
      <q-editor 
        v-model="editor" 
        min-height="50rem" 
        placeholder="내용을 입력해주세요" 
        TODO
        :rules="[ val => val && val.length > 0 || '반드시 하나 이상의 태그를 입력해주세요']"
        :definitions="{
          link: {
            tip: 'Link your Url',
            icon: 'link',
            handler: link
          },
          image: {
            tip: 'Upload your Image',
            icon: 'insert_photo',
            handler: uploadIt
          }
        }"
        :toolbar="[
          [{
            label: $q.lang.editor.formatting,
            icon: $q.iconSet.editor.formatting,
            list: 'no-icons',
            options: ['p', 'h3', 'h4', 'h5', 'h6', 'code']
          }],
          ['bold', 'italic', 'strike', 'underline'],
          ['image', 'link']
        ]">
        <pre style="white-space: pre-line"></pre>
      </q-editor>
    </q-card>
    <!-- 미리보기 화면 -->
    <q-card flat filled class="col bg-grey-3">
      <q-card-section class="text-h4 text-weight-bold q-mx-sm q-my-lg" v-html="title" />
      <ul class="row q-ml-md">
        <li class="q-mr-sm cursor-pointer" v-for="(tag, index) in propsTagData" :key="index">
          <q-chip outline square color="primary">
            {{ tag }}
          </q-chip>
        </li>
      </ul>
      <q-card-section class="q-mx-sm" v-html="editor" />
    </q-card>
  </div>
</template>

<script>
export default {
  props: ['propsTagData'],
  data () {
    return {
      title: '',
      tagItem: '',
      editor: '',
    }
  },
  methods: {
    createTag: function() {
      if (this.tagItem !== '') {
        this.$emit('addTagItem', this.tagItem);
        this.tagItem = ''
      }
    },
    removeTag: function(tagItem, index) {
      // console.log("삭제?")
      this.$emit('removeTagItem', tagItem, index);
    },
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>