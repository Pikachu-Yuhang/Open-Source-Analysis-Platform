<template>
    <div class="all">
        <div style="height: 6vw"></div>
        <div class="wrapper">
            <h1>Repo Management</h1>
            <input id="111" type="text" placeholder="Add Repo"/><button-vue @click="addRepo" style="vertical-align:middle;"></button-vue>
            <div style="width:90%;margin:auto">
                <repo-card class="repocard" name="Pytorch"></repo-card>
                <repo-card class="repocard" name="TensorFlow" ></repo-card>
                <repo-card v-for="item in repolist" class="repocard" :name="item" :state="false" :key="item"></repo-card>
            </div>
            
        </div>
        
    </div>
</template>
  
<script>
import buttonVue from '@/components/buttonVue.vue';
import repoCard from '@/components/repoCard.vue'
export default {
  components: { buttonVue,repoCard },
    name: "HomeVue",
    data() {
        return {
            repolist:[],
        }
    },
    created() {
        // pytorch star data
        this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
            .then((res) => {
                console.log(res.data.starred);
                this.starDataPytorch = res.data.starred;
            })
        this.$http.get('/puller/pytorch/pytorch/commit_per_month/2022/')
            .then((res) => {
                this.commitDataPytorch = res.data.pushed;
            })

    },
    props: {},
    methods:{
        addRepo(){
            var n=document.getElementById("111");
            this.repolist.push(n.value);
        }
    }
    
    
};

</script>
  
<style scoped>
.all{
    background-image: url(@/assets/log.jpg);
    background-size: cover;
    min-height:100vh;
    background-attachment: fixed;
    position:relative;
}
.repocard{
    float:left;
    margin:20px;
}
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
   
    margin: 0;
    padding: 0;
}

/* left-bar */


.wrapper {
    position: relative;
   
    margin-left: 0;
    min-height: 90vh;
    padding-left: 2vw;
    text-align: center;
}
.wrapper input{
    background-color: white;
    height:60px;
    width:300px;
    border:none;
    border-radius: 5px;
    margin-top:30px;
    padding-left:10px;
    box-sizing: border-box;
    vertical-align: middle;
    margin-right: 20px;
    transform: translateY(-7px);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
}

.wrapper h1 {
   
    font-size: 3em;
    background: linear-gradient(90deg, #23aee5 0%, #218cd9 5%, #9189ff 10%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 580;
    text-align: center;
}

.wrapper h2 {
    font-size: 2.5em;
    background: linear-gradient(90deg, #23aee5 0%, #218cd9 5%, #9189ff 10%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 580;
}


</style>
  