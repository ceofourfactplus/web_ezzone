
<template>
  <div>
    <nav-app :url_name="'RawMaterials'" :rm_menu="true">PO&#160;Notice</nav-app>
    <!-- Second Nav -->
    <div class="row" style="width: 90%; margin: auto">
      <div class="col-8" style="width: 100%; padding-left: 0px">
        <SearchBar style="width: 100%" @search="serchByTyping" />
      </div>
      <div class="col-2 w-100" style="padding: 0px">
        <button
          class="btn-dropdown w-100"
          @click="dropdown_status = !dropdown_status"
        >
          Item<span class="icon-dropdown"></span>
        </button>
      </div>
      <div class="col-2 w-100">
        <button class="btn-ghost" @click="addPO()">+ PO</button>
      </div>
    </div>

    <!-- Table for admin -->
    <Table
      v-if="is_staff"
      :head1="'Item'"
      :head2="'Qty'"
      :head3="'Unit'"
      :head4="'Min Sup'"
      :head5="'Status'"
      :elements="nearly_items"
      :category="'po_notice'"
      @show_pickup="showPickup"
      @show_rm_detail="editRM"
      @po_detail="po_detail"
      @selected_items="selected_item_vals"
    />
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
      is_staff: false,
      dropdown_status: false,
      po_detail_status: false,
      po_item: null,
      search_item: null,
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
    // fetchPriceRM() {
    //   api_raw_material.get("/price-raw-material/").then((response) => {
    //     console.log(response.data, "price-raw-material data");
    //   });
    // },
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
        this.temp_items.forEach((element) => {
          if (element.raw_material_set.name.indexOf(val) + 1 != 0) {
            temp.push(element);
          }
        });
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
  mounted() {},
  beforeMount() {
    this.fetchNearlySOItems()
  }
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