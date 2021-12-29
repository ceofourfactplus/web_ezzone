<template>
  <div>
    <nav-app>Topping Category</nav-app>
    <div class="row" v-if="is_staff">
      <div class="col-11 wrap-search">
        <SearchBar @search="search_by_typing" />
      </div>
      <div style="padding-left: 0px">
        <button class="btn-ghost" @click="add_category_status = true">
          + New
        </button>
      </div>
    </div>
    <SearchBar v-else @search="search_by_typing" />
    <!-- Table -->
    <div class="table" style="margin-top: 10px">
      <div class="table-header">
        <!-- Is Staff -->
        <div v-if="is_staff" class="row w-100">
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
        <div v-if="is_staff">
          <div
            class="row table-item"
            v-for="(item, idx) in categories"
            :key="idx"
            style="
              padding-right: 0px;
              margin: 10px 0px 0px 0px;
              background-color: #303344;
              border-radius: 10px;
            "
          >
            <div class="col-6" style="text-align: left; width: 100%">
              {{ item.category }}
            </div>
            <div class="col-2" style="margin-left: -5px">
              topping
            </div>
            <div class="col-2" style="margin-left: 40px">
              {{ get_topping(item.id) }}
            </div>
            <div class="col-1" style="position: absolute; right: 50px">
              <img
                @click="edit(item)"
                src="../../assets/icon/edit.png"
                alt="img"
              />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Popup create category -->
    <div class="blur" v-if="add_category_status">
      <div class="category-popup">
        <img
          @click="add_category_status = false"
          style="position: absolute; right: 10px; top: 10px"
          src="../../assets/icon/delete.png"
        />
        <div class="h1 mt-2" style="color: #ea7c69">Create Categories</div>
        <div class="mb-1">
          <label for="category" style="color: white">Name : &nbsp;</label>
          <input
            v-model="category"
            @input="check_category"
            type="text"
            name="category"
            class="for-category"
          />
        </div>
        <button v-if="!status" style="margin-top:30px" class="btn-save" @click="save">
          <span class="icon-save"></span>Save
        </button>
        <button v-else style="margin-top: 30px" class="btn-save-gray">
          <span class="icon-save-gray"></span>Save
        </button>
      </div>
    </div>

    <!-- popup edit category -->
    <div class="blur" v-if="edit_category_status">
      <div class="category-popup">
        <img
          @click="edit_category_status = false"
          style="position: absolute; right: 10px; top: 10px"
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

        <button
          class="btn-save"
          :class="{ disable: status }"
          style="margin-top: 30px"
          @click="edit_submit"
        >
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
import NavApp from "../../components/main_component/NavAppHam.vue";
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
    this.fetchToppingCategories();
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
      categories: [],
      temp_categories: [],
      status: "",
    };
  },
  methods: {
    fetchToppingCategories() {
      api_product.get("topping-category/").then((response) => {
        this.categories = response.data;
        this.temp_categories = response.data;
      });
    },
    save() {
      this.alert = true;
      api_product
        .post("topping-category/", {
        category: this.category,
        create_by_id: 1,
      })
        .then((response) => {
          setTimeout(() => {
            this.alert = false;
            this.add_category_status = false;
            this.fetchToppingCategories;
          }, 2000);
        })
        .catch((error) => {
          this.err = error;
        });
      this.category = "";
    },
    edit_submit() {
      this.alert = true;
      var data = {
        category: this.edit_category.category,
        create_by: 1,
      };
      api_product
        .put("topping/category/" + this.edit_category.id, data)
        .then((response) => {
          setTimeout(() => {
            "unit_set", (this.alert = false);
            this.edit_category_status = false;
            this.fetchToppingCategories;
          }, 2000);
        });
      this.category = "";
    },
    search_by_typing(val) {
      var temp = [];
      if (val == "") {
        this.categories = this.temp_categories;
      } else {
        this.temp_categories.forEach((element) => {
          if (element.category.indexOf(val) + 1 != 0) {
            temp.push(element);
          }
        });
        this.categories = temp;
      }
    },
    get_topping(category_id) {
      api_product
        .get("category/get-amount-product/" + category_id)
        .then((reponse) => {
          return reponse.data.amount;
        });
    },
    edit(item) {
      this.edit_category = item;
      this.edit_category_status = true;
    },
    check_category() {
      if (this.category != "") {
        api_product
          .get("check-category-topping/" + this.category)
          .then((response) => {
            this.status = response.data.status;
            console.log(response.data.status);
          });
      }
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
.btn-save-gray {
  font-weight: bold;
  font-size: 24px;
  color: #889898;
  border-color: #889898;
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
span.icon-save-gray {
  background: url("../../assets/icon/save-gray.png") no-repeat transparent;
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
  top: 240px;
  left: 140px;
  font-weight: bold;
  font-size: 30px;
  width: 450px;
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