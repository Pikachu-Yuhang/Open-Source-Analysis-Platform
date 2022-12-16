<template>
  <div>
    <div style="height:5vh"></div>
  <div id="companyIssueCreator" style="color:black">Company Issue Creator</div>
  <company-chart2 :data="companyIssueCreatorData" :chart-key="1" :title="'Issue Creators\' Company'"></company-chart2>
  <card-vue intro="The major contributor company" name1="Facebook" name2="Google" explain="here we will expalin how we choose this data here we will expalin how ll expalin how we choose this data here we will expalin how we choose this data here we will expalin how we choose this data here we will expalin how we choose this data here we will expalin how we choose this data "></card-vue>
  <card-vue intro="The number of important company" name1="15" name2="18"></card-vue>

  <div style="height:5vh"></div>
  <div style="height:5vh"></div>
  <div id="companyPullRequestCreator">Company Pull Request Creator</div>
  <company-chart2 :data="companyPullRequestData" :chart-key="2" :title="'Pull Request Creators\' Company'"></company-chart2>
  <card-vue intro="The major coder company" name1="Facebook" name2="Google"></card-vue>
  <div style="height:5vh"></div>
  <div style="height:5vh"></div>
  <div id="companyStargazer">Company Stargazers</div>
  <company-chart2 :data="companyStargazerData" :chart-key="3" :title="'Stargazers\' Company'"></company-chart2>
  <card-vue intro="The company has most fans of" name1="Microsoft" name2="Google"></card-vue>
</div>
</template>

<script>
import CompanyChart2 from "@/components/companyChart2.vue";
import cardVue from "@/components/cardVue.vue"
export default {
  name: "companyVue",
  components: {CompanyChart2,cardVue},
  data() {
    return {
      companyIssueCreatorData: [
      {
        "name": "Facebook",
        "value": 86,
        "project": "pytorch"
      },
      {
        "name": "Microsoft",
        "value": 83,
        "project": "pytorch"
      },
      {
        "name": "NVIDIA",
        "value": 65,
        "project": "pytorch"
      },
      {
        "name": "Google",
        "value": 45,
        "project": "pytorch"
      },
      {
        "name": "Tsinghua University",
        "value": 29,
        "project": "pytorch"
      },
      {
        "name": "Intel",
        "value": 28,
        "project": "pytorch"
      },
      {
        "name": "Zhejiang University",
        "value": 20,
        "project": "pytorch"
      },
      {
        "name": "Tencent",
        "value": 17,
        "project": "pytorch"
      },
      {
        "name": "CMU",
        "value": 17,
        "project": "pytorch"
      },
      {
        "name": "Meta",
        "value": 17,
        "project": "pytorch"
      },
      {
        "name": "Peking University",
        "value": 16,
        "project": "pytorch"
      },
      {
        "name": "Baidu",
        "value": 14,
        "project": "pytorch"
      },
      {
        "name": "MIT",
        "value": 13,
        "project": "pytorch"
      },
      {
        "name": "Stanford University",
        "value": 13,
        "project": "pytorch"
      },
      {
        "name": "Alibaba",
        "value": 11,
        "project": "pytorch"
      },
      {
        "name": "Google",
        "value": 161,
        "project": "tensorflow"
      },
      {
        "name": "Microsoft",
        "value": 85,
        "project": "tensorflow"
      },
      {
        "name": "NVIDIA",
        "value": 68,
        "project": "tensorflow"
      },
      {
        "name": "Tencent",
        "value": 26,
        "project": "tensorflow"
      },
      {
        "name": "Alibaba",
        "value": 25,
        "project": "tensorflow"
      },
      {
        "name": "Facebook",
        "value": 20,
        "project": "tensorflow"
      },
      {
        "name": "Tsinghua University",
        "value": 20,
        "project": "tensorflow"
      },
      {
        "name": "Amazon",
        "value": 19,
        "project": "tensorflow"
      },
      {
        "name": "IBM",
        "value": 17,
        "project": "tensorflow"
      },
      {
        "name": "AWS",
        "value": 15,
        "project": "tensorflow"
      },
      {
        "name": "Peking University",
        "value": 15,
        "project": "tensorflow"
      },
      {
        "name": "ByteDance",
        "value": 14,
        "project": "tensorflow"
      },
      {
        "name": "Baidu",
        "value": 14,
        "project": "tensorflow"
      },
      {
        "name": "University of Toronto",
        "value": 14,
        "project": "tensorflow"
      },
      {
        "name": "University of Cambridge",
        "value": 12,
        "project": "tensorflow"
      },
      {
        "name": "Zhejiang University",
        "value": 11,
        "project": "tensorflow"
      },
      {
        "name": "Apple",
        "value": 11,
        "project": "tensorflow"
      },
      {
        "name": "DeepMind",
        "value": 11,
        "project": "tensorflow"
      },
      ],
      companyPullRequestData: [
      {
        "name": "Facebook",
        "value": 170,
        "project": "pytorch"
      },
      {
        "name": "Microsoft",
        "value": 50,
        "project": "pytorch"
      },
      {
        "name": "NVIDIA",
        "value": 42,
        "project": "pytorch"
      },
      {
        "name": "Meta",
        "value": 33,
        "project": "pytorch"
      },
      {
        "name": "Google",
        "value": 27,
        "project": "pytorch"
      },
      {
        "name": "Intel",
        "value": 24,
        "project": "pytorch"
      },
      {
        "name": "Quansight",
        "value": 11,
        "project": "pytorch"
      },
      {
        "name": "Pytorch",
        "value": 10,
        "project": "pytorch"
      },
      {
        "name": "AMD",
        "value": 9,
        "project": "pytorch"
      },
      {
        "name": "IBM",
        "value": 8,
        "project": "pytorch"
      },
      {
        "name": "LightningAI",
        "value": 7,
        "project": "pytorch"
      },
      {
        "name": "Apple",
        "value": 6,
        "project": "pytorch"
      },
      {
        "name": "UW",
        "value": 6,
        "project": "pytorch"
      },
      {
        "name": "Tencent",
        "value": 5,
        "project": "pytorch"
      },
      {
        "name": "AWS",
        "value": 5,
        "project": "pytorch"
      },
      {
        "name": "Amazon",
        "value": 5,
        "project": "pytorch"
      },
      {
        "name": "University of Chicago",
        "value": 5,
        "project": "pytorch"
      },
      {
        "name": "Google",
        "value": 150,
        "project": "tensorflow"
      },
      {
        "name": "NVIDIA",
        "value": 45,
        "project": "tensorflow"
      },
      {
        "name": "Intel",
        "value": 33,
        "project": "tensorflow"
      },
      {
        "name": "Microsoft",
        "value": 31,
        "project": "tensorflow"
      },
      {
        "name": "Tencent",
        "value": 20,
        "project": "tensorflow"
      },
      {
        "name": "ARM",
        "value": 18,
        "project": "tensorflow"
      },
      {
        "name": "Facebook",
        "value": 15,
        "project": "tensorflow"
      },
      {
        "name": "AMD",
        "value": 12,
        "project": "tensorflow"
      },
      {
        "name": "IBM",
        "value": 12,
        "project": "tensorflow"
      },
      {
        "name": "Alibaba",
        "value": 11,
        "project": "tensorflow"
      },
      {
        "name": "Bytedance",
        "value": 10,
        "project": "tensorflow"
      },
      {
        "name": "Amazon",
        "value": 9,
        "project": "tensorflow"
      },
      {
        "name": "Samsung Electronics",
        "value": 7,
        "project": "tensorflow"
      },
      {
        "name": "Graphcore",
        "value": 7,
        "project": "tensorflow"
      },
      {
        "name": "Tensorflow",
        "value": 6,
        "project": "tensorflow"
      },
      {
        "name": "UW",
        "value": 6,
        "project": "tensorflow"
      },
      ],
      companyStargazerData: [
      {
        "name": "Microsoft",
        "value": 214,
        "project": "pytorch"
      },
      {
        "name": "Google",
        "value": 164,
        "project": "pytorch"
      },
      {
        "name": "Facebook",
        "value": 139,
        "project": "pytorch"
      },
      {
        "name": "Tsinghua University",
        "value": 121,
        "project": "pytorch"
      },
      {
        "name": "Alibaba",
        "value": 108,
        "project": "pytorch"
      },
      {
        "name": "Tencent",
        "value": 103,
        "project": "pytorch"
      },
      {
        "name": "ByteDance",
        "value": 94,
        "project": "pytorch"
      },
      {
        "name": "Zhejiang University",
        "value": 94,
        "project": "pytorch"
      },
      {
        "name": "NVIDIA",
        "value": 79,
        "project": "pytorch"
      },
      {
        "name": "Peking University",
        "value": 78,
        "project": "pytorch"
      },
      {
        "name": "Baidu",
        "value": 70,
        "project": "pytorch"
      },
      {
        "name": "Amazon",
        "value": 64,
        "project": "pytorch"
      },
      {
        "name": "Intel",
        "value": 53,
        "project": "pytorch"
      },
      {
        "name": "CMU",
        "value": 51,
        "project": "pytorch"
      },
      {
        "name": "Fudan University",
        "value": 46,
        "project": "pytorch"
      },
      {
        "name": "Google",
        "value": 670,
        "project": "tensorflow"
      },
      {
        "name": "Microsoft",
        "value": 505,
        "project": "tensorflow"
      },
      {
        "name": "Tencent",
        "value": 391,
        "project": "tensorflow"
      },
      {
        "name": "Alibaba",
        "value": 356,
        "project": "tensorflow"
      },
      {
        "name": "ByteDance",
        "value": 295,
        "project": "tensorflow"
      },
      {
        "name": "Amazon",
        "value": 177,
        "project": "tensorflow"
      },
      {
        "name": "Baidu",
        "value": 176,
        "project": "tensorflow"
      },
      {
        "name": "Facebook",
        "value": 174,
        "project": "tensorflow"
      },
      {
        "name": "Tsinghua University",
        "value": 131,
        "project": "tensorflow"
      },
      {
        "name": "Zhejiang University",
        "value": 124,
        "project": "tensorflow"
      },
      {
        "name": "AWS",
        "value": 106,
        "project": "tensorflow"
      },
      {
        "name": "NVIDIA",
        "value": 102,
        "project": "tensorflow"
      },
      {
        "name": "Intel",
        "value": 99,
        "project": "tensorflow"
      },
      {
        "name": "Peking University",
        "value": 97,
        "project": "tensorflow"
      },
      {
        "name": "IBM",
        "value": 95,
        "project": "tensorflow"
      },
      {
        "name": "Huawei",
        "value": 92,
        "project": "tensorflow"
      },
      {
        "name": "CMU",
        "value": 85,
        "project": "tensorflow"
      },
      {
        "name": "NetEase",
        "value": 78,
        "project": "tensorflow"
      },
      {
        "name": "Apple",
        "value": 77,
        "project": "tensorflow"
      },
      {
        "name": "Shanghai Jiaotong University",
        "value": 68,
        "project": "tensorflow"
      },
      ]
    };
  },
  created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
  },
}
</script>

<style scoped>
#companyTitle {
  font-weight: 700;
  font-size: 32px;
  background: linear-gradient(90deg, #12E2DA 0%, #23AEE5 6%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

#companyOverview, #companyIssueCreator, #companyPullRequestCreator, #companyStargazer {
  font-weight: 600;
  color: #222222;
  font-size: 23px;
}


</style>