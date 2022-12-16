<template>
    <div>
        <div style="height: 4vw"></div>
        <div class="wrapper">
            <div style="height:15vh"></div>
            <div >
                <div class="left">
                    <h3>
                        Welcome
                    </h3>
                    <div class="text">
                        Open source project analyst is a system
                        that can visualize the data of projects in
                        a vivid way.
                    </div>
                </div>
                <div class="right">
                    <h3> Login </h3>
                    <input type="text" id="1111" placeholder="User Name" />
                    <input type="password" placeholder="Passward" />
                    <button @click="addUser">登录</button>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import router from '@/router';
export default {
    name: "HomeVue",
    data() {
        return {
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
        addUser(){
            var n=document.getElementById("1111");
            localStorage.setItem("user",n.value);
            var m=confirm("登录成功");
            if(m==true)
            {
                router.replace({path:'/'})
            }

        }
    }

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


.wrapper {
    position: relative;
    background-color: #FAFAFA;
    margin-left: 0;
    min-height: 90vh;
    padding-left: 2vw;
    z-index: 0;
    background-image: url(@/assets/log.jpg);
    background-size: cover;
    min-height: 92vh;
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
.left{
    margin-left:10vw;
    width:580px;
    height:388px;
    background-image: url(@/assets/log.png);
    background-size: 100%,100%;
    background-repeat: no-repeat;
    padding:40px;
    display: inline-block;
}
.left h3{
    color:white;
    font-size:42px;
    font-weight: 700;
}
.left .text{
    padding-top:40px;
    font-size:22px;
    line-height: 60px;
    color:white;
    font-weight: 500;
}
.right{
    margin-left:3vw;
    width:300px;
    height:412px;
    border-radius: 30px;
    background-color: #F0F0F0;
    vertical-align: middle;
    padding-left:40px;
    padding-right:40px;
    padding-top:40px;
    display: inline-block;
}
.right h3{
    color:black;
    font-size:42px;
    font-weight: 700;
}
.right input{
    background-color: white;
    height:50px;
    width:300px;
    border:none;
    border-radius: 5px;
    margin-top:30px;
    padding-left:10px;
    box-sizing: border-box;
}
.right button{
    margin-top:40px;
    height:50px;
    width:300px;
    border-radius: 5px;
    text-align: center;
    color:white;
    font-size:25px;
    font-weight: 600;
    border:none;
    background: linear-gradient(90deg, #23aee5 0%, #218cd9 50%, #9189ff 100%);
}
.right button:active{
    transition:0s;
    transform: scale(0.95);
}
</style>
  