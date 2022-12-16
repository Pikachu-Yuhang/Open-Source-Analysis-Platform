<template>
    <div style="margin-top:5vh;margin-bottom:5vh">
        <div class="card-c" style="margin-left:2%" @click="change1">
            <div class="card-w left" v-if="show1">
                <div class="intro">{{ intro }}<span>Pytorch</span></div>
                <div class="name">{{ name1 }}</div>
                <div class="hover">
                    Click me to check our algorithm
                </div>
            </div>
            <div v-if="!show1" class="card-w left">
                <div class="explain"><span>Algorithm:</span></div>
                <div class="explain">{{explain}}</div>
            </div>
        </div>


        <div class="card-c" @click="change2">
            <div class="card-w right" v-if="show2">
                <div class="intro">{{ intro }}<span>TensorFlow</span></div>
                <div class="name">{{ name2 }}</div>
                <div class="hover">
                    Click me to check our algorithm
                </div>
            </div>
            <div v-if="!show2" class="card-w right">
                <div class="explain"><span>Algorithm:</span></div>
                <div class="explain">{{explain}}</div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'CardVue',
    data(){
        return{
            show1:true,
            show2:true,
        }
    },
    created:function(){
    // this.$http.get('/puller/pytorch/pytorch/star_per_month/2022/')
    //   .then((res) => {
    //     <data to be load> = res.data.<key>;
    //   })
  },
    methods:{
        change1(){
            this.show1=!this.show1;
          },
          change2(){
            this.show2=!this.show2;
          }
    },
    props: {
        intro: {
            String,
        },
        name1: {
            String
        },
        name2: {
            String
        },
        explain:{

            default:"here we will expalin how we choose this data"
        }

    }

}
</script>
<style scoped>
.explain{
    padding-top:20px;
    padding-left:30px;
    padding-right:30px;
    color:white;
    font-size:17px;
    text-align: justify;
    font-weight: 500;
}
.left .explain span{
    font-size: 24px;
    color: #3382DF;
    padding-left: 6px;
}
.right .explain span{
    color: #842DB9;
    font-size: 24px;
    padding-left: 6px;
}
.card-c {
    width: 45%;
    text-align: center;
    position: relative;
    display: inline-block;
}

.card-w {
    vertical-align: middle;
    position: relative;
    display: inline-block;
    width: 520px;
    height: 260px;
    transition:1s;
}

.right {
    background: linear-gradient(107.96deg, #D5C7FF 0%, #AA8EFF 57.2%, #9189FF 100%);
    border-radius: 22px;
}

.left {
    background: linear-gradient(107.42deg, #54F9F2 0.8%, #4EC5F4 51.8%, #32A5F8 99.89%);
    border-radius: 22px;
}

.intro {
    text-align: left;
    height: 60px;
    line-height: 60px;
    font-size: 16px;
    color: white;
    padding-left: 30px;
    font-weight: 550;
}

.left .intro span {
    font-size: 24px;
    color: #3382DF;
    padding-left: 6px;
}


.right .intro span {
    font-size: 24px;
    color: #842DB9;
    padding-left: 6px;
}

.name {
    height: 100px;
    line-height: 100px;
    font-size: 35px;
    color: white;
    font-weight: 700;
}

.left .hover {
    position: absolute;
    bottom: 20px;
    left: 30px;
    font-size: 15px;
    color: #9EE8FF
}

.right .hover {
    position: absolute;
    bottom: 20px;
    left: 30px;
    font-size: 15px;
    color: #E2C3FF
}
</style>