<template>
  <div>
    <!-- Head -->
    <nav-app>Database Settings</nav-app>
    <!-- Content -->
    <div class="content">
      <!-- Change Setting -->
      <div class="row" style="margin-top: 20px;">
        <div class="col-5 w-100 dbs-font" style="margin-top: 20px;">
          Change Setting
        </div>
        <div class="col-6 w-100 dbs-font" style="margin-top: 20px;">
          <input type="text" style="width: 224px; height: 50px; background: #717171; display: inline;"><p style="display: inline; margin-left: 6px;">บาท</p>
        </div>
        <div class="col-1 w-100" style=" margin-top: 20px;">
          <div class="img-wrap">
           <img src="../../assets/icon/save.png" style="width: 30px; margin-top: 9px;" @click="save"> 
          </div>
        </div>
      </div>
      <!-- Unit Setting -->
      <div class="row" style="margin-top: 45px;">
        <div class="col-4 w-100 dbs-font">
          Unit Setting
        </div>
        <div class="col-1 w-100">
          <img src="../../assets/icon/edit-orange.png" style="width: 25px; margin-top: 5px" @click="$router.push({ name: 'RMUnit'})">
        </div>
      </div>
      <!-- Unit Items -->
      <div class="row">
          <div class="col-3 w-100 dbs-font" style="font-weight: normal">
            x Unit
          </div>
      </div>
      <!-- Sale Channel Setting -->
      <div class="row" style="margin-top: 45px;">
        <div class="col-6 w-100 dbs-font" style="margin-left: -5px;">
          Sale Channel Setting
        </div>
        <div class="col-1 w-100">
          <img src="../../assets/icon/edit-orange.png" style="width: 25px; margin-top: 5px" @click="$router.push({ name: 'SaleChannel'})">
        </div>
      </div>
      <!-- Sale Channel -->
      <div class="row" style="width: 540px; margin-left: 39px;">
        <div class="col-6 w-100" style="margin-top: 10px;">
          <img src="../../assets/icon/lineman-35x35.png" style="display: inline;">
          <p style="display: inline; font-size: 20px; color: white; margin-left: 10px;">Line Man</p>
          <div class="sc-status">ACTIVE</div>
        </div>
        <div class="col-6 w-100" style="margin-top: 10px;">
          <img src="../../assets/icon/robin-35x35.png" style="display: inline;">
          <p style="display: inline; font-size: 20px; color: white; margin-left: 10px;">Line Man</p>
          <div class="sc-status">ACTIVE</div>
        </div>
      </div>
      <div class="row" style="width: 540px; margin: 20px 0px 0px 39px;">
        <div class="col-6 w-100" style="margin-top: 10px;">
          <img src="../../assets/icon/foodpanda-35x35.png" style="display: inline;">
          <p style="display: inline; font-size: 20px; color: white; margin-left: 10px;">Line Man</p>
          <div class="sc-status">ACTIVE</div>
        </div>
        <div class="col-6 w-100" style="margin-top: 10px;">
          <img src="../../assets/icon/grab-35x35.png" style="display: inline;">
          <p style="display: inline; font-size: 20px; color: white; margin-left: 10px;">Line Man</p>
          <div class="sc-status">ACTIVE</div>
        </div>
      </div>
    </div>
    <!-- card pop up -->
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img src="../../assets/icon/btn-pass.png" alt="" />
      </div>
      <div class="main-text">Saved successfully</div>
    </div>
  </div>
</template>

<script>
// import { api_raw_material } from "../../api/api_raw_material";
import Tabs from "../../components/materials/Tabs.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";
import Table from "../../components/main_component/Table.vue";
import PickupPopup from "../../components/materials/PickupPopup.vue";

export default {
  components: {
    Tabs,
    SearchBar,
    NavApp,
    Table,
    PickupPopup,
  },
  mounted() {

  },

  data() {
    return {
      alert: false,
    };
  },
methods: {
  save() {
    this.alert = true
    setTimeout(() => {
      this.alert = false;
    }, 2000)
  },
}
};
</script>

<style scoped>
  .sc-status {
    width: 65px;
    height: 24px;
    display: inline;
    font-size: 12px;
    background: #50D1AA;
    border-radius: 999px;
    padding: 4px 8px;
    margin-left: 10px;
  }
  .dbs-font {
    font-size: 24px; 
    color: white; 
    font-weight: bold;
  }
  .img-wrap {
    width: 55px;
    height: 50px;
    border: 1px solid #EA7C69;
    box-sizing: border-box;
    border-radius: 5px;
    background: transparent;
    margin-right: 12px;
  }
  .content {
    width: 616px;
    height: 414px;
    margin-left: 77px;
    margin-top: 58px;
    background: #303344;
    border-radius: 20px;
  }
</style>