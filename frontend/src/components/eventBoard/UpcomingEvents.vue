<template>
<div>
  <!-- 소제목 타이틀 -->
  <div class="text-h6 text-weight-bold">Upcoming Events</div>
  <!-- 이벤트 카테고리 -->
  <div class="q-pa-md float-right">
    <q-btn-dropdown color="black" label="Category">
      <q-list>
        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>conference</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>workshop</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>hackathon</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </div>
  <!-- 이벤트 목록 -->
  <div class="q-pa-sm" style="clear: both;">
    <div class="row justify-center q-gutter-sm">
      <q-intersection
        v-for="index in 27"
        :key="index"
        once
        transition="scale"
        class="example-item"
      >
        <q-card class="q-ma-sm">
          <q-card-section>
            <div class="q-pa-sm" style="height: 200px;">
              <span class="text-weight-bold" style="font-size: 18px; margin-top: 20px;">Vue.js Conference</span>
              <q-btn flat round color="primary" icon="bookmark" style="margin-left: 27px;"/>
              <div class="text-caption" style="margin-bottom: 80px;">#JavaScript #Workshop</div>
              <div>
                <span class="text-subtitle2 text-weight-bold text-primary">2021.03.15</span>
                <span>
                  <img
                    src="https://cdn.quasar.dev/img/mountains.jpg"
                    style="width: 50px; height: 40px; margin-left: 100px; border-radius: 10px;"
                  >
                </span>
              </div>
            </div>
          </q-card-section>
        </q-card>
      </q-intersection>
    </div>
  </div>
</div>
</template>

<script>
export default {

}
</script>

<style scoped>
.example-item {
  height: 290px;
  width: 290px;
}
</style>