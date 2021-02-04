<template>
  <div class="row q-pa-md justify-center q-mt-md fu">
    <div class="row col-6">
      <!-- 타이틀 -->
      <div class="q-mb-md">
        <span class="text-h4 text-weight-bolder">Settings for </span>
        <span class="text-h4 text-weight-bolder text-primary">{{
          username
        }}</span>
        <p class="text-subtitle2 q-mt-sm">
          회원정보 수정 페이지입니다 :)
        </p>
      </div>

      <!-- 입력 폼 -->
      <profile-setting-form></profile-setting-form>
    </div>
  </div>
</template>

<script>
// import { loadProfile, updateProfile } from '@/api/profileSetting';
import ProfileSettingForm from '@/components/profileSetting/ProfileSettingForm';
export default {
  components: { ProfileSettingForm },
};
</script>

<style scoped></style>
