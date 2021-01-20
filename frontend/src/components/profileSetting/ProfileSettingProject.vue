<template>
  <div style="margin-bottom: 70px;">
    <div class="text-h6 text-weight-bold" style="margin-bottom: 40px;">Project URL</div>
    <label for="project">project</label>
    <div class="row" style="width:730px; margin: 7px 0 30px 0; display:flex; justify-content:space-between;">
      <div id="project">
        <q-input 
          outlined 
          v-model="ph"
          placeholder="프로젝트 이름을 입력해주세요" 
          style="width:250px;"
          :dense="dense" 
        />
      </div>
      <div>
        <q-input 
          outlined 
          v-model="ph"
          placeholder="프로젝트 URL을 입력해주세요" 
          style="width:400px;"
          :dense="dense" 
        />
      </div>
      <q-btn
        padding="xs"
        color="primary"
        icon="add"
        style="width:60px;"
        :click="addForm"
      />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      addFormArea: '',
      project: []
    }
  },
  methods: {
    addForm: function() {
      this.addFormArea.push({
        
      })
    }
  }
}
</script>

<style>

</style>