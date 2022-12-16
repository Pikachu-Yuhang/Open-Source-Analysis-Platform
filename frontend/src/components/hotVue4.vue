<template>
    <div id="hot4" style="width:100%;height: 550px;">

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
        var myChart = echarts.init(document.getElementById("hot4"));
        const hours = [
            "2018","2019","2020","2021","2022"
        ];
        const days = [
            "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"
        ];

        //change data here
        var option = {
            title:{
                text: "Commit Amount From 2018-2022 for TensorFlow",
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
                max: 3000,
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
                    name: 'Punch Card',
                    type: 'heatmap',
                    data: [
      [0, 0, 1323], [0, 1, 1354], [0, 2, 1391], [0, 3, 1602], [0, 4, 1357], [0, 5, 1747], [0, 6, 1502], [0, 7, 1809], [0, 8, 1381], [0, 9, 1756], [0, 10, 1590], [0, 11, 1518],
      [1, 0, 1730], [1, 1, 2135], [1, 2, 2142], [1, 3, 2247], [1, 4, 2444], [1, 5, 2226], [1, 6, 2408], [1, 7, 2791], [1, 8, 4759], [1, 9, 2386], [1, 10, 2384], [1, 11, 2098],
      [2, 0, 2450], [2, 1, 2558], [2, 2, 2272], [2, 3, 2571], [2, 4, 2070], [2, 5, 2507], [2, 6, 2731], [2, 7, 2270], [2, 8, 2339], [2, 9, 2280], [2, 10, 1756], [2, 11, 1863],
      [3, 0, 1726], [3, 1, 1690], [3, 2, 1975], [3, 3, 1646], [3, 4, 2341], [3, 5, 1841], [3, 6, 1800], [3, 7, 1775], [3, 8, 1242], [3, 9, 850], [3, 10, 1247], [3, 11, 1201],
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