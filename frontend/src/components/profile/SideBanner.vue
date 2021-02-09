<template>
  <q-card class="side-banner">
    <div class="row">
      <div class="row col-6 items-center">
        <q-card-section>
          <pie-chart
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
                  v-for="(tag, index) in tagNames"
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
              <div class="row" style="width:100%">
                <q-list separator style="width:100%">
                  <q-item
                    clickable
                    v-ripple
                    style="background-color:#F0ECEC; border-radius:6px; "
                    class="q-mb-sm q-pl-lg"
                    v-if="info.projects[0]['project_name1']"
                  >
                    <q-item-section>
                      <div
                        style="color: #08458C"
                        class="text-center"
                        @click="window.open(info.projects[0]['project_url1'])"
                      >
                        {{ info.projects[0]['project_name1'] }}
                      </div>
                    </q-item-section>
                  </q-item>
                  <q-item
                    clickable
                    v-ripple
                    style="background-color:#F0ECEC; border-radius:6px; "
                    class="q-mb-sm q-pl-lg"
                    v-if="info.projects[0]['project_name2']"
                  >
                    <q-item-section>
                      <div
                        style="color: #08458C"
                        class="text-center"
                        @click="window.open(info.projects[0]['project_url2'])"
                      >
                        {{ info.projects[0]['project_name2'] }}
                      </div>
                    </q-item-section>
                  </q-item>
                  <q-item
                    clickable
                    v-ripple
                    style="background-color:#F0ECEC; border-radius:6px; "
                    class="q-mb-sm q-pl-lg"
                    v-if="info.projects[0]['project_name3']"
                  >
                    <q-item-section>
                      <div
                        style="color: #08458C"
                        class="text-center"
                        @click="window.open(info.projects[0]['project_url3'])"
                      >
                        {{ info.projects[0]['project_name3'] }}
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

      <!-- <div class="col-3">
        
        
      </div> -->
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
        labels: [],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: [],
            data: [],
          },
        ],
      },
    };
  },
  computed: {
    tagColors() {
      return colorListMapper(this.tagNames, 0.5);
    },
    tagBoldColors() {
      return colorListMapper(this.tagNames, 1);
    },
    tagNames() {
      return Object.keys(this.info.tags);
    },
    tagLength() {
      return this.tagNames.length;
    },
    tagCounts() {
      return Object.values(this.info.tags);
    },
  },
  created() {
    this.chartData.labels = this.tagNames;
    this.chartData.datasets[0].backgroundColor = this.tagBoldColors;
    this.chartData.datasets[0].data = this.tagCounts;
  },
};
</script>

<style scoped>
.side-banner {
  width: 60%;
  position: relative;
  top: -5vh;
  z-index: 1;
}
</style>
