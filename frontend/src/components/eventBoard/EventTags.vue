<template>
  <div class="col-12" style="margin-bottom: 50px;">
    <div class="text-h6 text-weight-bold" style="margin-bottom: 20px;">Tags</div>
      <div>
        <ul class="row">
          <li v-for="(tag, index) in tags" :key="index" style="margin-right: 10px; cursor: pointer;">
            <q-chip v-if="tag.tagName !== 'ALL' && tag.tagName !== 'end'" outline square :style="{ 'color' : tag.tagColor }">
              <q-avatar icon="local_offer" />
              {{ tag.tagName }}
              <span @click="removeTag(tag, index)" style="margin-left: 10px;">X</span>
            </q-chip>
            <q-chip v-else-if="index === 0" square color="black" text-color="white">
              <q-avatar icon="local_offer" />
              {{ tag.tagName }}
            </q-chip>
            <!-- 태그 추가 버튼 -->
            <q-chip @click="addTag" v-else-if="tag.tagName === 'end'" square color="primary" style="width: 100px;">
              <q-avatar icon="add" style="margin: 0 auto; color: white;"/>
              <q-menu style="width: 200px; heigth: 300px;">
                <div class="row no-wrap q-pa-md">
                  <q-input
                    outlined 
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
                      {{ tag.tagName }}
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
      tags: [
        { tagName: 'ALL', tagColor: '#000000'},
        { tagName: 'Vue.js', tagColor: '#2F9D27'},
        { tagName: 'Python', tagColor: '#CC3D3D'},
        { tagName: 'JavaScript', tagColor: '#F29661'},
        { tagName: 'React', tagColor: '#4641D9'},
        { tagName: 'end', tagColor: '#008299S'},
      ],
    }
  },
  methods: {
    removeTag: function() {

    },
    addTag: function() {
      
    }
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>