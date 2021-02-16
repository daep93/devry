<template>
  <div class="full-width q-mb-xl">
    <div class="text-h6 text-weight-bold q-mb-md">
      Tech Stack
    </div>
    <div class="full-width row q-mb-sm">
      <q-input
        class=" col-11"
        outlined
        stack-label
        label-slot
        v-model="techStack"
        placeholder="보유하신 기술을 입력해주세요"
        @keypress.enter.prevent="addTechStack"
      >
        <template v-slot:label>
          <span class="text-primary">
            Skills/Language
          </span>
          <br />
        </template>
      </q-input>
      <div class="col-1 q-pl-sm row justify-end items-center">
        <q-btn
          class="overflow-auto"
          color="primary"
          icon="add"
          @click="addTechStack"
          style="height:100%"
        />
      </div>
    </div>
    <ul class="row q-gutter-sm">
      <li
        v-for="(skill, index) in propsTechStackData"
        :key="index"
        class="cursor-pointer"
      >
        <q-badge color="light-blue-8" class="q-pa-sm shadow-3">
          {{ skill }}
          <span @click="removeTechStack(skill, index)" class="q-ml-sm">X</span>
        </q-badge>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    propsTechStackData: Array,
  },
  data() {
    return {
      techStack: '',
      techStacks: [],
    };
  },
  methods: {
    addTechStack: function() {
      if (this.techStack !== '') {
        this.$emit('addTechStackItem', this.techStack);
        this.techStack = '';
      }
    },
    removeTechStack: function(skill, index) {
      this.$emit('removeTechStackItem', skill, index);
    },
  },
  watch: {
    propsTechStackData(newValue) {
      console.log(newValue);
      this.techStacks = newValue;
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
