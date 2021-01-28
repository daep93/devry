<template>
  <div class="row justify-center q-ml-md q-mt-lg">
    <div class="row col-8">
      <div class="text-h4 text-weight-bold q-mb-lg col-12">Forum 게시판</div>
      <div class="row justify-between col-12">
        <!-- tab 라벨 -->
        <q-tabs
          v-model="tab"
          no-caps
          dense
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          narrow-indicator
        >
          <q-tab name="feed" label="Feed" />
          <q-tab name="latest" label="Latest" />
        </q-tabs>
        <!-- 서치바, 태그 버튼 -->
        <div class="row justify-end q-gutter-lg">
          <q-input v-model="search" type="search" outlined>
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
      <!-- 탭 시작 -->
      <ForumList :tab="tab"></ForumList>
    </div>
  </div>
</template>

<script>
import ForumList from '@/components/forum/ForumList';

export default {
  data() {
    return {
      tab: 'feed',
    };
  },
  components: {
    ForumList,
  },
};
</script>

<style scoped>
.q-tab >>> .q-tab__label {
  font-size: 13pt;
  font-weight: bold;
}
.q-input >>> .q-icon {
  size: 5px;
}
.q-input >>> .q-field__control {
  height: 40px;
}
.q-input >>> .q-field__append {
  height: 40px;
}
.tag-filter {
  height: 38px;
  margin-left: 15px;
}
</style>
