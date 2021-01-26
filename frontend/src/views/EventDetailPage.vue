<template>
  <div class="q-pa-md">
    <div class="justify-center" style="width: 85%; padding: 50px; margin:0 auto;">
      <!-- 이벤트 메인 -->
      <div class="row" style="margin-left: 100px;">
        <!-- 이벤트 이미지 -->
        <div class="col-4" style="width: 535px; height: 357px; background-color: black; border-radius: 10px; margin-bottom: 70px;">
          <div style="text-align: center; margin-top: 100px;">
            <p class="text-h5 text-white" style="padding-top: 30px;">For Developer vol.1</p>
            <p class="text-h4 text-teal-8 text-weight-bolder">2021 Vue.js Online</p>
          </div>
        </div>
        <!-- 이벤트 소개 -->
        <div class="col-4" style="margin-left: 80px;">
          <div class="text-caption text-primary" style="margin:20px 0px 20px 0px;">신청 진행중</div>
          <div class="text-h4 text-weight-bold" style="margin-bottom: 50px;">Vue.js 컨퍼런스</div>
          <div style="margin-bottom: 15px;">
            <span class="text-h6 text-weight-bold" style="margin-right: 20px;">장소</span>
            <span class="text-h7">Online</span>
          </div>
          <div style="margin-bottom: 15px;">
            <span class="text-h6 text-weight-bold" style="margin-right: 20px;">일시</span>
            <span class="text-h7">2021년 2월 15일</span>
            <div class="text-h7" style="margin-left: 60px;">오후 6:00 - 오후 7:30</div>
          </div>
          <div style="margin-bottom: 15px;">
            <span class="text-h6 text-weight-bold" style="margin-right: 20px;">주최</span>
            <span class="text-h7">Eddie</span>
          </div>
          <div style="margin-bottom: 15px;">
            <span class="text-h6 text-weight-bold" style="margin-right: 20px;">비용</span>
            <span class="text-h7">무료</span>
          </div>
        </div>
      </div>
      <!-- 이벤트 신청 -->
       <hr />
       <div style="margin: 30px 0px 0px 30px;">
        <div class="row">
          <div class="col-4" style="margin-left: 100px;">
            <p><q-icon size="xs" name="group" /> 159명 신청중</p>
            <p><q-icon size="xs" name="calendar_today" /> 신청기간 : 2021.01.30 - 02.14</p>
          </div>
          <q-btn
            color="blue-12"
            class="col-4"
            label="참가 신청"
            style="width:300px; height:50px; border-radius:5px; margin-left: 200px;"
          />
        </div>
       </div>
       <hr />
       <!-- 이벤트 상세 정보 -->
       <div style="margin-left: 130px;">
         <!-- 참가대상 -->
         <div style="margin-top: 70px;">
          <div class="text-h6 text-weight-bold" style="margin-bottom: 20px;">Event 참가대상</div>
          <div>개발자 혹은 개발에 관심있는 누구나</div>
         </div>
         <!-- 소개 -->
         <div style="margin-top: 70px;">
          <div class="text-h6 text-weight-bold" style="margin-bottom: 20px;">Event 소개</div>
          <div>프론트엔드 개발을 위한 Vue.js 컨퍼런스입니다.</div>
         </div>
         <!-- 스케쥴 -->
         <div style="margin-top: 70px;">
          <div class="text-h6 text-weight-bold" style="margin-bottom: 20px;">Event 스케쥴</div>
          <div>1. 주최자 소개 <br> 2. 컨퍼런스 소개 <br> 3. 프론트엔드 프레임워크 소개</div>
         </div>
         <!-- 관련 태그 -->
         <div style="margin-top: 70px;">
          <div class="text-h6 text-weight-bold" style="margin-bottom: 20px;">관련 태그</div>
          <ul class="row">
            <li v-for="(tag, index) in tags" :key="index" style="margin-right: 10px; cursor: pointer;">
              <q-chip square color="primary" text-color="white">
                <q-avatar icon="local_offer" />
                {{ tag }}
                <span @click="removeTag(tag, index)" style="margin-left: 10px;">X</span>
              </q-chip>
            </li>
          </ul>  
         </div>
       </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tags: ['Vue.js', 'Frontend', 'Online']
    }
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>