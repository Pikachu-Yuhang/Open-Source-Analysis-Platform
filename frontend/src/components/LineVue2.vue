<template>
    <div id="line2" style="width:100%;height: 600px;">
    </div>
  </template>
  <script>
  import * as echarts from 'echarts'
  export default {
    name: 'LineVue',

    created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
  },
    mounted: function () {
      console.log(this.datas)
      var myChart = echarts.init(document.getElementById("line2"));
      // 指定图表的配置项和数据
      var option = {
        title:{
                text: "Commit Amount From Jan-Dec in 2022",
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
          data: [1465, 1165, 1545, 1034, 1437, 1029, 1081, 2051, 1635, 1685, 1660, 767]
        },
        {
          name: 'Pytorch',
          type: 'line',
          data: [6697, 5015, 6570, 7525, 7375, 8131, 7700, 7700, 7047, 8801, 7165, 4271]
        }]
      };
      myChart.setOption(option,true);
    }
  }
  </script>