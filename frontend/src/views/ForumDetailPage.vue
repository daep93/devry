<template>
  <div class="row">
    <div class="justify-center col-md-9" style="width: 900px; height: 600px;">
      <div class="q-pa-md row items-start q-gutter-md">
        <q-card flat bordered class="my-card" style="padding: 10px;">
          <q-card-section>
            <div class="text-h4">
              <b>{{ title }}</b>
            </div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <span style="cursor: pointer;">
              <q-avatar @click="goToProfile" style="width: 35px; height: 35px;"
                ><img :src="profile_img" />
              </q-avatar>
            </span>
            <span style="margin-left: 12px; font-size: 17px;">{{
              username
            }}</span>
            <span style="font-size: 10px; margin-left: 7px;"> 7시간 전</span>
          </q-card-section>
          <br />
          <q-card-section class="q-pt-none">
            <div v-for="i in 3" :key="i">
              <span class="icon-position" style="margin-left: 10px;">
                <q-badge color="blue">
                  # Vue
                </q-badge>
              </span>
            </div>
          </q-card-section>
          <br />
          <q-card-section class="q-pt-none">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem
            ipsum, dolor sit amet consectetur adipisicing elit. Eveniet est
            voluptatem eius sunt. Dicta assumenda et fugiat cumque similique
            nesciunt qui labore earum blanditiis, alias quam dignissimos culpa.
            Cupiditate tempore facilis laudantium enim perferendis, tenetur
            nobis fugiat necessitatibus doloremque eaque quidem, quisquam nihil
            aut. Neque asperiores tempora quos consequuntur eaque architecto
            quas nemo molestias quam tempore magnam necessitatibus, quidem
            tenetur aliquam officiis cumque? Eveniet enim accusantium doloribus
            delectus vitae totam itaque modi magni possimus aspernatur, eligendi
            nesciunt laborum voluptatum. Tempora accusamus tenetur blanditiis
            magnam et, atque cupiditate, officia libero adipisci impedit
            praesentium, iure nam eius. Illo deleniti atque suscipit veritatis?
          </q-card-section>
        </q-card>
      </div>
    </div>

    <div class="col-md-3">
      <ForumShortProfile></ForumShortProfile>
    </div>
  </div>
</template>

<script>
import ForumShortProfile from '@/components/forum/ForumShortProfile';

export default {
  components: {
    ForumShortProfile,
  },
  data() {
    return {
      title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      username: 'test user',
      profile_img: 'https://cdn.quasar.dev/img/avatar.png',
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
