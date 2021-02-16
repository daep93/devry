<template>
  <div class="row q-pa-md justify-center q-mt-md fu">
    <div class="row col-6">
      <!-- 타이틀 -->
      <div class="q-mb-md">
        <span class="text-h4 text-weight-bolder">Settings for </span>
        <span class="text-h4 text-weight-bolder text-primary">{{
          $store.state.nickname
        }}</span>
        <p class="text-subtitle2 q-mt-sm">
          회원정보 수정 페이지입니다 :)
        </p>
      </div>

      <!-- 입력 폼 -->
      <profile-setting-form
        v-if="profile_info.username"
        :info="profile_info"
      ></profile-setting-form>
    </div>
  </div>
</template>

<script>
import ProfileSettingForm from '@/components/profileSetting/ProfileSettingForm';
import { loadProfile } from '@/api/profileSetting';
export default {
  components: { ProfileSettingForm },
  data() {
    return {
      profile_info: {
        bio: '',
        email: '',
        group: '',
        link: [],
        my_tags: [],
        profile_img: null,
        project: [],
        region: '',
        tech_stack: [],
        username: '',
      },
    };
  },
  async created() {
    try {
      this.$q.loading.show();
      const { data } = await loadProfile(this.$store.state.id);
      const username = this.$store.state.nickname;

      this.profile_info.bio = data.bio;
      this.profile_info.email = data.email;
      this.profile_info.group = data.group;
      this.profile_info.link = data.link;
      this.profile_info.my_tags = data.my_tags;
      this.profile_info.profile_img = data.profile_img;
      this.profile_info.project = data.project;
      this.profile_info.region = data.region;
      this.profile_info.tech_stack = data.tech_stack;
      this.profile_info.username = username;
    } catch (error) {
      console.log(error);
    } finally {
      this.$q.loading.hide();
    }
  },
};
</script>

<style scoped></style>
