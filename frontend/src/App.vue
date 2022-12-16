<template>
  <div class="nav-bar">
    <div class="nav-bar-title">Open Source Project</div>
    <div class="nav-bar-choose">
      <router-link to="./"><div class="nav-item">{{user}}</div></router-link>
      <router-link to="./home"><div class="nav-item">Analysize</div></router-link>
      <router-link to="./manage"><div class="nav-item">Repo Manage</div></router-link>
    </div>
    <div class="nav-bar-search">
      <div class="container">
        <form action="" class="parent">
          <input type="text" class="search" placeholder="Search a repo" />
          <input type="button" name="" id="" class="btn" />
        </form>
      </div>
    </div>
  </div>
  <router-view></router-view>
</template>
<script>
// import tableVue from "@/components/TableVue.vue"
// import EchartsOne from "@/components/EchartsOne.vue"
// import ButtonVue from "@/components/buttonVue.vue"
// import hotVue from "@/components/hotVue.vue"
// import lineVue from "@/components/LineVue.vue"
// import codeVue from "@/components/codeVue.vue"
// import cardVue from "@/components/cardVue.vue"
// import companyVue from "@/components/companyVue.vue"
// import Issue from './components/issue.vue'
// import Pull from './components/pull.vue'
export default {
  name: "App",
  data() {
    return {
      
      user:"Log in"
    };
  },
  created:function(){
    this.user=localStorage.getItem("user");
    console.log('ss'+this.user)
    if(this.user==null)
    {
      this.user="Log in";
    }
  }


};
</script>
<style>
.container {
  position: absolute;
  right: 2vw;
  top: 0.7vw;
  height: 3vw;
  width: 20vw;
}
.nav-bar {
  z-index: 1;
  position: fixed;
  width: 100vw;
  height: 4vw;
  top: 0;
  left: 0;
  background-image: url(@/assets/nav.jpg);
  background-size: 100vw;
  background-repeat: no-repeat;
  padding-left: 3vw;
  padding-right: 3vw;
}
.btn {
  height: 2vw;
  width: 2vw;
  position: absolute;
  left: 12vw;
  top: 0.3vw;
  background: url("@/pic/s.png");
  background-size: 1.5vw 1.5vw;
  background-repeat: no-repeat;
  border: none;
  outline: none;
  cursor: pointer;
}
.nav-bar-title {
  line-height: 4vw;
  font-size: 1.5em;
  font-weight: 800;
  color: black;
  height: 4vw;
}
.nav-bar-choose{
  position:absolute;
  right:24vw;
  bottom:0;
  width:400px;
  height:4vw;
}
.nav-bar-choose .nav-item{
  width:fit-content;
  padding-left:20px;
  padding-right: 20px;
  height:3.8vw;
  line-height: 3.8vw;
  color:rgb(127, 189, 240);
  font-size:17px;
  font-weight: 600;
  display: inline-block;
  text-align: center;
  cursor:alias;
  /* transition:0.7s; */
}
.nav-bar-choose .nav-item:hover{
  border-bottom:rgb(127, 189, 240) solid 4px;
}
.search {
  width: 13vw;
  height: 2vw;
  border-radius: 5px;
  outline: none;
  border: 1px solid #F1F9FD;
  padding-left: 20px;
  position: absolute;
  font-size: 1em;
  color: grey;
  background-color: #F1F9FD;
}

* {
  margin: 0;
  padding: 0;
}

li {
  list-style: none;
}
/* table  */

</style>
