<template>
    <div :id="'pullHistoryChart'+chartKey"></div>
  </template>
  
  <script>
  import * as echarts from 'echarts'
  export default {
    name: "pullChart2",
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
    created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
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
            text: 'Pull Request History'
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
              name: 'New PR',
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
              data: this.data.new
            },
            {
              name: 'Total PR',
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
              data: this.data.total
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
        var issueChart2 = echarts.init(document.getElementById('pullHistoryChart' + this.chartKey));
        issueChart2.setOption(option);
      }
    }
  }
  </script>
  
  <style scoped>
  
  #pullHistoryChart3 {
    width: 100%;
    height: 500px;
  }

  #pullHistoryChart4 {
    width: 100%;
    height: 500px;
  }
  
  </style>