<template>
  <div style="height:5vh"></div>
  <div id="issueOverview">Overview</div>
  
  <table-vue :tableContent="issueOverview"></table-vue>
  <div style="height:5vh"></div>
  <div id="issueFirstRespondedTime">Issue First Responded Time</div>
  <div style="height:5vh"></div><div style="height:5vh"></div>
  <issue-chart1 :x-list="xList" :data="issueFirstRespondTime.pytorch" :chart-key="1"></issue-chart1>
  <issue-chart1 v-show="isCompare" :x-list="xList" :data="issueFirstRespondTime.tensorflow" :chart-key="2"></issue-chart1>
  <div style="height:5vh"></div><div style="height:5vh"></div>
  <div id="issueHistory">Issue History</div>
 <issue-chart2 :data="issueHistory.pytorch" :chart-key="3"></issue-chart2>
 <issue-chart2 :data="issueHistory.tensorflow" :chart-key="4"></issue-chart2>
</template>

<script>
import IssueChart1 from "@/components/issueChart1.vue";
import TableVue from "@/components/TableVue.vue";
import IssueChart2 from "@/components/issueChart2.vue";

export default {
  name: "issueVue",
  components: {IssueChart2, TableVue, IssueChart1},
  data() {
    return {
      isCompare: true,
      xList: [
        "2022.1",
        "2022.2",
        "2022.3",
        "2022.4",
        "2022.5",
        "2022.6",
        "2022.7",
        "2022.8",
        "2022.9",
        "2022.10",
        "2022.11",
        "2022.12",
      ],
      issueFirstRespondTime: {
        "pytorch": [
          [0.0000116, 0.0417, 0.917, 6, 1095],
          [0.0000116, 0.0417, 0.667, 8, 1095],
          [0.0000116, 0.125, 1, 7, 1460],
          [0.0000116, 0.0417, 0.667, 5, 1095],
          [0.0000116, 0.0194, 0.542, 3, 360],
          [0.0000116, 0.0417, 0.792, 5, 730],
          [0.0000116, 0.01875, 0.625, 3, 1460],
          [0.0000116, 0.00764, 0.5, 3, 730],
          [0.0000116, 0.0833, 1, 4, 365],
          [0.0000116, 0.00008, 0.333, 3, 1095],
          [0.0000116, 0.125, 0.875, 4, 365],
          [0.0000116, 0.0417, 0.75, 4, 1095]
        ],
        "tensorflow": [
          [0.0000116, 0.167, 0.542, 1, 730],
          [0.0001273, 0.0833, 0.417, 1, 730],
          [0.0000451, 0.125, 0.708, 2, 730],
          [0.000174, 0.125, 0.667, 2, 1095],
          [0.000149, 0.125, 0.667, 1, 1095],
          [0.000231, 0.0833, 0.708, 2, 1095],
          [0.000174, 0.208, 0.667, 1, 1095],
          [0.0000579, 0.125, 0.75, 1, 1095],
          [0.0000335, 0.167, 0.667, 1, 730],
          [0.000162, 0.125, 1, 1, 730],
          [0.000336, 0.0417, 0.375, 2, 1095],
          [0.0003, 0.25, 0.708, 1, 1095]
        ]
      },
      issueOverview: [
        {
          "first": "",
          "second": "Pytorch",
          "third": "Tensorflow"
        },
        {
          "first": "Total Issues",
          "second": 28955,
          "third": 36056
        },
        {
          "first": "Creators",
          "second": 10694,
          "third": 20012
        },
        {
          "first": "Comments",
          "second": 341044,
          "third": 322893
        },
        {
          "first": "Commenters",
          "second": 17699,
          "third": 37826
        }
      ],
      issueHistory: {
        "pytorch": {
          "newly_opened": [410, 446, 424, 436, 597, 484, 510, 586, 431, 673, 413, 226],
          "newly_closed": [264, 333, 307, 245, 289, 328, 283, 380, 241, 498, 296, 236],
          "total_opened": [22979, 23243, 23667, 24103, 24700, 25184, 25694, 26280, 26711, 27384, 27797, 28023],
          "total_closed": [16494, 16827, 17134, 17379, 17668, 17996, 18279, 18659, 18900, 19398, 19694, 19930]
        },
        "tensorflow": {
          "newly_opened": [224, 195, 215, 186, 210, 185, 193, 248, 205, 199, 183, 81],
          "newly_closed": [337, 244, 264, 243, 261, 282, 172, 247, 221, 244, 222, 99],
          "total_opened": [32901, 33096, 33311, 33497, 33707, 33892, 34085, 34333, 34538, 34737, 34920, 35001],
          "total_closed": [31920, 32164, 32428, 32671, 32932, 33214, 33386, 33633, 33854, 34098, 34320, 34419]
        }
      },
    };
  },
  created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
  },
}
</script>

<style scoped>

#issueTitle {
  font-weight: 700;
  font-size: 32px;
  background: linear-gradient(90deg, #12E2DA 0%, #23AEE5 5%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

#issueOverview, #issueFirstRespondedTime, #issueHistory {
  font-weight: 600;
  color: #222222;
  font-size: 23px;
}


</style>