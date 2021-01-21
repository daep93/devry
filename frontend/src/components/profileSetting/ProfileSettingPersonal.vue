<template>
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
        <div class="col-6">
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
          style="height:100px; margin: 7px 0 30px 0;"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: 'emma@gmail.com',
      username: 'Emma',
      region: '',
      group: '',
      bio: '',
      imageUrl: 'https://placeimg.com/500/300/nature',
      // url: 'http://localhost:4444/upload'
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
    onRejected (rejectedEntries) {
      // Notify plugin needs to be installed
      // https://quasar.dev/quasar-plugins/notify#Installation
      this.$q.notify({
        type: 'negative',
        message: `${rejectedEntries.length} file(s) did not pass validation constraints`
      })
    }
  },
}
</script>

<style scoped></style>