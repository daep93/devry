<template>
  <div
    class="row q-mb-sm"
    style="width:100%; border: 1px solid #C1B9B9; border-radius: 8px"
  >
    <div class="col-2">
      <q-img
        :src="require('@/assets/keyboard.png')"
        alt="change-password"
        style="height:120px; clip: inherit;"
      ></q-img>
    </div>
    <div class="col-10 q-pl-sm">
      <div class="row justify-between q-pt-xs">
        <div class="row items-baseline">
          <div class="q-mr-sm text-weight-regular">@Go ssafy</div>
          <div class="text-weight-thin" style="font-size:8pt">
            Jan 17(15 hours)
          </div>
        </div>
        <div class="row">
          <div class="row items-center q-mr-sm">
            <q-icon
              :name="$i.ionHeart"
              color="red"
              size="30px"
              class="q-mr-sm"
            ></q-icon>
            <span>30</span>
          </div>
          <div class="row items-center q-mr-md">
            <q-icon
              :name="$i.ionChatboxEllipsesOutline"
              style="color:#617E9F"
              size="30px"
              class="q-mr-sm"
            ></q-icon>
            <span>6</span>
          </div>
          <div></div>
        </div>
      </div>
      <div class="text-bold" style="font-size:14pt">
        React interview questions and answers for JS developers
      </div>
      <div class="row justify-end items-end">
        <q-btn
          dense
          rounded
          v-for="item in tags"
          :key="item.tagName"
          class="q-mb-sm q-mr-sm text-grey-2"
          :style="{ 'background-color': item.tagColor }"
          style="font-size:8pt"
          >{{ item.tagName }}</q-btn
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tags: [
        { tagName: '#vue', tagColor: '#41B883' },
        { tagName: '#javascript', tagColor: '#F7BF33' },
        { tagName: '#react', tagColor: '#36A8FD' },
        { tagName: '#Angular', tagColor: '#B52E31' },
      ],
    };
  },
};
</script>

<style scoped></style>
