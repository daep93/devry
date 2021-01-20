<template>
  <div style="margin-bottom: 70px;">
    <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">Tech Stack</div>
    <div>
      <label for="tech">Skills</label>
      <q-input
        outlined 
        v-model="skill"
        id="tech"
        placeholder="보유하신 기술을 입력해주세요" 
        style="width:730px; margin: 7px 0 30px 0;"
        @keypress.enter="addSkill"
        :dense="dense" 
      />
    </div>
    <ul>
      <li v-for="item in skills" :key="item">
        <q-badge color="blue">
          {{ item.skill }}
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
    addSkill: function() {
      this.skills.push({
        skill: this.skill
      })
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