<template>
  <div style="width:100%">
    <div class="row back-header justify-center"></div>
    <div class="row justify-center ">
      <header-banner></header-banner>
    </div>
    <div class="row justify-center body-banner">
      <div class="row  justify-between" style="width: 60%;">
        <div style="width:28%">
          <q-card class="side-banner">
            <q-card-section>
              <pie-chart :data="chartData" :options="chartOptions"></pie-chart>
            </q-card-section>
            <q-card-section>
              <div class="text-bold q-mb-md q-pl-md">
                My Tags
              </div>
              <div class="row q-mb-xl">
                <q-btn
                  rounded
                  v-for="item in tags"
                  :key="item.tagName"
                  class="q-mb-sm q-mr-xs text-grey-2"
                  :style="{ 'background-color': item.tagColor }"
                  >{{ item.tagName }}</q-btn
                >
              </div>
            </q-card-section>
            <q-card-section>
              <div class="q-pl-md text-bold q-mb-md">
                My Skills/languages
              </div>
              <div class="row q-mb-xl">
                <q-btn
                  rounded
                  v-for="skill in skills"
                  :key="skill"
                  class="q-mb-sm q-mr-xs "
                  style="background-color: #E5E5E5"
                  >{{ skill }}</q-btn
                >
              </div>
            </q-card-section>
          </q-card>
        </div>
        <div style="width: 65%">
          <div class="q-mb-sm row items-center">
            <q-icon
              :name="$i.ionAttachOutline"
              style="color: #B54333"
              size="md"
              class="q-mr-xs"
            ></q-icon>
            <span class="text-h5">Pinned</span>
          </div>
          <q-card class="q-mb-lg">
            <q-card-section
              style="width:100%;border: 2px solid #FBAA9F; border-raidus:5px; "
            ></q-card-section>
          </q-card>
          <div class="q-mb-sm row items-center">
            <q-icon
              :name="$i.ionLayersOutline"
              style="color: #259EC5"
              size="md"
              class="q-mr-xs"
            ></q-icon>
            <span class="text-h5">History</span>
          </div>
          <q-card>
            <q-card-section
              style="width:100%;border: 2px solid #2F95B4; border-raidus:5px; "
            >
              <div style=""></div>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderBanner from '@/components/profile/HeaderBanner';
import PieChart from '@/utils/pieChart';
export default {
  components: {
    HeaderBanner,
    PieChart,
  },
  data() {
    return {
      tags: [
        { tagName: '#vue', tagColor: '#41B883' },
        { tagName: '#javascript', tagColor: '#F7BF33' },
        { tagName: '#react', tagColor: '#36A8FD' },
        { tagName: '#Angular', tagColor: '#B52E31' },
      ],
      skills: ['HTML', 'MongoDB', 'Javascript', 'vue'],
      chartOptions: {
        responsive: true,
        cutoutPercentage: 75,
        legend: {
          display: true,
          position: 'right',
          fullWidth: true,
          labels: {
            boxWidth: 10,
            fontSize: 14,
          },
        },
        title: {
          text: '태그로 보는 포스팅 횟수',
          fontSize: 15,
          fontFamily: "'roboto'",
          fontColor: '#000000',
          display: true,
          padding: 10,
        },
        animation: {
          animateScale: true,
        },
        hoverBorderWidth: 20,
      },
      chartData: {
        hoverBackgroundColor: 'red',
        hoverBorderWidth: 10,
        labels: ['Javascript', 'React', 'Vue', 'Angular'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: ['#F7BF33', '#36A8FD', '#41B883', '#B52E31'],
            data: [23, 14, 8, 3],
          },
        ],
      },
    };
  },
};
</script>

<style scoped>
.back-header {
  height: 15vh;
  background-color: #1595dc;
}
.body-banner {
  position: relative;
  top: -5vh;
}
.side-banner {
  width: 100%;
}
.contents-banner {
  width: 100%;
}
</style>
