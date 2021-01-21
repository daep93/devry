<template>
  <div>
    <div v-for="n in 10" :key="n" class="q-pa-xs">
      <div class="q-pa-md row col-align" style="height:80px;">
        <!-- follow 유저 정보 -->
        <div class="col-8 row" style="height:100%">
          <q-list style="min-width:300px; margin-left: 30px;">
            <!-- <q-list bordered style="min-width:300px; margin-left: 30px;"> -->
            <q-item>
              <q-item-section avatar>
                <q-avatar>
                  <img src="https://cdn.quasar.dev/img/boy-avatar.png" />
                </q-avatar>
              </q-item-section>
              <q-item-section>
                <span>
                  <a
                    href="javascript:;"
                    @click="goToProfile"
                    class="change-tag-color"
                  >
                    <b style="font-size: 15px;">유저 이름</b></a
                  ></span
                >
                <span>글 0 · 팔로워 0</span>
              </q-item-section>
            </q-item>
          </q-list>
        </div>
        <!-- follow 버튼 -->
        <!-- <div class="col-4 row justify-center items-center" style="height:100%"> -->
        <div class="col-4 row justify-center items-center" style="height:100%">
          <div v-if="follow">
            <q-btn
              no-caps
              color="primary"
              id="follow-btn"
              label="Follow"
              style="width:90px;"
              @click="checkFollow"
            />
          </div>
          <div v-else>
            <q-btn
              no-caps
              outline
              color="primary"
              label="Following"
              style="width:90px;"
              @click="checkFollow"
            />
          </div>

          <!-- <q-btn
            no-caps
            color="primary"
            id="follow-btn"
            label="Follow"
            style="width:90px;"
          /> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getFollower, followFollower, unfollowFollower } from '@/api/follow';

export default {
  data() {
    return {
      followerData: [],
      follow: true,
    };
  },
  methods: {
    checkFollow() {
      this.follow = !this.follow;
    },
    goToProfile() {
      console.log('click!');
      this.$router.push({ name: 'Profile' });
    },
    async followMyFollower() {
      try {
        await followFollower();
      } catch (error) {
        console.log(error);
      }
    },
    async unfollowMyFollower() {
      try {
        await unfollowFollower();
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
      const { data } = await getFollower(unitData);
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

.container q-btn {
  background-color: green;
}

.container q-btn.selected {
  background-color: red;
}
</style>
