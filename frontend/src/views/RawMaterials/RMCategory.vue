
<template>
  <div>
    <nav-app :url_name="'RawMaterials'" :rm_menu="true">RM Category</nav-app>
    <div class="row" v-if="is_staff">
      <div class="col-11 wrap-search">
        <SearchBar @search="search_by_typing" />
      </div>
      <div style="padding-left: 0px">
        <button class="btn-ghost" style="white-space: nowrap" @click="add_category_status = true">
          + New
        </button>
      </div>
    </div>
    <SearchBar v-else @search="search_by_typing" />
    <!-- Table -->
    <div class="table" style="margin-top: 10px">
      <div class="table-header">
        <!-- Is Staff -->
        <div v-if="is_staff" class="row" style="padding-right: 80px">
          <div class="col-6" style="margin-left: 90px">Name</div>
          <div class="col-3" style="padding-left: 10px">Product</div>
          <div class="col-3" style="padding-left: 20px">Amount</div>
        </div>
      </div>
      <div
        style="
          height: 660px;
          overflow-y: scroll;
          overflow-x: hidden;
          border-radius: 10px;
        "
      >
        <div v-if="is_staff">
          <div
            class="row table-item"
            v-for="(item, idx) in rm_categories"
            :key="idx"
            style="
              padding-right: 0px;
              margin: 10px 0px 0px 0px;
              background-color: #303344;
              border-radius: 10px;
            "
          >
            <div class="col-6" style="text-align: left; width: 100%; position: relative; bottom: 8px;">
              {{ item.name }}
            </div>
            <div class="col-2" style="margin-left: -20px; position: relative; bottom: 8px;">{{item.product}}</div>
            <div class="col-2" style="margin-left: 30px; position: relative; bottom: 8px;">{{item.amount}}</div>
            <div class="col-2 w-100" style="position: relative; bottom: 8px;">
              <img
                @click="SelectCategory(item)"
                src="../../assets/icon/edit.png"
                alt="img"
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
          style="position: absolute; right: 10px; top: 10px; width: 25px;"
          src="../../assets/icon/delete.png"
        />
        <h2>Create RM Category</h2>
        <label for="category" style="color: white">category : &nbsp;</label>
        <input
          v-model="category"
          type="text"
          name="category"
          class="for-category"
        />
        <br />
        <button class="btn-save" @click="save">
          <span class="icon-save"></span>Save
        </button>
      </div>
    </div>
    <!-- pop up edit -->
    <div class="blur" v-if="edit_category">
      <div class="category-popup" v-if="edit_category">
        <img
          @click="edit_category = false"
          style="position: absolute; right: 10px; top: 10px; width: 25px;"
          src="../../assets/icon/delete.png"
        />
        <h2>Edit RM Category</h2>
        <label for="category" style="color: white">category : &nbsp;</label>
        <input
          v-model="select.name"
          type="text"
          name="category"
          class="for-category"
        />
        <br />
        <button class="btn-save" @click="edit()">
          <span class="icon-save"></span>Save
        </button>
      </div>
    </div>
    <!-- Card Popup -->
    <SavePopup :alert="alert" />

    <!-- Input Datalist -->
    <!-- <label class="category-select-for-add">Category : </label>
    <input
      list="categories"
      type="text"
      v-model="raw_material_item.category"
      class="select-input"
    />
    <datalist id="categories">
      <option v-for="(cate, idx) in categories" :key="idx">
        {{ cate }}
      </option>
    </datalist>

    .select-input { width: 200px; height: 35px; background-color: #2f414e;
    color: white; margin: 17px -10px 0px 5px; background-image:
    url("../../assets/icon/down-arrow.png"); background-position: center right;
    background-size: 24px; background-repeat: no-repeat; } -->
  </div>
</template>

<script>
import SavePopup from "../../components/main_component/SavePopup.vue"
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";
import { api_raw_material } from "../../api/api_raw_material";

export default {
  components: {
    SearchBar,
    NavApp,
    SavePopup,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
    this.fetchRMCategories();
  },
  data() {
    return {
      is_staff: false,
      alert: false,
      add_category_status: false,
      category: "",
      rm_categories: [],
      temp_categories: [],
      edit_category: false,
      select:{},
    };
  },
  methods: {
    fetchRMCategories() {
      api_raw_material.get("/category/").then((response) => {
        this.rm_categories = response.data;
        this.temp_categories = response.data;
      });
    },
    save() {
      this.alert = true;
      var data = {
        name: this.category,
      };
      api_raw_material.post("/category/", data).then(() => {
        setTimeout(() => {
          this.alert = false;
          this.add_category_status = false;
          this.fetchRMCategories();
        }, 1000);
      });
      this.category = ''
    },
    search_by_typing(val) {
      var temp = [];
      if (val == "") {
        this.rm_categories = this.temp_categories;
      } else {
        this.temp_categories.forEach((element) => {
          if (element.name.toLowerCase().indexOf(val.toLowerCase()) + 1 != 0) {
            temp.push(element);
          }
        });
        this.rm_categories = temp;
      }
    },
    edit() {
      this.alert = true;
      api_raw_material
        .put("/category/" + this.select.id, this.select)
        .then(() => {
          setTimeout(() => {
            this.alert = false;
            this.edit_category = false;
            this.fetchRMCategories();
          }, 1000);
        });
    },
    SelectCategory(item) {
      this.select = item;
      this.edit_category = true;
    },
  },
};
</script>

<style scoped>
.card {
  width: 542px;
  height: 350px;
  top: 230px;
  left: 90px;
}
.btn-save {
  font-weight: bold;
  font-size: 24px;
  color: #ea7c69;
  border-color: #ea7c69;
  margin-top: 45px;
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
  margin: 40px 0px 0px 0px;
  width: 300px;
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
  top: 230px;
  left: 160px;
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
  margin: 0px 38px 0px 0px;
}
.wrap-search {
  min-width: 610px;
  width: fit-content;
  padding: 0px;
  margin-left: 45px;
}
</style>