<template>
  <q-card class="side-banner">
    <q-card-section>
      <pie-chart :data="chartData" :options="chartOptions"></pie-chart>
    </q-card-section>
    <q-card-section>
      <div class="text-bold q-mb-md q-pl-md">
        My Tags
      </div>
      <div class="row q-mb-xl q-pl-sm">
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
      <div class="row q-mb-xl q-pl-sm">
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
    <q-card-section>
      <div class="q-pl-md text-bold ">
        My Projects
      </div>
      <div class="row q-mb-xl q-pl-xs">
        <ul>
          <li style="color: #08458C" v-for="item in projects" :key="item">
            {{ item }}
          </li>
        </ul>
      </div>
      <div class="row q-mb-xl">
        <div class="q-pl-md text-bold q-mb-md">
          My History
        </div>
        <q-list separator class="q-pl-sm">
          <q-item
            clickable
            v-ripple
            style="background-color:#FADDDD; border-radius:6px"
            class="q-mb-sm q-pl-lg"
          >
            <q-item-section avatar>
              <span
                ><q-icon :name="$i.ionDocumentTextOutline" size="24px" />
                posts</span
              >
            </q-item-section>
            <q-item-section
              ><div class="row text-bold justify-end">4</div></q-item-section
            >
          </q-item>
          <q-item
            clickable
            v-ripple
            style="background-color:#BAD9F6; border-radius:6px"
            class="q-mb-sm q-pl-lg"
          >
            <q-item-section avatar>
              <span
                ><q-icon :name="$i.ionChatboxEllipsesOutline" size="24px" />
                comments</span
              >
            </q-item-section>
            <q-item-section
              ><div class="row text-bold justify-end">16</div></q-item-section
            >
          </q-item>
          <q-item
            clickable
            v-ripple
            style="background-color:#DCA4E5; border-radius:6px; "
            class="q-pl-lg"
          >
            <q-item-section avatar>
              <span
                ><q-icon :name="$i.ionPricetagsOutline" size="24px" />
                tags</span
              >
            </q-item-section>
            <q-item-section>
              <div class="row text-bold justify-end">
                <span>4</span>
              </div>
            </q-item-section>
          </q-item>
        </q-list>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
import PieChart from '@/utils/pieChart';

export default {
  components: {
    PieChart,
  },
  data() {
    return {
      projects: ['ssafy-common', 'ssafy-special', 'ssafy-complete'],
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

<style scoped></style>
