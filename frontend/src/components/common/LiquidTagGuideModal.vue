<template>
  <q-dialog v-model="$store.state.liquidTagGuideModal" position="right">
    <q-card style="min-width:800px; height:100%">
      <q-card-section class="row items-center q-pb-none justify-between">
        <div class="text-h5 text-weight-bold text-primary">
          Liquid 태그 가이드
        </div>
        <q-btn icon="close" flat round dense v-close-popup />
        <q-separator />
      </q-card-section>
      <q-card-section>
        <q-scroll-area
          :thumb-style="thumbStyle"
          :bar-style="barStyle"
          class="col-6  preview-shadow q-py-lg"
          style="height: 800px"
        >
          <v-md-preview :text="guide"></v-md-preview>
        </q-scroll-area>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script>
export default {
  data() {
    return {
      thumbStyle: {
        right: '4px',
        borderRadius: '5px',
        backgroundColor: '#dddddd',
        width: '6px',
        opacity: 0.75,
      },

      barStyle: {
        right: '2px',
        borderRadius: '9px',
        backgroundColor: '#dddddd',
        width: '7px',
        opacity: 0.2,
      },
      guide: `
      _가이드에서 소개하는 기능들의 입력 양식에서 입력 값은 ()로 구분합니다._
# 1. **Youtube**
### 입력 양식: **{% youtube (video_id) (width) (height) %}**
* **video_id**: youtube 영상 url 주소의 watch?v= 이후에 오는 문자열
* **width**:  임베드 영상의 너비. 기본 단위는 px. % 사용 가능
* **height**: 임베드 영상의 높이. 기본 단위는 px. % 사용 불가능
* 예시) 
1. 삽입하고 싶은 영상을 찾는다 => https://www.youtube.com/watch?v=DV_FnRXZimc
2. {% youtube DV_FnRXZimc 100% 300px %}

# 2. **CodeSandBox**
### 입력 양식: **{% codesandbox (project_name) (width) (height) %}**
* **project_name**: codesandbox 임베드 url 주소의 embed/ 이후에 오는 문자열
* **width**:  임베드 영상의 너비. 기본 단위는 px. % 사용 가능
* **height**: 임베드 영상의 높이. 기본 단위는 px. % 사용 불가능
* 예시) 
1. 삽입하고 싶은 프로젝트의 임베드 url을 찾는다 => "https://codesandbox.io/embed/vue-chartjs-pie-chart-forked-fqqcm?fontsize=14&hidenavigation=1&theme=dark"
2. {% codesandbox vue-chartjs-pie-chart-forked-fqqcm 100% 300px %}

# 3. **Repl.it**
### 입력 양식: **{% repl (username) (repl_id) (width) (height) %}**
* **username**: repl url 주소의 @ 이후에 오는 문자열
* **repl_id**: repl url 주소의 username 이후에 오는 문자열
* **width**:  임베드 영상의 너비. 기본 단위는 px. % 사용 가능
* **height**: 임베드 영상의 높이. 기본 단위는 px. % 사용 불가능
* 예시) 
1. 삽입하고 싶은 프로젝트의 url을 찾는다 => "https://repl.it/@eoy1313/test"
2. {% repl eoy1313 test 100% 300px %} 

# 4. **Instagram**
### 입력 양식: **{% instagram (page_id) (width) (height) %}**
* **page_id**: instagram 페이지 주소의 p/ 이후에 오는 문자열
* **width**:  임베드 영상의 너비. 기본 단위는 px. % 사용 가능
* **height**: 임베드 영상의 높이. 기본 단위는 px. % 사용 불가능
* 예시) 
1. 삽입하고 싶은 인스타그램 페이지의 url을 찾는다 => "https://www.instagram.com/p/B7C7cZalBKR/"
2. {% instagram B7C7cZalBKR 320px 460px %} 





      
      `,
    };
  },
  components: {},
};
</script>

<style scoped></style>
