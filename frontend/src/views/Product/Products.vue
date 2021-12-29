<template>
  <div>
    <nav-app>Products</nav-app>
    <div class="row" style="margin: auto; width: 94%" v-if="is_staff">
      <div class="col-10 w-100">
        <SearchBar @search="search_by_typing" />
      </div>
      <div class="col-2 w-100" style="padding-left: 0px">
        <button
          style="width: 100px"
          class="btn-ghost"
          @click="$router.push({ name: 'CreateProduct' })"
        >
          + New
        </button>
      </div>
    </div>

    <div style="margin-left: 0px">
      <Tabs
        :elements="products_categories"
        :status="'category'"
        @select_item="select_category"
      />
    </div>

    <div class="table mt-1">
      <div class="table-header" style="line-height: 40px; font-size: 30px">
        <div class="row">
          <div class="col-2 w-100" style="margin: auto">Code</div>
          <div class="col-4 w-100" style="text-align: center">Name</div>
          <div class="col-2 w-100" style="margin: auto; margin-left: -10px">
            Qty
          </div>
          <div class="col-2 w-100" style="margin: auto">Price</div>
          <div class="col-2 w-100"></div>
        </div>
      </div>

      <div style="overflow-x: auto; height: 650px">
        <div v-for="product in show_products" :key="product.id" class="table-item">
          <div class="row" style="width: 100%">
            <div
              class="col-2 w-100"
              style="margin: auto; margin-left: 0px; text-align: left"
            >
              <!-- <span>
                <img
                  v-if="product.img != null"
                  :src="product.img"
                  class="img-user-status me-1"
                /><img
                  v-else
                  src="../../assets/icon/blank-user.png"
                  class="img-user-status me-1"
                />
              </span> -->
              {{ product.code }}
            </div>
            <div class="col-4 w-100" style="margin: auto; text-align: center" @click="$router.push({name:'EditProduct',params:{id:product.id}})">
              {{ product.name }}
            </div>
            <div class="col-2 w-100" style="margin: auto; text-align: center">
              {{ product.remain }}
            </div>
            <div
              class="col-2 w-100"
              style="margin: auto; width: 175px; text-align: left"
            >
              <!-- {{get_price(product.id)}} -->
            </div>
            <div
              class="col-2 w-100"
              style="margin: auto; text-align: center; padding: 0px"
            >
              <button class="btn-ghost-b" style="width: 100px">+ Qty</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";
import Tabs from "../../components/materials/Tabs.vue";
import Table from "../../components/main_component/Table.vue";
import { api_product } from "../../api/api_product";

export default {
  components: {
    SearchBar,
    NavApp,
    Tabs,
    Table,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
    this.fetchProducts();
    this.fetchProductCategories();
  },
  data() {
    return {
      is_staff: false,
      products_categories: [],
      products: [],
      show_products: [],
    };
  },
  methods: {
    fetchProducts() {
      api_product.get("product/").then((response) => {
        this.show_products = response.data;
        this.products = response.data;
      });
    },
    fetchProductCategories() {
      api_product.get("/category/").then((response) => {
        console.log(response.data);
        this.products_categories = response.data;
      });
    },
    select_category(category_id) {
      api_product.get("product/category/" + category_id).then((response) => {
        this.products = response.data;
        this.show_products = response.data;
      });
    },
    get_price() {},
    search_by_typing(val) {
      var temp = [];
      if (val == "") {
        this.show_products = this.products;
      } else {
        this.products.forEach((element) => {
          if (element.name.indexOf(val) + 1 != 0) {
            temp.push(element);
          }
        });
        this.show_products = temp;
      }
    },
  },
};
</script>

<style scoped>
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
.row {
  width: 100%;
  margin: 0px;
}
</style>