<template>
    <div :id="'pullChart'+chartKey"></div>
  </template>
  
  <script>
  import * as echarts from 'echarts'
  
  export default {
    name: "pullChart1",
    props: {
      chartKey: {
        required: true
      },
      xList: {
        type: Array,
        required: true
      },
      data: {
        type: Array,
        required: true
      }
    },
    created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
  },
    mounted() {
      this.init();
    },
    methods: {
      init() {
        var option = {
          title: [{
            text: "Pull Request Time Cost",
            left: "center"
          }],
          xAxis: {
            type: "category",
            data: this.xList,
            boundaryGap: true,
            nameGap: 30,
            splitArea: {
              show: false
            },
            axisLabel: {
              formatter: "{value}",
            },
            splitLine: {
              show: false
            }
          },
          dataZoom: {},
          yAxis: {
            name: "Duration(days)",
            splitArea: {
              show: false
            },
            splitLine: {
              show: false
            }
          },
          series: [{
            name: "boxplot",
            type: "boxplot",
            data: this.data,
            itemStyle: {
              color: this.chartKey === 1 ? 'rgba(34, 154, 222, 0.1)' : 'rgba(115, 228, 155, 0.1)',
              borderColor: this.chartKey === 1 ? 'rgb(82, 139, 234)' : 'rgb(22, 218, 219)',
              borderCap: 'round'
            },
          }],
          emphasis: {
            disabled: false,
            itemStyle: {
              color: this.chartKey === 1 ? 'rgba(34, 164, 226, 0.3)' : 'rgba(115, 228, 155, 0.3)',
              borderCap: 'round',
            }
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              animation: true,
            },
            confine: true
          },
        }
        var pullChart1 = echarts.init(document.getElementById('pullChart' + this.chartKey));
        pullChart1.setOption(option);
      }
    }
  }
  </script>
  
  <style scoped>
  
  #pullChart1 {
    width: 100%;
    height: 500px;
  }
  
  #pullChart2 {
    width: 100%;
    height: 500px;
  }
  
  </style>