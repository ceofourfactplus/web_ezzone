
<template>
  <div>
    <nav-app save="true">PO&#160;Notice</nav-app>
    <!-- Second Nav -->
    <div class="row" style="width: 680px; margin-left: 20px">
      <div class="col-8" style="width: 100%">
        <SearchBar @search="serchByTyping" />
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
        <button class="btn-ghost" @save="addPO()">+ PO</button>
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
        <div class="col-4 item-in-row" style="text-align: left">
          {{ item.name }}
        </div>
        <div class="col-1 item-in-row">{{ item.remain }}</div>
        <div class="col-2 item-in-row" style="padding-left: 10px">
          {{ item.unit_s_id }}
        </div>
        <div class="col-3 item-in-row">Min Sup</div>
        <div class="col-1 item-in-row" style="padding-right: 20px">
          <img :src="$store.state.raw_material.status_image[item.status]" />
        </div>
      </div>
    </div>

    <div class="dropdown-list" v-if="dropdown_status">
      <div class="row">
        <div class="col-12">
          <button style="width: 100%; height: 50px; background: trnasparent">
            Item
          </button>
        </div>
        <div class="col-12">
          <button style="width: 100%; height: 50px; background: trnasparent">
            Sth
          </button>
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
      dropdown_status: false,
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
    addPO() {
      this.selected_items.forEach((item) => {
        console.log(item.unit_s_id, 'unit id')
        var data = {
          raw_material_id: item.id,
          supplier_id: 1,
          unit_id: item.unit_s_id,
          create_by_id: this.$store.state.auth.userInfo.id,
          amount: item.remain,
          status: false,
        };
        api_raw_material.post("/po/", data).then((response) => {
          console.log(response.data, "po");
        });
      });
    },
    serchByTyping(val) {
      var temp = [];
      if (val == "") {
        this.nearly_items = this.temp_items;
      } else {
        this.temp_items.forEach((element) => {
          if (element.raw_material_set.name.indexOf(val) + 1 != 0) {
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