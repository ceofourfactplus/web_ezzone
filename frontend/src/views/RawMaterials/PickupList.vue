<template>
  <div>
    <nav-app :rm_menu="true" :url_name="'DashBoard'">Pickup&#160;List</nav-app>
    <div class="row" style="width: 100%; margin: auto">
      <div class="col-12">
        <SearchBar
          @search="serchByTyping"
          style="width: 98%; margin-left: 5px"
        />
      </div>
    </div>

    <div class="table">
      <div class="table-header" style="width: 115%; margin-left: -49px;">
        <div class="row">
          <div class="col-3 w-100" style="margin-left: 10px">Date</div>
          <div
            class="col-4 w-100"
            style="margin-left: 18px; text-align: center"
          >
            Name
          </div>
          <div class="col-1 w-100">Qty</div>
          <div class="col-1 w-100" style="margin-left: 14px">Unit</div>
          <div class="col-3 w-100">Pickup By</div>
        </div>
      </div>
      <div class="row table-item" v-for="item in pickup_items" :key="item.id" style="width: 115%; margin-left: -49px;">
        <div class="col-3 w-100">
          {{ item.create_at.slice(0, 10).replace(/-/g, "/") }}
        </div>
        <div class="col-4 w-100" style="text-align: left; padding-left: 20px; white-space: nowrap; overflow-x: auto;">
          {{ item.raw_material_set.name }}
        </div>
        <div class="col-1 w-100" style="margin-left: 5px">
          {{ item.amount }}
        </div>
        <div class="col-1 w-100" style="margin-left: 20px; margin-right: -20px">
          {{ item.unit_set.unit }}
        </div>
        <div class="col-3 w-100" style="margin-left: 10px">
          {{ item.create_by_set.username }}
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
    this.fetchPickupItems();
    api_raw_material.get("category").then((response) => {
      this.categories = response.data;
    });
    api_raw_material.get("unit").then((response) => {
      console.log(response.data, "unit");
      this.units = response.data;
    });
  },
};
</script>

<style scoped>
.table {
  width: 680px;
  margin-top: 15px;
}
div.row.table-item {
  margin-left: 0px;
}
</style>