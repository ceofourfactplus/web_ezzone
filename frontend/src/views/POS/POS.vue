<template>
  <div class="container" id="sd">
    <NavbarPOS
      :categories="categories"
      :select_category_id="select_category_id"
      @select_category="select_category"
      @clear_category="clear_category"
      @see_order="see_order"
    />
    <div class="row">
      <div class="col-7">
        <!-- if don`t have select category  -->
        <div class="row cart-area" v-if="show_category">
          <div class="row">
            <div
              v-for="category in categories"
              :key="category.id"
              class="col-3"
            >
              <button
                class="btn btn-light m-2 fs-1"
                @click="select_category(category.id)"
                style="width: 180px; height: 180px"
              >
                {{ category.category }}
              </button>
            </div>
          </div>
        </div>

        <!-- if has product -->
        <div class="row cart-area" v-else-if="products.length == 0">
          this category don`t have product
        </div>

        <div class="row cart-area" v-else>
          <div v-for="product in products" :key="product.id" class="col-4">
            <card-product
              :product="product"
              :sale_channel_id="select_sale_channel.id"
              @select_product="selectProduct"
              @add_to_cart="addProduct"
            />
          </div>
        </div>

        <panel-bottom class="panel-bottom" :table="order.table" :delivery="order.sale_channel" :customer="order.customer"/>
      </div>

      <!-- bill -->
      <div class="col-5">
        <bill :order="order" />
      </div>
    </div>
    <select-topping
      :product_select="select_product"
      :toppings="topping_for_product"
      :sale_channel_id="order.sale_channel.id"
      @delete_topping="delete_topping"
      @add_topping="add_topping"
      @select_size="select_size"
      @select_flavour_level="select_flavour_level"
      @increase_amount="increase_amount"
      @decrease_amount="decrease_amount"
      @add_to_cart="add_to_cart"
    />
    <select-table @select_table="select_table"/>
    <select-sale-channel />
  </div>
</template>

<script>
import axios from "axios";
import Bill from "../../components/pos/Bill.vue";
import CardProduct from "../../components/pos/CardProduct.vue";
import NavbarPOS from "../../components/pos/NavPOS.vue";
import SelectTopping from "../../components/pos/SelectTopping.vue";
import PanelBottom from "../../components/pos/PanelBottom.vue";
import SelectTable from "../../components/pos/SelectTable.vue";
import SelectSaleChannel from '../../components/pos/SelectSaleChannel.vue';

export default {
  components: {
    NavbarPOS,
    Bill,
    CardProduct,
    SelectTopping,
    PanelBottom,
    SelectTable,
    SelectSaleChannel,
  },
  name: "POS",
  data() {
    return {
      products: [],
      show_category: true,
      categories: [],
      select_category_id: null,
      select_sale_channel: {},
      topping_for_product: [],
      order: {
        cart: [],
        customer: {},
        sale_channel: {},
        payment: null,
        status_delivery: null,
        total_amount: null,
        total_price: null,
        descriptions: "",
        table:''
      },
      select_product: {
        product: {},
        amount: 1,
        topping: [],
        size: "M",
        flavour_level: "medium",
        total_price: 0,
        descriptions: "",
      },
    };
  },
  methods: {
    selectProduct(clone) {
      this.select_product.product = clone;
      this.topping_for_product = clone.type_topping.tabletopping_set;
    },
    addProduct(ProductDetail) {
      this.select_product.product = ProductDetail;
      this.order.cart.push(JSON.parse(JSON.stringify(this.select_product)));
      this.clear_form;
    },
    delete_topping(index) {
      this.select_product.topping.splice(index, 1);
    },
    add_topping(topping) {
      this.select_product.topping.push(JSON.parse(JSON.stringify(topping)));
    },
    select_category(category_id) {
      this.select_category_id = category_id;
      axios
        .get("http://127.0.0.1:8000/product/product-pos/" + category_id + "/")
        .then((response) => {
          this.products = response.data;
        });
    },
    clear_category() {
      this.products = [];
      this.select_category_id = 0;
    },
    getCategory() {
      axios.get("http://127.0.0.1:8000/product/category/").then((response) => {
        this.categories = response.data;
      });
    },
    select_flavour_level(level) {
      this.select_product.flavour_level = level;
    },
    select_size(size) {
      this.select_product.size = size;
    },
    decrease_amount() {
      if (this.select_product.amount != 1) {
        this.select_product.amount--;
      }
    },
    increase_amount() {
      this.select_product.amount++;
    },
    add_to_cart() {
      this.order.cart.push(JSON.parse(JSON.stringify(this.select_product)));
      this.clear_form();
    },
    clear_form() {
      this.select_product = {
        product: {},
        amount: 1,
        topping: [],
        size: "M",
        flavour_level: "medium",
        total_price: 0,
        descriptions: "",
      };
    },
    select_table(table){
      this.order.table = table
    }
  },
  watch: {
    select_category_id() {
      if (this.select_category_id == 0) {
        this.show_category = true;
      } else {
        this.show_category = false;
      }
    },
  },
  mounted() {
    this.getCategory();
  },
};
</script>

<style scoped>
#price {
  white-space: nowrap;
}
.panel-bottom {
  top: 0.7vh;
  /* left: 3vw; */
  position: fixd;
  width: 30vw;
}

.cart-area {
  height: 75vh;
  overflow: auto;
  overflow-x: hidden;
}
</style>
