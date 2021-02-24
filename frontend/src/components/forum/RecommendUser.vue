<template>
  <infinite-slide-bar
    class="row full-width q-pa-sm items-center"
    style="border: 2px solid #ECEFF1;border-radius: 8px; height:300px;"
    duration="50s"
  >
    <div class="row full-width items-center" style="height:250px">
      <q-card
        v-for="profile in filtered_profiles"
        style="width:200px"
        :key="profile.user_id"
        class="q-mx-xs"
      >
        <div class="row full-width justify-center q-my-sm">
          <q-avatar style="border: 1px solid #ECEFF1" size="10.0em">
            <q-img
              :src="
                profile.profile_img
                  ? profile.profile_img
                  : require('@/assets/basic_image.png')
              "
              style="height:2em"
            />
          </q-avatar>
        </div>
        <div
          class="row full-width justify-center q-mb-sm"
          style="font-size:1.3em"
        >
          @{{ profile.username }}
        </div>
        <div class="row justify-center q-mb-md">
          <q-btn
            color="primary"
            label="follow"
            class="col-8"
            @click="goToProfile(profile.user_id)"
          />
        </div>
      </q-card>
    </div>
  </infinite-slide-bar>
</template>

<script>
import { getProfiles } from '@/api/profile';
import InfiniteSlideBar from 'vue-infinite-slide-bar';
export default {
  components: {
    InfiniteSlideBar,
  },
  data() {
    return {
      profiles: [],
      unit: 10,
      cur: 1,
      max: 1,
    };
  },
  computed: {
    filtered_profiles() {
      return this.profiles.filter(
        profile => profile.user_id != this.$store.state.id,
      );
    },
  },
  created() {
    // 사용자들을 불러온다.
    this.loadProfiles();
  },
  methods: {
    async loadProfiles() {
      try {
        const { data } = await getProfiles();
        this.profiles = data;
        this.max = Math.ceil(data.length / this.unit);
      } catch (error) {
        console.log(error);
      }
    },
    goToProfile(id) {
      this.$router.push(`/profile/${id}/`);
    },
  },
};
</script>

<style scoped>
.vifnslb-container >>> .vifnslb-element {
  width: auto;
  min-width: none;
}
</style>
