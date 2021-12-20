<template>
  <div>
    <nav-app @back="back">Products</nav-app>
    <div class="row" v-if="is_staff">
      <div class="col-11 wrap-search">
        <SearchBar @search="serch_by_typing" />
      </div>
      <div style="padding-left: 0px">
        <button class="btn-ghost" @click="$router.push({ name: 'ProductDetail'})">+ New</button>
      </div>
    </div>
    <SearchBar v-else @search="serch_by_typing" />
    <div style="margin-left: -60px;">
        <Tabs :elements="products_categories" />
    </div>
    <Table :head1="'Name'" :head2="'Qty'" :head3="'Unit'" :head4="'Status'" :elements="products" />
  </div>
</template>

<script>
import SearchBar from "../../components/materials/SearchBar.vue"
import NavApp from "../../components/main_component/NavApp.vue";
import Tabs from "../../components/materials/Tabs.vue"
import Table from "../../components/main_component/Table.vue"
import {apiProduct} from "../../api/apiProduct"

export default {
  components: {
      SearchBar,
      NavApp,
      Tabs,
      Table,
  },
  mounted() {
      this.is_staff = this.$store.state.auth.userInfo['is_staff']
      this.fetchProducts()
  },
  data() {
    return {
        is_staff: false,
        products_categories: [
            {name: 'All'},
            {name: 'Drink'},
            {name: 'Food'},
            {name: 'Dessert'},
            {name: 'Topping'},
            {name: 'Consignment'},
        ],
        products: [
        {
          name: "คอร์นเฟลคคาราเมลธัญพืช",
          qty: 5,
          unit: "pack",
          status: "1",
        },
        {
          name: "ปังป็อบ",
          qty: 2,
          unit: "pack",
          status: "2",
        },
        {
          name: "พายสับปะรด",
          qty: 20,
          unit: "piece",
          status: "1",
        },
        {
          name: "ปังกรอบ",
          qty: 10,
          unit: "pack",
          status: "3",
        },
      ],
    };
  },
  methods: {
      fetchProducts() {
          apiProduct.get('/product').then(response => {
              console.log(response.data, 'response')
          })
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
</style>