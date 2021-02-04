<template>
  <div class="q-pl-md">
    <q-card flat bordered style="width: 40px; height: 245px;">
      <div style="margin:0 auto; text-align:center" class="q-pt-sm">
        <q-icon
          :name="$i.ionHeartOutline"
          style="color:#727272"
          size="17px"
          class="cursor-pointer"
        ></q-icon>
        <br />
        <span>8</span>
        <br />
        <br />
        <q-icon
          :name="$i.ionChatboxEllipsesOutline"
          style="color:#727272"
          size="17px"
        ></q-icon>
        <br />
        <span>2</span>
        <br />
        <br />
        <q-icon :name="$i.ionEyeOutline" color="grey-6" size="17px"></q-icon>
        <br />
        <span>21</span>
        <br />
        <br />
        <q-icon
          :name="$i.ionBookmarkOutline"
          color="grey-6"
          size="17px"
          class="cursor-pointer"
        ></q-icon>
        <br />
        <span>3</span>
      </div>
    </q-card>
  </div>
</template>

<script>
export default {};
</script>

<style scoped></style>
