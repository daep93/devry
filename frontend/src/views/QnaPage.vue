<template>
  <div class="row justify-center q-pt-lg ">
    <tag-filter></tag-filter>
    <div class="row col-8 justify-center q-pl-lg">
      <div class="row  q-mb-sm items-end col-12">
        <div class="text-h5 text-weight-bold ">QnA 게시판</div>
      </div>
      <div class="row justify-between  col-12">
        <q-tabs dens v-model="sort" style="color:#3B77AF">
          <q-tab name="latest" label="최신순" />
          <q-tab name="orderByComment" label="댓글순" />
          <q-tab name="orderByRecommend" label="추천순" />
        </q-tabs>
        <q-input v-model="search" type="search" class="q-mb-sm" outlined>
          <template v-slot:append>
            <q-icon :name="$i.ionSearchOutline" />
          </template>
        </q-input>
      </div>
      <div class="row  q-mt-md col-12">
        <qna-entity
          v-for="item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
          :key="item"
        ></qna-entity>
      </div>
      <div class="row q-mt-sm col-12 q-mb-xl justify-between">
        <div class="col-9 row q-py-xs">
          <div class="row col-2 q-pb-xs q-mr-md">
            <div
              class="row col-12 shadow-1 overflow-hidden"
              style="border-radius:5px;"
            >
              <div class="col-2" style="background-color:#1976D2"></div>
              <div class="col-10 text-center">답변 완료</div>
            </div>
          </div>
          <div class="row col-2 q-pb-xs">
            <div
              class="row col-12 shadow-1 overflow-hidden"
              style="border-radius:5px;"
            >
              <div class="col-2" style="background-color:#C8DAFE"></div>
              <div class="col-10 text-center">답변 대기</div>
            </div>
          </div>
        </div>
        <div class="col-3 row justify-end">
          <q-pagination
            v-model="current"
            color="grey"
            :max="5"
            :boundary-links="true"
          >
          </q-pagination>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TagFilter from '@/components/qna/TagFilter';
import QnaEntity from '@/components/qna/QnaEntity.vue';
export default {
  components: {
    TagFilter,
    QnaEntity,
  },
  data() {
    return {
      sort: 'latest',
      current: '3',
    };
  },
};
</script>

<style scoped>
.q-input >>> .q-field__control {
  height: 40px;
}
.q-input >>> .q-field__append {
  height: 40px;
}
</style>
