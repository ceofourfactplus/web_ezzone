<template>
  <div>
    <nav-app @back="back">Product Category</nav-app>
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
            v-for="(item, idx) in products_categories"
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
            <div class="col-2" style="margin-left: -5px">100</div>
            <div class="col-2" style="margin-left: 40px">1000</div>
            <div class="col-1" style="position: absolute; right: 50px;">
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

    <!-- Popup -->
    <div class="category-popup" v-if="add_category_status">
        <img @click="add_category_status = false" style="position: absolute; right: 10px; top: 10px;" src="../../assets/icon/delete.png">
      <h2>Create Category</h2>
      <label for="category" style="color: white">Name : &nbsp;</label>
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
    this.fetchProductCategories()
  },
  data() {
    return {
      is_staff: false,
      alert: false,
      add_category_status: false,
      category: "",
      products_categories: [],
      temp_categories: [],
    };
  },
  methods: {
    fetchProductCategories() {
        api_product.get('/category/').then((response) => {
            console.log(response.data)
            this.products_categories = response.data
            this.temp_categories = response.data
        })
    },
    save() {
      this.alert = true;
      var data = {
        category: this.category,
        type_category: 2,
        create_by: 2,
      };
      api_product.post("/category/", data).then((response) => {
        console.log(response.data, "response category");
        setTimeout(() => {
          this.alert = false;
          this.add_category_status = false;
          this.products_categories.push(response.data);
        }, 2000);
      });
      this.category = ''
    },
    search_by_typing(val) {
          console.log(val, 'val')
          var temp = []
          if (val == '') {
              this.products_categories = this.temp_categories
          } else {
              this.temp_categories.forEach(element => {
                if(element.category.indexOf(val) + 1 != 0) {
                    temp.push(element)
                }
            });
            this.products_categories = temp
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