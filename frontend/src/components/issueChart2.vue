<template>
  <div :id="'issueHistoryChart'+chartKey"></div>
</template>

<script>
import * as echarts from 'echarts'
export default {
  name: "issueChart2",
  created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
  },
  props: {
    chartKey: {
      required: true
    },
    data: {
      required: true,
    }
  },
  mounted() {
    this.init();
  },
  methods: {
    init() {
      var option = {
        tooltip: {
          trigger: 'axis',
          position: function (pt) {
            return [pt[0], '10%'];
          }
        },
        title: {
          left: 'center',
          text: 'Issue History'
        },
        xAxis: {
          type: 'category',
          boundaryGap: true,
          data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        },
        yAxis: [
          {
            type: 'value',
            boundaryGap: [0, '100%'],
            splitLine: {
              show: false
            }
          },
          {
            type: 'value',
            boundaryGap: [0, '100%'],
            splitLine: {
              show: false
            }
          },
        ],
        dataZoom: [
          {
            type: 'inside',
          }
        ],
        series: [
          {
            name: 'Newly Opened',
            type: 'line',
            smooth: true,
            symbol: 'none',
            yAxisIndex: 0,
            itemStyle: {
              color: 'rgb(61, 178, 247)'
            },
            lineStyle: {
              color: 'rgb(61, 178, 247)'
            },
            areaStyle: {
              color: 'rgba(61, 178, 247, 0.5)'
            },
            data: this.data.newly_opened
          },
          {
            name: 'Newly Closed',
            type: 'line',
            smooth: true,
            symbol: 'none',
            yAxisIndex: 0,
            itemStyle: {
              color: 'rgb(147, 234, 129)'
            },
            lineStyle: {
              color: 'rgb(147, 234, 129)'
            },
            areaStyle: {
              color: 'rgba(147, 234, 129, 0.5)'
            },
            data: this.data.newly_closed
          },
          {
            name: 'Total Opened',
            type: 'line',
            smooth: true,
            symbol: 'none',
            yAxisIndex: 1,
            itemStyle: {
              color: 'rgb(29, 136, 222)'
            },
            lineStyle: {
              color: 'rgb(29, 136, 222)'
            },
            data: this.data.total_opened
          },
          {
            name: 'Total Closed',
            type: 'line',
            smooth: true,
            symbol: 'none',
            yAxisIndex: 1,
            itemStyle: {
              color: 'rgb(131, 148, 243)'
            },
            lineStyle: {
              color: 'rgb(131, 148, 243)'
            },
            data: this.data.total_closed
          },
        ],
        legend: {
          left: '20',
          top: '20'
        },
        emphasis: {
          focus: 'series'
        }
      };
      var issueChart2 = echarts.init(document.getElementById('issueHistoryChart' + this.chartKey));
      issueChart2.setOption(option);
    }
  }
}
</script>

<style scoped>

#issueHistoryChart3 {
  width: 100%;
  height: 500px;
}

#issueHistoryChart4 {
  width: 100%;
  height: 500px;
}


</style>