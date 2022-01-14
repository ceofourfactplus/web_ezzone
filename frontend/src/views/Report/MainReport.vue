<template>
  <div>
    <nav-app>Weekly Report</nav-app>
    <div class="row" style="width: 85%; margin: auto">
      <div class="col-12 w-100 header" style="display: flex">
        <h1>Total Balance Report</h1>
        <select name="" id="">
          <option value=""></option>
        </select>
      </div>
      <div
        class="col-12 mt-1"
        style="background-color: #303344; border-radius: 10px"
      >
        <div class="row w-100">
          <div class="col-9" style="height: 240px"></div>
          <div class="col-3"></div>
        </div>
      </div>
      <div class="col-3 p-1 header">Sale Channel</div>
      <div class="col-6 p-1 header">Const</div>
      <div class="col-3 p-1 header">Best Seller</div>
      <div class="col-3 space"></div>
      <div class="col-6 space"></div>
      <div class="col-3 space"></div>
    </div>
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
export default {
  components: { NavApp },
};
</script>

<style scoped>
h1 {
  color: #fff;
  font-weight: bold;
  font-size: 36px;
  margin-bottom: 0px;
  line-height: 48px;
  margin-left: 20px;
}
.header {
  background-color: #bd523f;
  height: 55px;
  border-radius: 10px;
}
select {
  width: 175px;
  height: 40px;
  margin: auto;
  margin-right: -4px;
}
.row .header {
  width: 95%;
  margin: auto;
  margin-top: 10px;
}
.row .col-6 {
  margin: auto;
  margin-top: 10px;
}
.row .space {
  width: 95%;
  margin: auto;
  background-color: #303344;
  margin-top: 10px;
  height: 445px;
  border-radius: 10px;
}
</style>