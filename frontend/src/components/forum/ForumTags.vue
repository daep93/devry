<template>
  <div>
    <div
      class="justify-center"
      style="width: 1200px; height: 150px; margin:0 auto;"
    >
      <q-card
        flat
        class="my-card"
        style="width: 800px; margin-top: 50px; margin-left: 35px;"
      >
        <q-card-section>
          <div class="text-h6">Tags</div>
        </q-card-section>

        <span
          v-for="i in 3"
          :key="i"
          class="icon-position"
          style="margin-left: 10px;"
        >
          <q-badge color="blue">
            # Vue
          </q-badge>
        </span>
      </q-card>

      <q-card-section class="q-pt-none">
        {{ lorem }}
      </q-card-section>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped></style>
