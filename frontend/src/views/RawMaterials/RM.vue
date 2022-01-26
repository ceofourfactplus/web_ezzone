<template>
  <div>
    <!-- Head -->
    <nav-app :url_name="'DashBoard'" :rm_menu="true">Raw Material</nav-app>
    <div class="row" v-if="is_staff" style="margin: auto; width: 90%">
      <div class="col-10 w-100 ps-0">
        <SearchBar @search="serchByTyping" />
      </div>
      <div class="col-2 w-100" style="padding: 0px">
        <button
          class="btn-ghost w-100 p-0"
          style="height: 45px; white-space: nowrap"
          @click="$router.push({ name: 'CreateRM' })"
        >
          + New
        </button>
      </div>
    </div>

    <!-- search bar -->
    <SearchBar
      v-else
      style="width: 90%; margin: auto"
      @search="serchByTyping"
    />

    <!-- select category -->
    <div
      style="
        display: flex;
        height: 50px;
        overflow-x: auto;
        margin: auto;
        width: 90%;
        overflow-y: hidden;
        
      "
      class="mt-2"
    >
      <button
        class="btn-gray category me-1"
        style="
          min-width: 100px;
          white-space: nowrap;
          padding: 0px;
          opacity: 0.6;
        "
        :class="{
          active: select_category == 'all',
          'text-active': select_category == 'all',
        }"
        @click="select_category = 'all'"
      >
        all
      </button>
      <button
        v-for="category in categories"
        :key="category.id"
        class="btn-gray category me-1"
        style="min-width:265px; white-space: nowrap; padding: 0px;opacity:0.6;"
        :class="{
          active: select_category == category.id,
          'text-active': select_category == category.id,
        }"
        @click="select_category = category.id"
      >
        {{ category.name }}
      </button>
    </div>

    <!-- Table -->
    <div class="table">
      <div class="table-header">
        <div class="row" style="padding-right: 0px;">
          <div class="col-6 w-100">Item</div>
          <div class="col-2 w-100">Qty</div>
          <div class="col-2 w-100">Unit</div>
          <div class="col-1 w-100">Status</div>
          <div class="col-1 w-100" style="margin-right: 20px;">Pickup</div>
        </div>
      </div>
      <div class="row table-item" v-for="item in raw_materials" :key="item.id" style="padding-right: 0px; background-color: #303344; border-radius: 10px; margin: 0px; margin-top: 5px; line-height: 40px;">
          <div
              class="col-6 w-100"
              @click="editRM(item)"
              style="text-align: left; white-space:nowrap;overflow-x:auto;"
            >
              {{ item.name }}
            </div>
            <div
              class="col-2 w-100"
              style="margin-left: 16px;"
            >
              {{ item.remain }}
            </div>
            <div
              class="col-2 w-100"
              style="margin-left: 23px;"
            >
              {{ item.unit_set.unit }}
            </div>
            <div
              class="col-1 w-100"
              style="margin-right: 70px;"
            >
              <img
                :src="
                  $store.state.raw_material.status_image[item.status]['img']
                "
                style="position: relative; bottom: 3px; margin-right: -30px;"
                :style="$store.state.raw_material.status_image[item.status]['style']"
                alt="img"
              />
            </div>
            <div
              class="col-1 w-100"
              @click="showPickup(item)"
              style="margin-right: 20px;"
            >
              <img style="width: 52px; height: 50px; position: relative; bottom: 3px;" src="../../assets/icon/pickup.png" alt="img" />
            </div>
      </div>
    </div>

    <!-- Card Popup -->
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img src="../../assets/icon/btn-pass.png" alt="" />
      </div>
      <div class="main-text">Saved successfully</div>
    </div>

    <!-- Show Pickup Popup -->
    <div class="blur" style="height:100%;" v-if="show_pickup_status" @click="sjot = false">
      <PickupPopup
        :item="raw_material_item"
        @show_status="hideShowPickup"
        @confirm="pickup"
      />
    </div>

  </div>
</template>

<script>
import { api_raw_material } from "../../api/api_raw_material";
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
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
    console.log(this.$route.name, "query page");
    this.fetchRMCategories();
    this.fetchRMUnit()
  },
  beforeMount() {
    this.fetchRawMaterials();
  },
  data() {
    return {
      category: "all",
      image: "",
      show_img: null,
      show_pickup_status: false,
      is_staff: false,
      add_rm: false,
      unit: "",
      alert: false,
      slide_show: false,
      select_category: "",
      raw_material_item: {
        img: "",
        status: 1,
        name: "",
        category: "",
        qty: null,
        minimum: 1,
        maximum: 10,
        price: 0,
        avg_price: null,
        max_price: null,
        min_price: null,
        in_refrigerator: false,
      },
      categories: [],
      img: require("../../assets/icon/frame.png"),
      raw_materials: [],
      temp_rm: [],
      units: [],
    };
  },
  methods: {
    fetchRMCategories() {
      api_raw_material.get("/category/").then((response) => {
        this.categories = response.data;
      });
    },
    fetchRawMaterials() {
      api_raw_material.get("raw-material/").then((response) => {
        console.log(response.data, "response");
        this.raw_materials = response.data;
        this.temp_rm = response.data;
      });
    },
    fetchRMUnit() {
      api_raw_material.get("/unit/").then((response) => {
        this.units = response.data;
      });
    },
    saveChange() {
      this.alert = true;
      setTimeout(() => {
        this.alert = false;
        this.add_rm = false;
        // this.$router.push({ name: "RawMaterials" });
      }, 2000);
      this.raw_material_item.img = "";
      this.raw_material_item.status = 1;
      this.raw_material_item.name = "";
      this.raw_material_item.category = "";
      this.raw_material_item.qty = "";
      this.raw_material_item.minimum = 1;
      this.raw_material_item.maximum = 10;
      this.raw_material_item.price = 0;
      this.raw_material_item.avg_price = null;
      this.raw_material_item.max_price = null;
      this.raw_material_item.min_price = null;
      this.raw_material_item.in_refrigerator = false;
    },
    onFileChange(e) {
      this.img = e.target.files[0];
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
    },
    edit(item) {
      console.log(item, "item");
    },
    showPickup(item) {
      this.raw_material_item = item;
      this.show_pickup_status = true;
      this.show_rm_detail_status = false;
    },
    showRmDetial(item) {
      this.show_rm_detail_status = true;
      this.raw_material_item = item;
      api_raw_material.get(`/category/${item.category_id}`).then((response) => {
        this.category = response.data.name;
      });
    },
    queryCategory(cate) {
      api_raw_material.get(`query_category/${cate}`).then((response) => {
        this.raw_materials = response.data;
      });
    },
    selectCategory(cate) {
      this.category = cate;
    },
    serchByTyping(val) {
      var temp = [];
      if (val == "") {
        this.raw_materials = this.temp_rm;
      } else {
        this.temp_rm.forEach((element) => {
          if (element.name.indexOf(val) + 1 != 0) {
            temp.push(element);
          }
        });
        this.raw_materials = temp;
      }
    },
    pickup(pickup_val, item) {
      item.remain -= pickup_val
      item.pricerawmaterial_set.forEach(el => {
        el.unit_name = item.unit_set.unit
      })
      var id_list = [{unit: '', id:item.unit_s_id}, {unit: '', id:item.unit_m_id}, {unit: '', id:item.unit_l_id}]
      id_list.forEach(el => {
        this.units.forEach(unit => {
          if(unit.id == el.id) {
            el.unit = unit.unit
          }
        })
      })
      item.unit_s_name = id_list[0].unit
      item.unit_m_name = id_list[1].unit
      item.unit_l_name = id_list[2].unit
      var idx = this.raw_materials.indexOf(item)
      this.raw_materials[idx] = item
      api_raw_material
          .put(`edit-rm/${item.id}`, item)
          .then((response) => {
            console.log(response.data)
          });
      this.show_pickup_status = false;
    },
    hideShowPickup() {
      this.show_pickup_status = false;
    },
    editRM(item) {
      this.$router.push({ name: "EditRM", params: { id: item.id } });
    },
  },
  watch: {
    select_category(category) {
      if (category == "all") {
        this.temp_rm = this.raw_materials;
      } else {
        this.temp_rm = this.raw_materials.filter((m) => {
          return m.category_id == category;
        });
      }
    },
  },
};
</script>

<style scoped>
.card {
  width: 625px;
  height: 756px;
  top: 7%;
  left: 7%;
}
.unit-select-input {
  width: 150px;
  height: 40px;
  background-color: #2f414e;
  background-image: url("../../assets/icon/down-arrow.png");
  background-position: center right;
  background-size: 24px;
  background-repeat: no-repeat;
}
.select-input {
  width: 200px;
  height: 35px;
  background-color: #2f414e;
  color: white;
  margin: 17px -10px 0px 5px;
  background-image: url("../../assets/icon/down-arrow.png");
  background-position: center right;
  background-size: 24px;
  background-repeat: no-repeat;
}
input::-webkit-calendar-picker-indicator {
  opacity: 0;
}
.active {
  color: #fff;
  opacity: 1 !important;
}
.edit-block {
  position: absolute;
  top: 250px;
  left: 30px;
  width: 74px;
  height: 28.23px;
  background-color: #c4c4c4;
  border-radius: 5px;
}
.raw-image {
  position: fixed;
  border-radius: 30px;
}
.last-input-in-add {
  background-color: #717171;
  width: 217px;
  height: 37px;
  margin: 20px 0px 0px 20px;
}
.input-in-third-section {
  width: 150px;
  height: 37px;
  background-color: #717171;
  margin-right: -70px;
  margin-top: 0px;
}
.input-in-add {
  width: 150px;
  height: 40px;
  background-color: #717171;
}
#qty[data-v-8556b7f6] {
  width: 150px;
  height: 40px;
}
.input-in-add-sp {
  width: 300px;
  height: 40px;
  background-color: #717171;
  margin-right: -70px;
}
#qty {
  width: 130px;
  height: 40px;
}
.third-form-wrap {
  width: 597px;
  height: 215px;
  margin: 12px 0px 0px 15px;
  color: white;
  border-radius: 20px;
  background-color: #252836;
}
.second-form-wrap {
  width: 597px;
  height: 157px;
  margin: 265px 0px 0px 15px;
  color: white;
  border-radius: 20px;
  background-color: #252836;
}
input:checked + label {
  background-color: green;
}
input:checked + .switch-label:after {
  left: calc(100% - 5px);
  transform: translateX(-100%);
}
.switch-label {
  display: block;
  width: 64px;
  height: 30px;
  background-color: #477a85;
  border-radius: 100px;
  position: relative;
  cursor: pointer;
  transition: 0.5s;
  box-shadow: 0 0 20px #477a8550;
}
.switch-label::after {
  content: "";
  width: 30px;
  height: 30px;
  background-color: #e8f5f7;
  position: absolute;
  border-radius: 70px;
  top: 0px;
  left: 5px;
  transition: 0.5s;
}
input[type="checkbox"] {
  width: 0;
  height: 0;
  visibility: hidden;
}
.status-show {
  width: 110px;
  height: 33px;
  font-weight: 600;
  font-size: 20px;
  margin: 0px -60px 0px 70px;
  background-color: #ffb572;
  border-radius: 3px;
}
.category-select-for-add {
  font-size: 30px;
  line-height: 56px;
  color: white;
  margin: 4px 0px 0px 6px;
  height: 57px;
  text-align: left;
}
.input-for-add {
  background-color: #c4c4c4;
  color: black;
  width: 340px;
  height: 46px;
  margin: 24px 0px 0px 0px;
}
.first-form-wrap {
  position: absolute;
  width: 60%;
  height: 255px;
  border-radius: 20px;
  margin: 0px 0px 0px 37px;
  background-color: #252836;
}
.txt-for-add {
  font-weight: bold;
  font-size: 36px;
  line-height: 56px;
  text-align: center;
  width: 100%;
  color: white;
}
.image-for-add {
  position: absolute;
  width: 167px;
  height: 196px;
  margin: 42px 0px 0px 34px;
  border-radius: 20px;
  background-image: url("../../assets/img/warehouse.jpeg");
  background-repeat: no-repeat;
  background-size: contain;
}
.popup-add-rm {
  width: 625px;
  height: 756px;
  top: 7%;
  left: 7%;
  position: absolute;
  background-color: #303344;
  border: 2px solid #ea7c69;
  border-radius: 20px;
}
.btn-ghost {
  border-color: #65b0f6;
  color: #65b0f6;
  width: 119px;
  height: 50px;
}

.wrap-search {
  min-width: 560px;
  width: fit-content;
  padding: 0px;
  margin-left: 45px;
}

.search-bar {
  background-size: contain;
  background-repeat: no-repeat;
  background-color: #3a3d49;
  text-indent: 65px;
  padding-left: 10px;
  margin-left: 3px;
  border-radius: 20px;
  width: 90%;
  height: 45px;
  background-image: url("../../assets/icon/Search-19x18-1.png");
  background-repeat: no-repeat;
  background-position: 2% 50%;
  /* Extra Styling */
}
::placeholder {
  font-size: 130px !important;
}
</style>