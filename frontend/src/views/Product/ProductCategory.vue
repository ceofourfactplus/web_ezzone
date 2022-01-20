<template>
  <div>
    <nav-app :url_name="'DashBoard'" :product_menu="true"
      >Product Category</nav-app
    >
    <div class="row" style="width: 90%; margin: auto">
      <div class="col-10 w-100" style="padding-left:0px;">
        <SearchBar @search="search_by_typing" />
      </div>
      <div class="col-2 w-100" style="padding-left: 0px">
        <button class="btn-ghost" style="
          white-space: nowrap;" @click="add_category_status = true">
          + New
        </button>
      </div>
    </div>
    <!-- Table -->
    <div class="table" style="margin-top: 10px">
      <div class="table-header">
        <!-- Is Staff -->
        <div class="row w-100">
          <div class="col-6 w-100" style="margin: auto">Name</div>
          <div class="col-2 w-100" style="margin: auto">Type</div>
          <div class="col-3 w-100" style="margin: auto">Product</div>
          <div class="col-1 w-100" style="margin: auto"></div>
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
        <div
          class="row table-item"
          v-for="(item, idx) in products_categories"
          :key="idx"
          style="
            padding-right: 0px;
            margin: 10px 0px 0px 0px;
            background-color: #303344;
            border-radius: 10px;
            line-height: 100%;
          "
        >
          <div class="col-6" style="text-align: left; width: 100%;padding-left:80px;">
            {{ item.category }}
          </div>
          <div class="col-2" style="margin-left: -5px">
            {{ get_type_category(item.type_category) }}
          </div>
          <div class="col-2" style="margin-left: 40px">
            {{ item.product_set.length }}
          </div>
          <div class="col-1" style="right: 50px">
            <img
              style="width: 20px"
              @click="edit(item)"
              src="../../assets/icon/edit.png"
              alt="img"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Popup create category -->
    <div class="blur" v-if="add_category_status">
      <div class="category-popup">
        <img
          @click="add_category_status = false"
          style="position: absolute; right: 10px; top: 10px; height: 30px"
          src="../../assets/icon/delete.png"
        />
        <div class="h1 mt-2" style="color: #ea7c69">Create Categories</div>
        <div class="mb-1">
          <label for="category" style="color: white">Name : &nbsp;</label>
          <input
            v-model="category"
            type="text"
            name="category"
            class="for-category"
          />
        </div>

        <div class="mb-1">
          <label for="category" style="color: white"
            >Type Category : &nbsp;</label
          >
          <select
            v-model="type_c"
            type="text"
            name="category"
            style="margin-top: 10px; width: 180px"
            class="for-category"
          >
            <option value="1">DESSERT</option>
            <option value="2">DRINK</option>
            <option value="3">FOOD</option>
          </select>
        </div>
        <button style="margin-top: 30px" class="btn-save" @click="save">
          <span class="icon-save"></span>Save
        </button>
      </div>
    </div>

    <!-- popup edit category -->
    <div class="blur" v-if="edit_category_status">
      <div class="category-popup">
        <img
          @click="edit_category_status = false"
          style="position: absolute; right: 10px; top: 10px;width:30px;"
          src="../../assets/icon/delete.png"
        />
        <div class="h1 mt-2" style="color: #ea7c69">Edit Categories</div>
        <div class="mb-1">
          <label for="category" style="color: white">Name : &nbsp;</label>
          <input
            v-model="edit_category.category"
            type="text"
            name="category"
            class="for-category"
          />
        </div>

        <div class="mb-1">
          <label for="category" style="color: white"
            >Type Category : &nbsp;</label
          >
          <select
            v-model="edit_category.type_category"
            type="text"
            name="category"
            style="margin-top: 10px; width: 180px"
            class="for-category"
          >
            <option value="1">DESSERT</option>
            <option value="2">DRINK</option>
            <option value="3">FOOD</option>
          </select>
        </div>

        <button class="btn-save" style="margin-top: 30px" @click="edit_submit">
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
// import Table from "../../components/main_component/Table.vue";
import { api_product } from "../../api/api_product";

export default {
  components: {
    SearchBar,
    NavApp,
    // Table,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
    this.fetchProductCategories();
  },
  data() {
    return {
      is_staff: false,
      alert: false,
      add_category_status: false,
      edit_category_status: false,
      category: "",
      type_c: "",
      edit_category: "",
      products_categories: [],
      temp_categories: [],
    };
  },
  methods: {
    fetchProductCategories() {
      api_product.get("/category/").then((response) => {
        this.products_categories = response.data;
        this.temp_categories = response.data;
      });
    },
    save() {
      this.alert = true;
      var data = {
        category: this.category,
        type_category: this.type_c,
        create_by: 1,
      };
      api_product.post("category/", data).then(() => {
        setTimeout(() => {
          "unit_set", (this.alert = false);
          this.edit_category_status = false;
        }, 1000);
        this.fetchProductCategories();
      });
      this.category = "";
    },
    edit_submit() {
      this.alert = true;
      var data = {
        category: this.edit_category.category,
        type_category: this.edit_category.type_category,
        create_by: 1,
      };
      api_product.put("category/" + this.edit_category.id, data).then(() => {
        setTimeout(() => {
          "unit_set", (this.alert = false);
          this.edit_category_status = false;
        }, 1000);
        this.fetchProductCategories();
      });
      this.category = "";
    },
    search_by_typing(val) {
      var temp = [];
      if (val == "") {
        this.products_categories = this.temp_categories;
      } else {
        this.temp_categories.forEach((element) => {
          if (element.category.toLowerCase().indexOf(val.toLowerCase()) + 1 != 0) {
            temp.push(element);
          }
        });
        this.products_categories = temp;
      }
    },
    get_type_category(type) {
      if (type == 1) {
        return "DESSERT";
      }
      if (type == 2) {
        return "DRINK";
      }
      if (type == 3) {
        return "FOOD";
      }
    },
    get_product(category_id) {
      var amount = 0;
      api_product
        .get("category/get-amount-product/" + category_id)
        .then((reponse) => {
          amount = reponse.data.amount;
        });
      return amount;
    },
    edit(item) {
      this.edit_category = item;
      this.edit_category_status = true;
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
  left: 90px;
  font-weight: bold;
  font-size: 30px;
  width: 520px;
  height: 300px;
  background: #252836;
  border: 2px solid #ea7c69;
  box-sizing: border-box;
  border-radius: 10px;
}
.btn-ghost {
  border-color: #65b0f6;
  color: #65b0f6;
  width: 119px;
  height: 45px;
  margin: 0px 30px 0px 0px;
}
.wrap-search {
  min-width: 520px;
  width: fit-content;
  padding: 0px;
  margin-left: 45px;
}
</style>