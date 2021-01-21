<template>
  <div>
    <div v-for="n in 10" :key="n" class="q-pa-xs">
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
                <q-avatar>
                  <img src="https://cdn.quasar.dev/img/boy-avatar.png" />
                </q-avatar>
              </q-item-section>
              <q-item-section>
                <span><b style="font-size: 15px;">유저 이름 2</b></span>
                <span>글 0 · 팔로워 0</span>
              </q-item-section>
            </q-item>
          </q-list>
        </div>
        <!-- follow 버튼 -->
        <div class="col-4 row justify-center items-center" style="height:100%">
          <q-btn
            no-caps
            outline
            color="primary"
            label="Following"
            style="width:90px;"
          />
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
      followeeData: [],
    };
  },
  methods: {
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
</style>
