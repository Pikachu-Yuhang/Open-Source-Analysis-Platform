<template>
  <div>
    <div class="nav-bar-2">
      <span class="nav2-name"><img src="@/pic/nav22.png" alt="" />PyTorch</span>
      <span class="nav2-vs"></span>
      <span class="nav3-name"><img src="@/pic/nav22.png" alt="" />TensorFlow</span>
      <span class="nav2-add"><span>add another project</span> </span>
    </div>
    <div class="left-bar">
      <div class="left-text-1 left-text left-active" style="margin-bottom:2vh">
        <img src="@/pic/l1.png" alt="" /> <span>Analytics</span>
      </div>
      <!-- <div v-for="content in contentAll" :key="content.title" class="left-text leftScroll" :class="content.scrollClass"><a :href="('#'+content.title)">{{content.title}}</a> </div>
    </div> -->
      <div class="left-text leftScroll " @click="scrollHome('overview')"><a href="#/home">Overview</a> </div>
      <div class="left-text leftScroll " @click="scrollHome('companny')"><a href="#/home">Company</a> </div>
      <div class="left-text leftScroll " @click="scrollHome('code')"><a href="#/home">Code</a> </div>
      <div class="left-text leftScroll" @click="scrollHome('pull')"><a href="#/home">Pull Request</a> </div>
      <div class="left-text leftScroll " @click="scrollHome('issues')"><a href="#/home">Issues</a> </div>
      <div class="left-text leftScroll " @click="scrollHome('star')"><a href="#/home">Star</a> </div>
      <div class="left-text leftScroll " @click="scrollHome('commit')"><a href="#/home">Commit</a> </div>
    </div>
    <div style="height: 7.3vw"></div>
    <div class="wrapper" style="padding-top: 40px">
      <h1>PyTorch</h1>
      <div style="height:5vh"></div>
      <div class="herf">
        <img src="@/pic/herf.png" alt="" /> github.com/pytorch/pytorch
      </div>
      <div class="herf" style="margin-left:1vw">
        <img src="@/pic/herf.png" alt="" /> github.com/tensorflow/tensorflow
      </div>



      <!-- demo -->
      <div>
        <div style="height:8vw" id="overview"></div>
        <div>
          <h2 class="scroll-listen titleScroll" style="width:80%;display: inline-block;">Overview </h2>
          <button-vue class="btn-right"></button-vue>
        </div>
        <div>
          <table-vue :tableContent="table1" style="display:inline-block;vertical-align: top;"></table-vue>
          
        </div>
      </div>

      <div>
        <div style="height:8vw" id="companny"></div>
        <div>
          <h2 class="scroll-listen titleScroll" style="width:80%;display: inline-block;">Company</h2>
          <button-vue class="btn-right"></button-vue>
        </div>
        <company-vue></company-vue>
      </div>
      <div>
        <div style="height:8vw" id="code"></div>
        <div>
          <h2 class="scroll-listen titleScroll" style="width:80%;display: inline-block;">Code</h2>
          <button-vue class="btn-right"></button-vue>
        </div>
        <code-vue></code-vue>
        <code-vue2></code-vue2>
        <card-vue :intro="'The Main Construct Stage of'" :name1="'Jan to Mar'" :name2="'Aug to Oct'"
          :explain="'We consider that the period of code construction is a period of rapid code growth, and the end of this period should be accompanied by a large number of code additions and deletions (but the total code volume growth is slower)'"></card-vue>
      </div>
      <!-- demo over -->
      <div>
        <div style="height:8vw" id="pull"></div>
        <div>
          <h2 class="scroll-listen titleScroll" style="width:80%;display: inline-block;">Pull Requests</h2>
          <button-vue class="btn-right"></button-vue>
        </div>
        <pull></pull>
        <card-vue intro="Highest Level of Coding Participation" name1="Oct to Nov" name2="Mar"
          explain="Differentiation of pull request number and review number reveal the participation of developers. This index takes the pull request number, pull request creator, review number and reviewer number into consideration in a given weight, and chooses the period with the greatest differentiation as the highest level of coding participation."></card-vue>
      </div>

      <div>
        <div style="height:8vw" id="issues"></div>
        <div>
          <h2 class="scroll-listen titleScroll" style="width:80%;display: inline-block;">Issues</h2>
          <button-vue class="btn-right"></button-vue>
        </div>
        <issue></issue>
        <card-vue intro="Period of highest issue detection level of" name1="Oct" name2="Aug"
          explain="Issues reflect the detection of bugs and problems in code. Issue first responded time reveals the level of concern about the project code quality. Issue history gives the newly opened and closed issue number, and displays the frequency of issue proposal and resolution. This index takes these factors into account in a given weight and get the highest value."></card-vue>
      </div>

      <div>
        <div style="height:8vw" id="star"></div>
        <div>
          <h2 class="scroll-listen titleScroll" style="width:80%;display: inline-block;">Star</h2>
          <button-vue class="btn-right" @click="updateStar"></button-vue>
        </div>
        <line-vue-1></line-vue-1>
        <hot-vue-1></hot-vue-1>
        <hot-vue-2></hot-vue-2>
        <card-vue :intro="'Fastest period of publication of'" name1="2019-2020" name2="2018-2019"
          explain="Since the number of stars itself decreases as the project becomes more widely known, we set a threshold above which we all consider to be the main promotion period of the project"></card-vue>
      </div>
      <div>
        <div style="height:8vw" id="commit"></div>
        <div>
          <h2 class="scroll-listen titleScroll" style="width:80%;display: inline-block;">Commits</h2>
          <button-vue class="btn-right" @click="updateCommits"></button-vue>
        </div>
        <line-vue2></line-vue2>
        <hot-vue3></hot-vue3>
        <hot-vue4></hot-vue4>
        <card-vue :intro="'Major Development Stage of'" name1="2021-2022" name2="2019-2020"
          explain="We consider that the period when the number of project commits and the total number of code lines of the project are clearly proportional is the period of major development of code"></card-vue>
      </div>
    </div>
  </div>
</template>
  
<script>
import tableVue from "@/components/TableVue.vue"
import ButtonVue from "@/components/buttonVue.vue"
import hotVue1 from "@/components/hotVue1.vue"
import hotVue2 from "@/components/hotVue2.vue"
import hotVue3 from "@/components/hotVue3.vue"
import hotVue4 from "@/components/hotVue4.vue"
import lineVue1 from "@/components/LineVue1.vue"
import lineVue2 from "@/components/LineVue2.vue"
import codeVue from "@/components/codeVue.vue"
import codeVue2 from "@/components/codeVue2.vue"
import cardVue from "@/components/cardVue.vue"

import companyVue from "@/components/companyVue.vue"
import Issue from '@/components/issue.vue'
import Pull from '@/components/pull.vue'
export default {
  name: "HomeVue",
  data() {
    return {
      table1: [
    {
      "first": "",
      "second": "Pytorch",
      "third": "Tensorflow"
    },
    {
      "first": "Stars",
      "second": 63596,
      "third": 186311
    },
    {
      "first": "Commits",
      "second": 242293,
      "third": 138492

    },
    {
      "first": "Issues",
      "second": 28953,
      "third": 36056
    },
    {
      "first": "Forks",
      "second": 16980,
      "third": 87547
    },
    {
      "first": "Pull Requests",
      "second": 3543,
      "third": 4479

    },
    {
      "first": "Language",
      "second": "C++",
      "third": "C++"
    }
  ],
      commitDataPytorch: [],
      starDataPytorch: [],
      user: "Log in"
    };
  },
  created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
  },
  methods: {
    updateCommits() {
      this.$http.get('/puller/pytorch/pytorch/commit_per_month/2022/')
        .then((res) => {
          console.log("update");
          this.commitDataPytorch = res.data.pushed;
        })
    },
    updateStar() {
      this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
        .then((res) => {
          this.starDataPytorch = res.data.starred;
        })
    },
    scrollHome(id){
      var n=document.getElementById(id);
      n.scrollIntoView({
        behavior:"smooth",
        block:"start"
      })
    }
  },

  props: {},
  mounted: function () {
    // function hasClass(element, cName) {        //检查class是否存在
    //   return !!element.className.match(new RegExp('(\\s|^)' + cName + '(\\s|$)'));
    // }

    console.log(this.user);


    function addClass(element, cName) {        //添加一个class
      if (!element.className.match(new RegExp('(\\s|^)' + cName + '(\\s|$)'))) {
        element.className += ' ' + cName;
      }
    }
    function removeClass(element, cName) {        //移除一个class
      if (element.className.match(new RegExp('(\\s|^)' + cName + '(\\s|$)'))) {
        element.className = element.className.replace(new RegExp('(\\s|^)' + cName + '(\\s|$)'), ' ');
      }
    }
    var h2List = document.getElementsByClassName("titleScroll");
    var parent = document.getElementsByClassName("leftScroll");
    window.onscroll = function () {
      var scrollTop =
        document.documentElement.scrollTop || document.body.scrollTop;
      var now;
      for (var i = 0; i < h2List.length; ++i) {
        if (scrollTop > h2List[i].offsetTop - window.innerHeight * 0.33) {
          now = i;
        }
      }
      for (i = 0; i < parent.length; ++i) {
        if (i == now) {
          addClass(parent[i], "left-active");
        }
        else {
          removeClass(parent[i], "left-active");
        }
      }
    };
  },
  components: {
    tableVue,  ButtonVue, hotVue1,hotVue2,hotVue3,hotVue4, lineVue1, lineVue2, codeVue, cardVue, companyVue,
    Issue,codeVue2,
    Pull
  },
};

</script>
  
<style scoped>
* {
  margin: 0;
  padding: 0;
}

li {
  list-style: none;
}

.left-text a {
  width: fit-content;
  text-decoration: none;
}

@font-face {
  font-family: "IcoMoon-Free";
  src: url("@/assets/Font/IcoMoon-Free.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

body {
  background-color: #FAFAFA;
  margin: 0;
  padding: 0;
}



/* search */
.warpper {
  background-color: #F1F9FD;
}

.parent {
  width: 20vw;
  height: 3vw;
  position: relative;
}

.parent input::-webkit-input-placeholder {
  color: #b7b7b8;
}



/* left-bar */
.left-bar {
  padding-top: 8vw;
  position: fixed;
  width: 13vw;
  background-color: white;
  left: 0;
  top: 0;
  height: 100vh;
  z-index: 0;
}

.left-text-1 {
  font-size: 1.35em !important;
  font-weight: 900 !important;
}

.left-text {
  position: relative;
  font-size: 1.2em;
  font-weight: 530;
  padding-left: 3vw;
  height: 2.5vw;
  line-height: 2.5vw;
  margin-bottom: 0.8vh;
  color: black;
}

.left-text a {
  color: #777777;
}

.left-text:hover {
  background: linear-gradient(90deg,
      #23aee5 0%,
      #218cd9 33.33%,
      #9189ff 60.38%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 580;
}

.left-active {
  background: linear-gradient(90deg,
      #23aee5 0%,
      #218cd9 33.33%,
      #9189ff 60.38%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 580;
}

.left-text img {
  position: absolute;
  left: 1vw;
  top: 0.5vw;
  width: 1.5vw;
  height: 1.5vw;
}

/* navbar 2 */
.nav-bar-2 {
  position: fixed;
  top: 4vw;
  left: 13vw;
  height: 3.3vw;
  width: 87vw;
  background: rgba(245, 244, 244, 0.8);
  backdrop-filter: blur(20px);
  padding-left: 2vw;
  z-index: 1;
}

.nav2-name {
  vertical-align: middle;

  font-size: 1.2em;
  font-weight: 730;
  width: 10vw;
  height: 3vw;
  line-height: 3vw;
  color: black;
}

.nav2-name img {
  vertical-align: middle;
  width: 1.7vw;
  height: 1.7vw;
  margin-right: 1vw;
}

.nav3-name {
  vertical-align: middle;

  font-size: 1.2em;
  font-weight: 730;
  width: 10vw;
  height: 3vw;
  line-height: 3vw;
  color: black;
}

.nav3-name img {
  vertical-align: middle;
  width: 1.7vw;
  height: 1.7vw;
  margin-right: 1vw;
}

.nav2-name::after {
  vertical-align: middle;
  margin-left: 1vw;
  margin-right: 1vw;
  content: "VS.";
  font-size: 1em;
  font-weight: 530;
  width: 10vw;
  height: 3vw;
  line-height: 3vw;
  color: #646464;
}

.nav2-add {
  position: absolute;
  right: 90px;
  padding-right: 1vw;
  transform: translateY(0.5vw);
  display: inline-block;
  border-radius: 10px;
  border: dashed 1px #646464;
  font-size: 1em;
  min-width: 10vw;
  height: 1.7vw;
  line-height: 1.7vw;
  color: #646464;
}

.nav2-add::before {
  vertical-align: middle;
  content: "\ea0a";
  margin-right: 0.5vw;
  margin-left: 0.3vw;
  color: grey;
  line-height: 3vw;
  font-size: 0.8vw;
  font-family: "IcoMoon-Free";
  font-style: normal;
  font-weight: normal;
  font-variant: normal;
  text-transform: none;
  line-height: 1;
  letter-spacing: 0;
  -webkit-font-feature-settings: "liga";
  -moz-font-feature-settings: "liga=1";
  -moz-font-feature-settings: "liga";
  -ms-font-feature-settings: "liga" 1;
  -o-font-feature-settings: "liga";
  font-feature-settings: "liga";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.nav2-add:hover {
  transition: 1s;
  transform: scale(0.95);
}

.wrapper {
  position: relative;
  background-color: #FAFAFA;
  margin-left: 13vw;
  min-height: 90vh;
  padding-left: 2vw;
  z-index: 0;
}

.wrapper h1 {
  font-size: 3em;
  background: linear-gradient(90deg, #23aee5 0%, #218cd9 5%, #9189ff 10%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 580;
}

.wrapper h2 {
  font-size: 2.5em;
  background: linear-gradient(90deg, #23aee5 0%, #218cd9 5%, #9189ff 10%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 580;
}

.herf {
  width: fit-content;
  height: 20px;
  line-height: 20px;
  display: inline-block;
  position: relative;
  padding-right: 0.5vw;
  padding-bottom: 0.2vw;
  padding-top: 2px;
  font-size: 0.7vw;
  color: black;
  border-radius: 1000000px;
  border: solid grey 1px;

  line-height: 1vw;
}

.herf img {
  margin-left: 0.3vw;
  height: 80%;
  vertical-align: middle;
}
</style>
  