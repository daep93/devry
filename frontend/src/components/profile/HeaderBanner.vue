<template>
  <q-card class="header-banner">
    <q-card-section>
      <div class="row q-pl-xl">
        <div class="col-2">
          <q-img
            :src="require('@/assets/change_pwd.png')"
            alt="change-password"
            style="width:150px; height:150px;border:5px solid #ECE1E1; border-radius:100px"
          ></q-img>
        </div>
        <div class="col-9 q-ml-lg">
          <div class="row q-mb-sm justify-between">
            <span class="text-h5 q-pl-xs">Ssafy Park</span>
            <q-btn
              style="background-color:#1595DC;"
              class="text-white text-bold"
              >follow</q-btn
            >
          </div>
          <div class="row  q-mb-md">
            <div class="q-mr-md row items-center">
              <q-icon
                :name="$i.ionLocationOutline"
                size="sm"
                class="q-mr-xs"
              ></q-icon>
              <span>Daejeon</span>
            </div>
            <div class="q-mr-md row items-center">
              <q-icon
                :name="$i.ionBriefcaseOutline"
                size="sm"
                class="q-mr-xs"
              ></q-icon>
              <span>Multi Campus</span>
            </div>
            <div class="row items-center">
              <q-icon
                :name="$i.ionMailOutline"
                size="sm"
                class="q-mr-xs"
              ></q-icon>
              <span>ssafyPark@edu.ssafy.com</span>
            </div>
          </div>
          <div class="row  q-mb-md">
            <q-icon
              :name="$i.ionLogoGithub"
              size="sm"
              color="grey-8"
              class="q-mr-xs"
            ></q-icon>
            <q-icon
              :name="$i.ionLogoGitlab"
              size="sm"
              color="grey-8"
              class="q-mr-xs"
            ></q-icon>
            <q-icon
              :name="$i.ionLogoFacebook"
              color="grey-8"
              size="sm"
              class="q-mr-xs"
            ></q-icon>
            <q-icon
              :name="$i.ionLogoLinkedin"
              color="grey-8"
              size="sm"
              class="q-mr-xs"
            ></q-icon>
          </div>
          <div class="row q-mb-sm justify-between">
            <div class="row items-center">
              <q-icon
                :name="$i.ionCalendarClearOutline"
                color="grey-8"
                size="xs"
                class="q-mr-xs"
              ></q-icon>
              <span>joined on 2020/07/08</span>
            </div>
            <div>
              <span class="q-mr-md">팔로워: <b>4302</b></span>
              <span>팔로우: <b>246</b></span>
            </div>
          </div>
        </div>
      </div>
      <div class="row q-pl-xl q-my-md">
        <p>
          Jumped into web development 1st of January 2020 and I'm completely in
          love. I have little experience as a blogger but practice makes
          perfect! 🤖🦾
        </p>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
export default {};
</script>

<style scoped>
.header-banner {
  width: 60%;
  position: relative;
  top: -10vh;
  z-index: 1;
}
</style>
