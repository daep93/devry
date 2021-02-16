<template>
  <div class="q-pa-md q-gutter-sm row justify-center">
    <div class="q-pa-sm" style="width: 85vw;">
      <div class="q-pa-md q-gutter-sm">
        <!-- 제목 입력 -->
        <q-input
          class=" q-my-md text-h4 text-weight-bolder"
          borderless
          v-model="title"
          placeholder="제목을 입력해주세요"
        />
        <!-- 태그 입력 -->
        <q-input
          borderless
          v-model="tagItem"
          placeholder="태그를 하나 이상 입력해주세요"
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
              @click="checkDuplicateTag(tag)"
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
        <markdown-editor
          :height="'800px'"
          :fetchData="content"
          @input="getContents"
        ></markdown-editor>
      </div>
      <!-- 버튼 -->
      <div class="q-mb-xl q-mt-xl" style="text-align: center;">
        <slot
          name="buttons"
          :createQna="createQna"
          :updateQna="updateQna"
          :deleteQna="deleteQna"
          :createForum="createForum"
        ></slot>
      </div>
    </div>
  </div>
</template>

<script>
import { filtered_tags, first_matched_tag } from '@/utils/autoComplete';
import MarkdownEditor from '@/components/common/MarkdownEditor';
import {
  createQnaItem,
  updateQnaItem,
  deleteQnaItem,
  loadQnaItem,
} from '@/api/qna';
import { createForumItem, loadForumItem } from '@/api/forum';
export default {
  components: {
    MarkdownEditor,
  },
  data() {
    return {
      user: '',
      profile: '',
      title: '',
      tagItem: '',
      content: '',
      ref_tags: [],
      img: '',
      imgUrl: 'https//',
      tags: { ...this.$store.state.tags_selected },
    };
  },
  methods: {
    // 마크다운 에디터에서 input 이벤트가 발생할 경우 데이터를 content에 저장한다.
    getContents(data) {
      this.content = data;
    },
    // QnA 포스트를 새롭게 생성한다.
    async createQna() {
      if (this.title === '') {
        alert('제목은 필수 입력 항목입니다');
        return;
      }
      if (this.ref_tags.length < 2) {
        alert('태그를 둘 이상 입력해주세요');
        return;
      }
      if (this.ref_tags.length > 4) {
        alert('태그를 넷 이하로 입력해주세요');
        return;
      }
      if (this.content === '') {
        alert('내용은 필수 입력항목 입니다');
        return;
      }

      try {
        this.$q.loading.show();
        console.log('problem');
        await createQnaItem({
          title: this.title,
          user: this.$store.state.id,
          content: this.content,
          ref_tags: this.ref_tags,
        });
        // 이전 페이지로 이동
        this.$router.go(-1);
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    // 기존의 QnA 포스트를 수정한다.
    async updateQna() {
      if (this.title === '') {
        alert('제목은 필수 입력 항목입니다');
        return;
      }
      if (this.ref_tags.length < 2) {
        alert('태그를 둘 이상 입력해주세요');
        return;
      }
      if (this.ref_tags.length > 4) {
        alert('태그를 넷 이하로 입력해주세요');
        return;
      }
      if (this.content === '') {
        alert('내용은 필수 입력항목 입니다');
        return;
      }
      try {
        // post_id 넘겨주기
        const post_id = this.$route.params.id;
        this.$q.loading.show();
        await updateQnaItem(post_id, {
          title: this.title,
          user: this.user.id,
          content: this.content,
          ref_tags: this.ref_tags,
        });
        // 이전 페이지로 이동
        this.$router.go(-1);
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    // 기존의 QnA 포스트를 삭제한다.
    async deleteQna() {
      try {
        const post_id = this.$route.params.id;
        this.$q.loading.show();
        await deleteQnaItem(post_id);
        // 이전 페이지로 이동
        this.$router.go(-1);
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },

    // Forum post 생성
    async createForum() {
      if (this.title === '') {
        alert('제목은 필수 입력 항목입니다');
        return;
      }
      if (this.ref_tags.length < 2) {
        alert('태그를 둘 이상 입력해주세요');
        return;
      }
      if (this.ref_tags.length > 4) {
        alert('태그를 넷 이하로 입력해주세요');
        return;
      }
      if (this.content === '') {
        alert('내용은 필수 입력항목 입니다');
        return;
      }
      try {
        this.$q.loading.show();
        await createForumItem({
          title: this.title,
          user: this.$store.state.id,
          content: this.content,
          ref_tags: this.ref_tags,
        });
        // 이전 페이지로 이동
        this.$router.go(-1);
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    // 태그 일부 입력시 정규 표현식을 통해 적합한 태그를 자동 등록해줌
    createTag() {
      if (this.tagItem !== '') {
        const str = first_matched_tag(this.tagItem);
        this.checkDuplicateTag(str);
      }
    },
    // 태그 중복 확인
    checkDuplicateTag(tag) {
      if (tag && this.ref_tags.indexOf(tag) < 0) {
        this.ref_tags.push(tag);
        this.tagItem = '';
      }
    },
    // 태그 삭제
    removeTag(tag, index) {
      this.ref_tags.splice(index, 1);
    },
  },
  computed: {
    // 일부 문자열을 받고 정규 표현식을 활용하여 비슷한 형태의 문자열 목록을 반환
    suggests() {
      return filtered_tags(this.tagItem);
    },
  },
  async created() {
    // update의 경우에만 기존의 data를 불러옴
    const post_id = this.$route.params.id;
    if (post_id) {
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
      } finally {
        this.$q.loading.hide();
      }
    }
  },
};
</script>
<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
.preview-shadow {
  box-shadow: 0 2px 12px 0 rgb(0 0 0 / 10%);
}
</style>
