<template>
    <div id="hot3" style="width:100%;height: 550px;">

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
        var myChart = echarts.init(document.getElementById("hot3"));
        const hours = [
            "2018","2019","2020","2021","2022"
        ];
        const days = [
            "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"
        ];

  
        //change data here
        var option = {
            title:{
                text: "Commit Amount From 2018-2022 for Pytorch",
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
                max: 10000,
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
                    name: 'Punch Card',
                    type: 'heatmap',
                    data: [
      [0, 0, 353], [0, 1, 396], [0, 2, 3982], [0, 3, 525], [0, 4, 496], [0, 5, 554], [0, 6, 497], [0, 7, 832], [0, 8, 865], [0, 9, 1093], [0, 10, 1098], [0, 11, 652],
      [1, 0, 910], [1, 1, 862], [1, 2, 1230], [1, 3, 2192], [1, 4, 1964], [1, 5, 2416], [1, 6, 2194], [1, 7, 3828], [1, 8, 4526], [1, 9, 4496], [1, 10, 4883], [1, 11, 2915],
      [2, 0, 2968], [2, 1, 3595], [2, 2, 5126], [2, 3, 4948], [2, 4, 3900], [2, 5, 3851], [2, 6, 2908], [2, 7, 3815], [2, 8, 5655], [2, 9, 3982], [2, 10, 3514], [2, 11, 3714],
      [3, 0, 3442], [3, 1, 3719], [3, 2, 4505], [3, 3, 7447], [3, 4, 4872], [3, 5, 5339], [3, 6, 5687], [3, 7, 8720], [3, 8, 7047], [3, 9, 8801], [3, 10, 7165], [3, 11, 4271],
      [4, 0, 6697], [4, 1, 5015], [4, 2, 6570], [4, 3, 7525], [4, 4, 7375], [4, 5, 8131], [4, 6, 7700], [4, 7, 7700], [4, 8, 7047], [4, 9, 8801], [4, 10, 7165], [4, 11, 4271]
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