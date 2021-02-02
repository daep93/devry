<template>
  <div class="row col-12">
    <q-card flat bordered class="my-card q-px-lg q-pt-lg row col-12">
      <div class="row col-12">
        <!-- 답변 상태 표기 -->
        <div
          class="row col-2 q-pl-md q-pb-md"
          v-for="(color, msg) in {
            '답변 완료': '#1976D2',
          }"
          :key="msg"
        >
          <div
            class="row col-12 shadow-1 overflow-hidden"
            style="border-radius:5px; max-width: 100px;"
          >
            <div class="col-2" :style="{ 'background-color': color }"></div>
            <div class="col-10 text-center">{{ msg }}</div>
          </div>
        </div>
      </div>

      <q-card-section class="row col-12">
        <div class="text-h4 text-weight-bold">
          Lorem, ipsum dolor sit amet consectetur
        </div>
      </q-card-section>
      <div class="row col-12 q-ml-sm">
        <span v-for="i in 3" :key="i" class="q-ml-sm">
          <q-badge color="blue">
            # Vue
          </q-badge>
        </span>
      </div>
      <br />
      <br />

      <q-card-section class="row col-12">
        <div class="text-h5">This is my question</div>
        <br />
        <br />
        <div class="text-body2 row col-12">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Odio,
          dignissimos. Numquam fuga suscipit facilis at quia repellendus
          nesciunt voluptate totam in fugit nobis accusantium sit quos sed
          placeat temporibus inventore nostrum alias eius porro soluta
          laudantium eum, nulla dolores! Hic amet alias ex voluptatem obcaecati
          commodi provident vel facilis laboriosam. Dolorum laudantium ut atque
          sint, reprehenderit sit aspernatur excepturi reiciendis voluptatum
          iste consectetur fugiat eius odio necessitatibus et officia quos.
          Aperiam quam pariatur illo optio praesentium ipsam aliquam accusamus
          magni inventore officiis impedit natus laborum eligendi doloribus
          libero, molestiae quae incidunt mollitia, nostrum tenetur amet ab in
          enim. Nihil, aut.
          <br /><br />
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Odio,
          dignissimos. Numquam fuga suscipit facilis at quia repellendus
          nesciunt voluptate totam in fugit nobis accusantium sit quos sed
          placeat temporibus inventore nostrum alias eius porro soluta
          laudantium eum, nulla dolores! Hic amet alias ex voluptatem obcaecati
          commodi provident vel facilis laboriosam. Dolorum laudantium ut atque
          sint, reprehenderit sit aspernatur excepturi reiciendis voluptatum
          iste consectetur fugiat eius odio necessitatibus et officia quos.
          Aperiam quam pariatur illo optio praesentium ipsam aliquam accusamus
          magni inventore officiis impedit natus laborum eligendi doloribus
          libero, molestiae quae incidunt mollitia, nostrum tenetur amet ab in
          enim. Nihil, aut.
        </div>
      </q-card-section>
      <q-card-section class="row col-12">
        <qna-small-comment></qna-small-comment>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import QnaSmallComment from '@/components/qna/QnaSmallComment';

export default {
  components: {
    QnaSmallComment,
  },
  data: function() {
    return {
      msg: true,
    };
  },
};
</script>

<style scoped>
.icon-position {
  float: right;
}
</style>
