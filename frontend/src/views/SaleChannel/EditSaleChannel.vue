<template>
  <div>
    <nav-app :save="true" @save="create_sale_channel" :url_name="'SaleChannel'"
      >Edit Sale Channel</nav-app
    >
    <div class="row" style="margin-top: 20px">
      <!-- form sale channel -->
      <div class="col-4 w-100" style="margin: auto">
        <label id="select_img" for="file" style="margin-top: 0px">
          <img
            :src="show_img"
            style="
              border-radius: 10px;
              width: 150px;
              height: 132px;
              object-fit: cover;
            "
            class="image"
            v-if="show_img != null"
          />
          <img
            v-else
            src="../../assets/icon/View.png"
            style="width: 150px"
            alt=""
          />
        </label>
        <input
          type="file"
          @change="onFileChange"
          style="display: none"
          id="file"
          class="raw-image"
        />
      </div>
      <div class="col-8 w-100">
        <div style="display: flex" class="mb-2">
          <label class="col-3" for="name">Name </label>
          <input
            v-model="sale_channel_set.sale_channel"
            class="input"
            type="text"
            id="name"
          />
        </div>
        <div style="display: flex">
          <label class="col-3" for="gp">GP% </label>
          <input
            style="width: 120px"
            class="input"
            v-model="sale_channel_set.gp"
            type="number"
            id="gp"
          />
          <div class="status ms-1">
            Status :
            <div class="switch">
              <Switch
                @switch="sale_channel_set.status = !sale_channel_set.status"
                :value="sale_channel_set.status"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- function create delete -->
      <div class="col-12" style="padding: 0px">
        <hr />
        <div class="col-12" style="margin-top: 10px">
          <div style="display: flex">
            <div class="col-3 product" style="text-align: left">Product</div>
            <div class="col-9">
              <button
                class="btn-ghost-b me-3"
                style="width: 202px; height: 50px; white-space: nowrap"
                @click="
                  add_product_to_salechannel = true;
                  select_product_update_id = null;
                  delete_status = false;
                "
              >
                +&#160;New Product
              </button>
              <button
                v-if="!delete_status"
                class="btn-ghost-r"
                style="width: 235px; height: 50px; white-space: nowrap"
                @click="
                  delete_status = true;
                  add_product_to_salechannel = false;
                  select_product_update_id = null;
                "
              >
                <img
                  src="../../assets/icon/r-trash.png"
                  width="20"
                  alt=""
                />&#160;Delete Product
              </button>
              <button
                v-else
                class="btn-ghost-r"
                style="width: 235px; height: 50px"
                @click="delete_selected()"
              >
                <img src="../../assets/icon/r-trash.png" />&#160;Delete Product
              </button>
            </div>
          </div>
        </div>
        <div class="col-12" style="margin-top: 8px">
          <search-bar @search="search_all_product" />
        </div>
      </div>

      <!-- select product -->
      <div
        class="col-12 mt-2"
        style="text-align: left; padding: 0px; overflow-x: auto; display: flex"
      >
        <button
          :class="{ 'btn-gray-active': type_item == 3 }"
          @click="type_item = 3"
          style="width: fit-content; margin: auto"
          class="btn-gray me-2"
        >
          FOOD
        </button>
        <button
          :class="{ 'btn-gray-active': type_item == 2 }"
          @click="type_item = 2"
          style="width: fit-content; margin: auto; white-space: nowrap"
          class="btn-gray me-2"
        >
          DRINK
        </button>
        <button
          :class="{ 'btn-gray-active': type_item == 1 }"
          @click="type_item = 1"
          style="width: fit-content; margin: auto"
          class="btn-gray me-2"
        >
          DRESSERT
        </button>
        <button
          :class="{ 'btn-gray-active': type_item == 4 }"
          @click="type_item = 4"
          style="width: fit-content; margin: auto"
          class="btn-gray me-2"
        >
          TOPPING
        </button>
        <button
          :class="{ 'btn-gray-active': type_item == 5 }"
          @click="type_item = 5"
          style="width: fit-content; margin: auto"
          class="btn-gray me-2"
        >
          CONSIGNMENT
        </button>
        <button
          :class="{ 'btn-gray-active': type_item == 6 }"
          @click="type_item = 6"
          style="width: fit-content; margin: auto"
          class="btn-gray"
        >
          PACKAGE
        </button>
      </div>
    </div>
    <!-- table -->
    <div class="table" style="margin-top: 10px">
      <!-- header -->
      <div class="table-header" style="line-height: 40px; font-size: 24px">
        <div class="row">
          <div
            class="col-5 w-100"
            style="margin-left: 10px; text-align: left; line-height: 100%"
          >
            Product Name
          </div>
          <div
            class="col-3 w-100"
            style="margin-left: 10px; text-align: left; line-height: 100%"
          >
            Sale Price
          </div>
          <div
            class="col-4 w-100"
            style="margin: auto; margin-left: -10px; line-height: 100%"
          >
            Net Price
          </div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 470px">
        <div class="table-item" v-for="item in items" :key="item.id">

          <!-- update -->
          <form
            style="padding: 3px"
            @submit="update_product(item)"
            v-if="check_type_update(item)"
          >
            <div class="row">
              <div class="col-5 w-100" style="margin: auto; line-height: 100%">
                <input
                  type="text"
                  class="input-product"
                  v-model="update_product_name"
                  :class="{ incorrect: create_input }"
                  required
                />
                <ul>
                  <li
                    v-for="product in search_product"
                    :key="product.id"
                    @click="select_update(product)"
                  >
                    <p
                      v-if="type_item == 6"
                      class="w-100"
                      :class="{ selected: selected_product.id == product.id }"
                    >
                      {{ product.promotion }}
                    </p>
                    <p
                      v-else
                      class="w-100"
                      :class="{ selected: selected_product.id == product.id }"
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
                  v-if="type_item == 6"
                  type="number"
                  class="input-product"
                  v-model="item.discount_price"
                  required
                />
                <input
                  v-else
                  type="number"
                  class="input-product"
                  v-model="item.price"
                  required
                />
              </div>
              <div
                v-if="type_item == 6"
                class="col-3 w-100"
                style="line-height: 130%; font-size: 24px"
              >
                {{ net_price(item.discount_price) }}
                <input type="submit" style="display: none" />
              </div>
              <div
                v-else
                class="col-3 w-100"
                style="line-height: 130%; font-size: 24px"
              >
                {{ net_price(item.price) }}
                <input type="submit" style="display: none" />
              </div>

              <div class="col-1" style="line-height: 145%">
                <img
                  src="../../assets/icon/incorrect.png"
                  style="width: 30px"
                  alt=""
                  @click="select_product_update_id = null"
                />
              </div>
            </div>
          </form>

          <!-- topping -->
          <div
            class="row"
            v-else-if="item['topping'] !== undefined"
            style="width: 90%; margin: auto; font-size: 24px"
          >
            <div class="col-1">
              <div class="checkbox-orange" v-if="delete_status">
                <input
                  type="checkbox"
                  :value="item.topping"
                  v-model="delete_list_topping"
                />
              </div>
            </div>
            <div
              class="col-4 w-100"
              style="line-height: 100%; text-align: left"
              @click="select_product_update(item)"
            >
              {{ item.topping_set.name }}
            </div>
            <div
              class="col-3 w-100"
              style="margin: auto; line-height: 100%"
              @click="select_product_update(item)"
            >
              {{ item.price }}
            </div>
            <div class="col-4 w-100" style="margin: auto; line-height: 100%">
              {{ net_price(item.price) }}
            </div>
          </div>

          <!-- product -->
          <div
            class="row"
            v-else-if="item['product'] !== undefined"
            style="width: 100%; margin: auto; font-size: 24px"
          >
            <div class="col-1">
              <div class="checkbox-orange" v-if="delete_status">
                <input
                  type="checkbox"
                  :value="item.product"
                  v-model="delete_list_product"
                />
              </div>
            </div>
            <div
              class="col-4 w-100"
              style="line-height: 100%; text-align: left"
              @click="select_product_update(item)"
            >
              {{ item.product_set.name }}
            </div>
            <div
              class="col-3 w-100"
              style="margin: auto; line-height: 100%"
              @click="select_product_update(item)"
            >
              {{ item.price }}
            </div>
            <div class="col-4 w-100" style="margin: auto; line-height: 100%">
              {{ net_price(item.price) }}
            </div>
          </div>

          <!-- package -->
          <div
            class="row"
            v-if="item['package'] != undefined"
            style="width: 100%; margin: auto; font-size: 24px"
          >
            <div class="col-1">
              <div class="checkbox-orange" v-if="delete_status">
                <input
                  type="checkbox"
                  :value="item.package"
                  v-model="delete_list_package"
                />
              </div>
            </div>
            <div
              class="col-4 w-100"
              style="line-height: 100%; text-align: left"
              @click="select_product_update(item)"
            >
              {{ item.package_set.promotion }}
            </div>
            <div
              class="col-3 w-100"
              style="margin: auto; line-height: 100%"
              @click="select_product_update(item)"
            >
              {{ item.discount_price }}
            </div>
            <div class="col-4 w-100" style="margin: auto; line-height: 100%">
              {{ net_price(item.discount_price) }}
            </div>
          </div>
        </div>
        <!-- to create product -->
        <div class="table-item" v-if="add_product_to_salechannel">
          <form style="padding: 3px" @submit="add_product">
            <div class="row">
              <div class="col-5 w-100" style="margin: auto; line-height: 100%">
                <input
                  type="text"
                  class="input-product"
                  @input="get_product"
                  v-model="product"
                  :class="{ incorrect: create_input }"
                  required
                />
                <ul>
                  <li
                    v-for="product in search_product"
                    :key="product.id"
                    @click="select_product(product)"
                  >
                    <p
                      v-if="type_item == 6"
                      class="w-100"
                      :class="{ selected: selected_product.id == product.id }"
                    >
                      {{ product.promotion }}
                    </p>
                    <p
                      v-else
                      class="w-100"
                      :class="{ selected: selected_product.id == product.id }"
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
                {{ net_price(price) }}
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
      </div>
    </div>
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import SavePopup from "../../components/main_component/SavePopup.vue"
import { api_product } from "../../api/api_product";
import { api_promotion } from "../../api/api_promotion";
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
export default {
  components: { NavApp, Switch, SearchBar, SavePopup },
  mounted() {
    api_product
      .get("sale-channel/" + this.$route.params.id + "/")
      .then((response) => {
        this.sale_channel_set = response.data;
      });
    api_product
      .get("sale-channel-update-img/" + this.$route.params.id + "/")
      .then((response) => {
        this.show_img = response.data.img;
      });
    api_promotion.get("package").then((response) => {
      this.all_packages = response.data;
    });
  },
  data() {
    return {
      alert: false,
      show_img: null,
      img: null,
      sale_channel_set: {
        sale_channel: "",
        gp: 0,
        status: true,
        create_by: 1,
        price_product: [],
        price_topping: [],
        price_package: [],
      },
      type_item: 1,
      items: [],
      add_product_to_salechannel: false,
      product: "",
      selected_product: {},
      price: 0,
      search_product: [],
      create_input: false,
      delete_list_product: [],
      delete_list_package: [],
      delete_list_topping: [],
      delete_status: false,
      select_product_update_id: 0,
      selected_product_update: {},
      update_product_name: "",
      all_packages: [],
    };
  },
  methods: {
    delete_selected() {
      this.sale_channel_set.price_product =
        this.sale_channel_set.price_product.filter((item) => {
          return !this.delete_list_product.includes(item.product);
        });
      this.sale_channel_set.price_topping =
        this.sale_channel_set.price_topping.filter((item) => {
          return !this.delete_list_topping.includes(item.topping);
        });
      this.sale_channel_set.price_package =
        this.sale_channel_set.price_package.filter((item) => {
          return !this.delete_list_package.includes(item.package);
        });
      this.filter_product();
      this.delete_status = false;
      this.delete_list_product = [];
      this.delete_list_topping = [];
      this.delete_list_package = [];
    },
    select_product(item) {
      this.selected_product = item;
      if (this.type_item == 6) {
        this.product = item.promotion;
      } else {
        this.product = item.name;
      }
      setTimeout(() => {
        this.search_product = [];
        console.log(';akjsdlakjfl;akjsdflakndlkas;lkdfcadlskfja;lskdfj')
      }, 100);
    },
    onFileChange(e) {
      this.img = e.target.files[0];
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
    },
    create_sale_channel() {
      api_product
        .put(
          "sale-channel/" + this.$route.params.id + "/",
          this.sale_channel_set
        )
        .then((response) => {
          if (this.img != null) {
            const data = new FormData();
            data.append("img", this.img, this.img.name);
            api_product
              .put("sale-channel-update-img/" + response.data.id + "/", data)
              .then(() => {
              this.alert = true
              setTimeout(() => {
                this.alert = false
                this.$router.push({ name: "SaleChannel" });
              }, 2000)
              });
          } else {
            this.alert = true
            setTimeout(() => {
              this.alert = false
              this.$router.push({ name: "SaleChannel" });
            }, 2000)
          }
        });
    },
    status_switch(val) {
      this.sale_channel_set.status = val;
    },
    cancel_to_create() {
      this.add_product_to_salechannel = false;
      this.product = "";
      this.price = 0;
      this.selected_product = {};
    },
    get_price(list_price) {
      list_price.forEach((item) => {
        if (item.sale_channel == this.$store.state.ezzone_id) {
          return item.price;
        }
      });
    },
    add_product() {
      if (this.selected_product["id"] !== undefined) {
        if (this.type_item == 4) {
          this.sale_channel_set.price_topping.push({
            topping: this.selected_product.id,
            price: this.price,
            topping_set: this.selected_product,
          });
        }else if (this.type_item == 6) {
          this.sale_channel_set.price_package.push({
            package: this.selected_product.id,
            discount_price: this.price,
            normal_price: 0,
            package_set: this.selected_product,
          });
          this.filter_product();
        } else {
          this.sale_channel_set.price_product.push({
            product: this.selected_product.id,
            price: this.price,
            product_set: this.selected_product,
          });
          this.filter_product();
        }
        this.cancel_to_create();
        this.add_product_to_salechannel = false;
      } else {
        this.create_input = true;
      }
    },
    net_price(price) {
      return (price * (100 - this.sale_channel_set.gp)) / 100;
    },
    filter_same_product(data) {
      for (var item of this.sale_channel_set.price_product) {
        if (item.product == data.id) {
          return false;
        }
      }
      return true;
    },
    filter_same_topping(data) {
      for (var item of this.sale_channel_set.price_topping) {
        if (item.topping == data.id) {
          return false;
        }
      }
      return true;
    },
    filter_same_package(data) {
      for (var item of this.sale_channel_set.price_package) {
        if (item.package == data.id) {
          return false;
        }
      }
      return true;
    },
    search_all_product(val) {
      var temp = [];
      if (val == "") {
        this.type_item = 3;
      } else {
        this.type_item = 0;
        this.sale_channel_set.price_product.forEach((element) => {
          if (element.product_set.name.indexOf(val) + 1 != 0) {
            temp.push(element);
          }
        });
        this.sale_channel_set.price_topping.forEach((element) => {
          if (element.topping_set.name.indexOf(val) + 1 != 0) {
            temp.push(element);
          }
        });this.sale_channel_set.price_package.forEach((element) => {
          if (element.topping_set.promotion.indexOf(val) + 1 != 0) {
            temp.push(element);
          }
        });
        this.items = temp;
      }
    },
    filter_product() {
      if (this.type_item == 1) {
        // get drink
        this.items = this.sale_channel_set.price_product.filter((item) => {
          return item.product_set.type_product == 1;
        });
      } else if (this.type_item == 2) {
        this.items = this.sale_channel_set.price_product.filter((item) => {
          return item.product_set.type_product == 2;
        });
      } else if (this.type_item == 3) {
        this.items = this.sale_channel_set.price_product.filter((item) => {
          return item.product_set.type_product == 3;
        });
      } else if (this.type_item == 4) {
        this.items = this.sale_channel_set.price_topping;
      } else if (this.type_item == 5) {
        this.items = [];
      } else if (this.type_item == 6) {
        this.items = this.sale_channel_set.price_package;
      }
    },
    select_product_update(item) {
      if (this.type_item == 4) {
        this.select_product_update_id = item.topping;
        this.update_product_name = item.topping_set.name;
        this.selected_product_update = item.topping_set;
      } else if (this.type_item == 6) {
        this.select_product_update_id = item.package;
        this.update_product_name = item.package_set.promotion;
        this.selected_product_update = item.package_set;
      }  else {
        this.select_product_update_id = item.product;
        this.update_product_name = item.product_set.name;
        this.selected_product_update = item.product_set;
      }
    },
    select_update(item) {
      this.selected_product_update = item;
      this.update_product_name = item.name;
      setTimeout(() => {
        this.search_product = [];
        console.log('in 729 line')
      }, 100);
    },
    update_product(item) {
      if (this.type_item == 4) {
        const data = this.sale_channel_set.price_topping.find(
          (x) => x.topping === item.topping
        );
        data.topping = this.selected_product_update.id;
        data.topping_set = this.selected_product_update;
      }else if (this.type_item == 6) {
        const data = this.sale_channel_set.price_package.find(
          (x) => x.package === item.package
        );
        data.package = this.selected_product_update.id;
        data.package_set = this.selected_product_update;
      }  else {
        const data = this.sale_channel_set.price_product.find(
          (x) => x.product === item.product
        );
        data.product = this.selected_product_update.id;
        data.product_set = this.selected_product_update;
      }
      this.search_product = [];
      console.log('in 752 line')
      this.select_product_update_id = null;
    },
    check_type_update(item) {
      if (this.type_item == 4) {
        return item.topping == this.select_product_update_id;
      } else if (this.type_item == 6) {
        return item.package == this.select_product_update_id;
      }  else {
        return item.product == this.select_product_update_id;
      }
    },
  },
  watch: {
    type_item() {
      this.cancel_to_create();
      this.filter_product();
    },
    product(newProduct) {
      this.create_input = false;
      console.log(this.type_item)
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
        } else if (this.type_item == 6) {
          console.log('type_four')
          var temp = [];
          this.all_packages.forEach((element) => {
            if (
              element.promotion
                .toLowerCase()
                .indexOf(newProduct.toLowerCase()) +
                1 !=
                0 &&
              this.filter_same_package(element)
            ) {
              temp.push(element);
            }
          });
          this.search_product = temp;
          console.log(this.search_product);
        }  else {
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
      this.search_product = [];
      }
    },
    update_product_name(newProduct) {
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
  },
};
</script>

<style scoped>
.row {
  width: 90%;
  margin: auto;
}
.input {
  width: 300px;
  margin: auto;
  background-color: #717171;
}
label {
  color: #ea7c69;
  font-weight: 800;
  display: inline-block;
  text-align: left;
}
input {
  display: inline-block;
}
.status {
  color: #ea7c68;
  text-align: left;
  font-size: 30px;
  font-weight: 800;
}
hr {
  background-color: #717171;
  height: 3px;
  opacity: 1;
}
.product {
  font-size: 36px;
  color: #fff;
  font-weight: 800;
}
button {
  font-weight: 500;
}

.switch {
  display: inline-block;
  top: 10px;
}

.btn-gray {
  font-weight: 700;
  padding: 0px 10px;
}

.input-product {
  width: 100% !important;
  height: 100%;
  background-color: #717171;
}
ul {
  background-color: #ea7c69;
  margin-top: 10px;
  list-style-type: none;
  padding: 0px;
  border-radius: 10px;
  min-width: 30%;
  z-index: 1;
  position: absolute;
}
p {
  font-size: 20px;
  font-weight: 500;
  text-align: left;
  padding-left: 10px !important;
  padding: 7px;
  margin: 0px;
}
.selected {
  background-color: #717171;
  border-radius: 10px;
}
.incorrect {
  background-image: url("../../assets/icon/incorrect.png");
  background-repeat: no-repeat;
  background-position: 97% 50%;
  background-size: 25px;
  /* border: 5px solid #ea7c68; */
}
input:checked::after {
  top: -7px !important;
}
</style>
