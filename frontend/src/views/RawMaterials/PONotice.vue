
<template>
  <div>
    <nav-app save="true">PO&#160;Notice</nav-app>
    <!-- Second Nav -->
    <div class="row" style="width: 680px; margin-left: 20px">
      <div class="col-8" style="width: 100%">
        <SearchBar style="width: 450px" @search="serchByTyping" />
      </div>
      <div class="col-2" style="width: 100%">
        <button
          class="btn-dropdown"
          @click="dropdown_status = !dropdown_status"
        >
          Item<span class="icon-dropdown"></span>
        </button>
      </div>
      <div class="col-2" style="width: 100%">
        <button class="btn-ghost" @click="addPO()">+ PO</button>
      </div>
    </div>
    <!-- Table -->
    <div class="table">
      <div class="table-header">
        <div class="row">
          <div class="col-5 item-in-row">Item</div>
          <div class="col-1 item-in-row" style="padding-left: 30px">Qty</div>
          <div class="col-2 item-in-row" style="padding-left: 10px">Unit</div>
          <div class="col-3 item-in-row">Min Sup</div>
          <div class="col-1 item-in-row" style="padding-right: 20px">
            Status
          </div>
        </div>
      </div>
      <div
        class="row table-item"
        v-for="item in nearly_items"
        :key="item.id"
        style="margin-left: 0px"
      >
        <div class="col-1 item-in-row">
          <div class="checkbox-orange">
            <input
              type="checkbox"
              class="me-3 mt-2"
              :value="item"
              v-model="selected_items"
            />
          </div>
        </div>
        <div class="col-4 item-in-row" style="text-align: left" @click="po_detail(item)">
          {{ item.raw_material_set.name }}
        </div>
        <div class="col-1 item-in-row" @click="po_detail(item)">{{ item.raw_material_set.remain }}</div>
        <div class="col-2 item-in-row" @click="po_detail(item)" style="padding-left: 10px">
          {{ item.unit_set.unit }}
        </div>
        <div class="col-3 item-in-row" @click="po_detail(item)">{{ item.supplier_set.company_name }}</div>
        <div class="col-1 item-in-row" @click="po_detail(item)" style="padding-right: 20px">
          <img :src="$store.state.raw_material.status_image[item.raw_material_set.status]" />
        </div>
      </div>
    </div>
    <!-- Dropdown List -->
    <div class="dropdown-list" v-if="dropdown_status">
      <div class="row">
        <div class="col-12">
          <button style="width: 100%; height: 50px; background: transparent">
            Item
          </button>
        </div>
        <div class="col-12">
          <button style="width: 100%; height: 50px; background: transparent">
            Sth
          </button>
        </div>
      </div>
    </div>

    <!-- PO Detail -->
    <PODetail v-if="po_detail_status" :po_item="po_item" @show_status="po_detail_status = false" />
    
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
import PODetail from "../../components/materials/PODetail.vue";
import { api_raw_material } from "../../api/api_raw_material.js";
export default {
  components: { NavApp, Switch, SearchBar, PODetail },
  data() {
    return {
      dropdown_status: false,
      po_detail_status: false,
      po_item: null,
      categories: [],
      units: [],
      nearly_items: [],
      temp_items: [],
      selected_items: [],
    };
  },
  methods: {
    fetchNearlySOItems() {
      api_raw_material.get("/get-nearly-sold-out/").then((response) => {
        console.log(response.data, "nearly data");
        this.nearly_items = response.data;
        this.temp_items = response.data;
      });
    },
    fetchPriceRM() {
      api_raw_material.get("/price-raw-material/").then((response) => {
        console.log(response.data, "price-raw-material data");
      });
    },
    addPO() {
      this.selected_items.forEach((item) => {
        console.log(item, 'unit id')
        var data = {
          raw_material_id: item.raw_material_id,
          supplier_id: item.supplier_id,
          unit_id: item.unit_id,
          create_by_id: this.$store.state.auth.userInfo.id,
          amount: item.raw_material_set.remain,
          status: item.raw_material_set.status,
          last_price: item.last_price,
        };
        api_raw_material.post("/po/", data).then((response) => {
          console.log(response.data, "po");
        });
      });
    },
    po_detail(item) {
      console.log(item, "item")
      this.po_detail_status = true
      this.po_item = item
    },
    serchByTyping(val) {
      var temp = [];
      if (val == "") {
        this.nearly_items = this.temp_items;
      } else {
        this.temp_items.forEach((element) => {
          if (element.name.indexOf(val) + 1 != 0) {
            temp.push(element);
          }
        });
        this.nearly_items = temp;
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
    this.fetchNearlySOItems();
    this.fetchPriceRM();
  },
};
</script>

<style scoped>
.item-in-row {
  text-align: center;
  font-size: 28px;
  width: 100%;
}
.dropdown-list {
  background: white;
  position: absolute;
  top: 135px;
  right: 100px;
  width: 180px;
}
.btn-ghost {
  width: 100px;
  border: 1px solid #65b0f6;
  color: #65b0f6;
  margin-left: 28px;
}
.table {
  margin-top: 15px;
}
.btn-dropdown {
  width: 110px;
  height: 45px;
  color: #889898;
  background: #303344;
  font-weight: bold;
  font-size: 24px;
  border-radius: 10px;
  text-align: center;
  margin-left: 20px;
}
span.icon-dropdown {
  background: url("../../assets/icon/down-arrow.png") no-repeat transparent;
  background-size: 20px;
  float: right;
  margin-right: 0px;
  margin-top: 10px;
  width: 20px;
  height: 20px;
}
</style>