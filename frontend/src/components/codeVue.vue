<template>
    <div id="codeVue1" style="width:100%;height: 600px;">
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
        var myChart = echarts.init(document.getElementById('codeVue1'));
        // 指定图表的配置项和数据
        var option = {
            title:{
                text: "Lines of Code Changed of Pytorch",
                left: "center"
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
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
                    data: [60898, 127267, 72007, 133, 710, 3368, 7193, 1001, 715, 1787, 1567, 1704],
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
                    data: [38659, 40154, 56835, -2078, -77, 2480, 3481, 685, 664, -7087, 788, 1102],
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
                    data: [-22239, -87113, -15172, -2211, -787, -888, -3712, -316, -51, -8874, -779, -602],
                }
            ]
      
        }
        myChart.setOption(option, true);
    }
}
</script>