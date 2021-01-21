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
        <div class="col-4 row justify-center items-center" style="height:100%">
          <q-btn
            no-caps
            color="primary"
            id="follow-btn"
            label="Follow"
            style="width:90px;"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToProfile() {
      console.log('click!');
      this.$router.push({ name: 'Profile' });
    },
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
