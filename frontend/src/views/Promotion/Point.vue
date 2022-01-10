<template>
  <div>
    <nav-app>{{ tab }}</nav-app>
    <!-- Head -->
    <div class="row">
      <div class="col-11 wrap-search">
        <SearchBar @search="search_by_typing" />
      </div>
      <div style="padding-left: 0px">
        <button v-if="tab == 'Point'" class="btn-ghost" @click="$router.push({ name: 'NewPoint'})">
          + Point
        </button>
        <button style="width: 128px;" v-if="tab == 'Voucher'" class="btn-ghost" @click="$router.push({ name: 'NewVoucher'})">
          + Voucher
        </button>
        <button style="width: 128px;" v-if="tab == 'Package'" class="btn-ghost" @click="$router.push({ name: 'NewPackage'})">
          + Package
        </button>
        <button style="width: 128px;" v-if="tab == 'Rewards'" class="btn-ghost" @click="$router.push({ name: 'NewReward'})">
          + Reward
        </button>
      </div>
    </div>
    <!-- Tabs -->
    <div class="tab">
      <button
        v-for="(item, idx) in ['Point', 'Voucher', 'Package', 'Rewards']"
        :key="idx"
        @click="select_item(item)"
        class="tab-item"
      >
      <p :class="{'tab-selected': item == tab}" style="font-size: 24px;">{{ item }}</p>
        
      </button>
    </div>
    <PointComponent v-if="tab == 'Point'" />
    <Voucher v-if="tab == 'Voucher'" style="margin-top: 10px;" />
    <Package v-if="tab == 'Package'" style="margin-top: 10px;" />
    <Rewards v-if="tab == 'Rewards'" style="margin-top: 10px;" />
    <!-- Card Popup -->
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img src="../../assets/icon/btn-pass.png" alt="" />
      </div>
      <div class="main-text">Saved successfully</div>
    </div>
  </div>
</template>

<script>
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import PointComponent from "../../components/promotion/Point.vue";
import Voucher from "../../components/promotion/Voucher.vue";
import Package from "../../components/promotion/Package.vue";
import Rewards from "../../components/promotion/Rewards.vue";
// import {api_promotion} from "../../api/api_promotion"

export default {
  name: "Point",
  components: {
    SearchBar,
    NavApp,
    Switch,
    PointComponent,
    Voucher,
    Package,
    Rewards,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
  },
  data() {
    return {
      is_staff: false,
      alert: false,
      tab: 'Point',
    };
  },
  methods: {
      select_item(item) {
          this.tab = item
      },
  },
};
</script>

<style scoped>
.tab-selected {
    color: white;
}
.card {
  width: 542px;
  height: 350px;
  top: 230px;
  left: 90px;
}
.btn-ghost {
  border-color: #50D1AA;
  color: #50D1AA;
  width: 119px;
  height: 50px;
  margin: 0px 25px 0px 0px;
}
.wrap-search {
  min-width: 530px;
  width: fit-content;
  padding: 0px;
  margin-left: 35px;
}
.tab {
  overflow: hidden;
  width: 90%;
  height: 46px;
  margin-right: 1%;
  margin-left: 22px;
  margin-top: 10px;
  text-align: left !important;
}

.tab-item {
  background-color: #2f3446;
  color: gray;
  border: none;
  outline: none;
  cursor: pointer;
  padding-top: 6px;
  transition: 0.3s;
  font-size: 26.5px;
  font-style: normal;
  border-radius: 15px 15px 0px 0px;
  margin-top: 0px;
  margin-bottom: 1em;
  height: 59px;
  width: 150px;
  block-size: fit-content;
  text-decoration: none;
  line-height: 31px;
}
</style>