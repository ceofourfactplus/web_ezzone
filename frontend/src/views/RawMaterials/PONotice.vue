
<template>
  <div>
    <nav-app :url_name="'RawMaterials'" :rm_menu="true">PO&#160;Notice</nav-app>
    <!-- Second Nav -->
    <div class="row" style="width: 90%; margin: auto">
      <div class="col-8" style="width: 100%; padding-left: 0px">
        <SearchBar style="width: 100%" @search="serchByTyping" />
      </div>
      <div class="col-2 w-100" style="padding: 0px">
        <select v-model="search_type" style="width: 120px; height: 50px">
          <option value="item" selected>Item</option>
          <option value="supplier">Supplier</option>
        </select>
      </div>
      <div class="col-2 w-100">
        <button class="btn-ghost" style="white-space: nowrap" @click="addPO()">
          + PO
        </button>
      </div>
    </div>

    <!-- Table -->
    <div class="table">
      <div class="table-header">
        <div class="row" style="padding-right: 0px">
          <div class="col-1"></div>
          <div
            class="col-4 w-100"
            style="text-align: right; margin-left: -100px"
          >
            Item
          </div>
          <div class="col-1 w-100" style="margin-left: 14px">Qty</div>
          <div class="col-2 w-100">Unit</div>
          <div class="col-3 w-100" style="margin-left: -35px">Min Sup</div>
          <div class="col-1 w-100" style="margin-left: -35px">Status</div>
        </div>
      </div>
      <div
        class="row table-item ps-0"
        v-for="(item, idx) in nearly_items"
        :key="idx"
        style="
          padding-right: 0px;
          background-color: #303344;
          border-radius: 10px;
          margin: 0px;
          margin-top: 5px;
          line-height: 20px;
        "
      >
        <div class="col-1">
          <div class="checkbox-orange" style="position: relative; bottom: 6px">
            <input
              type="checkbox"
              class="me-3 mt-2"
              :value="item"
              @input="selected_item_vals(item)"
            />
          </div>
        </div>
        <div
          class="col-4 w-100"
          @click="po_detail(item)"
          style="
            text-align: left;
            font-size: 24px;
            overflow-x: auto;
            white-space: nowrap;
            line-height: 40px;
            margin-left: -20px;
          "
        >
          {{ item.raw_material_set.name }}
        </div>
        <div class="col-1 w-100" style="text-align: right; line-height: 40px">
          {{ item.raw_material_set.remain }}
        </div>
        <div class="col-2 w-100">
          <p>{{ item.unit_set.unit }}</p>
        </div>
        <div
          class="col-3 w-100"
          style="
            text-align: left;
            overflow-x: auto;
            white-space: nowrap;
            line-height: 40px;
          "
        >
          {{ item.supplier_set.company_name }}
        </div>
        <div class="col-1">
          <img
            style="
              margin-right: 5px;
              position: relative;
              bottom: 3px;
              height: 45px;
              width: 45px;
              transform: rotate(180deg);
            "
            :src="
              $store.state.raw_material.status_image[
                item.raw_material_set.status
              ]['img']
            "
            alt="img"
          />
        </div>
      </div>
    </div>
    <!-- Dropdown List -->
    <div class="dropdown-list" v-if="dropdown_status">
      <div class="row">
        <div class="col-12" v-for="btn in ['Item', 'Supplier']" :key="btn">
          <button class="btn-dropdown-item" @click="select_search(btn)">
            {{ btn }}
          </button>
        </div>
      </div>
    </div>

    <!-- PO Detail -->
    <PODetail
      v-if="po_detail_status"
      :po_item="po_item"
      @show_status="po_detail_status = false"
    />
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
import PODetail from "../../components/materials/PODetail.vue";
import { api_raw_material } from "../../api/api_raw_material.js";
import Table from "../../components/main_component/Table.vue";
export default {
  components: { NavApp, Switch, SearchBar, PODetail, Table },
  data() {
    return {
      search_type: null,
      is_staff: false,
      dropdown_status: false,
      po_detail_status: false,
      po_item: null,
      search_item: null,
      categories: [],
      units: [],
      nearly_items: [],
      temp_items: [
        {
          unit_set: { unit: "" },
          supplier_set: { company_name: "" },
          raw_material_set: { remain: 0, name: "" },
        },
      ],
      selected_items: [],
    };
  },
  methods: {
    fetchNearlySOItems() {
      api_raw_material.get("get-nearly-sold-out/").then((response) => {
        console.log(response.data, "nearly data");
        this.nearly_items = response.data;
        this.temp_items = response.data;
      });
    },
    addPO() {
      this.selected_items.forEach((item) => {
        console.log(item, "unit id");
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
      this.$router.push({ name: "PO" });
    },
    po_detail(item) {
      console.log(item, "item");
      this.po_detail_status = true;
      this.po_item = item;
    },
    serchByTyping(val) {
      var temp = [];
      if (val == "") {
        this.nearly_items = this.temp_items;
      } else {
        if (this.search_type == "item") {
          this.temp_items.forEach((element) => {
            if (element.raw_material_set.name.indexOf(val) + 1 != 0) {
              temp.push(element);
            }
          });
        } else {
          this.temp_items.forEach((element) => {
            if (element.supplier_set.company_name.indexOf(val) + 1 != 0) {
              temp.push(element);
            }
          });
        }
        this.nearly_items = temp;
      }
    },
    selected_item_vals(item) {
      if (!this.selected_items.includes(item)) {
        this.selected_items.push(item);
      } else {
        var idx = this.selected_items.indexOf(item);
        this.selected_items.splice(idx, 1);
      }
      console.log(this.selected_items, "selected");
    },
    select_search(btn) {
      this.search_item = btn;
      this.dropdown_status = false;
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
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
    api_raw_material.get("get-nearly-sold-out/").then((response) => {
      console.log(response.data, "data");
      response.data.forEach((el, idx) => {
        if (el.supplier_set == undefined) {
          var idx = response.data.indexOf(el);
          response.data.splice(idx, 1);
          console.log(el.raw_material_set.name, "id");
        }
      });
      this.nearly_items = response.data;
      this.temp_items = response.data;
    });
  },
};
</script>

<style scoped>
.btn-dropdown-item {
  width: 100%;
  height: 45px;
  background: transparent;
  border: none;
  border-bottom: 1px solid;
}
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
  white-space: nowrap;
  width: 100px;
  height: 50px;
  border: 1px solid #65b0f6;
  color: #65b0f6;
}
.table {
  margin-top: 15px;
}
.btn-dropdown {
  border: 0;
  width: 100%;
  height: 50px;
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