<template>
  <div>
    <q-card
      flat
      bordered
      class="my-card row col-12 q-pa-sm q-mb-sm"
      style="max-width: 250px; max-height: 280px;"
    >
      <q-card-section>
        <div class="row col-12">
          <div class="row col-2">
            <span class="q-mt-xs">
              <q-avatar
                @click="goToProfile"
                style="width: 35px; height: 35px;"
                class="cursor-pointer"
                ><img :src="profile_img" />
              </q-avatar>
            </span>
          </div>
          <div class="row col-10">
            <div class="row col-12">
              <div
                class="q-pl-lg"
                style="font-size: 15px; color: #464646"
                @click="goToProfile"
              >
                <b class="cursor-pointer">{{
                  profile ? profile.username : info.user.username
                }}</b>
                <div class="text-caption row">
                  글 ?? · 팔로워 {{ follower_num }}
                  <!-- 글 {{ info.profile ? profile.post_num : 0 }} · 팔로워
                  {{ profile ? profile.follow_num : 0 }} -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </q-card-section>
      <div class="q-px-md q-pb-md" v-if="profile">
        <div style="font-size: 13px;">
          {{ info.profile.bio }}
        </div>
      </div>
      <div
        class="row col-12 justify-center"
        v-if="info.profile.user != $store.state.id"
      >
        <template v-if="is_following">
          <q-btn
            no-caps
            outline
            color="primary"
            label="Following"
            @click="checkFollow"
            class="q-mb-sm row col-10"
          />
        </template>
        <template v-else>
          <q-btn
            no-caps
            color="primary"
            id="follow-btn"
            label="Follow"
            @click="checkFollow"
            class="q-mb-sm row col-10"
          />
        </template>
      </div>
    </q-card>
    <q-card
      flat
      bordered
      class="my-card row col-12 q-px-sm q-pt-md"
      style="max-width: 250px; max-height: 280px;"
      v-if="info.profile.pinned_posts"
    >
      <div class="q-px-md q-pb-sm">
        <div style="font-size: 13px;">
          <div class="q-my-sm">
            <span
              class="text-weight-bold cursor-pointer"
              style="color: #598FFC"
              >{{ info.profile.username }}</span
            >
            <span>님의 글 더보기</span>
          </div>
          <template v-for="post in info.profile">
            <q-separator :key="post.pinned_posts" />
            <div class="q-my-sm" :key="post.pinned_posts">
              {{ post.pinned_posts }}
            </div>
          </template>

          <q-separator />
        </div>
      </div>
    </q-card>
  </div>
</template>

<script>
import { checkQnaFollowing } from '@/api/qna';

export default {
  props: {
    info: Object,
  },
  data() {
    return {
      title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      username: 'Test User',
      profile_img: 'https://cdn.quasar.dev/img/avatar.png',
      is_following: this.info.is_following,
      follower_num: this.info.user.follower_num,
    };
  },
  methods: {
    async checkFollow() {
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
      try {
        await checkQnaFollowing(this.info.post_id);
        this.is_following = !this.is_following;
        if (this.is_following) {
          this.follower_num = this.follower_num + 1;
        } else {
          this.follower_num = this.follower_num - 1;
        }
      } catch (error) {
        console.log(error);
      }
    },
    goToProfile() {
      this.$router.push(`/profile/${this.info.profile.user}`);
    },
  },
  computed: {
    profile() {
      return this.info.profile;
    },
  },
};
</script>

<style scoped></style>
