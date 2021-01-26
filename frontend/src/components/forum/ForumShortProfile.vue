<template>
  <div>
    <div style="margin-top: 16px;">
      <q-card flat bordered class="my-card" style="padding: 10px;">
        <q-card-section>
          <span style="cursor: pointer;">
            <q-avatar @click="goToProfile" style="width: 35px; height: 35px;"
              ><img :src="profile_img" />
            </q-avatar>
          </span>
          <span style="margin-left: 12px; font-size: 17px;">{{
            username
          }}</span>
        </q-card-section>
        <q-card-section>
          <div v-if="follow">
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
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      username: 'test user',
      profile_img: 'https://cdn.quasar.dev/img/avatar.png',
      follow: true,
    };
  },
  methods: {
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
    checkFollow() {
      this.follow = !this.follow;
    },
  },
};
</script>

<style scoped></style>
