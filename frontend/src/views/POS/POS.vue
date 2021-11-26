<template>
  <div class="container" id="sd">
    <NavbarPOS />
    <div class="row" style="height: 20vw">
      <div class="col-7">
        <div class="row">
          <div v-for="product in products" :key="product.id" class="col-4">
            <card-product
              :product="product"
              :sale_channel_id="sale_channel.id"
              @select_product="selectProduct"
              @add_to_cart="addProduct"
            />
          </div>
        </div>
      </div>
      <div class="col-5">
        <bill :bill="order.cart" />
      </div>
    </div>
    <select-topping
      :product_select="select_product"
      @delete_topping="delete_topping"
    />
  </div>
</template>

<script>
import axios from "axios";
import Bill from "../../components/pos/Bill.vue";
import CardProduct from "../../components/pos/CardProduct.vue";
import NavbarPOS from "../../components/pos/NavPOS.vue";
import SelectTopping from "../../components/pos/SelectTopping.vue";

export default {
  components: { NavbarPOS, Bill, CardProduct, SelectTopping },
  name: "POS",
  data() {
    return {
      products: [],
      order: {
        cart: [],
        customer_name: "",
        sale_channel: null,
        payment: null,
        status_delivery: null,
        total_amount: null,
        total_price: null,
        descriptions: "",
      },
      select_product: {
        product: {},
        amount: 1,
        topping: [],
        size: "M",
        sweetness: "",
        total_price: 0,
        descriptions: "",
      },
      sale_channel: {},
    };
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/product/product-pos/").then((response) => {
      this.products = response.data;
    });
  },
  methods: {
    selectProduct(ProductDetail) {
      const clone = Object.assign({}, ProductDetail);
      this.select_product.product = clone;
    },
    addProduct(ProductDetail) {
      const clone = Object.assign({}, ProductDetail);
      this.select_product.product = clone;
      this.order.cart.push(this.select_product);
    },
    deleteTopping(index) {
      this.select_product.topping.splice(index, 1);
    },
    add_topping(topping) {
      this.select_product.topping.push(topping);
    },
  },
};
</script>

<style scoped>
#price {
  white-space: nowrap;
}
</style>
