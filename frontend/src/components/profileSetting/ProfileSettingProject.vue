<template>
  <div class="col-12" style="margin-bottom: 70px;">
    <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">Project URL</div>
    <label for="project">project(최대 3개까지 입력가능)</label>
    <div id="project" class="row" style="margin: 7px 0 30px 0; display:flex; justify-content:space-between;">
      <div class="col-4">
        <q-input 
          outlined 
          v-model="pjtName"
          placeholder="프로젝트 이름을 입력해주세요" 
        />
      </div>
      <div class="col-6">
        <q-input 
          outlined 
          v-model="pjtUrl"
          placeholder="프로젝트 URL을 입력해주세요" 
        />
      </div>
      <q-btn
        padding="xs"
        color="primary"
        icon="add"
        style="width:60px;"
        @click="addProject"
      />
    </div>
    <ul v-for="(project, index) in propsProjectData" :key="index">
      <li v-if="index < 3">
        <q-btn color="primary" size="sm">
          {{ project.project_name }} [{{ project.project_url }}]
          <span @click="removeProject(project, index)" style="margin-left: 10px;">
            <q-icon :name="$i.ionTrash"></q-icon>
          </span>
        </q-btn>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ['propsProjectData'],
  data() {
    return {
      pjtName: '',
      pjtUrl: '',
    }
  },
  methods: {
    addProject: function(project, index) {
      if (this.pjtUrl !== '' && this.pjtName !== '') {
        this.$emit('addProjectItem', this.pjtUrl, this.pjtName);
        this.pjtName = '',
        this.pjtUrl = ''
      }
    },
    removeProject: function(project, index) {
      this.$emit('removeProjectItem', project, index)
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