<template>
  <div style="margin-bottom: 50px;">
    <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">Following Tags</div>
    <div>
      <label for="tag">tags</label>
      <q-input
        outlined 
        v-model="tagItem"
        id="tag"
        placeholder="팔로우할 태그를 입력해주세요" 
        style="width:730px; margin: 7px 0 30px 0;" 
        @keypress.enter="createTag"
      />
    </div>
    <div>
      <ul class="row">
        <li v-for="(tag, index) in tags" :key="index" style="margin-right: 10px;">
          <q-badge color="primary">
            # {{ tag }}
            <span :click="removeTag" style="margin-left: 10px;">X</span>
          </q-badge>
        </li>
        <!-- <li v-for="(tag, index) in tags" :key="index"># {{ tag }}
          <span :click="removeTag(tag, index)">X</span>
        </li> -->
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tagItem: '',
      tags: [],
    }
  },
  methods: {
    createTag: function() {
      if (this.tagItem !== '') {
        console.log(this.tagItem)
        localStorage.setItem(this.tagItem, JSON.stringify(this.tagItem))
        this.tagItem = ''
      }
    },
    removeTag: function(tag, index) {
      console.log(tag, index);
      localStorage.removeItem(tag);
      this.tags.splice(index, 1);
    }
  },
  created: function() {
    if (localStorage.length > 0) {
      for (var i = 0; i < localStorage.length ; i ++) {
        this.tags.push(JSON.parse(localStorage.getItem(localStorage.key(i))));
      }
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