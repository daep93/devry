<template>
  <div class="row full-width">
    <q-card
      flat
      bordered
      class="q-px-lg row col-12 q-pt-xs"
      style="min-height: 300px;"
    >
      <div class="row col-12 justify-end">
        <span>
          <q-btn flat round dense icon="more_vert" class="q-mt-md">
            <q-menu>
              <q-list style="min-width: 100px">
                <q-item clickable v-close-popup>
                  <q-item-section>수정하기</q-item-section>
                </q-item>
                <q-item clickable v-close-popup>
                  <q-item-section>삭제하기</q-item-section>
                </q-item>
                <q-separator />
              </q-list>
            </q-menu>
          </q-btn>
        </span>
      </div>
      <q-card-section class="row col-12 q-py-none">
        <div class="row col-12 text-weight-bold q-mb-md">
          <span>{{ title }}</span>
        </div>
        <div class="text-subtitle2 text-grey-6 q-mb-md">
          작성 시각
        </div>
      </q-card-section>
      <q-card-section class="q-pa-none full-width">
        <div class="q-ml-md">
          태그 자리
        </div>
      </q-card-section>
      <div class="row col-12 q-px-md q-mt-lg" style="min-height: 120px;">
        <div>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum
          asperiores exercitationem distinctio vel commodi sunt. Laborum dicta
          nisi at facilis. Assumenda provident nihil possimus voluptates, sint
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum
          asperiores exercitationem distinctio vel commodi sunt. Laborum dicta
          nisi at facilis. Assumenda provident nihil possimus voluptates, sint
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum
          asperiores exercitationem distinctio vel commodi sunt. Laborum dicta
          nisi at facilis. Assumenda provident nihil possimus voluptates, sint
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum
          asperiores exercitationem distinctio vel commodi sunt. Laborum dicta
          nisi at facilis. Assumenda provident nihil possimus voluptates, sint
        </div>
        <v-md-editor v-model="content" mode="preview"> </v-md-editor>
      </div>
    </q-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: 'Add a YouTube stats widget to your iPhone with JavaScript',
      username: 'test user',
      profile_img: 'https://cdn.quasar.dev/img/avatar.png',
    };
  },
};
</script>

<style scoped></style>
