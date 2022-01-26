<template>
  <div>
    <nav-app :url_name="'DataBaseSettings'">Payment Channel</nav-app>
    <div class="row" v-if="is_staff" style="width: 90%; margin: auto">
      <div class="col-10 w-100 ps-0">
        <SearchBar @search="search_by_typing" />
      </div>
      <div class="col-2 w-100 ps-0 pe-0">
        <button
          class="btn-ghost w-100"
          style="white-space: nowrap; height: 45px"
          @click="add_category_status = true"
        >
          + New
        </button>
      </div>
    </div>
    <SearchBar v-else @search="search_by_typing" />
    <!-- Table -->
    <div class="table" style="margin-top: 10px">
      <div class="table-header">
        <!-- Is Staff -->
        <div v-if="is_staff" class="row" style="width: 100%; margin: auto">
          <div class="col-1"></div>
          <div class="col-7 w-100">Payment</div>
          <div class="col-3 w-100">Status</div>
        </div>
      </div>
      <div
        style="
          height: 740px;
          overflow-y: scroll;
          overflow-x: hidden;
          border-radius: 10px;
        "
      >
        <div v-if="is_staff">
          <div
            class="row table-item p-0"
            v-for="(item, idx) in all_unit"
            style="margin: 10px 0px"
            :key="idx"
          >
            <div class="col-1">
              <img
                :src="item.img"
                style="
                  height: 30px;
                  width: 30px;
                  border-radius: 10px;
                  object-fit: cover;
                "
              />
            </div>
            <div
              class="col-7"
              style="text-align: center; width: 100%"
              @click="select_sup(item)"
            >
              {{ item.payment }}
            </div>
            <div class="col-3 w-100" style="margin-left: -5px">
              <button
                v-if="item.is_active"
                class="btn-g"
                style="
                  width: 90px;
                  height: 30px;
                  margin-top: 5px;
                  line-height: 25px;
                  font-weight: bold;
                  font-size: 18px;
                "
              >
                Active
              </button>
              <button
                v-else
                class="btn-r"
                style="
                  width: 90px;
                  height: 30px;
                  margin-top: 5px;
                  line-height: 25px;
                  font-weight: bold;
                  font-size: 18px;
                "
              >
                Inactive
              </button>
            </div>
            <div class="col-1 w-100" style="right: 10px">
              <img
                v-if="!item.is_used"
                @click="delete_unit(item)"
                src="../../assets/icon/r-trash.png"
                style="bottom: 3px; width: 20px; height: 25px"
              />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Popup -->
    <div class="blur" v-if="add_category_status">
      <div class="category-popup" v-if="add_category_status">
        <img
          @click="add_category_status = false"
          style="position: absolute; right: 10px; top: 10px; width: 20px"
          src="../../assets/icon/delete.png"
        />
        <h2>Create Payment Channel</h2>
        <div class="row w-100" style="margin: auto">
          <div class="col-3 w-100">
            <label id="select_img" for="file" style="margin-top: 0px">
              <img :src="show_img" class="image" v-if="show_img != null" />
              <img
                src="../../assets/icon/image_blank.png"
                v-else
                class="image"
              />
            </label>
            <input
              type="file"
              @change="onFileChange"
              style="display: none"
              id="file"
              class="raw-image"
            />
          </div>
          <div class="col-9 w-100">
            <div class="row w-100">
              <div class="col-12 w-100">
                <label for="category" style="color: white"
                  >Payment : &nbsp;</label
                >
                <input
                  v-model="payment"
                  type="text"
                  name="category"
                  class="for-category"
                />
              </div>
              <div class="col-12 w-100" style="text-align: left">
                <label for="category" style="color: white"
                  >Status : &nbsp;</label
                >
                <Switch
                  :value="create_status"
                  @switch="create_status = !create_status"
                  style="margin-top: 10px; top: 12px"
                />
              </div>
            </div>
          </div>
        </div>

        <button class="btn-save" @click="create()">
          <span class="icon-save"></span>Save
        </button>
      </div>
    </div>

    <!-- edit pop up -->
    <div class="blur" v-if="edit_supplier_status">
      <div class="category-popup">
        <img
          @click="edit_supplier_status = false"
          style="position: absolute; right: 10px; top: 10px; width: 20px"
          src="../../assets/icon/delete.png"
        />
        <h2>Edit Payment Channel</h2>
        <div class="row w-100" style="margin: auto">
          <div class="col-3 w-100">
            <label id="select_img" for="file" style="margin-top: 0px">
              <img
                :src="show_img"
                class="image"
                v-if="selected_supplier.img != null"
              />
              <img
                src="../../assets/icon/image_blank.png"
                v-else
                class="image"
              />
            </label>
            <input
              type="file"
              @change="onEditFileChange"
              style="display: none"
              id="file"
              class="raw-image"
            />
          </div>
          <div class="col-9 w-100">
            <div class="row w-100">
              <div class="col-12 w-100">
                <label for="category" style="color: white"
                  >Payment : &nbsp;</label
                >
                <input
                  v-model="selected_supplier.payment"
                  type="text"
                  name="category"
                  class="for-category"
                />
              </div>
              <div class="col-12 w-100" style="text-align: left">
                <label for="category" style="color: white"
                  >Status : &nbsp;</label
                >
                <Switch
                  :value="selected_supplier.is_active"
                  @switch="
                    selected_supplier.is_active = !selected_supplier.is_active
                  "
                  style="margin-top: 10px; top: 12px"
                />
              </div>
            </div>
          </div>
        </div>

        <button class="btn-save" @click="edit()">
          <span class="icon-save"></span>Save
        </button>
      </div>
    </div>
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
import { api_pos } from "../../api/api_pos";
import Switch from "../../components/main_component/Switch.vue";

export default {
  name: "RMUnit",
  components: {
    SearchBar,
    NavApp,
    Switch,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
    this.fetchRMUnit();
  },
  data() {
    return {
      is_staff: false,
      alert: false,
      add_category_status: false,
      payment: "",
      all_unit: [],
      temp_categories: [],
      selected_supplier: {},
      edit_supplier_status: false,
      create_img: null,
      create_status: true,
      show_img: null,
      change_img: false,
    };
  },
  methods: {
    fetchRMUnit() {
      api_pos.get("payment/").then((response) => {
        this.all_unit = response.data;
        this.temp_categories = response.data;
      });
    },
    onFileChange(e) {
      this.create_img = e.target.files[0];
      if (this.create_img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.create_img);
      }
    },
    onEditFileChange(e) {
      this.change_img = true;
      this.selected_supplier.img = e.target.files[0];
      if (this.selected_supplier.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.selected_supplier.img);
      }
    },
    create() {
      this.alert = true;
      var data = new FormData();
      data.append("img", this.create_img, this.create_img.name);
      data.append("payment", this.payment);
      data.append("is_active", this.create_status);
      api_pos.post("payment/", data).then(() => {
        setTimeout(() => {
          this.alert = false;
          this.add_category_status = false;
          this.fetchRMUnit();
          this.unit = "";
        }, 1000);
      });
    },
    search_by_typing(val) {
      var temp = [];
      if (val == "") {
        this.all_unit = this.temp_categories;
      } else {
        this.temp_categories.forEach((element) => {
          if (element.unit.toLowerCase().indexOf(val.toLowerCase()) + 1 != 0) {
            temp.push(element);
          }
        });
        this.all_unit = temp;
      }
    },
    edit() {
      this.alert = true;
      var data = new FormData();
      if (this.change_img == true) {
        data.append(
          "img",
          this.selected_supplier.img,
          this.selected_supplier.name
        );
      }
      data.append("payment", this.selected_supplier.payment);
      data.append("is_active", this.selected_supplier.is_active);
      api_pos.put("payment/" + this.selected_supplier.id, data).then(() => {
        setTimeout(() => {
          this.alert = false;
          this.edit_supplier_status = false;
          this.fetchRMUnit();
          this.change_img = false;
        }, 1000);
      });
    },
    select_sup(item) {
      this.selected_supplier = item;
      this.show_img = item.img;
      this.edit_supplier_status = true;
    },
    delete_unit(item) {
      api_pos.delete("payment/" + item.id).then(() => {
        this.fetchRMUnit();
      });
    },
  },
};
</script>

<style scoped>
.card {
  width: 545px;
  height: 360px;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
.btn-save {
  font-weight: bold;
  font-size: 24px;
  color: #ea7c69;
  border-color: #ea7c69;
  margin-top: 15px;
  border-radius: 10px;
  text-align: center;
  background: transparent;
  line-height: 31px;
  width: 192px;
  height: 45px;
}
span.icon-save {
  background: url("../../assets/icon/save.png") no-repeat transparent;
  background-size: 30px;
  float: left;
  margin-left: 37px;
  width: 30px;
  height: 30px;
}
.for-category {
  margin: 25px 0px 0px 0px;
  width: 190px;
  height: 50px;
}
h2 {
  width: 100%;
  height: 39px;
  margin-top: 20px;
  margin: auto;
  top: 10px;
  color: #ea7c69;
}
.category-popup {
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  font-weight: bold;
  font-size: 30px;
  width: 520px;
  height: 250px;
  background: #252836;
  border: 2px solid #ea7c69;
  box-sizing: border-box;
  border-radius: 10px;
}
.btn-ghost {
  border-color: #65b0f6;
  color: #65b0f6;
  width: 119px;
  height: 50px;
  margin: 0px 40px 0px 0px;
}
#select_img {
  width: 85px;
  margin-top: 30px;
  border-radius: 15px;
  margin-right: 12px;
}
.image {
  width: 85px;
  height: 85px;
  object-fit: cover;
  margin-top: 30px;
  border-radius: 15px;
}
</style>