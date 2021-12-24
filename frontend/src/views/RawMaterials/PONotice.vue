
<template>
  <div>
    <!-- Head -->
    <nav-app>PO&#160;Notice</nav-app>
    <div class="row" style="width: 100%; margin-left: 25px">
      <div class="col-6 wrap-search w-100">
        <SearchBar @search="search_raw" style="width: 98%" />
      </div>
      <div class="col-3 w-100" style="padding-left:0px">
        <select v-model="filter_by" class="w-100" style="height:50px;">
          <option value="1">Item</option>
          <option value="2">Supplier</option>
          <option value="3">Unit</option>
        </select>
      </div>
      <div class="col-3 w-100" style="padding-left: 0px; text-align: left">
        <button class="btn-ghost-b" style="width: 120px;height:50px">+&#160;PO</button>
      </div>
    </div>
    <div class="table mt-3">
      <div class="table-header" style="line-height: 40px; font-size: 24px">
        <div class="row">
          <div class="col-5 w-100">Item</div>
          <div class="col-1 w-100">Qty.</div>
          <div class="col-2 w-100">Unit</div>
          <div class="col-2 w-100">Min&#160;Sup</div>
          <div class="col-2 w-100">Status</div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 650px">
        <div v-for="item in rm" :key="item.id" class="table-item">
          <div class="row" style="width: 100%">
            <div
              class="col-5 w-100"
              style="margin: auto; margin-left: 0px; text-align: left"
            ></div>
            <div class="col-1 w-100" style="margin: auto; text-align: left">

              {{ item.remain }}
            </div>
            <div
              class="col-2 w-100"
              style="margin: auto; width: 175px; text-align: left"
            >
              {{ item.unit_set.unit }}
            </div>
          </div>
          <div
            class="col-2 w-100"
            style="margin: auto; width: 175px; text-align: left"
          >
            {{ get_sup(item) }}
          </div>
          <div
            class="col-2 w-100"
            style="margin: auto; text-align: left; padding: 0px"
          >
            <img :src="get_status(item.status)" alt="" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
import { api_raw_material } from "../../api/api_raw_material.js";
export default {
  components: { NavApp, Switch, SearchBar },
  data() {
    return {
      categories: [],
      units: [],
      pickup_items: [],
      temp_pickup: [],
    };
  },
  methods: {
    fetchPickupItems() {
      api_raw_material.get("/pickup/").then((response) => {
        console.log(response.data, "pickup data");
        console.log(response.data.unit_set, "unit_set");
        this.pickup_items = response.data;
        this.temp_pickup = response.data;
      });
    }, 
    serchByTyping(val) {
      var temp = [];
      if (val == "") {
        this.pickup_items = this.temp_pickup;
      } else {
        this.temp_pickup.forEach((element) => {
          if (element.raw_material_set.name.indexOf(val) + 1 != 0) {
            temp.push(element);
          }
        });
        this.pickup_items = temp;
      }
    },
  },
  watch: {
    remain() {
      this.total_price = this.remain * this.avg_price;
    },
    avg_price() {
      this.total_price = this.remain * this.avg_price;
    },
  },
  mounted() {

  },
};
</script>

<style scoped>
</style>