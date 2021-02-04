<template>
  <q-form @submit.prevent="submitForm" class="full-width">
    <div class="q-mb-md">
      <div class="text-h6 text-weight-bold q-mb-sm">
        Personal details
      </div>
      <div class="row full-width">
        <div class="row col-6">
          <!-- 프로필 이미지 -->
          <q-img
            :src="profile_info.profile_img"
            spinner-color="white"
            style="height: 140px; max-width: 150px; position: relative; "
            class="rounded-borders q-mb-lg"
          />
          <div class="q-ml-sm">
            <div class="text-subtitle1">@{{ profile_info.username }}</div>
            <div class="text-caption text-grey">{{ profile_info.email }}</div>

            <!-- 이미지 업로드 -->
            <input
              ref="imageInput"
              type="file"
              hidden
              @change="onChangeImages"
            />
            <q-btn
              @click="onClickImageUpload"
              round
              color="primary"
              style="position: relative; left: -40px; top: 60px;"
            >
              <q-icon :name="$i.ionCamera"></q-icon>
            </q-btn>
            <span
              @click="onClickImageUpload"
              style="position: relative; left: -30px; top: 60px;"
            >
              {{
                profile_img === 'https://placeimg.com/500/300/nature'
                  ? '선택된 파일 없음'
                  : '이미지 업로드 성공'
              }}
            </span>
          </div>
        </div>
        <div class="row col-6">
          <div class="full-width">
            <q-input
              stack-label
              label-slot
              outlined
              v-model="profile_info.username"
              placeholder="이름을 입력해주세요"
            >
              <template v-slot:label>
                <span class="text-primary">이름</span>
                <br />
              </template>
            </q-input>
          </div>

          <div class="full-width">
            <q-input
              stack-label
              label-slot
              outlined
              v-model="profile_info.group"
              placeholder="현재 소속을 입력해주세요"
            >
              <template v-slot:label>
                <span class="text-primary">소속</span>
                <br />
              </template>
            </q-input>
          </div>
        </div>
      </div>

      <div class="row col-6">
        <div class="col-12 q-mb-md">
          <q-input
            stack-label
            label-slot
            outlined
            v-model="profile_info.region"
            placeholder="거주지역을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">거주지</span>
              <br />
            </template>
          </q-input>
        </div>
      </div>
      <!-- 이름, 소속, 거주지, 자기소개 -->
      <div class="full-width q-mb-xl">
        <div class="col-12">
          <q-input
            v-model="profile_info.bio"
            stack-label
            label-slot
            outlined
            type="textarea"
            placeholder="자기 소개를 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">자기소개</span>
              <br />
            </template>
          </q-input>
        </div>
      </div>
    </div>
    <!-- link 연동 -->
    <div class="full-width q-mb-xl">
      <div class="text-h6 text-weight-bold q-mb-md">
        Links
      </div>
      <div class="row items-center q-mb-sm">
        <div class="col-1 row justify-center">
          <q-icon :name="$i.ionLogoGithub" size="lg" />
        </div>
        <q-input
          class="q-pl-xs col-11"
          stack-label
          clearable
          clear-icon="clear"
          label-slot
          v-model="profile_info.links.github"
          placeholder="https://github.com/.."
        >
          <template v-slot:label>
            <span class="text-primary">
              Github URL
            </span>
            <br />
          </template>
        </q-input>
      </div>
      <div class="row items-center q-mb-sm">
        <div class="col-1 row justify-center">
          <q-icon :name="$i.ionLogoFacebook" size="lg" />
        </div>
        <q-input
          stack-label
          label-slot
          clearable
          clear-icon="clear"
          v-model="profile_info.links.facebook"
          placeholder="https://www.facebook.com/.."
          class="q-pl-xs col-11"
        >
          <template v-slot:label>
            <span class="text-primary">
              Facebook URL
            </span>
            <br />
          </template>
        </q-input>
      </div>
      <div class="row items-center">
        <div class="col-1 row justify-center">
          <q-icon :name="$i.ionLogoLinkedin" size="lg" />
        </div>
        <q-input
          stack-label
          label-slot
          clearable
          clear-icon="clear"
          v-model="profile_info.links.linkedin"
          placeholder="https://www.linkedin.com/in/.."
          class="q-pl-xs col-11"
        >
          <template v-slot:label>
            <span class="text-primary">
              LinkedIn URL
            </span>
            <br />
          </template>
        </q-input>
      </div>
    </div>
    <profile-setting-tech
      @addTechStackItem="addOneSkill"
      @removeTechStackItem="removeOneSkill"
      :propsTechStackData="profile_info.tech_stacks"
    ></profile-setting-tech>
    <profile-setting-project
      @addProjectItem="addOneProject"
      @removeProjectItem="removeOneProject"
      :propsProjectData="profile_info.projects"
    ></profile-setting-project>
    <profile-setting-tag
      @addTagItem="addOneTag"
      @removeTagItem="removeOneTag"
      :propsTagData="profile_info.tags"
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
</template>

<script>
import ProfileSettingTech from '@/components/profileSetting/ProfileSettingTech';
import ProfileSettingProject from '@/components/profileSetting/ProfileSettingProject';
import ProfileSettingTag from '@/components/profileSetting/ProfileSettingTag';
import { updateProfile } from '@/api/profileSetting';
// import { getProfile } from '@/api/profile';
export default {
  components: {
    ProfileSettingTech,
    ProfileSettingProject,
    ProfileSettingTag,
  },
  // 가짜 데이터
  data() {
    return {
      profile_info: {
        email: 'emma@gmail.com',
        username: 'Emma',
        region: 'Daejeon',
        group: 'SSAFY',
        bio: '안녕하세요! 만나서 반갑습니다.',
        profile_img: 'https://placeimg.com/500/300/nature',
        links: {
          Github: 'https://github.com/emma',
          Facebook: 'https://www.facebook.com/emma',
          Linkedin: 'https://www.linkedin.com/emma/',
        },
        tech_stacks: ['Python', 'Javascript', 'Vue.js'],
        projects: [
          {
            project_name: 'my_first_project',
            project_url: 'https://myproject.com',
          },
          {
            project_name: 'my_second_project',
            project_url: 'https://mysecondproject.com',
          },
        ],
        tags: ['Vue', 'React', 'Python', 'javascript'],
      },
      chageImg: false,
    };
  },

  // TODO : 프로필 수정 중 페이지를 이동할 때 경고문구 띄우기
  beforeRouteLeave(to, from, next) {
    const answer = window.confirm('정말 페이지를 나가시겠습니까?');
    if (answer) {
      next();
    } else {
      next(false);
    }
  },
  methods: {
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onChangeImages(e) {
      const file = e.target.files[0];
      console.log(file);
      this.profile_info.profile_img = URL.createObjectURL(file);
      // const file = this.$refs.imageInput.files[0];
    },

    addOneSkill(techStack) {
      if (this.profile_info.tech_stacks.indexOf(techStack) < 0)
        this.profile_info.tech_stacks.push(techStack);
    },
    removeOneSkill(skill, index) {
      this.profile_info.tech_stacks.splice(index, 1);
    },
    addOneProject(pjtName, pjtUrl) {
      this.profile_info.projects.push({
        project_name: pjtName,
        project_url: pjtUrl,
      });
    },
    removeOneProject(project, index) {
      this.profile_info.projects.splice(index, 1);
    },
    addOneTag(tagItem) {
      this.profile_info.tags.push(tagItem);
    },
    removeOneTag(tag, index) {
      this.profile_info.tags.splice(index, 1);
    },
    // 새로운 데이터 보내기
    async submitForm() {
      const frm = new FormData();
      frm.append('username', this.username);
      frm.append('profile_img', this.$refs.imageInput.files[0]);
      frm.append('region', this.region);
      frm.append('group', this.group);
      frm.append('bio', this.bio);
      frm.append('links', this.links);
      frm.append('tech_stack', this.tech_stack);
      frm.append('projects', this.projects);
      frm.append('tags', this.tags);
      try {
        this.$q.loading.show();
        await updateProfile(frm);
        // 이동 시킬 페이지 적어주기(이전 페이지로 이동)
        this.$router.go(-1);
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  // 기존 데이터 불러오기
  // async created() {
  //   try {
  //     this.$q.loading.show();
  //     const { data } = await getProfile(this.$store.state.id);
  //     this.profile_info = data;
  //   } catch (error) {
  //     console.log(error);
  //   } finally {
  //     this.$q.loading.hide();
  //   }
  // },
};
</script>

<style scoped></style>
