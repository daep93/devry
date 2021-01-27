<template>
  <div>
    <q-card flat bordered class="my-card" style="padding: 40px; width: 800px;">
      <div class="q-pt-none row">
        <div class="col-2" style="width: 50px; margin-right: 5px;">
          <span style="cursor: pointer;">
            <q-avatar @click="goToProfile" style="width: 35px; height: 35px;"
              ><img src="https://cdn.quasar.dev/img/avatar.png" />
            </q-avatar>
          </span>
        </div>
        <div class="col-10">
          <span>
            <q-input
              outlined
              v-model="text"
              :dense="dense"
              style="width: 660px;"
              placeholder="댓글을 입력해주세요"
            />
          </span>
        </div>
      </div>
      <q-card-section style="margin-right: -12px;">
        <div class="icon-position">
          <q-btn
            no-caps
            color="grey"
            id="follow-btn"
            label="Cancel"
            style="width:85px;"
          />
          <q-btn
            no-caps
            color="primary"
            id="follow-btn"
            label="Submit"
            style="width:85px; margin-left: 10px;"
          />
        </div>
      </q-card-section>
      <div style="margin-top: 50px;">
        <div class="q-pt-none row" v-for="n in 3" :key="n">
          <div class="col-2" style="width: 50px; margin-right: 5px;">
            <span style="cursor: pointer;">
              <q-avatar @click="goToProfile" style="width: 35px; height: 35px;"
                ><img :src="profile_img" />
              </q-avatar>
            </span>
          </div>
          <div class="col-10">
            <!-- 댓글 -->
            <span>
              <q-card
                flat
                bordered
                class="my-card"
                style="width: 660px; height: 100px; padding: 18px;"
              >
                <span>{{ username }}</span>
                <span style="margin-left: 10px; font-size: 5px;">7분 전</span>
                <div class="icon-position">
                  <q-icon
                    :name="$i.ionHeartOutline"
                    style="color:#727272"
                    size="22px"
                    class="q-mr-sm"
                  ></q-icon>
                  <span style="margin-right: 20px;">17 likes</span>
                  <q-icon
                    :name="$i.ionChatboxEllipsesOutline"
                    style="color:#727272"
                    size="22px"
                    class="q-mr-sm"
                  ></q-icon>
                  <span style="margin-right: 20px;">Reply</span>
                </div>
                <!-- 댓글 내용 -->
                <div style="padding-top: 5px;">댓글 내용</div>
              </q-card>
              <br />
            </span>
          </div>
        </div>
      </div>
    </q-card>
  </div>
</template>

<script>
export default {
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
