<template>
  <div>
    <div v-for="(data, index) in followeeData" :key="index" class="q-pa-xs">
      <!-- 이 영역 반복 -->
      <div class="q-pa-md row col-align" style="height:80px;">
        <!-- <div class="q-pa-md row col-align" style="height:100%"> -->
        <!-- follow 유저 정보 -->
        <div class="col-8 row" style="height:100%">
          <q-list style="min-width:300px; margin-left: 30px;">
            <!-- <q-list bordered style="min-width:300px; margin-left: 30px;"> -->
            <q-item>
              <!-- <q-item clickable v-ripple> -->
              <q-item-section avatar>
                <a href="javascript:;" @click="goToProfile">
                  <q-avatar> <img :src="data.profile_img" /> </q-avatar
                ></a>
              </q-item-section>
              <q-item-section>
                <span>
                  <a
                    href="javascript:;"
                    @click="goToProfile"
                    class="change-tag-color"
                  >
                    <b style="font-size: 15px;">{{ data.id }}</b></a
                  ></span
                >
                <span
                  >글 {{ data.post_num }} · 팔로워 {{ data.follower_num }}</span
                >
              </q-item-section>
            </q-item>
          </q-list>
        </div>
        <!-- follow 버튼 -->
        <div class="col-4 row justify-center items-center" style="height:100%">
          <div v-if="data.follow">
            <q-btn
              no-caps
              color="primary"
              id="follow-btn"
              label="Follow"
              style="width:90px;"
              @click="checkFollow(index)"
            />
          </div>
          <div v-else>
            <q-btn
              no-caps
              outline
              color="primary"
              label="Following"
              style="width:90px;"
              @click="checkFollow(index)"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getFollowee, unfollowFollowee, followingUser } from '@/api/follow';

export default {
  data() {
    return {
      followeeData: [
        {
          id: '유저',
          profile_img: 'https://cdn.quasar.dev/img/boy-avatar.png',
          follower_num: 50,
          post_num: 10,
          is_following: 30,
          follow: true,
        },
        {
          id: '유저2',
          profile_img: 'https://cdn.quasar.dev/img/avatar.png',
          follower_num: 22,
          post_num: 6,
          is_following: 60,
          follow: false,
        },
        {
          id: '유저3',
          profile_img: 'https://cdn.quasar.dev/img/boy-avatar.png',
          follower_num: 22,
          post_num: 6,
          is_following: 60,
          follow: true,
        },
        {
          id: '유저4',
          profile_img: 'https://cdn.quasar.dev/img/avatar.png',
          follower_num: 22,
          post_num: 6,
          is_following: 60,
          follow: true,
        },
        {
          id: '유저5',
          profile_img: 'https://cdn.quasar.dev/img/boy-avatar.png',
          follower_num: 2,
          post_num: 6,
          is_following: 6,
          follow: true,
        },
        {
          id: '유저6',
          profile_img: 'https://cdn.quasar.dev/img/boy-avatar.png',
          follower_num: 2,
          post_num: 6,
          is_following: 6,
          follow: true,
        },
        {
          id: '유저7',
          profile_img: 'https://cdn.quasar.dev/img/boy-avatar.png',
          follower_num: 2,
          post_num: 6,
          is_following: 6,
          follow: true,
        },
      ],
    };
  },
  methods: {
    checkFollow(index) {
      for (const btn of this.followeeData) {
        if (this.followeeData.indexOf(btn) === index) {
          btn.follow = !btn.follow;
        }
      }
    },
    goToProfile() {
      console.log('click!');
      this.$router.push({ name: 'Profile' });
    },
    async unfollowMyFollowee() {
      try {
        await unfollowFollowee();
      } catch (error) {
        console.log(error);
      }
    },
    async followUser() {
      try {
        await followingUser();
      } catch (error) {
        console.log(error);
      }
    },
  },
  async created() {
    const unit = 10;
    // 단위 시작 위치
    const unit_index = 1;
    const unitData = { unit, unit_index };
    try {
      const { data } = await getFollowee(unitData);
      this.followerData.push(data);
    } catch (error) {
      console.log(error);
    }
  },
};
</script>

<style scoped>
.col-align {
  display: flex;
  align-items: center;
}
.change-tag-color {
  text-decoration: none;
  color: #000000;
}
</style>
