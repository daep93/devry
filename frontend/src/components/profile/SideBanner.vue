<template>
  <q-card class="col-7">
    <div class="row full-width">
      <div class="row col-6 items-center">
        <q-card-section>
          <pie-chart
            v-if="loaded"
            :data="chartData"
            :options="chartOptions"
            style="width:25vw"
          ></pie-chart>
        </q-card-section>
      </div>
      <div class="row col-6 items-start">
        <div class="row items-start col-12">
          <div class="col-6">
            <q-card-section>
              <div class="text-bold q-mb-md  text-center">
                My Tags
              </div>
              <div class="row q-mb-xl ">
                <span
                  v-for="(tag, index) in info.myTags"
                  :key="tag"
                  class="q-mb-sm q-mr-xs q-pa-sm"
                  :style="{ 'background-color': tagColors[index] }"
                  style="font-size:10pt; border-radius:5pt;"
                  >#{{ tag }}</span
                >
              </div>
            </q-card-section>
          </div>
          <div class="col-6">
            <q-card-section>
              <div class=" text-bold q-mb-md text-center">
                My Skills/languages
              </div>
              <div class="row">
                <span
                  v-for="skill in info.skills"
                  :key="skill"
                  class="q-mb-sm q-mr-xs q-pa-sm"
                  style="background-color: #F0ECEC; font-size:10pt; border-radius:5pt "
                  >{{ skill }}</span
                >
              </div>
            </q-card-section>
          </div>
        </div>
        <div class="row items-start col-12 ">
          <div class="col-6 ">
            <q-card-section>
              <div class="text-bold text-center q-mb-md">
                My Projects
              </div>
              <div class="row full-width">
                <q-list separator class="full-width">
                  <q-item
                    clickable
                    v-ripple
                    style="background-color:#F0ECEC; border-radius:6px; "
                    class="q-mb-sm q-pl-lg"
                    v-for="project in info.projects"
                    :key="project.project_name"
                  >
                    <q-item-section>
                      <div
                        style="color: #08458C"
                        class="text-center"
                        @click="window.open(info.project.project_url)"
                      >
                        {{ info.project.project_name }}
                      </div>
                    </q-item-section>
                  </q-item>
                </q-list>
              </div>
            </q-card-section>
          </div>
          <div class="col-6">
            <q-card-section>
              <div class=" text-bold q-mb-md text-center">
                My History
              </div>
              <div class="row" style="width:100%">
                <q-list separator style="width:100%">
                  <q-item
                    clickable
                    v-ripple
                    style="background-color:#FADDDD; border-radius:6px; "
                    class="q-mb-sm q-pl-lg"
                  >
                    <q-item-section avatar>
                      <span
                        ><q-icon
                          :name="$i.ionDocumentTextOutline"
                          size="24px"
                        />
                        posts</span
                      >
                    </q-item-section>
                    <q-item-section
                      ><div class="row text-bold justify-end">
                        {{ info.postNum }}
                      </div></q-item-section
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
                        ><q-icon
                          :name="$i.ionChatboxEllipsesOutline"
                          size="24px"
                        />
                        comments</span
                      >
                    </q-item-section>
                    <q-item-section
                      ><div class="row text-bold justify-end">
                        {{ info.commentNum }}
                      </div></q-item-section
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
                        <span>{{ tagLength }}</span>
                      </div>
                    </q-item-section>
                  </q-item>
                </q-list>
              </div>
            </q-card-section>
          </div>
        </div>
      </div>
    </div>
  </q-card>
</template>

<script>
import PieChart from '@/utils/pieChart';
import { colorListMapper } from '@/utils/tagColorMapper';
export default {
  components: {
    PieChart,
  },
  props: {
    info: Object,
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        cutoutPercentage: 75,
        legend: {
          display: true,
          position: 'bottom',
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
        labels: '',
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '',
            data: '',
          },
        ],
      },
      tagNames: [],
      tagColors: [],
      tagBoldColors: [],
      tagLength: 0,
      tagCounts: [],
      loaded: false,
    };
  },
  // watch: {
  //   info() {
  //     this.tagNames = Object.keys(this.info.tags);
  //     this.tagColors = colorListMapper(this.tagNames, 0.5);
  //     this.tagBoldColors = colorListMapper(this.tagNames, 1);
  //     this.tagLength = this.tagNames.length;
  //     this.tagCounts = Object.values(this.info.tags);
  //     this.chartData.labels = this.tagNames;
  //     this.chartData.datasets[0].backgroundColor = this.tagBoldColors;
  //     this.chartData.datasets[0].data = this.tagCounts;
  //     this.loaded = true;
  //   },
  // },
  created() {
    this.tagNames = Object.keys(this.info.tags);
    this.tagColors = colorListMapper(this.tagNames, 0.5);
    this.tagBoldColors = colorListMapper(this.tagNames, 1);
    this.tagLength = this.tagNames.length;
    this.tagCounts = Object.values(this.info.tags);
    this.chartData.labels = this.tagNames;
    this.chartData.datasets[0].backgroundColor = this.tagBoldColors;
    this.chartData.datasets[0].data = this.tagCounts;
    this.loaded = true;
  },
};
</script>

<style scoped></style>
