<template>
  <div>
    <div style="color: white; font-size: 30px; margin-top: 20px;" v-if="loading"></div>
    <div v-else>
      <nav-app :url_name="'Promotion'" :save="true" @save="edit">Package Detail</nav-app>
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
                placeholder="Promotion"
                v-model="package_item.promotion"
              />
            </div>
          </div>
          <!-- Start Date -->
          <div class="row" style="margin-top: 20px">
            <div class="col-12 w-100 txt">
              Start Date&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;
              {{ format_date_show(package_item.start_date) }}&nbsp;&nbsp;
              <input
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
                v-model="package_item.amount_day"
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
                v-model="package_item.description"
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
            <Switch :value="package_item.status" @switch="switch_active" style="top: 9px" />
          </div>
          <div class="col-12 w-100" style="margin-top: 30px">
            <!-- Image -->
            <label id="select_img" for="file" style="margin-top: 0px">
              <img :src="show_img" class="image" v-if="show_img != null" />
              <img :src="require(`../../../../backend${package_item.img}`)" class="image" v-else />
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
      <div class="table-header" style="width: 104%; margin-left: -11px;">
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
      <div class="table-item" v-for="(item, idx) in item_of_package" :key="item" style="width: 104%; margin-left: -11px;">
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
            {{ item.product_set.name }}
          </div>
          <div class="col-3 w-100" v-if="item_toppings[idx] != undefined">{{ item_toppings[idx].topping_set.name }}</div>
          <div class="col-3 w-100" v-else>-</div>
          <div class="col-1 w-100">{{ item.qty }}</div>
          <div class="col-2 w-100">{{ item.total_price }}</div>
        </div>
      </div>
      <!-- Add Menu -->
      <div class="table-item" v-if="add_menu" style="width: 104%; margin-left: -11px;">
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
              v-model="total_price"
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
      <!-- Total -->
      <div class="table-item" style="width: 104%; margin-left: -11px;">
        <div
          class="row"
          style="font-size: 24px; color: white; line-height: 14px"
        >
          <div class="col-6 w-100"></div>
          <div class="col-4 w-100" style="text-align: right">Total</div>
          <div class="col-2 w-100" v-if="item_of_package.length == 1">{{ item_of_package[0].total_price }}</div>
          <div class="col-2 w-100" v-else-if="item_of_package.length > 1">{{ item_of_package.reduce((x, y) => x.total_price + y.total_price) }}</div>
          <div class="col-2 w-100" v-else>0</div>
        </div>
      </div>
      <!-- Discount Total Price -->
      <div class="table-item" style="width: 104%; margin-left: -11px;">
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
              v-model="package_item.discount_price"
            />
          </div>
        </div>
      </div>
    </div>
    <!-- Card Popup -->
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img
          src="../../assets/icon/btn-pass.png"
          style="width: 150px; height: 150px"
        />
      </div>
      <div class="main-text">Saved successfully</div>
    </div>
    </div>
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import { api_promotion } from "../../api/api_promotion";
import { api_product } from "../../api/api_product";

export default {
  name: "PackageDetail",
  components: {
    NavApp,
    Switch,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
  },
  data() {
    return {
      new_img: false,
      search_topping: false,
      search_product: false,
      is_staff: false,
      alert: false,
      add_menu: false,
      select_all: false,
      loading: false,
      item_toppings: [],
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
      package_item: {},
      item_of_package: {},
      products: [],
      products_for_topping: [],
      temp_products: [],
    };
  },
  methods: {
    fetchPackage() {
      this.loading = true
      api_promotion.get(`package/${this.$route.params.id}`).then((response) => {
        console.log(response.data, 'package');
        this.package_item = response.data;
        this.loading = false
      });
    },
    fetchPackageItem() {
        api_promotion.get(`package-item/${this.$route.params.id}`).then((response) => {
            console.log(response.data, 'item');
            this.item_of_package = response.data;
        });
    },
    fetchItemTopping() {
        api_promotion.get(`package-item-topping/${this.$route.params.id}`).then((response) => {
            console.log(response.data, 'item topping');
            this.item_toppings = response.data;
        });
    },
    fetchProducts() {
      api_product.get("product/").then((response) => {
        console.log(response.data, "response");
        this.products = response.data;
        this.temp_products = response.data;
      });
    },
    edit() {
      const data = new FormData();
      data.append("id", this.$route.params.id);
      data.append("promotion", this.package_item.promotion);
      data.append("start_date", this.package_item.start_date);
      data.append("amount_day", this.package_item.amount_day);
      data.append("discount_price", this.package_item.discount_price);
      data.append("normal_price", this.package_item.normal_price);
      data.append("description", this.package_item.description);
      data.append("total_amount", this.package_item.total_amount);
      data.append("status", this.package_item.status);
      data.append("update_by_id", this.$store.state.auth.userInfo.id);
      data.append("create_by_id", this.$store.state.auth.userInfo.id);
      if (this.new_img) {
        data.append("img", this.img, this.img.name);
      }

      api_promotion.put("package/", data).then((response) => {
        console.log(response.data, "response");
        this.item_of_package.forEach((element) => {
          const package_item = {
            id: element.id,
            product_id: element.product.id,
            qty: element.qty,
            total_price:
              parseInt(element.price) +
              parseInt(element.topping.priceproduct_set[0].price),
            description: element.description,
            package_id: response.data.id,
          };
          api_promotion.put("package-item/", package_item).then((res) => {
            console.log(res.data, "res");
            var idx = this.item_of_package.indexOf(element)
            var topping = this.item_toppings[idx]
            const item_topping = {
              id: topping.id,
              topping_id: element.topping.id,
              item_id: res.data.id,
              total_price: parseInt(element.topping.priceproduct_set[0].price),
              amount: 10,
            };
            api_promotion
              .put("package-item-topping/", item_topping)
              .then((it_res) => {
                console.log(it_res.data, "it_res");
                this.alert = true;
                setTimeout(() => {
                  this.alert = false;
                  this.$router.push({ name: "Promotion" });
                }, 2000);
              });
          });
        });
        
      });
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
      this.new_img = true
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
      console.log(this.img, "img");
    },
    format_date_show(date) {
      var temp_date = date.split("-");
      return `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
    },
    format_date(e) {
      this.package_item.start_date = e.target.value;
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
        price: this.total_price,
        description: this.description,
      };
      const package_item = {
          product_id: this.product_item.id,
          qty: this.qty,
          total_price: parseInt(this.product_item.priceproduct_set[0].price) + parseInt(this.topping_item.priceproduct_set[0].price),
          description: this.description,
          package_id: this.$route.params.id,
      };
      api_promotion.post("package-item/", package_item).then((res) => {
            console.log(res.data, "res");
            const item_topping = {
              topping_id: this.topping_item.id,
              item_id: res.data.id,
              total_price: parseInt(this.topping_item.priceproduct_set[0].price),
              amount: 10,
            };
            api_promotion
              .post("package-item-topping/", item_topping)
              .then((it_res) => {
                console.log(it_res.data, "it_res");
                this.alert = true;
                setTimeout(() => {
                  this.alert = false;
                  this.$router.push({ name: "Point" });
                }, 2000);
                this.item_of_package.push(data);
                this.add_menu = false;
                this.product_item = {};
                this.topping_item = {};
                this.qty = null;
                this.total_price = null;
              });
          });
          
      
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
        this.item_of_package.forEach((el) => {
          this.select_item(el);
        });
      } else {
        this.selected_items = [];
      }
    },
    delete_pip() {
      console.log(this.selected_items.length, "len");
      for (let index = 0; index < this.selected_items.length; index++) {
        api_promotion.put(`package-item/${this.selected_items[index].id}`).then(() => {
          var idx = this.item_of_package.indexOf(this.selected_items[index]);
          this.item_of_package.splice(idx, 1);
        })
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
  beforeMount() {
      this.fetchPackage()
      this.fetchPackageItem()
      this.fetchItemTopping()
      this.fetchProducts()
  },
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
</style>