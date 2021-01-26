<template>
  <div class="col-12" style="margin-bottom: 70px;">
    <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">Tech Stack</div>
    <div>
      <label for="tech">Skills</label>
      <q-input
        outlined 
        v-model="techStack"
        id="tech"
        placeholder="보유하신 기술을 입력해주세요" 
        style="margin: 7px 0 30px 0;"
        @keypress.enter="addTechStack"
        TODO
        @keypress.enter.prevent="submitForm()"
      />
    </div>
    <ul class="row">
      <li v-for="(skill, index) in propsTechStackData" :key="index" style="margin-right: 10px; cursor: pointer;">
        <q-badge color="blue">
          {{ skill }}
          <span @click="removeTechStack(skill, index)" style="margin-left: 10px;">X</span>
        </q-badge>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ['propsTechStackData'],
  data() {
    return {
      techStack: '',
    }
  },
  methods: {
    addTechStack: function() {
      if (this.techStack !== '') {
        this.$emit('addTechStackItem', this.techStack);
        this.techStack = ''
      }
    },
    removeTechStack: function(skill, index) {
      this.$emit('removeTechStackItem', skill, index);
    },
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>