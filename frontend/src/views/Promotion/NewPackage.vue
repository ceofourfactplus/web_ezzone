<template>
  <div>
    <nav-app :url_name="'Promotion'" :save="true" @save="save"
      >New Package</nav-app
    >
    <div class="card-content">
      <div class="row">
        <!-- Left Side -->
        <div class="col-8 w-100">
          <!-- Input -->
          <div class="row">
            <div class="col-12 w-100">
              <input
                type="text"
                class="input-top"
                placeholder="Package"
                v-model="promotion"
              />
            </div>
          </div>
          <!-- Start Date -->
          <div class="row" style="margin-top: 20px">
            <div class="col-12 w-100 txt">
              <div style="display: inline" v-if="temp_start == null">
                <span style="margin-left: -140px">Start Date</span
                >&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;{{ temp_start }}&nbsp;&nbsp;
              </div>
              <div style="display: inline" v-else>
                <span style="margin-left: 23px">Start Date</span
                >&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;{{ temp_start }}&nbsp;&nbsp;
              </div>
              <input
                style="display: inline"
                type="date"
                class="input-date"
                @change="format_date($event)"
              />
            </div>
          </div>
          <!-- Amount Day -->
          <div class="row" style="margin-top: 20px">
            <div class="col-12 w-100 txt" style="margin-left: 8px">
              Amount Day&nbsp;:&nbsp;<input
                type="text"
                class="input-promotion"
                style="width: 204px"
                v-model="amount_day"
              />
            </div>
          </div>
          <!-- Description -->
          <div class="row" style="margin-top: 20px">
            <div class="col-12 w-100 txt" style="margin-left: 7px">
              <textarea
                style="
                  width: 428px;
                  height: 110px;
                  background: #717171;
                  borde-radius: 10px;
                  margin-left: 24px;
                "
                placeholder="Description"
                v-model="description"
              ></textarea>
            </div>
          </div>
        </div>
        <!-- Right Side -->
        <div class="col-4 w-100">
          <div
            class="col-12 w-100"
            style="color: white; margin: 15px 10px 0px 0px"
          >
            Status&nbsp;:&nbsp;
            <Switch @switch="switch_active" style="top: 9px" />
          </div>
          <div class="col-12 w-100" style="margin-top: 30px">
            <!-- Image -->
            <label id="select_img" for="file" style="margin-top: 0px">
              <img :src="show_img" class="image" v-if="show_img != null" />
            </label>
            <input
              type="file"
              @change="onFileChange"
              style="display: none"
              id="file"
              class="raw-image"
            />
          </div>
        </div>
      </div>
    </div>
    <!-- Product in Package -->
    <div class="row" style="margin-top: 15px; margin-left: -40px">
      <div
        class="col-6 w-100"
        style="
          font-size: 36px;
          font-weight: bold;
          color: white;
          margin-left: 35px;
        "
      >
        Product in Package
      </div>
      <div class="col-1 w-100">
        <img
          src="../../assets/icon/save.png"
          style="position: relative; top: 5px"
          v-if="add_menu"
          @click="make_package_item"
        />
      </div>
      <div class="col-2 w-100" v-if="add_menu">
        <button
          class="btn-ghost"
          style="color: #ff7ca3; border-color: #ff7ca3"
          @click="cancel_to_create"
        >
          Cancel
        </button>
      </div>
      <div class="col-2 w-100" v-else>
        <button class="btn-ghost" @click="add_menu = true">+ New</button>
      </div>
      <div class="col-3 w-100">
        <button class="btn-save" @click="delete_pip()">
          <span class="icon-save"></span>Delete
        </button>
      </div>
    </div>
    <!-- Table -->
    <div class="table" style="margin-top: 10px">
      <div class="table-header" style="width: 104%; margin-left: -11px">
        <div
          class="row"
          style="font-size: 24px; font-weight: bold; color: white"
        >
          <div class="col-1 w-100">
            <div class="checkbox-white">
              <input
                type="checkbox"
                @input="select_all_items"
                style="margin-top: 4px; right: 0px; left: 23px; bottom: 3px"
              />
            </div>
          </div>
          <div class="col-5 w-100">Product</div>
          <div class="col-3 w-100">Topping</div>
          <div class="col-1 w-100">Qty</div>
          <div class="col-2 w-100">Price</div>
        </div>
      </div>
      <!-- Menu -->
      <div
        class="table-item"
        v-for="item in package_items"
        :key="item"
        style="width: 104%; margin-left: -11px"
      >
        <div class="row" style="font-size: 20px; color: white; line-height: 1">
          <div class="col-1 w-100">
            <div class="checkbox-orange">
              <input
                type="checkbox"
                style="margin-top: -2px; left: 23px"
                :value="item"
                v-model="selected_items"
              />
            </div>
          </div>
          <div class="col-5 w-100" style="margin-left: 10px; text-align: left">
            {{ item.product.name }}
          </div>
          <div class="col-3 w-100">{{ item.topping.name }}</div>
          <div class="col-1 w-100">{{ item.qty }}</div>
          <div class="col-2 w-100">{{ item.price }}</div>
        </div>
      </div>
      <!-- Add Menu -->
      <div
        class="table-item"
        v-if="add_menu"
        style="width: 104%; margin-left: -11px"
      >
        <div class="row" style="font-size: 20px; color: white; line-height: 1">
          <div class="col-5 w-100 mt--4">
            <input
              type="text"
              class="input-add-package w-100"
              placeholder="Menu"
              @input="searchByTyping($event, 'product')"
              v-model="product_item.name"
            />
          </div>
          <div class="col-3 w-100 mt--4">
            <input
              type="text"
              class="input-add-package w-100"
              placeholder="Topping"
              @input="searchByTyping($event, 'topping')"
              v-model="topping_item.name"
            />
          </div>
          <div class="col-2 w-100 mt--4">
            <input
              type="text"
              class="input-add-package w-100"
              placeholder="Qty"
              v-model="qty"
            />
          </div>
          <div class="col-2 w-100 mt--4">
            <input
              type="text"
              class="input-add-package w-100"
              placeholder="Price"
              :value="new_menu_price"
              readonly
            />
          </div>
          <div
            v-if="search_product"
            class="col-5 w-100"
            style="
              position: relative;
              height: 100px;
              background: white;
              padding: 0px;
            "
          >
            <div
              @click="
                product_item = { ...product };
                search_product = false;
                new_menu_price = parseInt(
                  product_item.priceproduct_set[0].price
                );
              "
              class="product-menu"
              v-for="product in products"
              :key="product"
            >
              {{ product.name }}
            </div>
          </div>
          <div v-if="search_topping" class="col-5 w-100"></div>
          <div
            v-if="search_topping"
            class="col-3 w-100"
            style="
              position: relative;
              height: 100px;
              background: white;
              padding: 0px;
            "
          >
            <div
              @click="
                topping_id = product.id;
                topping_item = { ...product };
                search_topping = false;
                new_menu_price += parseInt(
                  topping_item.priceproduct_set[0].price
                );
              "
              class="product-menu"
              v-for="product in products_for_topping"
              :key="product"
            >
              {{ product.name }}
            </div>
          </div>
        </div>
      </div>
      <!-- to create product -->
        <!-- <div class="table-item" v-if="add_menu">
          <form style="padding: 3px" @submit="add_product">
            <div class="row">
              <div class="col-5 w-100" style="margin: auto; line-height: 100%">
                <input
                  type="text"
                  class="input-product"
                  v-model="product"
                  :class="{ incorrect: create_input }"
                  required
                />
                <ul>
                  <li
                    v-for="product in products"
                    :key="product.id"
                    @click="select_product(product)"
                  >
                    <p
                      class="w-100"
                      :class="{ selected: product_item.id == product.id }"
                    >
                      {{ product.name }}
                    </p>
                  </li>
                </ul>
              </div>
              <div
                class="col-3 w-100"
                style="
                  margin: auto;
                  text-align: left;
                  line-height: 100%;
                  margin-top: 0px;
                "
              >
                <input
                  type="number"
                  class="input-product"
                  v-model="price"
                  required
                />
              </div>
              <div
                class="col-3 w-100"
                style="line-height: 130%; font-size: 24px"
              >
                <input type="submit" style="display: none" />
              </div>
              <div class="col-1" style="line-height: 145%">
                <img
                  src="../../assets/icon/incorrect.png"
                  style="width: 30px"
                  alt=""
                  @click="cancel_to_create"
                />
              </div>
            </div>
          </form>
        </div> -->
      <!-- Total -->
      <div class="table-item" style="width: 104%; margin-left: -11px">
        <div
          class="row"
          style="font-size: 24px; color: white; line-height: 14px"
        >
          <div class="col-6 w-100"></div>
          <div class="col-4 w-100" style="text-align: right">Total</div>
          <div class="col-2 w-100" v-if="package_items.length == 1">
            {{ package_items[0].price }}
          </div>
          <div class="col-2 w-100" v-else-if="package_items.length != 0">
            {{ package_items.reduce((x, y) => x.price + y.price) }}
          </div>
          <div class="col-2 w-100" v-else>0</div>
        </div>
      </div>
      <!-- Discount Total Price -->
      <div class="table-item" style="width: 104%; margin-left: -11px">
        <div
          class="row"
          style="font-size: 24px; color: white; line-height: 14px"
        >
          <div class="col-6 w-100"></div>
          <div class="col-4 w-100" style="text-align: right">
            Discount Total Price
          </div>
          <div class="col-2 w-100" style="margin: -4px 0px 0px -10px">
            <input
              type="text"
              class="input-promotion w-100"
              style="height: 90%"
              v-model="discount_price"
            />
          </div>
        </div>
      </div>
    </div>
    <!-- Card Popup -->
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import SavePopup from "../../components/main_component/SavePopup.vue"
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import { api_product } from "../../api/api_product";
import { api_promotion } from "../../api/api_promotion";

export default {
  name: "NewPackage",
  components: {
    SavePopup,
    NavApp,
    Switch,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
    this.fetchProducts();
  },
  data() {
    return {
      search_topping: false,
      search_product: false,
      is_staff: false,
      alert: false,
      add_menu: false,
      select_all: false,
      package_items: [],
      selected_items: [],
      temp_start: null,
      topping_item: {},
      // Item Topping
      topping_id: null,
      topping_price: null,
      item_id: null,
      // Package Item
      product_item: {},
      qty: null,
      total_price: null,
      package: null,
      // Promotion Package
      id: null,
      promotion: null,
      start_date: null,
      img: null,
      amount_day: null,
      discount_price: null,
      normal_price: 0,
      status: true,
      total_amount: 1,
      description: null,
      show_img: null,
      products: [],
      products_for_topping: [],
      temp_products: [],
      new_menu_price: null,
      product: '',
    };
  },
  methods: {
    fetchProducts() {
      api_product.get("product/").then((response) => {
        console.log(response.data, "response");
        this.products = response.data;
        this.temp_products = response.data;
      });
    },
    save() {
      const data = new FormData();
      data.append("promotion", this.promotion);
      data.append("start_date", this.start_date);
      data.append("img", this.img, this.img.name);
      data.append("amount_day", this.amount_day);
      data.append("discount_price", this.discount_price);
      data.append("description", this.description);
      data.append("total_amount", this.package_items.length);
      data.append("status", this.status);
      data.append("update_by_id", this.$store.state.auth.userInfo.id);
      data.append("create_by_id", this.$store.state.auth.userInfo.id);
      if (this.package_items.length == 1) {
        data.append("normal_price", this.package_items[0].price);
      } else if (this.package_items.length > 0) {
        data.append(
          "normal_price",
          this.package_items.reduce((x, y) => x.price + y.price)
        );
      } else {
        data.append("normal_price", 0);
      }

      api_promotion.post("package/", data).then((response) => {
        console.log(response.data, "response");
        this.package_items.forEach((element) => {
          const package_item = {
            product_id: element.product.id,
            qty: element.qty,
            total_price: element.price,
            description: element.description,
            package_id: response.data.id,
          };
          api_promotion.post("package-item/", package_item).then((res) => {
            console.log(res.data, "res");
            if (Object.keys(element.topping).length != 0) {
              const item_topping = {
                topping_id: element.topping.id,
                item_id: res.data.id,
                total_price: parseInt(
                  element.topping.priceproduct_set[0].price
                ),
                qty: 10,
              };
              api_promotion
                .post("package-item-topping/", item_topping)
                .then((it_res) => {
                  console.log(it_res.data, "it_res");
                  this.alert = true;
                  setTimeout(() => {
                    this.alert = false;
                    this.$router.push({ name: "Promotion" });
                  }, 2000);
                });
            }
          });
        });
      });
    },
    select_product(item) {
      this.product_item = { ...item };
      this.search_product = false;
      this.new_menu_price = parseInt(this.product_item.priceproduct_set[0].price);
      setTimeout(() => {
        this.search_product = [];
      }, 100);
    },
    searchByTyping(e, type) {
      var temp = [];
      if (e.target.value == "") {
        if (type == "product") {
          this.search_product = false;
          this.products = this.temp_products;
        }
        if (type == "topping") {
          this.search_topping = false;
          this.products_for_topping = this.temp_products;
        }
      } else {
        this.temp_products.forEach((element) => {
          if (element.name.indexOf(e.target.value) + 1 != 0) {
            temp.push(element);
          }
        });
        if (type == "product") {
          this.search_product = true;
          this.products = temp;
        }
        if (type == "topping") {
          this.search_topping = true;
          this.products_for_topping = temp;
        }
      }
    },
    onFileChange(e) {
      console.log(e, "e");
      this.img = e.target.files[0];
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
      console.log(this.img, "img");
    },
    format_date(e) {
      this.start_date = e.target.value;
      var temp_date = e.target.value.split("-");
      this.temp_start = `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
    },
    switch_active(val) {
      this.status = val;
    },
    make_package_item() {
      var data = {
        product: this.product_item,
        topping: this.topping_item,
        qty: this.qty,
        price: this.new_menu_price,
        description: this.description,
      };
      this.package_items.push(data);
      this.add_menu = false;
      this.product_item = {};
      this.topping_item = {};
      this.qty = null;
      this.total_price = null;
      this.new_menu_price = null;
    },
    select_item(item) {
      if (this.selected_items.includes(item)) {
        var idx = this.selected_items.indexOf(item);
        this.selected_items.splice(idx, 1);
      } else {
        this.selected_items.push(item);
      }
    },
    select_all_items() {
      this.select_all = !this.select_all;
      if (this.select_all) {
        this.package_items.forEach((el) => {
          this.select_item(el);
        });
      } else {
        this.selected_items = [];
      }
    },
    delete_pip() {
      console.log(this.selected_items.length, "len");
      for (let index = 0; index < this.selected_items.length; index++) {
        var idx = this.package_items.indexOf(this.selected_items[index]);
        this.package_items.splice(idx, 1);
      }
    },
    cancel_to_create() {
      this.add_menu = false;
      this.product_item = {};
      this.topping_item = {};
      this.qty = null;
      this.total_price = 0;
    },
  },
  watch: {
    product(newProduct) {
      this.create_input = false;
      if (newProduct != "") {
        if (this.type_item == 4) {
          api_product
            .get("topping-by-search/" + newProduct + "/")
            .then((response) => {
              var arr = [];
              this.search_product = response.data;
              this.search_product.forEach((item) => {
                if (this.filter_same_topping(item)) {
                  arr.push(item);
                }
              });
              this.search_product = arr;
            });
        } else {
          api_product
            .get(
              "product-by-type-and-search/" +
                this.type_item +
                "/" +
                newProduct +
                "/"
            )
            .then((response) => {
              var arr = [];
              this.search_product = response.data;
              this.search_product.forEach((item) => {
                if (this.filter_same_product(item)) {
                  arr.push(item);
                }
              });
              this.search_product = arr;
            });
        }
      } else {
        this.selected_product = {};
      }
      this.search_product = [];
    },
  }
};
</script>

<style scoped>
.product-menu {
  color: black;
  font-size: 24px;
  text-align: left;
  margin: 8px 0px 0px 5px;
}
.product-menu:hover {
  background: #717171;
}
.mt--4 {
  margin-top: -4px;
}
.input-add-package {
  height: 90%;
  line-height: 90%;
  background: #717171;
  border-radius: 12px;
  color: white;
  text-align: center;
}
.btn-ghost {
  border-color: #65b0f6;
  color: #65b0f6;
  width: 119px;
  height: 50px;
  margin: 0px 25px 0px 0px;
}
.btn-save {
  font-size: 24px;
  color: #ff7ca3;
  border-color: #ff7ca3;
  border-radius: 10px;
  text-align: center;
  background: transparent;
  line-height: 21px;
  width: 140px;
  height: 50px;
}
span.icon-save {
  background: url("../../assets/icon/bin.png") no-repeat transparent;
  background-size: 18px;
  float: left;
  margin-left: 17px;
  width: 19px;
  height: 27px;
}
#select_img {
  width: 170px;
  height: 170px;
  border-radius: 20px;
  margin-right: 12px;
  background-color: #c4c4c4;
}
.image {
  width: 170px;
  height: 170px;
  border-radius: 20px;
}
.colon {
  font-size: 30px;
  text-align: center;
  margin: 20px 0px 0px -40px;
  color: white;
}
.input-top {
  width: 215px;
  height: 50px;
  background: rgb(113, 113, 113);
  border-radius: 12px;
  color: white;
  float: left;
  margin: 10px 0px 0px 20px;
}
.input-code {
  width: 167px;
  height: 53px;
  background: #717171;
  border-radius: 10px;
  color: white;
}
#txt-right-side {
  margin-left: -40px;
}
.txt {
  font-size: 30px;
  font-weight: bold;
  color: white;
  /* text-align: left;
  margin: 20px 0px 0px 120px; */
}
.card-content {
  width: 765px;
  height: 342px;
  background: #303344;
  border-radius: 20px;
  margin: 15px 0px 0px 27px;
  font-size: 30px;
  font-weight: bold;
}
.checkbox-white input:checked::after {
  font-size: 20px;
  top: 1px;
  left: 1px;
}
.checkbox-white input::before {
  height: 30px;
  width: 30px;
}
.checkbox-white input {
  height: 28px;
  width: 28px;
}
.checkbox-orange input:checked::after {
  font-size: 20px;
  top: 4px;
  left: 4px;
}
.checkbox-orange input::before {
  height: 30px;
  width: 30px;
}
.checkbox-orange input {
  height: 28px;
  width: 28px;
}
ul {
  background-color: #ea7c69;
  margin-top: 10px;
  list-style-type: none;
  padding: 0px;
  border-radius: 10px;
  position: absolute;
  min-width: 30%;
  z-index: 1;
}
p {
  font-size: 20px;
  font-weight: 500;
  text-align: left;
  padding-left: 10px !important;
  padding: 7px;
  margin: 0px;
}
</style>