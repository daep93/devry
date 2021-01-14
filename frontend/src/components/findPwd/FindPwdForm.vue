<template>
  <div style="width:400px; height:665px; margin: 0 auto;">
    <q-icon
      :name="$i.ionCloseOutline"
      class="close-button"
      style="width:30px; height:30px; margin-left: 370px"
    >
    </q-icon>
    <div class="title text-h6 text-weight-bold">Create new password</div>
    <q-input
      class="input"
      v-model="newPwd"
      type="password"
      label="password"
      placeholder="6-12자 이내의 새로운 비밀번호를 입력해주세요"
      style="width:400px;"
      stack-label
      :dense="dense"
    />
    <q-input
      class="input"
      v-model="confirmNewPwd"
      type="password"
      label="confirm password"
      placeholder="비밀번호를 다시 한 번 입력해주세요"
      style="width:400px;"
      stack-label
      :dense="dense"
    />
    <q-btn
      :disabled="newPwd.length > 15 || newPwd.length < 6"
      class="save-button"
      color="primary"
      label="SAVE"
      style="width:400px; height:50px;"
      type="submit"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      password: '',
      newPwd: '',
      confirmNewPwd: '',
      dense: false
    }
  }
}
</script>

<style scoped>
.title {
  margin-bottom: 30px;
  padding-top: 30%;
}

.close-button {
  padding-top: 30px;
}

.input {
  margin-bottom: 25px;
}

.save-button {
  margin-top: 80px;
}

</style>