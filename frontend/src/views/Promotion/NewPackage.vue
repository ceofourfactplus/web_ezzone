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
            <div class="col-12 w-100 txt" style="margin-left: 18px">
              Amount Day&nbsp;:&nbsp;<input
                type="text"
                class="input-promotion"
                style="width: 240px"
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
      <div class="col-1 w-100"></div>
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
        <button class="btn-ghost" style="white-space: nowrap;" @click="add_menu = true">+ New</button>
      </div>
      <div class="col-3 w-100">
        <button class="btn-save" style="white-space: nowrap;" @click="delete_pip()">
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
          <div class="col-6 w-100">Product</div>
          <div class="col-1 w-100" style="margin-left: -10px">Qty</div>
          <div class="col-3 w-100" style="margin-left: -20px">Price</div>
          <div class="col-1 w-100"></div>
        </div>
      </div>
      <!-- Menu -->
      <div v-for="(item, idx) in package_items" :key="item">
        <!-- Package Item -->
        <div
          class="table-item"
          style="width: 104%; margin-left: -11px"
          v-if="!update_status.includes(item)"
        >
          <div
            class="row"
            style="font-size: 20px; color: white; line-height: 1"
          >
            <div class="col-1 w-100">
              <div class="checkbox-orange">
                <input
                  type="checkbox"
                  style="margin-top: -2px; left: 23px"
                  :value="item"
                  @change="select_del_item(item, true)"
                />
              </div>
            </div>
            <div
              class="col-6 w-100"
              style="margin-left: 10px; text-align: left"
              @click="update_status[0] = item"
            >
              {{ item.product.name }}
            </div>
            <div class="col-1 w-100">{{ item.qty }}</div>
            <div class="col-3 w-100">{{ (parseInt(item.product.priceproduct_set[0].price) * parseInt(item.qty)).toFixed(2) }}</div>
          </div>
        </div>

        <!-- Update Item -->
        <div class="table-item" v-else style="width: 104%; margin-left: -11px">
          <form style="padding: 3px" @submit="update_status = []; calc_total_price();">
            <div class="row" style="padding-top: 0px">
              <div class="col-7 w-100" style="margin: auto; line-height: 100%">
                <input
                  type="text"
                  class="input-add-package"
                  @input="searchByTyping($event, 'product')"
                  v-model="item.product.name"
                  :class="{ incorrect: create_input }"
                  required
                />
                <ul>
                  <li
                    v-for="product in products"
                    :key="product.id"
                    @click="select_update_product(product, idx)"
                  >
                    <p class="w-100">
                      {{ product.name }}
                    </p>
                  </li>
                </ul>
              </div>
              <div
                class="col-1 w-100"
                style="
                  margin: auto;
                  text-align: left;
                  line-height: 100%;
                  margin-top: 0px;
                "
              >
                <input
                  type="number"
                  class="input-add-package"
                  v-model="item.qty"
                  required
                />
              </div>
              <div
                class="col-3 w-100"
                style="line-height: 130%; font-size: 24px"
              >
                <input
                  type="number"
                  class="input-add-package"
                  :value="parseInt(item.product.priceproduct_set[0].price) * parseInt(item.qty)"
                  required
                />
                <input type="submit" style="display: none" />
              </div>
              <div class="col-1" style="line-height: 145%">
                <img
                  src="../../assets/icon/incorrect.png"
                  style="width: 30px"
                  alt=""
                  @click="update_status = []; calc_total_price();"
                />
              </div>
            </div>
          </form>
        </div>

        <div v-for="(topping, top_idx) in item.topping" :key="topping">
          <!-- Item Topping -->
          <div
            class="table-item"
            style="width: 104%; margin-left: -11px"
            v-if="!update_status.includes(topping)"
          >
            <div
              class="row"
              style="font-size: 20px; color: white; line-height: 1"
            >
              <div class="col-1 w-100"></div>
              <div class="col-1 w-100">
                <div class="checkbox-orange">
                  <input
                    type="checkbox"
                    style="margin-top: -2px; left: 23px"
                    :value="topping"
                    @change="select_del_item(item, false)"
                  />
                </div>
              </div>
              <div
                class="col-5 w-100"
                style="margin-left: 10px; text-align: left"
                @click="update_status[0] = topping; calc_total_price();"
              >
                {{ topping.name }}
              </div>
              <div class="col-1 w-100">{{ topping.remain }}</div>
              <div class="col-3 w-100">
                {{ topping.pricetopping_set[0].price }}
              </div>
            </div>
          </div>

          <!-- Update Item Topping -->
          <div
            class="table-item"
            v-else
            style="width: 104%; margin-left: -11px"
          >
            <form
              style="padding: 3px"
              @submit="
                update_status = [];
                calc_total_price();
              "
            >
              <div class="row" style="padding-top: 0px; margin-top: -10px;">
                <div class="col-1 w-100">Topping</div>
                <div
                  class="col-6 w-100"
                  style="margin: auto; line-height: 100%"
                >
                  <input
                    type="text"
                    class="input-add-package"
                    style="margin-left: -23px"
                    @input="searchByTyping($event, 'topping')"
                    :class="{ incorrect: create_input }"
                    v-model="topping.name"
                    required
                  />
                  <ul style="min-width: 40%">
                    <li
                      v-for="top in toppings"
                      :key="top.id"
                      @click="package_items[idx].topping[top_idx] = top; package_items[idx].topping[top_idx].remain = 1; calc_total_price();"
                    >
                      <p class="w-100">
                        {{ top.name }}
                      </p>
                    </li>
                  </ul>
                </div>
                <div
                  class="col-1 w-100"
                  style="
                    margin: auto;
                    text-align: left;
                    line-height: 100%;
                    margin-top: 0px;
                  "
                >
                  <input
                    type="number"
                    class="input-add-package"
                    v-model="topping.remain"
                    required
                  />
                </div>
                <div
                  class="col-3 w-100"
                  style="line-height: 130%; font-size: 24px"
                >
                  <input
                    type="number"
                    class="input-add-package"
                    :value="topping.pricetopping_set[0].price * topping.remain"
                    required
                  />
                  <input type="submit" style="display: none" />
                </div>
                <div class="col-1" style="line-height: 145%">
                  <img
                    src="../../assets/icon/incorrect.png"
                    style="width: 30px"
                    @click="update_status = []; calc_total_price();"
                  />
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>

      <!-- to create product -->
      <div
        class="table-item"
        v-if="add_menu"
        style="width: 104%; margin-left: -11px"
      >
        <form style="padding: 3px" @submit="make_package_item">
          <div class="row" style="padding-top: 0px">
            <div class="col-7 w-100" style="margin: auto; line-height: 100%">
              <input
                type="text"
                class="input-add-package"
                @input="searchByTyping($event, 'product')"
                v-model="product_item.name"
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
              class="col-1 w-100"
              style="
                margin: auto;
                text-align: left;
                line-height: 100%;
                margin-top: 0px;
              "
            >
              <input
                type="number"
                class="input-add-package"
                v-model="qty"
                required
              />
            </div>
            <div class="col-3 w-100" style="line-height: 130%; font-size: 24px">
              <input
                v-if="Object.keys(product_item).length != 0"
                type="number"
                class="input-add-package"
                :value="new_menu_price * qty"
                required
              />
              <input
                v-else
                type="number"
                class="input-add-package"
                value="0"
                required
              />
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
      </div>
      <!-- Add Topping -->
      <div
        class="table-item"
        v-if="add_topping && add_menu"
        style="width: 104%; margin-left: -11px"
      >
        <form style="padding: 3px" @submit="make_package_item">
          <div class="row" style="padding-top: 0px">
            <div class="col-1 w-100">Topping</div>
            <div class="col-6 w-100" style="margin: auto; line-height: 100%">
              <input
                type="text"
                class="input-add-package"
                style="margin-left: -23px"
                @input="searchByTyping($event, 'topping')"
                :class="{ incorrect: create_input }"
                v-model="topping_item.name"
                required
              />
              <ul style="min-width: 40%">
                <li
                  v-for="topping in toppings"
                  :key="topping.id"
                  @click="select_topping(topping)"
                >
                  <p
                    class="w-100"
                    :class="{ selected: topping_item.id == topping.id }"
                  >
                    {{ topping.name }}
                  </p>
                </li>
              </ul>
            </div>
            <div
              class="col-1 w-100"
              style="
                margin: auto;
                text-align: left;
                line-height: 100%;
                margin-top: 0px;
              "
            >
              <input
                type="number"
                class="input-add-package"
                v-model="topping_qty"
                required
              />
            </div>
            <div class="col-3 w-100" style="line-height: 130%; font-size: 24px">
              <input
                v-if="'pricetopping_set' in topping_item"
                type="number"
                class="input-add-package"
                :value="
                  topping_item.pricetopping_set[0].price * topping_item.remain
                "
                required
              />
              <input
                v-else
                type="number"
                class="input-add-package"
                value="0"
                required
              />
              <input type="submit" style="display: none" />
            </div>
            <div class="col-1" style="line-height: 145%">
              <img
                src="../../assets/icon/incorrect.png"
                style="width: 30px"
                @click="
                  add_topping = false;
                  topping_item = {};
                "
              />
            </div>
          </div>
        </form>
      </div>
      <!-- Add Topping To Item Toppings -->
      <div
        class="table-item"
        v-if="add_topping_to"
        style="width: 104%; margin-left: -11px"
      >
        <form style="padding: 3px" @submit="make_package_item_to">
          <div class="row" style="padding-top: 0px">
            <div class="col-1 w-100">Topping</div>
            <div class="col-6 w-100" style="margin: auto; line-height: 100%">
              <input
                type="text"
                class="input-add-package"
                style="margin-left: -23px"
                @input="searchByTyping($event, 'topping')"
                :class="{ incorrect: create_input }"
                v-model="topping_item.name"
                required
              />
              <ul style="min-width: 40%">
                <li
                  v-for="topping in toppings"
                  :key="topping.id"
                  @click="select_topping(topping)"
                >
                  <p class="w-100">
                    {{ topping.name }}
                  </p>
                </li>
              </ul>
            </div>
            <div
              class="col-1 w-100"
              style="
                margin: auto;
                text-align: left;
                line-height: 100%;
                margin-top: 0px;
              "
            >
              <input
                type="number"
                class="input-add-package"
                v-model="topping_qty"
                required
              />
            </div>
            <div class="col-3 w-100" style="line-height: 130%; font-size: 24px">
              <!-- <input
                v-if="Object.keys(topping_item).length != 0"
                type="number"
                class="input-add-package"
                :value="
                  topping_item.pricetopping_set[0].price * topping_item.remain
                "
                required
              />
              <input
                v-else
                type="number"
                class="input-add-package"
                value="0"
                required
              /> -->
              <input type="submit" style="display: none" />
            </div>
            <div class="col-1" style="line-height: 145%">
              <img
                src="../../assets/icon/incorrect.png"
                style="width: 30px"
                @click="
                  add_topping_to = false;
                  topping_item = {};
                "
              />
            </div>
          </div>
        </form>
      </div>
      <!-- Add Topping Txt -->
      <div
        class="table-item"
        style="width: 104%; margin-left: -11px"
        v-if="add_menu"
      >
        <div class="row" style="font-size: 20px; color: white; line-height: 1">
          <div
            v-if="Object.keys(topping_item).length == 0"
            class="col-3 w-100"
            style="margin-left: 20px; text-align: left; color: #50d1aa"
            @click="add_topping = true"
          >
            + Add Topping
          </div>
          <div
            v-else
            class="col-3 w-100"
            style="margin-left: 20px; text-align: left; color: #50d1aa"
            @click="
              make_package_item();
              add_topping_to = true;
            "
          >
            + Add Topping
          </div>
        </div>
      </div>

      <!-- Total -->
      <div class="table-item" style="width: 104%; margin-left: -11px">
        <div
          class="row"
          style="font-size: 24px; color: white; line-height: 14px"
        >
          <div class="col-6 w-100"></div>
          <div class="col-4 w-100" style="text-align: right">Total</div>
          <div class="col-2 w-100">{{ total_price }}</div>
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
import SavePopup from "../../components/main_component/SavePopup.vue";
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
    this.fetchToppings();
  },
  data() {
    return {
      search_topping: false,
      search_product: false,
      is_staff: false,
      alert: false,
      add_topping_to: false,
      add_topping: false,
      add_menu: false,
      select_all: false,
      topping_items: [],
      update_status: [],
      package_items: [],
      selected_item_toppings: [],
      selected_items: [],
      temp_start: null,
      topping_item: {},
      // Item Topping
      topping_id: null,
      topping_idx: 0,
      topping_price: null,
      topping_qty: 1,
      item_id: null,
      // Package Item
      product_item: {},
      qty: 1,
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
      description: "",
      show_img: null,
      products: [],
      toppings: [],
      temp_toppings: [],
      temp_products: [],
      new_menu_price: 0,
      product: "",
      topping_name: null,
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
    fetchToppings() {
      api_product.get("topping/").then((response) => {
        console.log(response.data, "toppings");
        this.toppings = response.data;
        this.temp_toppings = response.data;
      });
    },
    save() {
      const packageitem = [];
      this.package_items.forEach((element) => {
        var pi = {
          product: element.product.id,
          qty: element.qty,
          total_price: element.price,
          description: element.description,
          itemtopping_set: [],
        };
        if (element.topping.length != 0) {
          element.topping.forEach((el) => {
            pi.itemtopping_set.push({
              topping: el.id,
              total_price: parseInt(el.pricetopping_set[0].price),
              qty: el.remain,
            });
          });
        }
        packageitem.push(pi);
      });
      const data = {
        promotion: this.promotion,
        start_date: this.start_date,
        amount_day: this.amount_day,
        pricepackage_set: [
          {
            normal_price: this.total_price.toString(),
            discount_price: this.discount_price.toString(),
            sale_channel: this.$store.state.ezzone_id,
          },
        ],
        description: this.description,
        total_amount: this.package_items.length,
        status: this.status,
        create_by: this.$store.state.auth.userInfo.id,
        packageitem_set: packageitem,
      };
      console.log(data, "data");
      api_promotion.post("package/", data).then((response) => {
        const img_data = new FormData();
        img_data.append("img", this.img, this.img.name);
        api_promotion
          .put(`package-image/${response.data.id}`, img_data)
          .then(() => {
            this.$router.push({ name: "Promotion" });
          });
        this.alert = true;
        setTimeout(() => {
          this.alert = false;
        }, 2000);
      });
    },
    add_update_status(item) {
      this.update_status[0] = item
    },
    select_topping(item) {
      console.log(item, "item");
      item.remain = this.topping_qty;
      this.topping_item = item;
      this.toppings = [];
    },
    select_update_product(item, idx) {
      this.total_price = 0;
      this.package_items[idx].product = { ...item };
      this.calc_total_price()
      setTimeout(() => {
        this.products = [];
      }, 100);
    },
    select_product(item) {
      this.product_item = { ...item };
      this.new_menu_price = parseInt(
        this.product_item.priceproduct_set[0].price
      );
      setTimeout(() => {
        this.products = [];
      }, 100);
    },
    select_del_item(item, is_package_item) {
      if (is_package_item) {
        if (!this.selected_items.includes(item)) {
          this.selected_items.push(item);
        } else {
          var idx = this.selected_items.indexOf(item);
          this.selected_items.splice(idx, 1);
        }
      } else {
        if (!this.selected_item_toppings.includes(item)) {
          this.selected_item_toppings.push(item);
        } else {
          var idx = this.selected_item_toppings.indexOf(item);
          this.selected_item_toppings.splice(idx, 1);
        }
      }
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
          this.toppings = this.temp_toppings;
        }
      } else {
        if (type == "product") {
          this.temp_products.forEach((element) => {
            if (element.name.indexOf(e.target.value) + 1 != 0) {
              temp.push(element);
            }
          });
          this.search_product = true;
          this.products = temp;
        }
        if (type == "topping") {
          this.temp_toppings.forEach((element) => {
            if (element.name.indexOf(e.target.value) + 1 != 0) {
              temp.push(element);
            }
          });
          this.search_topping = true;
          this.toppings = temp;
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
      if (Object.keys(this.topping_item).length != 0) {
        this.topping_items.push(this.topping_item);
      }
      var data = {
        product: this.product_item,
        topping: this.topping_items,
        qty: this.qty,
        price: this.new_menu_price,
        description: this.description,
      };
      this.total_price = 0;
      this.package_items.push(data);
      this.calc_total_price();
      this.add_menu = false;
      this.add_topping = false;
      this.product_item = {};
      this.topping_item = {};
      this.topping_items = [];
      this.qty = 1;
      this.new_menu_price = null;
    },
    make_package_item_to() {
      this.total_price = 0;
      var idx = this.package_items.length - 1;
      this.package_items[idx].topping.push(this.topping_item);
      this.package_items.forEach((el) => {
        console.log("out");
        this.total_price += parseInt(el.product.priceproduct_set[0].price);
        el.topping.forEach((topping) => {
          console.log("in");
          this.total_price += parseInt(topping.pricetopping_set[0].price);
        });
      });
      this.calc_total_price()
      this.add_menu = false;
      this.add_topping_to = false;
      this.product_item = {};
      this.topping_item = {};
      this.topping_items = [];
      this.qty = 1;
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
      for (let index = 0; index < this.selected_items.length; index++) {
        var idx = this.package_items.indexOf(this.selected_items[index]);
        this.package_items.splice(idx, 1);
      }
      for (let i = 0; i < this.selected_item_toppings.length; i++) {
        var top_idx = this.package_items[i].topping.indexOf(
          this.selected_item_toppings[i]
        );
        this.package_items[i].topping.splice(top_idx - 1, 1);
      }
      this.selected_items = [];
      this.selected_item_toppings = [];
      this.calc_total_price();
    },
    cancel_to_create() {
      this.add_menu = false;
      this.product_item = {};
      this.topping_item = {};
      this.qty = null;
      this.total_price = 0;
    },
    calc_total_price() {
      this.total_price = 0;
      this.package_items.forEach((el) => {
        this.total_price += parseInt(el.product.priceproduct_set[0].price);
        el.topping.forEach((topping) => {
          this.total_price += parseInt(topping.pricetopping_set[0].price);
        });
      });
    },
  },
  watch: {},
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
  width: 100%;
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
  width: 85%;
  height: 50px;
  background: rgb(113, 113, 113);
  border-radius: 12px;
  color: white;
  float: left;
  margin: 10px 0px 0px 56px;
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
  background: rgb(113, 113, 113);
  margin-top: 10px;
  list-style-type: none;
  padding: 0px;
  border-radius: 10px;
  position: absolute;
  min-width: 50%;
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