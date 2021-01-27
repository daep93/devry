<template>
  <div class="row col-12">
    <div class="row justify-between  col-12">
      <q-tabs
        dens
        v-model="sort"
        style="color:#3B77AF"
        class="row justify-start"
      >
        <q-tab name="latest" label="최신순" />
        <q-tab name="orderByComment" label="댓글순" />
        <q-tab name="orderByRecommend" label="추천순" />
      </q-tabs>
      <div class="row justify-end q-gutter-lg">
        <q-input v-model="search" type="search" class="q-mb-sm" outlined>
          <template v-slot:append>
            <q-icon :name="$i.ionSearchOutline" />
          </template>
        </q-input>
        <q-btn
          class="tag-filter"
          outline
          color="primary"
          @click="$store.commit('toggleTagFilter')"
          >태그 선택</q-btn
        >
      </div>
    </div>
    <div class="row q-mt-md col-12">
      <qna-entity
        v-for="item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
        :key="item"
      ></qna-entity>
    </div>
  </div>
</template>

<script>
import QnaEntity from '@/components/qna/QnaEntity.vue';
export default {
  components: {
    QnaEntity,
  },
  data() {
    return {
      sort: 'latest',
      search: '',
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
.tag-filter {
  height: 40px;
}
</style>
