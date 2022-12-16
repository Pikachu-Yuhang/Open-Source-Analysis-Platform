<template>

        
            <div class="card-w" :class="state?'left':'right'"  v-if="show1">
                <div class="intro"><span>State:</span>
                    <svg v-if="state" t="1671158946135" style="vertical-align:text-bottom" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2685" width="30" height="30"><path d="M969.6 208c-9.6-9.6-25.6-9.6-35.2 0L425.6 745.6c-19.2 19.2-48 19.2-70.4 3.2L89.6 496c-9.6-9.6-25.6-9.6-35.2 0-9.6 9.6-9.6 25.6 0 35.2L320 784c38.4 38.4 102.4 35.2 137.6-3.2l508.8-537.6c12.8-9.6 12.8-25.6 3.2-35.2z" fill="white" p-id="2686"></path></svg>
                    <svg t="1671159168752" v-if="!state" style="vertical-align:text-bottom" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3633" width="30" height="30"><path d="M640 921.6V981.333333l-85.333333-85.333333-42.666667-42.666667h21.333333c174.933333 0 320-145.066667 320-320 0-145.066667-93.866667-264.533333-226.133333-307.2L571.733333 170.666667c183.466667 21.333333 324.266667 174.933333 324.266667 358.4 0 174.933333-123.733333 320-290.133333 354.133333l34.133333 38.4zM426.666667 145.066667V85.333333l85.333333 85.333334 42.666667 42.666666h-21.333334C358.4 213.333333 213.333333 354.133333 213.333333 533.333333c0 140.8 93.866667 264.533333 221.866667 302.933334l55.466667 55.466666c-179.2-21.333333-320-170.666667-320-358.4C170.666667 358.4 294.4 213.333333 460.8 179.2l-34.133333-34.133333z" fill="white" p-id="3634"></path></svg>
                </div>
                    <div class="name">{{ name }}</div>
                <div class="hover">
                    {{state?'this repo is ready!':"this repo is loading......"}}
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
        name:{
            String
        },
        state:{
            type:Boolean,
            default:true,
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
    width: 380px;
    height: 200px;
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
    margin-top:15px;
    text-align: left;
    /* height: 60px;
    line-height: 60px; */
    font-size: 16px;
    color: white;
    padding-left: 30px;
    font-weight: 550;
}

.left .intro span {
    font-size: 24px;
    color: #3382DF;
    padding-right: 16px;
}


.right .intro span {
    font-size: 24px;
    color: #842DB9;
    padding-left: 6px;
}

.name {
    height: 80px;
    line-height: 80px;
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