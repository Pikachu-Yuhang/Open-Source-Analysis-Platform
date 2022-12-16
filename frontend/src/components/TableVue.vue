<template>
      <div class="table-wrapper">
        <table>
            <tr v-for="row in tableContent" :key="row.left">
                <td>{{row.first}}</td>
                <td>{{row.second}}</td>
                <td>{{row.third}}</td>
            </tr>

        </table>
      </div>
</template>
<script>
export default {
  name: 'TableVue',
  props:{
    tableContent:{
        Array
    }
  }
}
</script>
<style scoped>
.table-wrapper {
  width: fit-content;
  position: relative;
}
.table-wrapper table {
  border-spacing: 1vw;
}
.wrapper tr {
  text-align: left;
}
.table-wrapper tr:first-child td{
  background-color: #E5E5E5;
  text-align: center;
  /* font-size: 17px; */
}
.table-wrapper td {
  display: inline-block;
  border-radius: 10px;

  /* display: inline; */
  height: 46px;
  line-height: 46px;
  font-size: 16px;
  
  color: black;
  margin-right: 2vw;
}
.table-wrapper td:first-child {
  background-color: #E5E5E5;
  min-width: 115px;
  width: fit-content;
  text-align: left;
  font-weight: 500;
  padding-left: 20px;
  padding-right: 20px;
}
.table-wrapper td:nth-child(2),td:nth-child(3) {
  background-color: #F0F0F0;
  width:180px;
  padding-right: 15px;
  text-align: right;
  font-weight: 550;
}
</style>>