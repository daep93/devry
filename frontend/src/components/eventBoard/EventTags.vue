<template>
  <div class="col-12" style="margin-bottom: 50px;">
    <div class="text-h6 text-weight-bold" style="margin-bottom: 30px;">Tags</div>
      <div>
        <ul class="row">
          <li v-for="(tag, index) in tags" :key="index" style="margin-right: 10px; cursor: pointer;">
            <q-chip v-if="index !== 0 && tag !== 'end'" square color="primary" text-color="white">
              <q-avatar icon="local_offer" />
              {{ tag }}
              <span @click="removeTag(tag, index)" style="margin-left: 10px;">X</span>
            </q-chip>
            <q-chip v-else-if="index === 0" square color="black" text-color="white">
              <q-avatar icon="local_offer" />
              {{ tag }}
            </q-chip>
            <!-- 태그 추가 버튼 -->
            <q-chip @click="addTag" v-else-if="tag === 'end'" outline square color="primary" style="width: 100px;">
              <q-avatar icon="add" style="margin: 0 auto;"/>
              <q-menu style="width: 200px; heigth: 300px;">
                <div class="row no-wrap q-pa-md">
                  <q-input
                    outlined 
                    v-model="tagItem"
                    id="tag"
                    placeholder="팔로우할 태그를 입력해주세요" 
                    style="margin: 7px 0 30px 0; width: 300px;" 
                    @keypress.enter="createTag"
                  />
                </div>
                <ul class="row">
                  <li v-for="(tag, index) in tags" :key="index" style="margin-right: 10px; cursor: pointer;">
                    <q-chip v-if="index !== 0 && tag !== 'end'" square color="primary" text-color="white">
                      <q-avatar icon="local_offer" />
                      {{ tag }}
                      <span @click="removeTag(tag, index)" style="margin-left: 10px;">X</span>
                    </q-chip>
                  </li>
                </ul>  
              </q-menu>
            </q-chip>
          </li>
        </ul>
      </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tags: ['ALL', 'Vue.js', 'Python', 'JavaScript', 'React', 'end']
    }
  },
  methods: {
    // removeTag: function() {

    // }
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>