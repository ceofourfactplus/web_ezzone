<template>
  <div>
    <nav-app :url_name="'DashBoard'" :product_menu="true">Topping</nav-app>
    <div class="row" style="margin: auto; width: 94%">
      <div class="col-10 w-100">
        <SearchBar @search="search_by_typing" />
      </div>
      <div class="col-2 w-100" style="padding-left: 0px">
        <button
          class="btn-ghost" style="
          white-space: nowrap;" 
          @click="$router.push({ name: 'CreateTopping' })"
        >
          + New
        </button>
      </div>
    </div>

    <div class="mt-2" style="margin: auto; width: 90%; display: flex">
      <button
        class="btn-gray me-2 p-0"
        style="width: 100px; height: 50px; opacity: 0.5"
        @click="select_category(2)"
        :class="{ 'type-active': select_type == 2 }"
      >
        Drink
      </button>
      <button
        class="btn-gray me-2 "
        style="width: 100px; height: 50px; opacity: 0.5"
        @click="select_category(3)"
        :class="{ 'type-active': select_type == 3 }"
      >
        Food
      </button>
      <button
        class="btn-gray p-0"
        style="width: 120px; height: 50px; opacity: 0.5"
        @click="select_category(1)"
        :class="{ 'type-active': select_type == 1 }"
      >
        Dressert
      </button>
    </div>

    <div class="table mt-2">
      <div class="table-header" style="line-height: 100%; font-size: 24px">
        <div class="row">
          <div class="col-3 w-100" style="margin: auto">Code</div>
          <div class="col-5 w-100" style="margin: auto">Name</div>
          <div class="col-2 w-100" style="margin: auto">Price</div>
          <div class="col-2 w-100" style="margin: auto">Status</div>
        </div>
      </div>

      <div style="overflow-x: auto; height: 650px">
        <div
          v-for="product in show_products"
          :key="product.id"
          class="table-item"
        >
          <div
            class="row"
            style="
              width: 100%;
              line-height: 100%;
              font-size: 24px;
              padding: 3px;
            "
          >
            <div class="col-3 w-100" style="margin: auto; margin-left: 0px">
              {{ product.code }}
            </div>
            <div
              class="col-5 w-100"
              style="margin: auto; text-align: left;"
              @click="
                $router.push({
                  name: 'EditTopping',
                  params: { id: product.id },
                })
              "
            >
              {{ product.name }}
            </div>
            <div
              class="col-2 w-100"
              style="margin: auto; width: 175px; color: #fff"
            >
              {{ get_price(product.pricetopping_set) }}
            </div>
            <div class="col-2 w-100" style="margin: auto">
              <Switch
                @switch="change_status(product)"
                :value="Boolean(Number(product.status))"
              />
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
// import Tabs from "../../components/materials/Tabs.vue";
import Table from "../../components/main_component/Table.vue";
import { api_product } from "../../api/api_product";
import Switch from "../../components/main_component/Switch.vue";

export default {
  components: {
    SearchBar,
    NavApp,
    // Tabs,
    Table,
    Switch,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
    this.fetchProducts();
  },
  data() {
    return {
      is_staff: false,
      products: [],
      show_products: [],
      select_type: 0,
    };
  },
  methods: {
    fetchProducts() {
      api_product.get("topping/").then((response) => {
        this.show_products = response.data;
        this.products = response.data;
      });
    },
    select_category(type) {
      this.select_type = type;
      api_product.get("topping-by-type/" + type).then((response) => {
        this.products = response.data;
        this.show_products = response.data;
      });
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
    get_price(price_list) {
      const price = price_list.filter((item) => {
        return item.sale_channel === this.$store.state.ezzone_id;
      })[0];
      if (price != undefined) {
        return price.price;
      }
      return "free";
    },
    change_status(product) {
      console.log(product);
      api_product
        .put("topping/status/" + product.id + "/", {
          status: !Boolean(Number(product.status)),
          update_by: this.$store.state.auth.userInfo.id,
        })
        .then((response) => {
          product.status = Boolean(Number(response.data.status));
        });
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