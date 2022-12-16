<template>
    <div id="codeVue2" style="width:100%;height: 600px;">
    </div>
</template>
<script>
import * as echarts from 'echarts'
export default {
    name: 'codeVue',
    created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
  },
    mounted: function () {
        var myChart = echarts.init(document.getElementById('codeVue2'));
        // 指定图表的配置项和数据
        var option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            title:{
                text: "Lines of Code Changed of TensorFlow",
                left: "center"
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: [
                {
                    type: 'value'
                }
            ],
            yAxis: [
                {
                    type: 'category',
                    axisTick: {
                        show: false
                    },
                    data: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
                }
            ],
            series: [
                {
                    name: 'addition',
                    type: 'bar',
                    label: {
                        show: true,
                        position: 'inside'
                    },
                    emphasis: {
                        focus: 'series'
                    },
                    data: [11346, 4036, 4604, 6266, 7596, 5289, 3312, 33252, 5637, 11237, 5937, 2337],
                },
                {
                    name: 'change',
                    type: 'bar',
                    stack: 'Total',
                    label: {
                        show: true
                    },
                    emphasis: {
                        focus: 'series'
                    },
                    data:  [7662, 2292, 2769, 1922, 5296, 3869, 1987, 13804, 2744, 9210, 3879, 1875]
                },
                {
                    name: 'deletion',
                    type: 'bar',
                    stack: 'Total',
                    label: {
                        show: true,
                        position: 'left'
                    },
                    emphasis: {
                        focus: 'series'
                    },
                    data: [-3684, -1744, -1835, -4344, -2300,-1420, -1325, -19448, -2893, -2027, -2058, -462]
                }
            ]
      
        }
        myChart.setOption(option, true);
    }
}
</script>