<template>
  <div style="margin-bottom: 70px;">
    <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">Connect with SNS</div>
    <div>
      <label for="github">Github Account <q-icon :name="$i.ionLogoGithub"></q-icon></label>
      <q-input 
        outlined 
        v-model="github"
        id="github"
        placeholder="Github 계정을 입력해주세요" 
        style="width:730px; margin: 7px 0 30px 0;"
        :dense="dense" 
      />
    </div>
    <div>
      <label for="facebook">Facebook Account <q-icon :name="$i.ionLogoFacebook"></q-icon></label>
      <q-input 
        outlined 
        v-model="facebook"
        id="facebook"
        placeholder="Facebook 계정을 입력해주세요" 
        style="width:730px; margin: 7px 0 30px 0;"
        :dense="dense" 
      />
    </div>
    <div>
      <label for="linkedin">LinkedIn Account <q-icon :name="$i.ionLogoLinkedin"></q-icon></label>
      <q-input 
        outlined 
        v-model="linkedin"
        id="linkedin"
        placeholder="LinkedIn 계정을 입력해주세요" 
        style="width:730px; margin: 7px 0 30px 0;"
        :dense="dense" 
      />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      github: '',
      facebook: '',
      linkedin: '',
    }
  }
}
</script>

<style>

</style>