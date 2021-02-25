<template>
  <div class="row col-12">
    <!-- 댓글 시작 -->
      <div class="row col-12">
        <!-- <div class="row col-12" v-for="(data, index) in info" :key="index"> -->
        <div class="row col-2">
          <!-- 댓글 좋아요 수, 댓글 수, 북마크 수 -->
          <div class="row col-9"></div>
        </div>
        <div class="row col-10">
          <div class="row col-9">
            <div class="text-h6 text-weight-bold q-mb-md">댓글 목록({{ contents.comment_set.length }}개)</div>
            <q-card flat bordered class="my-card q-pa-lg q-mb-xl row col-12">
              <div v-if="contents.comment_set.length === 0" class="full-width text-center text-grey-7">
                댓글이 없습니다.
              </div>
              <div v-for="(data, index) in info" :key="index" class="row col-12">
                <div class="row col q-mt-lg">
                  <div class="row col-11 q-mb-md">
                    <div class="q-pr-sm q-pt-xs">
                      <span class="cursor-pointer q-ml-sm">
                        <q-avatar size="lg"
                          ><img src="https://cdn.quasar.dev/img/avatar.png" />
                        </q-avatar>
                      </span>
                    </div>
                      
                    <div>
                      <div class="text-body1 text-weight-bold">{{
                        data.user.username
                      }}</div>
                      <div class="text-caption" style="color: gray">{{
                        data.written_time | moment('YYYY/MM/DD HH:mm')
                      }}</div>
                    </div>
                  </div>
                  <!-- 좋아요 로직 -->
                  <div class="q-ml-lg justify-end">
                    <template v-if="contents.comment_set[index].liked_comment">
                      <q-icon
                        :name="$i.ionHeart"
                        color="red"
                        size="20px"
                        class="cursor-pointer"
                        @click="checkLiked(index)"
                      ></q-icon>
                    </template>
                    <template v-else>
                      <q-icon
                        :name="$i.ionHeartOutline"
                        style="color:#727272"
                        size="20px"
                        class="cursor-pointer"
                        @click="checkLiked(index)"
                      ></q-icon>
                    </template>
                    <span class="q-ml-sm q-mt-md">{{ contents.comment_set[index].like_comment_num }}</span>
                    <br />
                    <br />
                  </div>
                </div>

                <div v-if="data.user.id == $store.state.id" class="row justify-end q-pt-md">
                  <div>
                    <q-btn flat round dense icon="more_vert">
                      <q-menu>
                        <q-list style="min-width: 100px">
                          <q-item
                            clickable
                            v-close-popup
                            @click="editerOpen(index)"
                          >
                            <q-item-section>수정하기</q-item-section>
                          </q-item>
                          <q-item
                            clickable
                            v-close-popup
                            @click="deleteComment(index)"
                          >
                            <q-item-section>삭제하기</q-item-section>
                          </q-item>
                        </q-list>
                      </q-menu>
                    </q-btn>
                  </div>
                </div>
          

                <div class="q-py-xs row col-12" v-if="modes[index] == 'editable'">
                  <q-input
                    clearable
                    type="textarea"
                    v-model="data.comment_content"
                    class="full-width q-pa-none q-mb-lg"
                    color="blue-10"
                    dense
                    autogrow
                    borderless
                    @keypress.enter="
                      updateComment(index)
                    "
                  />
                </div>
                <pre class="q-py-xs row col-12 q-mb-lg q-ml-sm" v-else>{{
                  data.comment_content
                }}</pre>
                <q-separator v-if="contents.comment_set.length !== index + 1" inset />
              </div> 
            </q-card>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import ForumCommentStatus from '@/components/forum/ForumCommentStatus';
import {
  loadForumItem,
  updateForumComment,
  deleteForumComment,
  toggleForumCommentLike,
} from '@/api/forum';
import { liquidResolver } from '@/utils/liquidTag';

export default {
  props: {
    info: Array,
  },
  components: {
    ForumCommentStatus,
  },
  data() {
    const res = [];
    for (const i in this.info) res.push('preview');
    this.modes = res;
    return {
      contents: '',
      content: '',
      modes: res,
      liked_comment: '',
      like_comment_num: '',
    };
  },
  methods: {
    // 북마크 토글하기
    async checkLiked(index) {
      // 로그인 확인
      if (!this.$store.getters.isLogined) {
        alert('로그인이 필요합니다');
        return;
      }
      try {
        await toggleForumCommentLike(this.contents.comment_set[index].id);
        // 넘겨줄 데이터
        this.contents.comment_set[index].liked_comment = !this.contents.comment_set[index].liked_comment;
        if (this.contents.comment_set[index].liked_comment) {
          this.contents.comment_set[index].like_comment_num = this.contents.comment_set[index].like_comment_num + 1;
        } else {
          this.contents.comment_set[index].like_comment_num = this.contents.comment_set[index].like_comment_num - 1;
        }
      } catch (error) {
        console.log(error);
      }
    },

    liquidResolve(tag) {
      return liquidResolver(tag);
    },
    getContents(fetchData, data) {
      fetchData.comment_content = data;
    },
    editerOpen(index) {
      this.modes[index] = 'editable';
      this.modes = [...this.modes];
    },
    async updateComment(index) {
      if (this.contents === '') {
        alert('내용은 필수 입력항목 입니다');
      }
      try {
        const comment_pk = this.info[index].id;
        const postId = this.info[index].post;
        this.modes[index] = 'preview';
        this.modes = [...this.modes];
        this.$q.loading.show();
        await updateForumComment(comment_pk, {
          comment_content: this.info[index].comment_content,
          post: this.contents.id,
          user: this.contents.user.id,
        });
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    async deleteComment(index) {
      try {
        this.$q.loading.show();
        const comment_pk = this.info[index].id;
        await deleteForumComment(comment_pk);
        location.reload();
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  async created() {
    const index = this.$route.params.id;
    try {
      const { data } = await loadForumItem(index);
      this.contents = data;
      this.author = data.user.id;
    } catch (error) {
      console.log(error);
    }
  },
};
</script>

<style scoped>
.icon-position {
  float: right;
}
</style>
