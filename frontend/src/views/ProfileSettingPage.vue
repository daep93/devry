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
        <!-- TODO : 기술과 태그 입력을 위해 enter를 치면 save 버튼이 반응하는 문제 발생  -->
        <q-form @submit.prevent="submitForm">
          <div class="col-12" style="margin-bottom: 70px;">
            <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">Personal details</div>
            <!-- 프로필 이미지 -->
            <div class="row">
              <q-img
                :src="profile_img"
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
                  {{ profile_img === 'https://placeimg.com/500/300/nature' ? '선택된 파일 없음' : '이미지 업로드 성공'}}
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
                v-model="links.github"
                id="github"
                placeholder="Github 계정을 입력해주세요" 
                style="margin: 7px 0 30px 0;"
              />
            </div>
            <div>
              <label for="facebook">Facebook Account <q-icon :name="$i.ionLogoFacebook"></q-icon></label>
              <q-input 
                outlined 
                v-model="links.facebook"
                id="facebook"
                placeholder="Facebook 계정을 입력해주세요" 
                style="margin: 7px 0 30px 0;"
              />
            </div>
            <div>
              <label for="linkedin">LinkedIn Account <q-icon :name="$i.ionLogoLinkedin"></q-icon></label>
              <q-input 
                outlined 
                v-model="links.linkedin"
                id="linkedin"
                placeholder="LinkedIn 계정을 입력해주세요" 
                style="margin: 7px 0 30px 0;"
              />
            </div>
          </div>
          <profile-setting-tech @addTechStackItem="addOneSkill"
            @removeTechStackItem="removeOneSkill"
            :propsTechStackData="tech_stacks"
          ></profile-setting-tech>
          <profile-setting-project @addProjectItem="addOneProject"
            @removeProjectItem="removeOneProject"
            :propsProjectData="projects"
          ></profile-setting-project>
          <profile-setting-tag @addTagItem="addOneTag"
            @removeTagItem="removeOneTag"
            :propsTagData="tags"
          ></profile-setting-tag>
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
// import { loadProfile, updateProfile } from '@/api/profileSetting';
import ProfileSettingTech from '@/components/profileSetting/ProfileSettingTech';
import ProfileSettingProject from '@/components/profileSetting/ProfileSettingProject';
import ProfileSettingTag from '@/components/profileSetting/ProfileSettingTag';

export default {
  components: { 
    ProfileSettingTech, 
    ProfileSettingProject, 
    ProfileSettingTag
  },
  // 가짜 데이터
  data() {
    return {
      email: 'emma@gmail.com',
      username: 'Emma',
      region: 'Daejeon',
      group: 'SSAFY',
      bio: '안녕하세요! 만나서 반갑습니다.',
      profile_img: 'https://placeimg.com/500/300/nature',
      links: {
        github: 'https://github.com/emma',
        facebook: 'https://www.facebook.com/emma',
        linkedin: 'https://www.linkedin.com/emma/',
      },
      tech_stacks: [
        'Python', 'Javascript', 'Vue.js'
      ],
      projects: [
        { project_name: 'my_first_project',
          project_url: 'https://myproject.com'
        },
        { project_name: 'my_second_project',
          project_url: 'https://mysecondproject.com'
        },
      ],
      tags: [
        'Vue.js', 'UX/UI', 'Python'
      ],
    }
  },
  // data() {
  //   return {
  //     email: '',
  //     username: '',
  //     region: '',
  //     group: '',
  //     bio: '',
  //     profile_img: 'https://placeimg.com/500/300/nature',
  //     links: {}
  //     techStacks: [],
  //     projects: [],
  //     tags: [],
  //   }
  // },

  // TODO : 프로필 수정 중 페이지를 이동할 때 경고문구 띄우기
  beforeRouteLeave(to, from, next) {
    const answer = window.confirm('정말 페이지를 나가시겠습니까?')
    if (answer) {
      next()
    } else {
      next(false)
    }
  },
  methods: {
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onChangeImages(e) {
      console.log(e.target.files)
      const file = e.target.files[0];
      this.profile_img = URL.createObjectURL(file);
    },
    addOneSkill(techStack) {
      this.tech_stacks.push(techStack)
    },
    removeOneSkill(skill, index) {
      this.tech_stacks.splice(index, 1)
    },
    addOneProject(pjtName, pjtUrl) {
      this.projects.push({project_name: pjtName, project_url: pjtUrl})
    },
    removeOneProject(project, index) {
      this.projects.splice(index, 1)
    },
    addOneTag(tagItem) {
      this.tags.push(tagItem)
    },
    removeOneTag(tag, index) {
      this.tags.splice(index, 1)
    },
    // 새로운 데이터 보내기
    async submitForm() {
      try {
        // id 넘겨주기
        const userid = this.$route.parmas.id;
        this.$q.loading.show();
        await updateProfile(userid, {
          // 넘길 데이터 적어주기
          username: this.username,
          region: this.region,
          group: this.group,
          bio: this.bio,
          profile_img: this.profile_img,
          links: this.links,
          tech_stack: this.tech_stacks,
          projects: this.projects,
          tags: this.tags,
        });
        // 이동 시킬 페이지 적어주기(이전 페이지로 이동)
        this.$router.go(-1);
      } catch (error) {
        console.log(error);
        // alert('에러가 발생했습니다!')
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  // 기존 데이터 불러오기
  async created() {
    // id 가져오기
    const userid = this.$route.params.id;
    try {
      this.$q.loading.show();
      await loadProfile(userid, {
        email: this.email,
        username: this.username,
        profile_img: this.profile_img,
        region: this.region,
        group: this.group,
        bio: this.bio,
        links: this.links,
        tech_stack: this.tech_stacks,
        projects: this.projects,
        tags: this.tags,
      });
    } catch (error) {
      console.log(error);
      // alert('에러가 발생했습니다.)
    } finally {
      this.$q.loading.hide();
    }
  }
};
</script>

<style scoped></style>
