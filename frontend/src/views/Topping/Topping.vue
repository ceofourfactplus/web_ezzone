<template>
  <div>
    <nav-app>Topping</nav-app>
    <div class="row" style="margin: auto; width: 94%">
      <div class="col-10 w-100">
        <SearchBar @search="search_by_typing" />
      </div>
      <div class="col-2 w-100" style="padding-left: 0px">
        <button
          style="width: 100px"
          class="btn-ghost"
          @click="$router.push({ name: 'CreateTopping' })"
        >
          + New
        </button>
      </div>
    </div>

    <div style="margin-left: 0px">
      <Tabs
        :elements="[
          { name: 'Drink', id: 2 },
          { name: 'Food', id: 3 },
          { name: 'Dressert', id: 1 },
        ]"
        @select_item="select_category"
      />
    </div>

    <div class="table mt-1">
      <div class="table-header" style="line-height: 40px; font-size: 30px">
        <div class="row">
          <div class="col-2 w-100" style="margin: auto">Code</div>
          <div class="col-5 w-100" style="text-align: center">Name</div>
          <div class="col-2 w-100" style="margin: auto">Price</div>
          <div class="col-2 w-100" style="margin: auto; margin-left: -10px">
            status
          </div>
          <div class="col-1 w-100"></div>
        </div>
      </div>

      <div style="overflow-x: auto; height: 650px">
        <div
          v-for="product in show_products"
          :key="product.id"
          class="table-item"
        >
          <div class="row" style="width: 100%">
            <div
              class="col-2 w-100"
              style="margin: auto; margin-left: 0px; text-align: left"
            >
              {{ product.code }}
            </div>
            <div
              class="col-5 w-100"
              style="margin: auto; text-align: center"
              @click="
                $router.push({
                  name: 'EditProduct',
                  params: { id: product.id },
                })
              "
            >
              {{ product.name }}
            </div>
            <div
              class="col-2 w-100"
              style="margin: auto; width: 175px; text-align: left; color: #fff"
            >
                {{ get_price(product.pricetopping_set) }}
            </div>
            <div class="col-2 w-100" style="margin: auto; text-align: center">
              <Switch />
            </div>
            <div
              class="col-1 w-100"
              style="margin: auto; text-align: center; padding: 0px"
            >
              <img src="../../assets/icon/edit.png" alt="" />
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
import Switch from "../../components/main_component/Switch.vue";

export default {
  components: {
    SearchBar,
    NavApp,
    Tabs,
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