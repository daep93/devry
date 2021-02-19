<template>
  <post-edit-form category="qna">
    <template slot="buttons" slot-scope="scopeProps">
      <q-btn
        outline
        color="blue-12"
        class="text-weight-bold q-px-xl q-py-sm q-mr-md"
        label="임시저장"
        size="md"
      />
      <q-btn
        color="blue-12"
        class="text-weight-bold q-px-xl q-py-sm"
        label="작성하기"
        size="md"
        @click="scopeProps.createQna"
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
  methods: {},
  created() {
    this.$store.commit('offLeft');
  },
};
</script>

<style scoped></style>
