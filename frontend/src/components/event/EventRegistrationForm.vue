<template>
  <q-form @submit.prevent="submitForm" class="full-width">
    <!-- 기본 정보 입력 part -->
    <div class="q-mb-md">
      <div class="text-h6 text-weight-bold q-mt-xl q-mb-sm">
        Event Information
      </div>
      <div class="full-width">
        <div class="row q-mb-xl relative-position">
          <!-- 이미지 등록 -->
          <q-img
            :src="thumnail"
            spinner-color="white"
            style="height: 215px; max-width: 500px; "
            class="rounded-borders col-"
          />
          <div class="q-ml-lg col-3">
            <!-- 이미지 등록 버튼 -->
            <input
              ref="thumnailInput"
              type="file"
              hidden
              @change="onChangeThumnails"
            />
            <q-btn
              @click="onClickThumnailUpload"
              color="primary"
              label="이미지 등록"
              style="width: 150px; height: 40px; border-radius:5px; position:absolute; bottom:0px;"
            >
            </q-btn>
          </div>
        </div>
        <!-- 이벤트 상태 및 카테고리 -->
        <div class="full-width row q-mb-xl">
          <q-select 
            class="col-6 q-pr-sm"
            stack-label
            label-slot
            outlined
            v-model="state"
            :options="state_options"
          >
            <template v-slot:label>
              <span class="text-primary">진행 상태</span>
              <br />
            </template>
             <template v-if="state" v-slot:append>
              <q-icon name="cancel" @click.stop="state = null" class="cursor-pointer" />
            </template>
          </q-select>
          <q-select 
            class="col-6"
            stack-label
            label-slot
            outlined
            v-model="category"
            :options="category_options"
          >
            <template v-slot:label>
              <span class="text-primary">카테고리</span>
              <br />
            </template>
            <template v-if="category" v-slot:append>
              <q-icon name="cancel" @click.stop="category = null" class="cursor-pointer" />
            </template>
          </q-select>
        </div>
        <!-- 이벤트 타이틀 -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            stack-label
            label-slot
            outlined
            v-model="title"
            placeholder="타이틀을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">타이틀</span>
              <br />
            </template>
          </q-input>
        </div>
        <!-- 이벤트 날짜 -->
        <div class="full-width row q-mb-xl">
          <q-input 
            class="col-6 q-pr-sm"
            stack-label
            label-slot
            outlined
            v-model="period.start"
            placeholder="이벤트 시작일을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">시작일</span>
              <br />
            </template>
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
                  <q-date v-model="period.start">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
          <q-input 
            class="col-6"
            stack-label
            label-slot
            outlined
            v-model="period.end"
            placeholder="이벤트 종료일을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">종료일</span>
              <br />
            </template>
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
                  <q-date v-model="period.end">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>
        <!-- 이벤트 시간 -->
        <div class="full-width row q-mb-xl">
          <q-input 
            class="col-6 q-pr-sm"
            stack-label
            label-slot
            outlined
            v-model="time.start"
            placeholder="시작 시간을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">시작시간</span>
              <br />
            </template>
            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy transition-show="scale" transition-hide="scale">
                  <q-time v-model="time.start">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
          <q-input 
            class="col-6"
            stack-label
            label-slot
            outlined
            v-model="time.end"
            placeholder="종료 시간을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">종료시간</span>
              <br />
            </template>
            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy transition-show="scale" transition-hide="scale">
                  <q-time v-model="time.end">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>
        <!-- 이벤트 장소 및 비용 -->
        <div class="full-width row q-mb-xl">
          <q-input 
            class="col-6 q-pr-sm"
            stack-label
            label-slot
            outlined
            v-model="place"
            placeholder="이벤트 장소를 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">장소</span>
              <br />
            </template>
          </q-input>
          <q-input 
            class="col-6"
            stack-label
            label-slot
            outlined
            v-model="cost"
            placeholder="이벤트 비용을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">비용</span>
              <br />
            </template>
          </q-input>
        </div>
      </div> 
    </div> 
    <!-- 이벤트 소개 part -->
    <div class="q-mb-md">
      <div class="text-h6 text-weight-bold q-mt-xl q-mb-sm">
        Event introduction
      </div>
      <div class="full-width"> 
        <!-- 참가대상 -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            stack-label
            label-slot
            outlined
            v-model="participation"
            placeholder="참가대상을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">참가대상</span>
              <br />
            </template>
          </q-input>
        </div>
        <!-- 이벤트 소개글 -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            stack-label
            label-slot
            outlined
            v-model="introduction"
            placeholder="이벤트를 소개해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">소개</span>
              <br />
            </template>
          </q-input>
        </div>
        <!-- 스케쥴 -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            stack-label
            label-slot
            outlined
            v-model="schedule"
            placeholder="스케쥴을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">스케쥴</span>
              <br />
            </template>
          </q-input>
        </div>
      </div>  
    </div>  
    <!-- 호스트 정보 입력 part -->
    <div class="q-mb-md">
      <div class="text-h6 text-weight-bold q-mt-xl q-mb-sm">
        Host Information
      </div>
      <div class="full-width">
        <div class="row q-mb-xl relative-position">
          <!-- 프로필 이미지 등록 -->
          <q-img
            :src="host_info.profile_img"
            spinner-color="white"
            style="height: 127px; max-width: 250px; "
            class="rounded-borders col-3"
          />
          <div class="q-ml-lg col-3">
            <!-- 프로필 이미지 등록 버튼 -->
            <input
              ref="profileInput"
              type="file"
              hidden
              @change="onChangeProfiles"
            />
            <q-btn
              @click="onClickProfileUpload"
              color="primary"
              label="프로필 등록"
              style="width: 150px; height: 40px; border-radius:5px; position:absolute; bottom:0px;"
            >
            </q-btn>
          </div>
        </div>
        <!-- 호스트 이름 -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            stack-label
            label-slot
            outlined
            v-model="host_info.host_name"
            placeholder="호스트 명을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">호스트 이름</span>
              <br />
            </template>
          </q-input>
        </div>
      </div> 
    </div> 
    <!-- 이벤트 관련 태그 -->
    <event-tag
      @addTagItem="addOneTag"
      @removeTagItem="removeOneTag"
      :propsTagData="ref_tags"
    ></event-tag>  
    <!-- 버튼 -->
    <div class="row q-mb-md q-mt-xl float-right" style="margin-bottom: 150px;">
      <q-btn
        color="primary"
        label="등록하기"
        style="width:200px; height:50px; border-radius:5px;"
        type="submit"
      />
    </div>
  </q-form>
</template>

<script>
import EventTag from '@/components/event/EventTag';
export default {
  components: {
    EventTag,
  },
  data() {
    return {
      state: 'ready',
      state_options: [
        'ready', 'start', 'end'
      ],
      thumnail: 'https://placeimg.com/500/300/nature',
      title: '',
      category: '컨퍼런스',
      category_options: [
        '컨퍼런스', '워크샵', '해커톤', '경진대회', '모임'
      ],
      place: '',
      time: {
        start: '',
        end: '',
      },
      cost: '',
      period: {
        start: '',
        end: '',
      },
      participation: '',
      introduction: '',
      schedule: '',
      host_info: {
        host_name: '',
        profile_img: 'https://placeimg.com/500/300/nature',
      },
      ref_tags: [],
    }
  },
  methods: {
    onClickThumnailUpload() {
      this.$refs.thumnailInput.click();
    },
    onChangeThumnails(e) {
      const file = e.target.files[0];
      console.log(file);
      this.thumnail = URL.createObjectURL(file);
    },
    onClickProfileUpload() {
      this.$refs.profileInput.click();
    },
    onChangeProfiles(e) {
      const file = e.target.files[0];
      console.log(file);
      this.host_info.profile_img = URL.createObjectURL(file);
    },
    addOneTag(tagItem) {
      this.ref_tags.push(tagItem);
    },
    removeOneTag(tag, index) {
      this.ref_tags.splice(index, 1);
    },
  }
}
</script>

<style>

</style>