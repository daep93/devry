<template>
  <div class="q-pa-md" style="text-align: justify; margin-top: 50px;">
    <div class="justify-center" style="width: 730px; margin:0 auto;">
      <!-- 타이틀 -->
      <div style="margin-bottom: 40px;">
        <span class="text-h4 text-weight-bolder">Settings for </span>
        <span class="text-h4 text-weight-bolder text-primary">{{ username }}</span>
        <p class="text-subtitle2" style="margin-top: 10px;">회원정보 수정 페이지입니다 :)</p>
      </div>
      <!-- 입력 폼 -->
      <div>
        <q-form>
          <profile-setting-personal></profile-setting-personal>
          <profile-setting-sns></profile-setting-sns>
          <profile-setting-tech></profile-setting-tech>
          <profile-setting-project></profile-setting-project>
          <profile-setting-tag></profile-setting-tag>
          <!-- 버튼 -->
          <div class="row q-mb-md q-mt-md float-right" style="margin-bottom: 150px;">
            <q-btn
              color="primary"
              label="SAVE"
              style="width:200px; height:50px; border-radius:5px;"
              type="submit"
            />
          </div>
        </q-form>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileSettingPersonal from '@/components/profileSetting/ProfileSettingPersonal';
import ProfileSettingSns from '@/components/profileSetting/ProfileSettingSns';
import ProfileSettingTech from '@/components/profileSetting/ProfileSettingTech';
import ProfileSettingProject from '../components/profileSetting/ProfileSettingProject.vue';
import ProfileSettingTag from '@/components/profileSetting/ProfileSettingTag';

export default {
  components: { 
    ProfileSettingPersonal, 
    ProfileSettingSns, 
    ProfileSettingTech, 
    ProfileSettingProject, 
    ProfileSettingTag
  },
  data() {
    return {
      username: 'Emma'
    }
  }
  
};
</script>

<style scoped></style>
