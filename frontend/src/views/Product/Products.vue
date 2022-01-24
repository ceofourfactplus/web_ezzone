<template>
  <div>
    <nav-app :url_name="'DashBoard'" :product_menu="true">Products</nav-app>
    <div class="row" style="margin: auto; width: 94%" v-if="is_staff">
      <div class="col-10 w-100">
        <SearchBar @search="search_by_typing" />
      </div>
      <div class="col-2 w-100" style="padding-left: 0px">
        <button
          style="width: 100%;white-space: nowrap;"
          class="btn-ghost"
          @click="$router.push({ name: 'CreateProduct' })"
        >
          + New
        </button>
      </div>
    </div>

    <div
      class="mt-2"
      style="margin: auto; width: 90%; display: flex; overflow: auto"
    >
      <button
        v-for="category in products_categories"
        :key="category.id"
        class="btn-gray p-0 me-2"
        style="
          min-width: 150px;
          height: 50px;
          opacity: 0.5;
          white-space: nowrap;
        "
        @click="select_category_f(category.id)"
        :class="{ 'type-active': select_category == category.id }"
      >
        {{ category.category }}
      </button>
    </div>

    <div class="table mt-1">
      <div class="table-header" style="line-height: 100%; font-size: 24px">
        <div class="row">
          <div class="col-2 w-100" style="margin: auto">Code</div>
          <div class="col-4 w-100" style="text-align: center">Name</div>
          <div class="col-2 w-100" style="margin: auto">Qty</div>
          <div class="col-2 w-100" style="margin: auto">Price</div>
          <div class="col-2 w-100"></div>
        </div>
      </div>

      <div style="overflow-x: auto; height: 685px">
        <div
          v-for="product in show_products"
          :key="product.id"
          class="table-item"
        >
          <div
            class="row"
            style="width: 100%; line-height: 100%; padding: 3px; height: 100%"
          >
            <div class="col-2 w-100" style="margin: auto">
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
            <div
              class="col-4 w-100"
              style="margin: auto; text-align: left"
              @click="
                $router.push({
                  name: 'EditProduct',
                  params: { id: product.id },
                })
              "
            >
              {{ product.name }}
            </div>
            <div class="col-2 w-100" style="margin: auto; text-align: center">
              {{ product.remain }}
            </div>
            <div
              class="col-2 w-100"
              style="margin: auto; width: 175px; text-align: right"
            >
              {{ get_price(product.priceproduct_set) }}
            </div>
            <div
              class="col-2 w-100"
              style="margin: auto; text-align: center; padding: 0px"
            >
              <button
                v-if="product.warehouse != 0"
                class="btn-ghost-b"
                style="font-size: 20px; line-height: 29px; height: 35px"
              >
                + Qty
              </button>
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
      select_category: null,
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
        this.products_categories = response.data;
      });
    },
    select_category_f(category_id) {
      this.select_category = category_id;
      api_product.get("product/category/" + category_id).then((response) => {
        this.products = response.data;
        this.show_products = response.data;
      });
    },
    get_price(price_list) {
      const price = price_list.filter((item) => {
        return item.sale_channel === this.$store.state.ezzone_id;
      })[0];
      if (price != undefined) {
        return price.price;
      }
      return "free";
    },
    search_by_typing(val) {
      var temp = [];
      if (val == "") {
        this.show_products = this.products;
      } else {
        this.products.forEach((element) => {
          if (element.name.toLowerCase().indexOf(val.toLowerCase()) + 1 != 0) {
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
.type-active {
  opacity: 1 !important;
  color: #fff !important;
}
</style>