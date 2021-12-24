<template>
  <div>
    <nav-app save="true" @save="save()">Pickup&#160;List</nav-app>
    <SearchBar
      @search="serchByTyping"
      style="width: 680px; margin-left: 40px"
    />

    <div class="table">
      <div class="table-header">
        <div class="row">
          <div class="col-3 item-in-row" style="margin-left: 10px">Date</div>
          <div class="col-5 item-in-row">Name</div>
          <div class="col-2 item-in-row" style="margin-left: -7px">Qty</div>
          <div class="col-2 item-in-row" style="margin-left: -12px">Unit</div>
        </div>
      </div>
      <div class="row table-item" v-for="item in pickup_items" :key="item.id">
        <div class="col-3 item-in-row i">
          {{ item.create_at.slice(0, 10).replace(/-/g, "/") }}
        </div>
        <div
          class="col-5 i"
          style="
            text-align: left;
            width: 100%;
            font-size: 28px;
            padding-left: 30px;
          "
        >
          {{ item.raw_material_set.name }}
        </div>
        <div class="col-2 item-in-row i">{{ item.amount }}</div>
        <div class="col-2 item-in-row i">{{ item.unit_set.unit }}</div>
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
.item-in-table-item {
  width: 100%;
  text-align: center;
}
.item-in-table-head {
  width: 100%;
  text-align: center;
}
.table-item-in-po {
  width: 100%;
  height: 59px;
  background: #303344;
  border-radius: 10px;
  margin-top: 10px;
  font-size: 30px;
}
.table-head-in-po {
  width: 100%;
  height: 59px;
  background: #889898;
  border-radius: 10px;
  margin-top: 10px;
  font-size: 30px;
  color: white;
}
.po-detail-img {
  width: 218px;
  height: 218px;
  margin: 20px 20px 20px 20px;
}
.over-wrapper {
  width: 619px;
  height: 271.11px;
}
.po-detail-popup {
  width: 619px;
  height: 640px;
  top: 20%;
  left: 12%;
  position: absolute;
  background-color: #252836;
  border: 2px solid #ea7c69;
  border-radius: 20px;
}
.popup-header {
  font-weight: 800;
  font-size: 48px;
  line-height: 56px;
  text-align: center;
  margin-top: 10px;
  width: 100%;
  color: white;
}
.item-in-row {
  text-align: center;
  font-size: 28px;
  width: 100%;
}
.i {
  padding: 0px;
}
.table {
  width: 680px;
  margin-top: 15px;
}
div.row.table-item {
  margin-left: 0px;
}
</style>