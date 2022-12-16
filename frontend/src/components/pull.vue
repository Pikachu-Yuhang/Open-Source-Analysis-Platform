<template>
    <div style="height:5vh"></div>
    <div id="pullOverview">Overview</div>
    
    <table-vue :tableContent="pullRequestOverview"></table-vue>
    <div style="height:5vh"></div>
    <div id="pullTimeCost">Pull Request Time Cost</div>
    <div style="height:5vh"></div><div style="height:5vh"></div>
    <pull-chart1 :x-list="xList" :data="pullTimeCost.pytorch" :chart-key="1"></pull-chart1>
    <pull-chart1 v-show="isCompare" :x-list="xList" :data="pullTimeCost.tensorflow" :chart-key="2"></pull-chart1>
    <div style="height:5vh"></div><div style="height:5vh"></div>
    <div id="pullHistory">Pull Request History</div>
   <pull-chart2 :data="pullRequestHistory.pytorch" :chart-key="3"></pull-chart2>
   <pull-chart2 :data="pullRequestHistory.tensorflow" :chart-key="4"></pull-chart2>
  </template>
  
  <script>
  import pullChart1 from "@/components/pullChart1.vue";
  import TableVue from "@/components/TableVue.vue";
  import pullChart2 from "@/components/pullChart2.vue";
  
  export default {
    name: "pullVue",
    components: {pullChart2, TableVue, pullChart1},
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
        pullRequestOverview:[
          {
            "first": "",
            "second": "Pytorch",
            "third": "Tensorflow"
          },
          {
            "first": "Total PRs",
            "second": 59533,
            "third": 21764
          },
          {
            "first": "Creators",
            "second": 3543,
            "third": 4479
          },
          {
            "first": "Reviews",
            "second": 111185,
            "third": 16453
          },
          {
            "first": "Reviewers",
            "second": 990,
            "third": 597
          }
        ],
        pullTimeCost:{
        "pytorch": [
          [0.000012, 0.042, 0.92, 6, 1095],
          [0.000012, 0.042, 0.67, 8, 1095],
          [0.000012, 0.125, 1, 7, 1460],
          [0.000012, 0.042, 0.67, 5, 1095],
          [0.000012, 0.0194, 0.542, 3, 365],
          [0.000012, 0.042, 0.792, 5, 730],
          [0.000012, 0.01875, 0.625, 3, 1460],
          [0.000012, 0.00764, 0.5, 3, 730],
          [0.000023, 0.0833, 1, 4, 365],
          [0.000012, 0.00008, 0.333, 3, 1095],
          [0.000012, 0.125, 0.875, 4, 365],
          [0.000012, 0.0417, 0.75, 4, 1095]
        ],
        "tensorflow": [
          [0.000116, 0.17, 0.542, 1, 730],
          [0.000127, 0.083, 0.417, 1, 730],
          [0.000045, 0.125, 0.708, 2, 730],
          [0.000174, 0.125, 0.67, 2, 1095],
          [0.000149, 0.083, 0.67, 1, 1095],
          [0.000231, 0.2083, 0.708, 2, 1095],
          [0.000012, 0.01875, 0.625, 3, 1460],
          [0.000012, 0.00764, 0.5, 3, 730],
          [0.000023, 0.083, 1, 4, 365],
          [0.000012, 0.00008, 0.333, 3, 1095],
          [0.000012, 0.125, 0.875, 4, 365],
          [0.000012, 0.0417, 0.75, 4, 1095]
        ]
      },
        pullRequestHistory: {
          "pytorch": {
            "new": [1025, 861, 909, 985, 1125, 1269, 1075, 1140, 1103, 1293, 1273, 613],
            "total": [44389, 45305, 46255, 47286, 48470, 49827, 50952, 52129, 53282, 54607, 55915, 56539]
          },
          "tensorflow": {
            "new": [379, 248, 441, 142, 242, 95, 97, 342, 124, 212, 140, 44],
            "total": [18897, 19151, 19605, 19750, 19995, 20093, 20195, 20540, 20669, 20885, 21033, 21081]
          }
        },
      };
    },
    // created() {
    //   // Overview data of pull request
    //   this.$http.get('/fetcher/pytorch/pytorch/pr/')
    //       .then((res) => {
    //         this.pullRequestOverview.push({
    //           'first': 'Pull Request Number',
    //           'second': res.data.result.pr_cnt,
    //           'third': ''
    //         });
    //         this.pullRequestOverview.push({
    //           'first': 'Pull Request Creator Number',
    //           'second': res.data.result.pr_creator_cnt,
    //           'third': ''
    //         });
    //         this.pullRequestOverview.push({
    //           'first': 'Review Number',
    //           'second': res.data.result.pr_review_cnt,
    //           'third': ''
    //         });
    //         this.pullRequestOverview.push({
    //           'first': 'Reviewer Number',
    //           'second': res.data.result.pr_reviewer_cnt
    //         });
    //       });

    //   // Pull request history
    //   this.$http.get('/puller/pytorch/pytorch/pr_per_month/2022/')
    //       .then((res) => {
    //         this.pullRequestHistory['newly_open'] = res.data.opened;
    //         this.pullRequestHistory['newly_closed'] = res.data.closed;

    //         let current_total_open = parseInt(this.pullRequestOverview[0].second);
    //         let total_open = [];
    //         total_open[this.pullRequestHistory['newly_open'].length - 1] = current_total_open;
    //         for (let i = this.pullRequestHistory['newly_open'].length - 1; i > 0; --i) {
    //           total_open[i - 1] = total_open[i] - this.pullRequestHistory['newly_open'][i - 1];
    //         }
    //         this.pullRequestHistory['total_open'] = total_open;
    //       });
    // }
  }
  </script>
  
  <style scoped>
  
  #pullTitle {
    font-weight: 700;
    font-size: 32px;
    background: linear-gradient(90deg, #12E2DA 0%, #23AEE5 5%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  
  #pullOverview, #pullTimeCost, #pullHistory {
    font-weight: 600;
    color: #222222;
    font-size: 23px;
  }
  
  
  </style>