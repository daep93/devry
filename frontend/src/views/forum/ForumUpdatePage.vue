<template>
  <post-edit-form>
    <template slot="buttons" slot-scope="scopeProps">
      <q-btn
        outline
        color="red-12"
        class="text-weight-bold q-px-xl q-py-sm q-mr-md"
        label="삭제하기"
        size="md"
        @click="scopeProps.deleteForum"
      />
      <q-btn
        color="blue-12"
        class="text-weight-bold q-px-xl q-py-sm"
        label="작성하기"
        size="md"
        @click="scopeProps.updateForum"
      />
    </template>
  </post-edit-form>
</template>

<script>
import PostEditForm from '@/components/common/PostEditForm';

export default {
  components: {
    PostEditForm,
  },
  async created() {
    this.$store.commit('offLeft');
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
.preview-shadow {
  box-shadow: 0 2px 12px 0 rgb(0 0 0 / 10%);
}
</style>
