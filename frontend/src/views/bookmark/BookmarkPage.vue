<template>
  <div class="row justify-center q-pt-lg ">
    <div class="row col-8 justify-center q-pl-lg">
      <div class="row q-mb-sm q-mb-lg col-12 text-h5 text-weight-bold">
        <div class="row col-9">
          <span>
            <q-icon :name="$i.ionBookmarkOutline" size="sm"></q-icon
          ></span>
          <span class="text-h5 text-weight-bold q-ml-xs">My Bookmark</span>
        </div>
      </div>

      <div class="row col-12">
        <q-tabs
          v-model="tab"
          dense
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
          <q-tab name="qna" label="QnA" no-caps />
          <q-tab name="forum" label="포럼" />
          <q-tab name="event" label="이벤트" />
        </q-tabs>

        <q-tab-panels v-model="tab" animated class="row col-12">
          <q-tab-panel name="qna">
            <div class="row col-12 q-mb-lg">
              <q-card class="row col-10 q-pa-lg" style="min-height: 200px">
                <qna-bookmark></qna-bookmark>
              </q-card>
            </div>
          </q-tab-panel>

          <q-tab-panel name="forum">
            <div class="row col-12 q-mb-lg">
              <q-card class="row col-10 q-pa-lg" style="min-height: 200px">
                <forum-bookmark></forum-bookmark>
              </q-card>
            </div>
          </q-tab-panel>

          <q-tab-panel name="event">
            <div class="row col-12 q-mb-lg">
              <q-card class="row col-10 q-pa-lg" style="min-height: 200px">
                <event-bookmark></event-bookmark>
              </q-card>
            </div>
          </q-tab-panel>
        </q-tab-panels>
      </div>
    </div>
  </div>
</template>

<script>
import QnaBookmark from '@/components/bookmark/QnaBookmark';
import ForumBookmark from '@/components/bookmark/ForumBookmark';
import EventBookmark from '@/components/bookmark/EventBookmark';

export default {
  components: {
    QnaBookmark,
    ForumBookmark,
    EventBookmark,
  },
  data() {
    return {
      tab: 'qna',
    };
  },
  async created() {
    this.$store.commit('onLeft');
  },
};
</script>

<style scoped></style>
