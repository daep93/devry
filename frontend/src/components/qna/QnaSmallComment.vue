<template>
  <div class="row col-12">
    <div v-for="(data, index) in answers" :key="index" class="row col-12">
      <div class="row col-12">
        <q-separator />
        <div class="row col-12 q-py-sm">
          <div class="row col-12 justify-between">
            <div class="row col-10">
              <span class="q-mr-xs">1.</span>
              <span class="q-mr-sm" style="color: blue">
                @{{ data.username }}
              </span>
              <span class="text-caption" style="color: gray">11분 전</span>
            </div>
            <div class="q-pl-xl row col-2">
              <div class="row items-center">
                <div v-if="data.liked" class="q-mr-xs q-ml-xl">
                  <q-icon
                    :name="$i.ionHeartOutline"
                    style="color:#727272"
                    size="17px"
                    class="cursor-pointer"
                    @click="checkLiked(index)"
                  ></q-icon>
                </div>
                <div v-else class="q-mr-xs q-ml-xl">
                  <q-icon
                    :name="$i.ionHeart"
                    color="red"
                    size="17px"
                    class="cursor-pointer"
                    @click="checkLiked(index)"
                  ></q-icon>
                </div>
                <div class="text-body2 q-pt-xs">
                  {{ data.like_num }}
                </div>
              </div>
            </div>
          </div>
          <div class="q-ml-lg q-py-xs row col-12">
            {{ data.contents }}
          </div>
        </div>
      </div>
    </div>
    <q-separator />
    <div class="q-mt-sm row col-12">
      <q-input borderless v-model="text" placeholder="댓글을 입력해주세요" />
    </div>
    <div class="row col-12">
      <div class="row col-10"></div>
      <div class="row col-2 q-pl-xl q-mb-lg">
        <q-btn color="primary" label="댓글 추가" size="sm" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      answers: [
        {
          contents: 'this is test small comment 1',
          userid: 1,
          username: 'test1',
          written_time: '2021-01-25T03:02',
          liked: true,
          like_num: 3,
        },
        {
          contents: 'this is test small comment 22',
          userid: 2,
          username: 'test2',
          written_time: '2021-01-25T03:02',
          liked: false,
          like_num: 1,
        },
      ],
    };
  },
  methods: {
    checkLiked(index) {
      for (const heart of this.answers) {
        if (this.answers.indexOf(heart) === index) {
          heart.liked = !heart.liked;
          if (heart.liked) {
            heart.like_num = heart.like_num - 1;
          } else {
            heart.like_num = heart.like_num + 1;
          }
        }
      }
    },
  },
};
</script>

<style scoped></style>
