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
            style="height: 215px;"
            class="rounded-borders col-8"
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
              class="float-right"
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
            v-model="sdata"
            placeholder="이벤트 시작일을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">시작일</span>
              <br />
            </template>
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
                  <q-date v-model="sdata">
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
            v-model="edata"
            placeholder="이벤트 종료일을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">종료일</span>
              <br />
            </template>
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
                  <q-date v-model="edata">
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
            v-model="stime"
            placeholder="시작 시간을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">시작시간</span>
              <br />
            </template>
            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy transition-show="scale" transition-hide="scale">
                  <q-time v-model="stime">
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
            v-model="etime"
            placeholder="종료 시간을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">종료시간</span>
              <br />
            </template>
            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy transition-show="scale" transition-hide="scale">
                  <q-time v-model="etime">
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
            v-model="location"
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
            type="textarea"
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
        <!-- 이벤트 등록 url -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            stack-label
            label-slot
            outlined
            v-model="host_info.register_url"
            placeholder="이벤트 등록을 위한 url을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">이벤트 등록 URL</span>
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
          v-if="this.$route.params.id !== undefined"
          outline
          color="red-12"
          class="text-weight-bold q-px-xl q-py-sm q-mr-md"
          label="삭제하기"
          size="md"
          @click="deleteEvent"
      />
      <q-btn
        color="blue-12"
        label="등록하기"
        class="text-weight-bold q-px-xl q-py-sm"
        size="md"
        type="submit"
      />
    </div>
  </q-form>
</template>

<script>
import EventTag from '@/components/event/EventTag';
import { loadEventItem, createEventItem, updateEventItem, deleteEventItem } from '@/api/eventRegistration';

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
      location: '',
      sdata: '',
      edata: '',
      stime: '',
      etime: '',
      cost: '',
      participation: '',
      introduction: '',
      schedule: '',
      host_info: {
        host_name: '',
        profile_img: 'https://placeimg.com/500/300/nature',
        register_url: '',
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
    async submitForm() {
      // 날짜 형식 변경
      const sArray = this.sdata.split('/')
      const start_date = sArray[0]+'-'+sArray[1]+'-'+sArray[2]
      const eArray = this.edata.split('/')
      const end_date = eArray[0]+'-'+eArray[1]+'-'+eArray[2]
      // id 가져오기
      const post_id = this.$route.params.id;
      try {
        this.$q.loading.show();
        // 이벤트 새로 생성하기
        if (post_id === undefined) {
          await createEventItem({
            // 넘길 데이터 적어주기
            state: this.state,
            thumnail: this.thumnail,
            title: this.title,
            category: this.category,
            location: this.location,
            sdata: start_date,
            edata: end_date,
            stime: this.stime,
            etime: this.etime,
            cost: this.cost,
            participation: this.participation,
            introduction: this.introduction,
            schedule: this.schedule,
            host_info: this.host_info,
            ref_tags: this.ref_tags,
          })
        }
        // 이벤트 수정하기
        else {
          await updateEventItem(post_id, {
            // 넘길 데이터 적어주기
            state: this.state,
            thumnail: this.thumnail,
            title: this.title,
            category: this.category,
            location: this.location,
            sdata: start_date,
            edata: end_date,
            stime: this.stime,
            etime: this.etime,
            cost: this.cost,
            participation: this.participation,
            introduction: this.introduction,
            schedule: this.schedule,
            host_info: this.host_info,
            ref_tags: this.ref_tags,
          })
        }
        console.log('데이터 넘어갔나?')
        // 이동 시킬 페이지 적어주기(이벤트 게시판)
        this.$router.push({ path: '/event' });
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    // 이벤트 삭제하기
    async deleteEvent() {
      try {
        const post_id = this.$route.params.id;
        this.$q.loading.show();
        await deleteEventItem(post_id);
        this.$router.push({ path: '/event' });
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  // Event 수정하기 (데이터 받아오기)
  async created() {
    // id 가져오기
    const post_id = this.$route.params.id;
    // post_id가 존재할 경우에 기존 정보 가져오기
    if (post_id !== undefined) {
      try {
        this.$q.loading.show();
        const { data } = await loadEventItem(post_id);
        // 날짜 형식 변환
        const sArray = data.sdata.split('-')
        const start_date = sArray[0]+'/'+sArray[1]+'/'+sArray[2]
        const eArray = data.edata.split('-')
        const end_date = eArray[0]+'/'+eArray[1]+'/'+eArray[2]
        // 가져올 데이터 목록
        this.state = data.state;
        this.thumnail = data.thumnail;
        this.title = data.title;
        this.category = data.category;
        this.location = data.location;
        this.sdata = start_date;
        this.edata = end_date;
        this.stime = data.stime;
        this.etime = data.etime;
        this.cost = data.cost;
        this.participation = data.participation;
        this.introduction = data.introduction;
        this.schedule = data.schedule;
        this.host_info = data.host_info;
        this.ref_tags = data.ref_tags;
      } catch (error) {
        console.log(error);
        // alert('에러가 발생했습니다.)
      } finally {
        this.$q.loading.hide();
      }
    }
  },
}
</script>

<style>

</style>