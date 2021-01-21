<template>
  <div class="q-pa-md" style="text-align: justify; margin-top: 50px;">
    <div class="justify-center" style="width: 60%; padding: 100px; margin:0 auto; background-color: white;">
      <!-- 타이틀 -->
      <div style="margin-bottom: 40px;">
        <span class="text-h4 text-weight-bolder">Settings for </span>
        <span class="text-h4 text-weight-bolder text-primary">{{ username }}</span>
        <p class="text-subtitle2" style="margin-top: 10px;">회원정보 수정 페이지입니다 :)</p>
      </div>
      <!-- 입력 폼 -->
      <div>
        <q-form @submit.prevent="submitForm">
          <div class="col-12" style="margin-bottom: 70px;">
            <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">Personal details</div>
            <!-- 프로필 이미지 -->
            <div class="row">
              <q-img
                :src="imageUrl"
                spinner-color="white"
                style="height: 140px; max-width: 150px; position: relative; margin-bottom: 40px;"
                class="rounded-borders"
              />
              <div style="margin-left:15px;">
                <div class="text-subtitle1">@{{ username }}</div>
                <div class="text-caption" style="color: gray;">{{ email }}</div>
                
                <!-- 이미지 업로드 -->
                <input ref="imageInput" type="file" hidden @change="onChangeImages">
                <q-btn @click="onClickImageUpload" round color="primary" style="position: relative; left: -40px; top: 60px;">
                  <q-icon :name="$i.ionCamera"></q-icon>
                </q-btn>  
                <span @click="onClickImageUpload" style="position: relative; left: -30px; top: 60px;">
                  {{ imageUrl === 'https://placeimg.com/500/300/nature' ? '선택된 파일 없음' : '이미지 업로드 성공'}}
                </span>
              </div>
            </div>
            <div class="col-12">
              <div class="row" style="display:flex; justify-content:space-between;">
                <div class="col-5 mr-3">
                  <label for="region">region</label>
                  <q-input 
                    outlined 
                    v-model="region"
                    id="region"
                    placeholder="지역을 입력해주세요" 
                    style="margin: 7px 0 30px 0;"
                    :dense="dense" 
                  />
                </div>
                <div class="col-6">
                  <label for="group">group</label>
                  <q-input 
                    outlined 
                    v-model="group"
                    id="group"
                    placeholder="소속을 입력해주세요" 
                    style="margin: 7px 0 30px 0;"
                    :dense="dense" 
                  />
                </div>
              </div>
              <div class="col-12">
                <label for="name">name</label>
                <q-input 
                  outlined 
                  v-model="username"
                  id="name"
                  placeholder="이름을 입력해주세요" 
                  style="margin: 7px 0 30px 0;"
                  :dense="dense" 
                />
              </div>
              <div class="col-12">
                <label for="bio">bio</label>
                <q-input
                  v-model="bio"
                  outlined
                  type="textarea"
                  placeholder="자기 소개를 입력해주세요" 
                  style="margin: 7px 0 30px 0;"
                />
              </div>
            </div>
          </div>
          <!-- sns 연동 -->
          <div class="col-12" style="margin-bottom: 70px;">
            <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">Connect with SNS</div>
            <div>
              <label for="github">Github Account <q-icon :name="$i.ionLogoGithub"></q-icon></label>
              <q-input 
                outlined 
                v-model="github"
                id="github"
                placeholder="Github 계정을 입력해주세요" 
                style="margin: 7px 0 30px 0;"
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
                style="margin: 7px 0 30px 0;"
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
                style="margin: 7px 0 30px 0;"
                :dense="dense" 
              />
            </div>
          </div>
          <profile-setting-tech @addTechStackItem="addOneSkill"></profile-setting-tech>
          <profile-setting-project @addProjectItem="addOneProject"></profile-setting-project>
          <profile-setting-tag @addTagItem="addOneTag"></profile-setting-tag>
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
import { loadProfile, updateProfile } from '@/api/profileSetting';
import ProfileSettingTech from '@/components/profileSetting/ProfileSettingTech';
import ProfileSettingProject from '@/components/profileSetting/ProfileSettingProject';
import ProfileSettingTag from '@/components/profileSetting/ProfileSettingTag';

export default {
  components: { 
    ProfileSettingTech, 
    ProfileSettingProject, 
    ProfileSettingTag
  },
  data() {
    return {
      email: 'emma@gmail.com',
      username: 'Emma',
      region: '',
      group: '',
      bio: '',
      imageUrl: 'https://placeimg.com/500/300/nature',
      github: '',
      facebook: '',
      linkedin: '',
      dense: false,
      techStacks: [],
      projects: [],
      tags: [],
    }
  },
  methods: {
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onChangeImages(e) {
      console.log(e.target.files)
      const file = e.target.files[0];
      this.imageUrl = URL.createObjectURL(file);
    },
    addOneSkill(techStack) {
      this.techStacks.push(techStack)
    },
    addOneProject(pjtName, pjtUrl) {
      this.projects.push({pjtName, pjtUrl})
    },
    addOneTag(tagItem) {
      this.tags.push(tagItem)
    },
  },
  // 새로운 데이터 보내기
  async submitForm() {
    try {
      this.$q.loading.show();
      await updateProfile({
        // 넘길 데이터 적어주기
        username: this.username,
        profile_img: this.imageUrl,
        region: this.region,
        group: this.group,
        bio: this.bio,
        // TODO : sns, projects, tags와 같은 이름 없이 넘겨줘도 되는지 확인!
        sns: [{'github':this.github, 'facebook':this.facebook, 'linkedin':this.linkedin}],
        tech_stack: this.techStacks,
        projects: this.projects,
        tags: this.tags,
      });
      // 이동 시킬 페이지 적어주기
    } catch (error) {
      console.log(error);
      alert('에러가 발생했습니다!')
    } finally {
      this.$q.loading.hide();
    }
  },
  // 기존 데이터 불러오기
  created() {
    loadProfile({
      username: this.username,
      user_email: this.email,
      profile_img: this.imageUrl,
      region: this.region,
      group: this.group,
      bio: this.bio,
      sns: [{'github':this.github, 'facebook':this.facebook, 'linkedin':this.linkedin}],
      tech_stack: this.techStacks,
      projects: this.projects,
      tags: this.tags,
    })
  }
  
};
</script>

<style scoped></style>
