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
        <div class="text-grey-4">
          Ctrl+S를 통해서 입력한 내용을 미리 보기할 수 있습니다
        </div>
        <!-- 마크다운 에디터 -->
        <div class="row full-width">
          <div class="col-6">
            <v-md-editor
              v-model="content"
              height="800px"
              left-toolbar="undo redo clear | h bold italic strikethrough quote | ul ol table hr | link image code video | save"
              right-toolbar=""
              :disabled-menus="['undo']"
              :toolbar="toolbar"
              mode="edit"
              @upload-image="handleUploadImage"
              @save="renderPreview"
            >
            </v-md-editor>
          </div>

          <q-scroll-area
            :thumb-style="thumbStyle"
            :bar-style="barStyle"
            class="col-6  preview-shadow q-py-lg"
            style="height:800px; "
          >
            <v-md-editor
              v-model="translation"
              mode="preview"
              class="col-6"
            ></v-md-editor>
          </q-scroll-area>
        </div>
      </div>
      <!-- 버튼 -->
      <div class="q-mb-xl q-mt-xl" style="text-align: center;">
        <slot
          name="buttons"
          :createQna="createQna"
          :updateQna="updateQna"
          :deleteQna="deleteQna"
        ></slot>
      </div>
    </div>
  </div>
</template>

<script>
import { filtered_tags, first_matched_tag } from '@/utils/autoComplete';
import { liquidResolver } from '@/utils/liquidTag';
import {
  createQnaItem,
  saveQnaImage,
  loadQnaImage,
  updateQnaItem,
  deleteQnaItem,
  loadQnaItem,
} from '@/api/qna';
export default {
  data() {
    return {
      thumbStyle: {
        right: '4px',
        borderRadius: '5px',
        backgroundColor: '#dddddd',
        width: '6px',
        opacity: 0.75,
      },

      barStyle: {
        right: '2px',
        borderRadius: '9px',
        backgroundColor: '#dddddd',
        width: '7px',
        opacity: 0.2,
      },
      user: '',
      profile: '',
      title: '',
      tagItem: '',
      content: '',
      translation: '',
      ref_tags: [],
      img: '',
      imgUrl: 'https//',
      tags: { ...this.$store.state.tags_selected },
      toolbar: {
        video: {
          title: '비디오',
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
        await createQnaItem({
          title: this.title,
          user: this.$store.state.id,
          content: this.content,
          img: this.img.length ? this.img : null,
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
    renderPreview(text) {
      this.translation = liquidResolver(text);
    },
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
    // TODO: img 폼데이터로 연결해서 전송
    async handleUploadImage(event, insertImage) {
      const frm = new FormData();
      frm.append('img', event.target.files[0]);
      try {
        await saveQnaImage(frm);
        // 이미지 url 받아오기
        const { data } = await loadQnaImage();
        this.imgUrl = this.imgUrl + data.imgUrl;
      } catch (error) {
        console.log(error);
      }
      // Here is just an example
      insertImage({
        url: this.imgUrl,
        desc: 'file_name',
        // responseType: 'blob',
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
  async created() {
    // update의 경우에만 해당 됨
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
