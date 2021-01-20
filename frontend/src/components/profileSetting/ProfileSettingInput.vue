<template>
  <div>
    <q-form>
      <!-- 회원 기본 정보 -->
      <div>
        <div class="text-h6 text-weight-bold">Personal details</div>
        <!-- 프로필 이미지 -->
        <div class="row">
          <q-img
            :src="'https://placeimg.com/500/300/nature'"
            spinner-color="white"
            style="height: 140px; max-width: 150px"
            class="rounded-borders"
          />
          <div>
            <p>@Emma</p>
            <p>emma@gmail.com</p>
            <q-file
              v-model="files"
              label="Pick files"
              filled
              counter
              :counter-label="counterLabelFn"
              max-files="3"
              multiple
              style="max-width: 300px"
              >
              <template v-slot:prepend>
                <q-icon name="attach_file" />
              </template>
            </q-file>
          </div>
        </div>
        <div>
          <div class="row" style="width:730px;">
            <div>
              <label for="region">region</label>
              <q-input 
                outlined 
                v-model="ph"
                id="region"
                placeholder="지역을 입력해주세요" 
                style="width:350px;"
                :dense="dense" 
              />
            </div>
            <div>
              <label for="group">group</label>
              <q-input 
                outlined 
                v-model="ph"
                id="group"
                placeholder="소속을 입력해주세요" 
                style="width:350px;"
                :dense="dense" 
              />
            </div>
          </div>
          <div>
            <label for="name">name</label>
            <q-input 
              outlined 
              v-model="ph"
              id="name"
              placeholder="이름을 입력해주세요" 
              style="width:730px;"
              :dense="dense" 
            />
          </div>
          <div>
            <label for="bio">bio</label>
            <q-input
              v-model="text"
              outlined
              type="textarea"
              placeholder="자기 소개를 입력해주세요" 
              style="width:730px; height:100px"
            />
          </div>
        </div>
      </div>
      <!-- SNS 연동 -->
      <div>
        <div class="text-h6 text-weight-bold">Connect with SNS</div>
        <div>
          <label for="github">Github Account <q-icon :name="$i.ionLogoGithub"></q-icon></label>
          <q-input 
            outlined 
            v-model="ph"
            id="github"
            placeholder="Github 계정을 입력해주세요" 
            style="width:730px;"
            :dense="dense" 
          />
        </div>
        <div>
          <label for="facebook">Facebook Account <q-icon :name="$i.ionLogoFacebook"></q-icon></label>
          <q-input 
            outlined 
            v-model="ph"
            id="facebook"
            placeholder="Facebook 계정을 입력해주세요" 
            style="width:730px;"
            :dense="dense" 
          />
        </div>
        <div>
          <label for="linkedin">LinkedIn Account <q-icon :name="$i.ionLogoLinkedin"></q-icon></label>
          <q-input 
            outlined 
            v-model="ph"
            id="linkedin"
            placeholder="LinkedIn 계정을 입력해주세요" 
            style="width:730px;"
            :dense="dense" 
          />
        </div>
      </div>
      <!-- 기술 스택 -->
      <div>
        <div class="text-h6 text-weight-bold">Tech Stack</div>
        <div>
            <label for="tech">Skills</label>
            <q-input
              outlined 
              v-model="ph"
              id="tech"
              placeholder="보유하신 기술을 입력해주세요" 
              style="width:730px;"
              :dense="dense" 
            />
          </div>
      </div>
      <!-- 프로젝트 -->
      <div>
        <div class="text-h6 text-weight-bold">Project URL</div>
        <label for="project">project</label>
        <div class="row" style="width:730px;">
          <div id="project">
            <q-input 
              outlined 
              v-model="ph"
              placeholder="프로젝트 이름을 입력해주세요" 
              style="width:250px;"
              :dense="dense" 
            />
          </div>
          <div>
            <q-input 
              outlined 
              v-model="ph"
              placeholder="프로젝트 URL을 입력해주세요" 
              style="width:400px;"
              :dense="dense" 
            />
          </div>
          <q-btn
            padding="xs"
            color="primary"
            icon="add"
            style="width:60px;"
          />
        </div>
      </div>
      <!-- 태그 -->
      <div>
        <div class="text-h6 text-weight-bold">Following Tags</div>
        <div>
          <label for="tag">tags</label>
          <q-input
            outlined 
            v-model="ph"
            id="tag"
            placeholder="팔로우할 태그를 입력해주세요" 
            style="width:730px;"
            :dense="dense" 
          />
        </div>
      </div>
      <!-- 버튼 -->
      <div class="row q-mb-md q-mt-md float-right">
        <q-btn
          color="primary"
          label="SAVE"
          style="width:200px; height:50px; border-radius:5px;"
          type="submit"
        />
      </div>
    </q-form>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>