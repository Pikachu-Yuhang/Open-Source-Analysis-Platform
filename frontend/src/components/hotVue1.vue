<template>
    <div id="hot1" style="width:100%;height: 550px;">

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
        var myChart = echarts.init(document.getElementById("hot1"));
        const hours = [
            "2018","2019","2020","2021","2022"
        ];
        const days = [
            "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"
        ];

        //change data here
        var option = {
            title:{
                text: "Star Amount From 2018-2022 for Pytorch",
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
                max: 2000,
                calculable: true,
                orient: 'horizontal',
                left: 'center',
                bottom: '15%',
                inRange: {
                    color: ['White','SkyBlue']
                }
            },
            series: [
                {
                    name: 'Star Amount',
                    type: 'heatmap',
                    data: [
      [0, 0, 1252], [0, 1, 744], [0, 2, 844], [0, 3, 1259], [0, 4, 1278], [0, 5, 796], [0, 6, 747], [0, 7, 811], [0, 8, 821], [0, 9, 1446], [0, 10, 1129], [0, 11, 1436],
      [1, 0, 1038], [1, 1, 984], [1, 2, 1280], [1, 3, 1256], [1, 4, 1268], [1, 5, 1000], [1, 6, 1083], [1, 7, 943], [1, 8, 852], [1, 9, 1341], [1, 10, 992], [1, 11, 1028],
      [2, 0, 790], [2, 1, 907], [2, 2, 1040], [2, 3, 1027], [2, 4, 1021], [2, 5, 845], [2, 6, 971], [2, 7, 840], [2, 8, 1580], [2, 9, 844], [2, 10, 936], [2, 11, 974],
      [3, 0, 913], [3, 1, 677], [3, 2, 889], [3, 3, 797], [3, 4, 639], [3, 5, 771], [3, 6, 809], [3, 7, 811], [3, 8, 753], [3, 9, 280], [3, 10, 770], [3, 11, 776],
      [4, 0, 864], [4, 1, 582], [4, 2, 858], [4, 3, 786], [4, 4, 789], [4, 5, 709], [4, 6, 689], [4, 7, 804], [4, 8, 957], [4, 9, 784], [4, 10, 785], [4, 11, 355]
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