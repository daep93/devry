<template>
  <q-form @submit.prevent="submitForm" class="full-width">
    <div class="q-mb-md">
      <div class="text-h6 text-weight-bold q-mb-sm">
        Personal details
      </div>
      <!-- 프로필 이미지 -->
      <div class="row">
        <q-img
          :src="profile_img"
          spinner-color="white"
          style="height: 140px; max-width: 150px; position: relative; "
          class="rounded-borders q-mb-lg"
        />
        <div class="q-ml-sm">
          <div class="text-subtitle1">@{{ username }}</div>
          <div class="text-caption text-grey">{{ email }}</div>

          <!-- 이미지 업로드 -->
          <input ref="imageInput" type="file" hidden @change="onChangeImages" />
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
      <!-- 이름, 소속, 거주지, 자기소개 -->
      <div class="full-width q-mb-xl">
        <div class="row justify-between q-mb-md">
          <div class="col-6 q-pr-md">
            <q-input
              stack-label
              label-slot
              outlined
              v-model="username"
              placeholder="이름을 입력해주세요"
            >
              <template v-slot:label>
                <span class="text-primary">이름</span>
                <br />
              </template>
            </q-input>
          </div>

          <div class="col-6">
            <q-input
              stack-label
              label-slot
              outlined
              v-model="group"
              placeholder="현재 소속을 입력해주세요"
            >
              <template v-slot:label>
                <span class="text-primary">소속</span>
                <br />
              </template>
            </q-input>
          </div>
        </div>
        <div class="col-12 q-mb-md">
          <q-input
            stack-label
            label-slot
            outlined
            v-model="region"
            placeholder="거주지역을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">거주지</span>
              <br />
            </template>
          </q-input>
        </div>
        <div class="col-12">
          <q-input
            v-model="bio"
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
    <div class="full-width q-mb-md">
      <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">
        Connect with SNS
      </div>
      <div>
        <label for="github"
          >Github Account <q-icon :name="$i.ionLogoGithub"></q-icon
        ></label>
        <q-input
          outlined
          v-model="links.github"
          id="github"
          placeholder="Github 계정을 입력해주세요"
          style="margin: 7px 0 30px 0;"
        />
      </div>
      <div>
        <label for="facebook"
          >Facebook Account <q-icon :name="$i.ionLogoFacebook"></q-icon
        ></label>
        <q-input
          outlined
          v-model="links.facebook"
          id="facebook"
          placeholder="Facebook 계정을 입력해주세요"
          style="margin: 7px 0 30px 0;"
        />
      </div>
      <div>
        <label for="linkedin"
          >LinkedIn Account <q-icon :name="$i.ionLogoLinkedin"></q-icon
        ></label>
        <q-input
          outlined
          v-model="links.linkedin"
          id="linkedin"
          placeholder="LinkedIn 계정을 입력해주세요"
          style="margin: 7px 0 30px 0;"
        />
      </div>
    </div>
    <profile-setting-tech
      @addTechStackItem="addOneSkill"
      @removeTechStackItem="removeOneSkill"
      :propsTechStackData="tech_stacks"
    ></profile-setting-tech>
    <profile-setting-project
      @addProjectItem="addOneProject"
      @removeProjectItem="removeOneProject"
      :propsProjectData="projects"
    ></profile-setting-project>
    <profile-setting-tag
      @addTagItem="addOneTag"
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
</template>

<script>
import ProfileSettingTech from '@/components/profileSetting/ProfileSettingTech';
import ProfileSettingProject from '@/components/profileSetting/ProfileSettingProject';
import ProfileSettingTag from '@/components/profileSetting/ProfileSettingTag';
export default {
  components: {
    ProfileSettingTech,
    ProfileSettingProject,
    ProfileSettingTag,
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
      tags: ['Vue.js', 'UX/UI', 'Python'],
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
      this.profile_img = URL.createObjectURL(file);
    },
    addOneSkill(techStack) {
      this.tech_stacks.push(techStack);
    },
    removeOneSkill(skill, index) {
      this.tech_stacks.splice(index, 1);
    },
    addOneProject(pjtName, pjtUrl) {
      this.projects.push({ project_name: pjtName, project_url: pjtUrl });
    },
    removeOneProject(project, index) {
      this.projects.splice(index, 1);
    },
    addOneTag(tagItem) {
      this.tags.push(tagItem);
    },
    removeOneTag(tag, index) {
      this.tags.splice(index, 1);
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
      // alert('에러가 발생했습니다.)
    } finally {
      this.$q.loading.hide();
    }
  },
};
</script>

<style scoped></style>
