<template>
  <div>
    <nav-app @back="back">Products</nav-app>
    <div class="row" v-if="is_staff">
      <div class="col-11 wrap-search">
        <SearchBar @search="search_by_typing" />
      </div>
      <div style="padding-left: 0px">
        <button class="btn-ghost" @click="$router.push({ name: 'ProductDetail'})">+ New</button>
      </div>
    </div>
    <SearchBar v-else @search="search_by_typing" />
    <div style="margin-left: 0px;">
        <Tabs :elements="products_categories" :status="'category'" @select_item="select_item" />
    </div>
    <Table :head1="'Name'" :head2="'Qty'" :head3="'Unit'" :head4="'Status'" :elements="products" />
  </div>
</template>

<script>
import SearchBar from "../../components/materials/SearchBar.vue"
import NavApp from "../../components/main_component/NavApp.vue";
import Tabs from "../../components/materials/Tabs.vue"
import Table from "../../components/main_component/Table.vue"
import {api_product} from "../../api/api_product"

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
      this.fetchProductCategories()
  },
  data() {
    return {
        is_staff: false,
        products_categories: [],
        temp_products: [
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
          api_product.get('/product').then(response => {
              console.log(response.data, 'response')
          })
      },
      fetchProductCategories() {
          api_product.get('/category/').then((response) => {
            console.log(response.data)
            this.products_categories = response.data
        })
      },
      select_item(item) {
          console.log(item)
      },
      search_by_typing(val) {
          console.log(val, 'val')
          var temp = []
          if (val == '') {
              this.products = this.temp_products
          } else {
              this.temp_products.forEach(element => {
                if(element.name.toLowerCase().indexOf(val.toLowerCase()) + 1 != 0) {
                    temp.push(element)
                }
            });
            this.products = temp
          }
      },
  },
};
</script>

<style scoped>

</style>