<template>
  <div class="row col-12">
    <!-- 댓글 시작 -->
    <div v-for="(n, index) in 3" :key="index" class="row col-12">
      <div class="row col-12">
        <!-- <div class="row col-12" v-for="(data, index) in info" :key="index"> -->
        <div class="row col-2">
          <!-- 댓글 좋아요 수, 댓글 수, 북마크 수 -->
          <div class="row col-9"></div>
          <div class="row col-3 q-mt-lg">
            <forum-comment-status></forum-comment-status>
          </div>
        </div>
        <div class="row col-10">
          <div class="row col-9">
            <q-card flat bordered class="my-card q-pa-lg q-mt-lg row col-12">
              <div class="row col-11 q-mt-sm">
                <div class="row col-12">
                  <div class="col-1">
                    <span class="cursor-pointer q-ml-sm">
                      <q-avatar size="lg"
                        ><img src="https://cdn.quasar.dev/img/avatar.png" />
                      </q-avatar>
                    </span>
                  </div>
                  <q-card flat bordered class="my-card col-11 q-pa-lg">
                    <span class="text-body1 text-weight-bold">유저이름</span>
                    <span class="q-ml-sm text-caption" style="color: gray"
                      >작성 시간</span
                    >
                    <div class="row col-12 q-mt-sm">
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                      Quam dolor amet ad modi doloribus veritatis a earum
                      repudiandae corporis enim, aspernatur doloremque, suscipit
                      accusamus debitis nesciunt voluptatibus nemo, libero illo
                      et ullam corrupti quas cumque magnam. Sed temporibus autem
                      dolor sunt commodi, fugiat consectetur, nobis dicta saepe,
                      suscipit aspernatur esse.
                    </div>
                  </q-card>
                </div>
              </div>

              <div class="row col-1 justify-end">
                <div>
                  <div>
                    <q-btn flat round dense icon="more_vert">
                      <q-menu>
                        <q-list style="min-width: 100px">
                          <q-item clickable v-close-popup>
                            <q-item-section>수정하기</q-item-section>
                          </q-item>
                          <q-item clickable v-close-popup>
                            <q-item-section>삭제하기</q-item-section>
                          </q-item>
                        </q-list>
                      </q-menu>
                    </q-btn>
                  </div>
                </div>
              </div>
            </q-card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ForumCommentStatus from '@/components/forum/ForumCommentStatus';

export default {
  components: {
    ForumCommentStatus,
  },
  data() {
    return {
      title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      username: 'test user',
      profile_img: 'https://cdn.quasar.dev/img/mountains.jpg',
    };
  },
  methods: {
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
  },
};
</script>

<style scoped>
.icon-position {
  float: right;
}
</style>
