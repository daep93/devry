<template>
  <div class="col-12" style="margin-bottom: 70px;">
    <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">Tech Stack</div>
    <div>
      <label for="tech">Skills</label>
      <q-input
        outlined 
        v-model="skill"
        id="tech"
        placeholder="보유하신 기술을 입력해주세요" 
        style="margin: 7px 0 30px 0;"
        @keypress.enter="addTechStack"
        :dense="dense" 
      />
    </div>
    <ul class="row">
      <li v-for="item in skills" :key="item" style="margin-right: 10px;">
        <q-badge color="blue">
          {{ item.skill }}
          <span @click="removeTechStack" style="margin-left: 10px;">X</span>
        </q-badge>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      skill: '',
      skills: []
    }
  },
  methods: {
    addTechStack: function() {
      if (this.skill !== '') {
        this.skills.push({skill: this.skill})
        this.$emit('addTechStackItem', this.skill);
        this.skill = ''
      }
    },
    removeTechStack: function(form, index) {
      this.skills.splice(index, 1)
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