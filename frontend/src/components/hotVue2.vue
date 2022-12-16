<template>
    <div id="hot2" style="width:100%;height: 550px;">

    </div>
</template>
<script>
import * as echarts from 'echarts'
export default {
    name: 'HotVue',
    created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
  },
    mounted: function () {
        var myChart = echarts.init(document.getElementById("hot2"));
        const hours = [
            "2018","2019","2020","2021","2022"
        ];
        const days = [
            "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"
        ];


        //change data here
        var option = {
            title:{
                text: "Star Amount From 2018-2022 for TensorFlow",
                left: "center"
            },
            tooltip: {
                position: 'top'
            },
            grid: {
                height: '50%',
                top: '10%'
            },
            xAxis: {
                type: 'category',
                data: hours,
                splitArea: {
                    show: true
                }
            },
            yAxis: {
                type: 'category',
                data: days,
                splitArea: {
                    show: true
                }
            },
            visualMap: {
                min: 0,
                max: 5000,
                calculable: true,
                orient: 'horizontal',
                left: 'center',
                bottom: '15%',
                inRange: {
                    color: ['White','#9F4CA6']
                }
            },
            series: [
                {
                    name: 'Star Amount',
                    type: 'heatmap',
                    data: [
      [0, 0, 4230], [0, 1, 3359], [0, 2, 4396], [0, 3, 3592], [0, 4, 3535], [0, 5, 2825], [0, 6, 2748], [0, 7, 2404], [0, 8, 2550], [0, 9, 2596], [0, 10, 2518], [0, 11, 2173],
      [1, 0, 2276], [1, 1, 2081], [1, 2, 3441], [1, 3, 2820], [1, 4, 2618], [1, 5, 1910], [1, 6, 2213], [1, 7, 1853], [1, 8, 2064], [1, 9, 2010], [1, 10, 2059], [1, 11, 1658],
      [2, 0, 1370], [2, 1, 1283], [2, 2, 1604], [2, 3, 1638], [2, 4, 1693], [2, 5, 1401], [2, 6, 1501], [2, 7, 1294], [2, 8, 1255], [2, 9, 1169], [2, 10, 1655], [2, 11, 1450],
      [3, 0, 1243], [3, 1, 1033], [3, 2, 1173], [3, 3, 1337], [3, 4, 945], [3, 5, 1142], [3, 6, 1115], [3, 7, 1120], [3, 8, 936], [3, 9, 428], [3, 10, 1018], [3, 11, 1000],
      [4, 0, 1365], [4, 1, 872], [4, 2, 1062], [4, 3, 911], [4, 4, 1027], [4, 5, 917], [4, 6, 877], [4, 7, 957], [4, 8, 833], [4, 9, 866], [4, 10, 896], [4, 11, 352]
    ],
                    label: {
                        show: true
                    },
                    emphasis: {
                        itemStyle: {
                            shadowBlur: 10,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        };
        myChart.setOption(option, true);
    }
}
</script>