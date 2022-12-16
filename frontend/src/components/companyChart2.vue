<template>
  <div id="companyChart2Container">
    <div :id="'companyChart'+chartKey"></div>
    <div id="legend">
      <div id="pytorchInLegend">
        <div id="pytorchIconInLegend"></div>
        <p id="pytorchNameInLegend">PyTorch</p>
      </div>
      <div id="anotherInLegend">
        <div id="anotherIconInLegend"></div>
        <p id="anotherNameInLegend">{{anotherProjectName}}</p>
      </div>
    </div>

    <div id="companyChartListContainer">
      <div id="topTenCompanies">Top 10 Companies</div>
      <div id="topCompaniesListBody">
        <div id="pytorchListBody">
          <div id="pytorchIconInList"></div><p id="pytorchListHeader">PyTorch</p>
          <ol id="pytorchList">
            <li v-for="(item, key) in pytorchData" v-show="key < 10" :key="key">
              <p class="companyNameInList" v-text="item.name"></p>
              <p class="valueInList" v-text="item.value"></p>
            </li>
          </ol>
        </div>
        <div id="anotherListBody">
          <div id="anotherIconInList"></div><p id="anotherListHeader">TensorFlow</p>
          <ol id="anotherList">
            <li v-for="(item, key) in tensorflowData" v-show="key < 10" :key="key">
              <p class="companyNameInList" v-text="item.name"></p>
              <p class="valueInList" v-text="item.value"></p>
            </li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts'
import 'echarts-wordcloud'
export default {
  name: "companyChart2",
  props: {
    chartKey: {
      required: true
    },
    isCompare: {
      default: false
    },
    title: {
      required: true
    },
    anotherProjectName: {
      default: 'TensorFlow'
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
    for (let i = 0; i < this.data.length; ++i) {
      if (this.data[i].project === 'pytorch')
        this.pytorchData.push(this.data[i]);
      else
        this.tensorflowData.push(this.data[i]);
    }
    this.init();
  },
  data() {
    return {
      pytorchData: [],
      tensorflowData: []
    };
  },
  methods: {
    init() {
      var companyChart2 = echarts.init(document.getElementById('companyChart' + this.chartKey));
      console.log(document.getElementById('companyChart' + this.chartKey))

      var option = {
        title: {
          text: this.title,
          left: 'center',
          top: '25',
          textStyle: {
            color: '#222222'
          }
        },
        series: [
          {
            type: 'wordCloud',
            sizeRange: [15, 80],
            rotationRange: [0, 0],
            rotationStep: 45,
            gridSize: 8,
            shape: 'pentagon',
            width: '100%',
            height: '100%',
            textStyle: {
              fontFamily: 'sans-serif',
              fontWeight: 'bold',
              color: function (param) {
                return param.data.project === 'pytorch' ? 'rgb(29, 192, 225)' : 'rgb(145, 137, 255)';
              }
            },
            emphasis: {
              focus: 'self',
            },
            data: this.data
          },
        ],
        tooltip: {},
        legend: {}
      };
      // 使用刚指定的配置项和数据显示图表。
      companyChart2.setOption(option);
    }
  }
}
</script>

<style scoped>

#companyChart2Container {
  position: relative;
  width: 100%;
}

#companyChart1, #companyChart2, #companyChart3 {
  display: inline-block;
  vertical-align: top;
  width: 60%;
  height: 550px;
  background-color: rgb(250, 250, 250);
  border-radius: 30px;
}

#legend {
  position: absolute;
  top: 10px;
  left: 10px;
  padding: 10px;
}

#pytorchInLegend, #anotherInLegend {
  margin: 5px;
}

#pytorchIconInLegend {
  display: inline-block;
  height: 14px;
  width: 14px;
  margin-right: 10px;
  background-color: rgb(29, 192, 225);
  border-radius: 7px;
}

#anotherIconInLegend {
  display: inline-block;
  height: 14px;
  width: 14px;
  margin-right: 10px;
  background-color: rgb(145, 137, 255);
  border-radius: 7px;
}

#pytorchNameInLegend, #anotherNameInLegend {
  display: inline-block;
  color: #222222;
  font-weight: 600;
}

#companyChartListContainer {
  display: inline-block;
  vertical-align: top;
  position: relative;
  width: 40%;
  height: 550px;
}

#topTenCompanies {
  margin-top: 20px;
  margin-left: 5%;
  padding: 15px 0 15px 5%;
  width: 80%;
  color: #222222;
  font-size: 20px;
  font-weight: 700;
  background-color: rgb(240, 240, 240);
  border-radius: 10px;
}

#topCompaniesListBody {
  margin-top: 20px;
  margin-left: 5%;
  width: 85%;
}

#pytorchListBody, #anotherListBody {
  display: inline-block;
  vertical-align: top;
  width: 50%;
}

#pytorchIconInList {
  margin-left: 5%;
  margin-right: 5px;
  display: inline-block;
  width: 14px;
  height: 14px;
  background-color: rgb(29, 192, 225);
  border-radius: 7px;
}

#anotherIconInList {
  margin-left: 5%;
  margin-right: 5px;
  display: inline-block;
  width: 14px;
  height: 14px;
  background-color: rgb(145, 137, 255);
  border-radius: 7px;
}

#pytorchListHeader, #anotherListHeader {
  display: inline-block;
  color: #222222;
  font-size: 18px;
  font-weight: 600;
}

.companyNameInList {
  position: absolute;
  color: #333333;
  font-weight: 500;
  left: 6%;
}

.valueInList {
  position: absolute;
  color: #777777;
  right: 6%;
  transform: translateY(3px);
}

li {
  padding: 20px 0;
  position: relative;
}

</style>