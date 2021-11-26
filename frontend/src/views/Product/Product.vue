<template>
  <div id="list-product">
    <table-product :all_product="all_product" @reload="reloadProduct()" @select_product="selectProduct"/>
    <product-create @reload="reloadProduct()" />
    <price-detail :all_price="select_product.price"/>
    <product-update  :select_product="select_product" @save="reloadProduct()"/>
  </div>
</template>

<script>
import axios from "axios";
import ProductCreate from "../../components/products/product/Create";
import TableProduct from '../../components/products/product/Table.vue'
import ProductUpdate from '../../components/products/product/Update.vue';
import PriceDetail from '../../components/products/product/PriceDetail.vue';
export default {
  components: { ProductCreate, TableProduct, ProductUpdate, PriceDetail },
  name: "product",
  data() {
    return {
      all_product: [],
      load: false,
      select_product: {},
    };
  },
  mounted() {
    this.reloadProduct();
  },
  methods: {
    reloadProduct() {
      axios.get("http://127.0.0.1:8000/product/product/").then((response) => {
        this.all_product = response.data;
      });
    },
    DeleteProduct(id) {
      axios.delete("http://127.0.0.1:8000/product/product/"+id+ "/").then(()=>{this.reloadCategories()})
    },
    selectProduct(product){
      this.select_product = product;
    }
  },
};
</script>

<style>
.scroll {
  scroll-behavior: smooth;
}
.center {
  margin-left: auto;
  margin-right: auto;
  display: block;
}
</style>