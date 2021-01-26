<template>
  <div class="col-12" style="margin-bottom: 50px;">
    <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">Following Tags</div>
    <div>
      <label for="tag">tags</label>
      <q-input
        outlined 
        v-model="tagItem"
        id="tag"
        placeholder="팔로우할 태그를 입력해주세요" 
        style="margin: 7px 0 30px 0;" 
        @keypress.enter="createTag"
        TODO
        @keypress.enter.prevent="submitForm()"
      />
    </div>
    <div>
      <ul class="row">
        <li v-for="(tag, index) in propsTagData" :key="index" style="margin-right: 10px; cursor: pointer;">
          <q-badge color="primary">
            # {{ tag }}
            <span @click="removeTag(tag, index)" style="margin-left: 10px;">X</span>
          </q-badge>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: ['propsTagData'],
  data() {
    return {
      tagItem: '',
    }
  },
  methods: {
    createTag: function() {
      if (this.tagItem !== '') {
        this.$emit('addTagItem', this.tagItem);
        this.tagItem = ''
      }
    },
    removeTag: function(tag, index) {
      this.$emit('removeTagItem', tag, index);
    }
  },
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>