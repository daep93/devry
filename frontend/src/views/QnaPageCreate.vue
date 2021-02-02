<template>
  <div class="q-pa-lg q-mt-sm row justify-center">
    <div class="q-pa-sm" style="width: 80vw;">
      <!-- 타이틀 -->
      <div class="q-mb-md">
        <span class="text-h4 text-weight-bolder">QnA Registration</span>
        <p class="text-subtitle2 q-mt-md q-mb-xl" >궁금하신 점을 질문해보세요:)</p>
      </div>
      <!-- QnA 입력 폼 -->
      <div class="q-pa-md q-gutter-sm row">
        <q-card flat bordered class="col">
          <!-- 제목 입력 -->
          <q-input 
            class="q-mx-md q-my-md text-h4 text-weight-bold" 
            borderless 
            v-model="title" 
            placeholder="제목을 입력해주세요"  
          />
          <!-- :rules="[ val => val && val.length > 0 || '제목은 필수항목 입니다']" -->
          <!-- 태그 입력 -->
          <q-input
            class="q-mx-md"
            borderless 
            v-model="tagItem"
            placeholder="태그를 하나 이상 입력해주세요" 
            TODO
            @keypress.enter="createTag"
          >
          <!-- :error="!isValid" -->
          <!-- :rules="[ ref_tags.length > 0 || '태그 필요!']" -->
            <!-- 태그 에러 -->
            <!-- <template v-slot:error>
              <p class="text-weight-bold">태그를 반드시 하나 이상 입력해주세요</p>
            </template> -->
          </q-input>
          <ul class="row">
            <li class="q-ml-sm cursor-pointer" v-for="(tag, index) in ref_tags" :key="index">
              <q-chip outline square color="primary">
                <div @click="removeTag(tag, index)">{{ tag }}</div>
              </q-chip>
            </li>
          </ul>  
          <!-- 입력 폼 -->
          <q-editor 
            v-model="contents" 
            min-height="50rem" 
            placeholder="내용을 입력해주세요" 
            :definitions="{
              link: {
                tip: 'Link your Url',
                icon: 'link',
              },
              image: {
                tip: 'Upload your Image',
                icon: 'insert_photo',
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
            <!-- TODO : 콘텐츠가 빈 값일 경우 에러 메시지를 띄워야 함  -->
            <!-- 콘텐츠 에러 -->
            <!-- <template v-slot:error>
              <p class="text-weight-bold">내용은 필수 항목입니다</p>
            </template> -->
          </q-editor>
        </q-card>
        <!-- 미리보기 화면 -->
        <q-card flat filled class="col bg-grey-3">
          <q-card-section class="text-h4 text-weight-bold q-mx-sm q-my-lg" v-html="title" />
          <ul class="row q-ml-md">
            <li class="q-mr-sm cursor-pointer" v-for="(tag, index) in ref_tags" :key="index">
              <q-chip outline square color="primary">
                {{ tag }}
              </q-chip>
            </li>
          </ul>
          <q-card-section class="q-mx-sm" v-html="contents" />
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
import { Notify } from 'quasar'

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
    }
  },
  methods: {
    createTag(tagItem) {
      if (this.tagItem !== '') {
        console.log(this.tagItem)
        this.ref_tags.push(this.tagItem)
        this.tagItem = ''
      }
    },
    removeTag(tag, index) {
      this.ref_tags.splice(index, 1)
    },
    // TODO : api 수정하기
    // qna 게시글 생성하기
    async submitQna() {
      if (this.title === '') {
      //   this.$q.notify({
      //   message: '제목을 입력해주세요',
      //   color: 'primary',
      // })
        alert('제목은 필수 입력 항목입니다')
      } 
      if (this.ref_tags.length === 0 ) {
        alert('태그를 하나이상 입력해주세요')
      } 
      if (this.contents === '') {
        alert('내용은 필수 입력항목 입니다')
      }
      try {
        console.log('성공!')
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
    isValid () {
      return this.tagItem === '' || this.ref_tags.length > 0
    },
    // isValidContent () {
    //   return this.content.length > 0
    // }
  },
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>