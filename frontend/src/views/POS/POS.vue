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
                class="btn m-2 fs-1"
                :style="{ 'background-color': category.color }"
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
              :sale_channel_id="order.sale_channel.id"
              @select_product="selectProduct"
              @add_to_cart="addProduct"
            />
          </div>
        </div>

        <panel-bottom
          class="panel-bottom"
          :table="order.table"
          :delivery="order.sale_channel"
          :customer="order.customer"
        />
      </div>

      <!-- bill -->
      <div class="col-5">
        <div style="height: 65vh; overflow-y: auto">
          <bill :order="order" />
        </div>

        <div class="row" style="top: 500px">
          <table class="table table-dark table-striped">
            <thead>
              <tr>
                <th scope="col">Customer : {{ order.customer.first_name }}</th>
                <th scope="col" v-if="order.table != ''">
                  Table : {{ order.table }}
                </th>
                <th scope="col" v-else>
                  Channel : {{ order.sale_channel.sale_channel }}
                </th>
                <th scope="col"></th>
                <th scope="col">Total Price : {{ order.total_price }}</th>
              </tr>
            </thead>
          </table>
        </div>
        <div class="row">
          <div class="btn-group fs-4" style="width: 100%; height: 70px">
            <button
              class="btn btn-danger"
              :class="{ disabled: order.cart.length == 0 }"
            >
              <h5>Cancel Order</h5>
            </button>
            <button
              class="btn btn-success"
              :class="{ disabled: order.cart.length == 0 }"
              @click="confirm_order()"
            >
              <h5>Confirm Order</h5>
            </button>
          </div>
        </div>
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
    <select-table @select_table="select_table" :table="order.table" />
    <select-sale-channel
      @select_channel="select_channel"
      @select_table="select_table"
      :selected_channel="order.sale_channel"
      :sale_channels="sale_channels"
      :table="order.table"
    />
    <customer-form @save_customer="save_customer" />
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
import SelectSaleChannel from "../../components/pos/SelectSaleChannel.vue";
import CustomerForm from "../../components/pos/CustomerForm.vue";
import {apiPOS} from "../../api/apiPOS";

const Swal = require("sweetalert2");
export default {
  components: {
    NavbarPOS,
    Bill,
    CardProduct,
    SelectTopping,
    PanelBottom,
    SelectTable,
    SelectSaleChannel,
    CustomerForm,
  },
  name: "POS",
  data() {
    return {
      products: [],
      show_category: true,
      categories: [],
      sale_channels: [],
      select_category_id: null,
      select_sale_channel: {},
      topping_for_product: [],
      order: {
        cart: [],
        customer: {},
        sale_channel: "",
        payment: null,
        status_delivery: null,
        total_amount: null,
        total_price: 0,
        descriptions: "",
        table: "",
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
      this.calculate_price_product();
      this.topping_for_product = clone.type_topping.tabletopping_set;
    },
    addProduct(ProductDetail) {
      this.select_product.product = ProductDetail;
      this.calculate_price_product();
      this.order.cart.push(JSON.parse(JSON.stringify(this.select_product)));
      this.calculate_total_price_amount();
      this.clear_form;
    },
    delete_topping(index) {
      this.select_product.topping.splice(index, 1);
      this.calculate_price_product();
    },
    add_topping(topping) {
      this.select_product.topping.push(JSON.parse(JSON.stringify(topping)));
      this.calculate_price_product();
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
    getSaleChannel() {
      axios
        .get("http://127.0.0.1:8000/product/sale-channel/")
        .then((response) => {
          this.sale_channels = response.data;
        });
    },
    select_flavour_level(level) {
      this.select_product.flavour_level = level;
    },
    select_size(size) {
      this.select_product.size = size;
      this.calculate_price_product();
    },
    decrease_amount() {
      if (this.select_product.amount != 1) {
        this.select_product.amount--;
      }
      this.calculate_price_product();
    },
    increase_amount() {
      this.select_product.amount++;
      this.calculate_price_product();
    },
    add_to_cart() {
      this.order.cart.push(JSON.parse(JSON.stringify(this.select_product)));
      this.clear_form();
      this.calculate_total_price_amount();
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
    select_table(table) {
      this.order.table = table;
    },
    select_channel(channel) {
      this.order.sale_channel = channel;
    },
    calculate_price_product() {
      const s = this.select_product;

      s.total_price = parseInt(
        s.product.price.find(
          (item) => item.sale_channel_id === this.order.sale_channel.id
        ).price
      );

      s.topping.forEach((topping) => {
        s.total_price =
          parseInt(s.total_price) +
          parseInt(
            topping.price_topping.find(
              (item) => item.sale_channel_id === this.order.sale_channel.id
            ).price
          );
      });
      if (s.size == "L") {
        s.total_price = s.total_price + parseInt(10);
      }
      s.total_price *= s.amount;
    },
    calculate_total_price_amount() {
      const r = this.order;
      r.total_price = 0;
      r.total_amount = 0;
      r.cart.forEach((item) => {
        r.total_price = r.total_price + parseInt(item.total_price);
        r.total_amount = parseInt(r.total_amount) + parseInt(item.amount);
      });
    },
    save_customer(customer) {
      this.order.customer = customer;
    },
    confirm_order() {
      if (this.order.customer.first_name != undefined) {
        if (this.order.payment != "") {
          // const c = this.order.customer 
          // const data = new FormData();
          // const d = (key, value) => {
          //   data.append(key, value);
          // };
          // d('first_name',c.first_name)
          // d('last_name',c.last_name)
          // d('phone_number',c.phone_number)
          // d('gender',c.gender)
          // d('address',c.address)
          // d('alley',c.alley)
          // d('house_number',c.house_number)
          // d('img',c.img,c.img.name)
          // d('folder',c.first_name+' '+c.last_name)
          // apiPOS.post("/customer/", data).then((response_customer)=>{
          // const data = new FormData();
          // const order = this.order;
          // data.append("status_delivery", order.status_delivery);
          // data.append("total_price", order.total_price);
          // data.append("total_amount", order.total_amount);
          // data.append("payment", this.payment.id);
          // data.append("sale_channel", order.sale_channel.id);
          // data.append("customer",response_customer.data.id);
          apiPOS.post("all-order/",this.order).then(()=>{
          console.log('ok')
            // for(const product in order.cart){
            //   apiPOS.post('order-item/',{
            //     product_id:product.product.id,
            //     flavour_level:product.flavour_level,
            //     order_id:response_order.data.id,
            //     total_price:product.total_price,
            //     amount:product.amount,
            //     size:product.size,
            //     descriptions:product.descriptions
            //   }).then((response_product)=>{
            //     for(const topping in product){
            //       apiPOS.post('order-item-topping/')
            //     }
            //   })
            // }
          // })
          })
          
        } else {
          Swal.fire({
            title: "Error!",
            text: "Please select payment",
            icon: "error",
            confirmButtonText: "Cool",
          });
        }
      } else {
        Swal.fire({
          title: "Error!",
          text: "Customer detail don`t have data",
          icon: "error",
          confirmButtonText: "Cool",
        });
      }
    },
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
    this.getSaleChannel();
  },
};
</script>

<style scoped>
#price {
  white-space: nowrap;
}
.panel-bottom {
  bottom: 1.2vh;
  left: 7vw;
  position: fixed;
  width: 35vw;
}

.cart-area {
  height: 75vh;
  overflow: auto;
  overflow-x: hidden;
}
</style>
