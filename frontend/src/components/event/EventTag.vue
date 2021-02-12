<template>
  <div class="full-width q-mb-xl">
    <div class="text-h6 text-weight-bold q-mb-sm">
      Related Tags
    </div>
    <div class="row full-width q-mb-sm">
      <q-input
        outlined
        stack-label
        label-slot
        v-model="tagItem"
        placeholder=" 태그를 입력해주세요"
        @keypress.enter="createTag"
        class="col-11"
      >
        <template v-slot:label>
          <span class="text-primary">
            태그
          </span>
          <br />
        </template>
      </q-input>
      <div class="col-1 q-pl-sm row justify-end items-center">
        <q-btn
          class="overflow-auto"
          color="primary"
          icon="add"
          @click="createTag"
          style="height:100%"
        />
      </div>
    </div>
    <div>
      <ul class="row q-gutter-sm">
        <li
          v-for="(tag, index) in propsTagData"
          :key="index"
          class="cursor-pointer"
        >
          <q-badge
            class="text-black q-pa-sm shadow-3"
            :style="{
              'background-color': tagColor(tag),
            }"
          >
            # {{ tag }}
            <span @click="removeTag(tag, index)" class="q-ml-sm">X</span>
          </q-badge>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import {
  colorSoloMapper,
  // matchingColorSoloMapper,
} from '@/utils/tagColorMapper';

export default {
  props: ['propsTagData'],
  data() {
    return {
      tagItem: '',
    };
  },
  methods: {
    createTag: function() {
      if (this.tagItem !== '') {
        this.$emit('addTagItem', this.tagItem);
        this.tagItem = '';
      }
    },
    removeTag: function(tag, index) {
      this.$emit('removeTagItem', tag, index);
    },
    tagColor(tag) {
      return colorSoloMapper(tag, 0.5);
    },
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>
