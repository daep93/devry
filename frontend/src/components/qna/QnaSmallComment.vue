<template>
  <div class="row col-12">
    <div class="row col-12">
      <q-separator />
      <div class="row col-12 q-py-sm">
        <div class="row col-12 justify-between">
          <div class="row col-9">
            <span class="q-mr-xs">1.</span>
            <span class="q-mr-sm" style="color: blue">
              @user
            </span>
            <span class="text-caption" style="color: gray">11분 전</span>
          </div>
          <div class="q-pl-xl row col-3">
            <div class="icon-position q-mb-xs row items-center">
              <div class="q-mr-xs">
                <q-icon
                  :name="$i.ionHeartOutline"
                  style="color:#727272"
                  size="17px"
                ></q-icon>
              </div>
              <div class="q-mr-md" style=" font-size: 10pt;">
                2
              </div>
              <div class="q-mr-sm">
                <q-icon
                  :name="$i.ionChatboxEllipsesOutline"
                  style="color:#727272"
                  size="17px"
                ></q-icon>
              </div>
              <span style="font-size: 10pt;">Reply</span>
            </div>
          </div>
        </div>
        <div class="q-ml-lg q-py-xs row col-12">
          Lorem, ipsum dolor sit amet consectetur adipisicing elit.
        </div>
      </div>
    </div>
    <div class="row col-12">
      <q-separator />
      <div class="row col-12 q-py-sm">
        <div class="row col-12 justify-between">
          <div class="row col-9">
            <span class="q-mr-xs">2.</span>
            <span class="q-mr-sm" style="color: blue">
              @user
            </span>
            <span class="text-caption" style="color: gray">11분 전</span>
          </div>
          <div class="q-pl-xl row col-3">
            <div class="icon-position q-mb-xs row items-center">
              <div class="q-mr-xs">
                <q-icon
                  :name="$i.ionHeartOutline"
                  style="color:#727272"
                  size="17px"
                ></q-icon>
              </div>
              <div class="q-mr-md" style=" font-size: 10pt;">
                5
              </div>
              <div class="q-mr-sm">
                <q-icon
                  :name="$i.ionChatboxEllipsesOutline"
                  style="color:#727272"
                  size="17px"
                ></q-icon>
              </div>
              <span style="font-size: 10pt;">Reply</span>
            </div>
          </div>
        </div>
        <div class="q-ml-lg q-py-xs row col-12">
          Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ducimus
          sapiente expedita nobis, explicabo totam ea beatae maxime eaque! Et
          adipisci neque odit voluptas deleniti distinctio ut? Doloremque
          cupiditate nesciunt voluptates.
        </div>
      </div>
    </div>
    <q-separator />
    <div class="q-mt-sm">
      <q-input borderless v-model="text" placeholder="댓글을 입력해주세요" />
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped></style>
