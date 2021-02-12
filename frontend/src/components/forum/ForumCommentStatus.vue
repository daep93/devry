<template>
  <div class="q-pl-md row col-12">
    <div class="row col-12">
      <q-card flat bordered style="width: 40px; height: 125px;">
        <div style="margin:0 auto; text-align:center" class="q-pt-sm">
          <template>
            <q-icon
              :name="$i.ionHeart"
              color="red"
              size="17px"
              class="cursor-pointer"
            ></q-icon>
          </template>
          <!-- <template v-else>
            <q-icon
              :name="$i.ionHeartOutline"
              style="color:#727272"
              size="17px"
              class="cursor-pointer"
              @click="checkLiked"
            ></q-icon>
          </template> -->

          <br />
          <span>5</span>
          <br />
          <br />
          <q-icon
            :name="$i.ionChatboxEllipsesOutline"
            style="color:#727272"
            size="17px"
          ></q-icon>
          <br />
          <span>0</span>
          <br />
          <br />
        </div>
      </q-card>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped></style>
