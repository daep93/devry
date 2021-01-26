<template>
  <div class="col-12" style="margin-bottom: 50px;">
    <!-- 소제목 타이틀 -->
    <div class="text-h6 text-weight-bold">Events for You</div>
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
    <!-- 이벤트 리스트 -->
    <!-- <div class="q-pa-md row items-start q-gutter-md" style="clear: both;">
      <q-card class="my-card col">
        <img src="https://cdn.quasar.dev/img/mountains.jpg">
        <q-card-actions align="right">
          <q-btn flat round color="red" icon="favorite" />
          <q-btn flat round color="teal" icon="bookmark" />
          <q-btn flat round color="primary" icon="share" />
        </q-card-actions>
      </q-card>
      <q-card class="my-card col">
        <img src="https://cdn.quasar.dev/img/mountains.jpg">
        <q-card-actions align="right">
          <q-btn flat round color="red" icon="favorite" />
          <q-btn flat round color="teal" icon="bookmark" />
          <q-btn flat round color="primary" icon="share" />
        </q-card-actions>
      </q-card>
      <q-card class="my-card col">
        <img src="https://cdn.quasar.dev/img/mountains.jpg">
        <q-card-actions align="right">
          <q-btn flat round color="red" icon="favorite" />
          <q-btn flat round color="teal" icon="bookmark" />
          <q-btn flat round color="primary" icon="share" />
        </q-card-actions>
      </q-card>
    </div> -->
    <!-- 이벤트 목록 -->
    <!-- <div class="q-pa-sm" style="clear: both;">
      <div class="row justify-center q-gutter-sm">
        <q-intersection
          v-for="index in 3"
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
    </div> -->
    <div class="q-pa-md" style="clear: both;">
      <div class="q-gutter-y-md" style="max-width: 1500px">
        <q-tabs
          v-model="tab"
          inline-label
          outside-arrows
          mobile-arrows
          class="bg-white text-black"
        >
          <q-tab>
            <q-intersection
              v-for="index in 9"
              :key="index"
              once
              transition="scale"
              class="example-item"
            >
              <q-card class="q-ma-sm">
                <q-card-section>
                  <div class="q-pa-sm" style="height: 200px;">
                    <span class="text-weight-bold" style="font-size: 18px; margin-top: 20px;">Vue.js Conference</span>
                    <q-btn flat round color="primary" icon="bookmark" style="margin-left: 40px;"/>
                    <div class="text-caption float-left" style="margin-bottom: 80px;">#JavaScript #Workshop</div>
                      <div style="clear: both;">
                        <span class="text-subtitle2 text-weight-bold text-primary">2021.03.15</span>
                        <span>
                          <img
                            src="https://cdn.quasar.dev/img/mountains.jpg"
                            style="width: 50px; height: 40px; margin-left: 130px; border-radius: 10px;"
                          >
                        </span>
                      </div>
                  
                  </div>
                </q-card-section>
              </q-card>
            </q-intersection>
          </q-tab>
        </q-tabs>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
</style>