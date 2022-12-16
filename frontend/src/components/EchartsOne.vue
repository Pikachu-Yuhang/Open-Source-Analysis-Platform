<template>
  <div id="echarts1" style="width:600px;height: 450px;">
  </div>
</template>
<script>
import * as echarts from 'echarts'
export default {
  name: 'EchartsOne',
  mounted: function () {
    var myChart = echarts.init(document.getElementById('echarts1'));
    // 指定图表的配置项和数据
    var option = {
      title: {
        text: 'Star History'
      },
      legend: {
        data: ['year']
      },
      tooltip: {
        trigger: 'axis'
      },
      xAxis: {
        data: ["1","2",'3','4','5','6','7','8','9','10','11','12']
      },
      yAxis: {},
      series: [{
        name: 'TensorFlow',
        type: 'line',
        data: [5000, 2000, 3006, 5000, 5000, 5000]
      },
      {
        name: 'Pytorch',
        type: 'line',
        data: [5781, 2672, 2786, 2780, 6730, 4780]
      }]
    };
    myChart.setOption(option,true);
  },
  created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
  },
}
</script>