<template>
    <div id="line1" style="width:100%;height: 600px;">
    </div>
  </template>
  <script>
  import * as echarts from 'echarts'
  export default {
    name: 'LineVue',
    methods:{
    },
    created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
  },
    mounted: function () {
      var myChart = echarts.init(document.getElementById("line1"));
      // 指定图表的配置项和数据
      var option = {
        title:{
                text: "Star Amount From Jan-Dec in 2022",
                left: "center"
            },
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          data: [ "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"],
          interval:2,
          boundaryGap:true,
        },
        dataZoom:{

        },
        yAxis: {},
        series: [{
          name: 'TensorFlow',
          type: 'line',
          data: [1365, 872, 1062, 911, 1027, 917, 877, 957, 833, 866, 896, 352]
        },
        {
          name: 'Pytorch',
          type: 'line',
          data: [864, 582, 858, 786, 789, 709, 689, 804, 957, 784, 785, 355],
        }]
      };
      myChart.setOption(option,true);
    }
  }
  </script>