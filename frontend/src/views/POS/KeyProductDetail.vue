<template>
  <div>
    <nav-app :url_name="'KeyOrder'">{{ product.product_set.name }}</nav-app>
    <div class="frame">
      <div class="row mt-2 w-100" style="margin-left: 0px">
        <div class="col-4 mt-3 w-100" style="margin: auto">
          <div class="container-img">
            <img
              v-if="product.product_set.img != null"
              class="img"
              :src="product.product_set.img"
              alt=""
            />
            <div v-else class="img" style="background-color: #c4c4c4"></div>
            <div class="code">
              {{ product.product_set.code }}
            </div>
          </div>
          <div class="price">
            {{ get_price_product(product.product_set.priceproduct_set)
            }}<sup>฿</sup>
            <!-- {{select_price(product.priceproduct_set)}}<sup>฿</sup> -->
          </div>
        </div>
        <div class="col-8 mt-3 w-100">
          <div class="w-100" style="margin: auto; display: flex">
            <div class="total-price me-2">{{ total_price() }}</div>
            <div class="baht me-4">฿</div>
            <button
              class="btn-ghost-g"
              style="display: inline"
              @click="add_to_cart()"
            >
              <img
                src="../../assets/icon/cart-g.png"
                style="width: 50px; height: 50px"
                alt=""
              />
            </button>
          </div>
          <div class="w-100 mt-30" style="display: flex; overflow-y: scroll">
            <div class="me-3" v-for="i in 4" :key="i">
              <button
                v-if="product.amount == i"
                class="btn square"
                style="color: #fff !important; line-height: 1px"
              >
                {{ i }}
              </button>
              <div v-else class="square" @click="product.amount = i">
                {{ i }}
              </div>
            </div>
          </div>
          <div
            class="w-100"
            style="margin: auto; display: flex; margin-top: 30px"
          >
            <div class="me-4">
              <button
                v-if="product.size == 'M'"
                class="btn square"
                style="color: #fff !important; line-height: 1px"
              >
                M
              </button>
              <div v-else class="square" @click="product.size = 'M'">M</div>
            </div>
            <div class="me-4">
              <button
                v-if="product.size == 'L'"
                class="btn square"
                style="color: #fff !important; line-height: 1px"
              >
                L
              </button>
              <div v-else class="square" @click="product.size = 'L'">L</div>
            </div>
            <div>
              <img
                @click="blur = true"
                src="../../assets/icon/Note.png"
                alt=""
                style="width: 55px"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="row w-100" style="width: 90%; margin: auto">
        <div class="col-9 w-100" style="height: 200px">
          <div class="row">
            <div
              v-for="topping in product.product_set.topping_category_set
                .settopping_set"
              :key="topping.topping"
              class="col-3 m-1 w-100"
            >
              <div
                v-if="
                  topping.topping_set.pricetopping_set.filter((item) => {
                    return (
                      item.sale_channel ==
                      $store.state.pos.order.sale_channel_id
                    );
                  }).length == 1
                "
                style="padding: 0px"
              >
                <div class="img-topping">
                  <img
                    :src="topping.topping_set.img"
                    style="
                      width: 100px;
                      height: 100px;
                      border-radius: 10px;
                      object-fit: cover;
                    "
                    alt=""
                    @click="add_topping(topping)"
                  />
                  <div
                    v-if="
                      product.orderitemtopping_set.filter((item) => {
                        return item.topping == topping.topping_set.id;
                      }).length != 0
                    "
                    class="amount-topping"
                    @click="increase_topping(topping.topping_set.id)"
                    @touchmove="get_topping(topping.topping_set.id)"
                    @touchstart="start_m"
                    @touchend="end_m"
                  >
                    {{
                      product.orderitemtopping_set.filter((item) => {
                        return item.topping == topping.topping_set.id;
                      })[0].amount
                    }}
                  </div>
                </div>
                <p>{{ topping.topping_set.name }}</p>
              </div>
            </div>
          </div>
        </div>
        <!-- select flavour level -->
        <div class="col-3 w-100" style="height: 200px">
          <div class="btn-group-vertical" role="group" v-if="product.product_set.flavour_level">
            <button
              class="btn btn-ghost"
              @click="product.flavour_level = 3"
              :class="{ 'level-150': product.flavour_level >= 3 }"
            >
              150%
            </button>
            <button
              class="btn btn-ghost"
              @click="product.flavour_level = 2"
              :class="{ 'level-100': product.flavour_level >= 2 }"
            >
              100%
            </button>
            <button
              class="btn btn-ghost"
              @click="product.flavour_level = 1"
              :class="{ 'level-50': product.flavour_level >= 1 }"
            >
              50%
            </button>
            <button
              class="btn btn-ghost"
              @click="product.flavour_level = 0"
              :class="{ 'level-0': product.flavour_level >= 0 }"
            >
              0%
            </button>
          </div>
        </div>
      </div>
    </div>
    <hr />
    <!-- code -->
    <div
      class="row mt-2"
      style="
        width: 90%;
        margin: auto;
        color: #fff;
        height: 35px;
        font-size: 24px;
        white-space: normal;
        overflow-y: auto;
        text-align: left;
      "
    >
      <div class="col-12">{{ this.product.code }}</div>
    </div>
    <div v-if="blur">
      <div class="blur" @click="blur=false"></div>
      <div class="card" :class="{ 'card-active': blur }">
        <div
          class="row"
          style="
            margin: auto;
            width: 90%;
            height: 150px;
            margin-top: 35px;
            margin-bottom: 0px;
          "
        >
          <div
            v-for="idea in description_list"
            :key="idea"
            class="col-6 w-100"
            style="display: flex"
          >
            <div class="checkbox-orange">
              <input
                type="checkbox"
                :id="idea"
                :value="idea"
                v-model="select_description"
                style="margin-right: 15px"
              />
            </div>
            <label :for="idea" style="line-height: 100%">{{ idea }}</label>
          </div>
        </div>
        <div
          class="row w-100"
          style="margin: auto; width: 90%; margin-top: 0px; margin-bottom: 10px"
        >
          <div class="col-12">
            <textarea
              v-model="product.description"
              style="
                height: 145px;
                width: 100%;
                background-color: #717171;
                font-size: 24px;
              "
            ></textarea>
          </div>
          <div class="col-6 w-100 mt-3">
            <button
              class="btn-ghost-r"
              style="width: 165px; height: 65px; font-size: 30px"
              @click="clear()"
            >
              Clear
            </button>
          </div>
          <div class="col-6 w-100 mt-3">
            <button
              class="btn-ghost-g"
              style="width: 165px; height: 65px; font-size: 30px;white-space: nowrap;"
              @click="blur = false"
            >
              Confirm
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_product } from "../../api/api_product";
import { mapGetters } from "vuex";
import NavApp from "../../components/main_component/NavApp.vue";
export default {
  components: { NavApp },
  mounted() {
    if (this.is_edit_product) {
      this.product = this.edit_product;
    } else {
      api_product
        .get("product/" + this.$route.params.product_id)
        .then((response) => {
          this.product.product_set = response.data;
          this.product.product = response.data.id;
          this.description_list =
            this.all_description[this.product.product_set.type_product - 1];
        });
    }
  },
  data() {
    return {
      product: {
        code: "",
        flavour_level: 2,
        product: 0,
        price_item: 0,
        total_price: 0,
        size: "M",
        description: "",
        amount: 1,
        product_set: {
          priceproduct_set: [],
          topping_category_set: [{ settopping_set: [] }],
        },
        orderitemtopping_set: [],
      },
      mouse_start: 0,
      topping: null,
      blur: false,
      all_description: [
      ["แยกนมข้น", "ไม่โรยหน้า", "ไม่โรยน้ำตาล", "ขอช้อนส้อม"],  
      ["แยกน้ำแข็ง", "แยกท๊อปปิ้ง", "ขอถุงหิ้ว", "ขอหลอดเพิ่ม"], 
      ["ไข่ไม่สุก", "ข้าวน้อย", "ไม่ใส่ผัก", "ขอช้อนส้อม"],      
      ],
      description_list: [],
      select_description: [],
    };
  },
  methods: {
    clear() {
      this.blur = false;
      this.select_description = [];
      this.product.description = "";
    },
    get_price_product(price_list) {
      if (price_list[0] != undefined) {
        const price = parseInt(
          price_list.filter((item) => {
            return (
              item.sale_channel == this.$store.state.pos.order.sale_channel_id
            );
          })[0].price
        );
        this.product.price_item = price;
        return price;
      }
    },
    get_price_topping(price_list) {
      if (price_list[0] != undefined) {
        return parseInt(
          price_list.filter((item) => {
            return (
              item.sale_channel == this.$store.state.pos.order.sale_channel_id
            );
          })[0].price
        );
      }
    },
    add_topping(topping) {
      var price_topping = this.get_price_topping(
        topping.topping_set.pricetopping_set
      );
      this.product.orderitemtopping_set.push({
        topping_set: topping.topping_set,
        topping: topping.topping_set.id,
        price_topping: price_topping,
        amount: 1,
        total_price: price_topping,
      });
    },
    total_price() {
      var description = "";
      var p = this.product;
      description = p.product_set.name;
      if (p.flavour_level == 3) {
        description += "(S+)";
      } else if (p.flavour_level == 1) {
        description += "(S-)";
      } else if (p.flavour_level == 0) {
        description += "(Sx)";
      }
      var price_size = 0;
      if (p.product_set.type_product == 2) {
        if (p.price_item >= 49 && p.size == "L") {
          price_size = 15;
          description = description + "(L)";
        } else if (p.size == "L") {
          price_size = 10;
          description = description + "(L)";
        }
      } else if (p.product_set.type_product == 3) {
        if (p.price_item >= 59 && p.size == "L") {
          price_size = 15;
          description = description + "(L)";
        } else if (p.size == "L") {
          price_size = 10;
          description = description + "(L)";
        }
      }
      var price_topping = 0;
      for (var topping of this.product.orderitemtopping_set) {
        price_topping += topping.total_price;
        if (topping.amount > 1) {
          description +=
            " + " + topping.topping_set.name + "(" + topping.amount + ")";
        } else {
          description += " + " + topping.topping_set.name;
        }
      }
      if (p.amount > 1) {
        description = "(" + description + ") x " + p.amount;
      }
      if (this.select_description.length != 0 || p.description != "") {
        var select_d = "";
        for (var content of this.select_description) {
          select_d += content + " ";
        }
        description =
          description + " + (" + p.description + " " + select_d + ")";
      }
      p.code = description;
      p.total_price = (p.price_item + price_size + price_topping) * p.amount;
      return p.total_price;
    },
    start_m(e) {
      this.mouse_start = e.touches[0].clientX;
    },
    end_m(e) {
      if (this.mouse_start - e.changedTouches[0].clientX < -40) {
        this.delete_topping(this.select_topping);
      }
    },
    get_topping(topping) {
      this.select_topping = topping;
    },
    delete_topping(topping_id) {
      this.product.orderitemtopping_set =
        this.product.orderitemtopping_set.filter((item) => {
          return item.topping != topping_id;
        });
      // this.total_price()
    },
    increase_topping(topping_id) {
      var topping = this.product.orderitemtopping_set.filter((item) => {
        return item.topping == topping_id;
      })[0];
      topping.amount += 1;
      topping.total_price = topping.amount * topping.price_topping;
    },
    add_to_cart() {
      if (this.select_description.length != 0) {
        var select_d = "";
        for (var content of this.select_description) {
          select_d += content + " ";
        }
        this.product.description = this.product.description + " " + select_d;
      }
      if (this.$store.state.pos.select_product_index != null) {
        this.$store.dispatch("pos/confirm_product", this.product);
        this.$router.push({ name: "OrderReceipt" });
      } else {
        this.$store.dispatch("pos/add_product", this.product);
        this.$router.push({
          name: "KeyOrder",
        });
      }
    },
    back() {
      if (this.is_edit_product) {
        this.$router.push({ name: "OrderReceipt" });
      } else {
        this.$router.push({ name: "KeyOrder" });
      }
    },
  },
  computed: {
    ...mapGetters({
      edit_product: "pos/edit_product",
      is_edit_product: "pos/is_edit_product",
    }),
  },
};
</script>

<style scoped>
.card {
  width: 524px;
  height: 450px;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.frame {
  width: 672px;
  height: 805px;
  margin: auto;
  padding: 0px !important;
}
.img {
  height: 200px;
  width: 200px;
  border-radius: 10px;
  object-fit: cover;
}
.code {
  position: absolute;
  bottom: 0px;
  right: 10px;
  color: #fff;
  font-size: 48px;
  font-weight: bold;
  text-shadow: rgb(0, 0, 0) 3px 0px 0px, rgb(0, 0, 0) 2.83487px 0.981584px 0px,
    rgb(0, 0, 0) 2.35766px 1.85511px 0px, rgb(0, 0, 0) 1.62091px 2.52441px 0px,
    rgb(0, 0, 0) 0.705713px 2.91581px 0px,
    rgb(0, 0, 0) -0.287171px 2.98622px 0px,
    rgb(0, 0, 0) -1.24844px 2.72789px 0px, rgb(0, 0, 0) -2.07227px 2.16926px 0px,
    rgb(0, 0, 0) -2.66798px 1.37182px 0px, rgb(0, 0, 0) -2.96998px 0.42336px 0px,
    rgb(0, 0, 0) -2.94502px -0.571704px 0px,
    rgb(0, 0, 0) -2.59586px -1.50383px 0px,
    rgb(0, 0, 0) -1.96093px -2.27041px 0px,
    rgb(0, 0, 0) -1.11013px -2.78704px 0px,
    rgb(0, 0, 0) -0.137119px -2.99686px 0px,
    rgb(0, 0, 0) 0.850987px -2.87677px 0px,
    rgb(0, 0, 0) 1.74541px -2.43999px 0px, rgb(0, 0, 0) 2.44769px -1.73459px 0px,
    rgb(0, 0, 0) 2.88051px -0.838247px 0px;
}
.container-img {
  position: relative;
}
.price {
  font-weight: bold;
  font-size: 68px;
  color: #889898;
}
sup {
  font-size: 36px;
  font-weight: 600;
  top: -2rem;
}
.total-price {
  color: #fff;
  background: #bd523f;
  border-radius: 15px;
  display: inline;
  font-weight: 500;
  font-size: 64px;
  line-height: 80px;
  width: 191px;
  height: 80px;
}
.baht {
  top: -50px;
  font-size: 40px;
  font-weight: 600;
  display: inline;
  color: #889898;
  margin-right: 35px;
}
.btn {
  background-color: #bd523f;
}
.btn-ghost-g {
  width: 165px;
  height: 80px;
}
.square {
  min-width: 70px;
  width: 70px;
  height: 60px;
  font-size: 48px;
  line-height: 125%;
  color: #ffffff80;
}
.mt-30 {
  margin-top: 30px;
}
p {
  white-space: nowrap;
  font-size: 19px;
  color: #d7dcdf;
}
.btn-ghost {
  background-color: #303344;
  width: 110px;
  height: 115px;
  font-weight: 500;
  font-size: 34px;
  padding: 0px;
  border: 3px solid #bd523f;
  color: #abbbc2;
}
.level-150 {
  background: #ff7ca3;
  color: #252629 !important;
}
.level-100 {
  background: #ffc692;
  color: #252629 !important;
}
.level-50 {
  background: #fffa76;
  color: #252629 !important;
}
.level-0 {
  background: #73e4c2;
  color: #252629 !important;
}
hr {
  background-color: #bd523f;
  height: 3px;
  margin-top: 1px !important;
  width: 93%;
  margin: auto;
  opacity: 1 !important;
}
.img-topping {
  position: relative;
}

.amount-topping {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 72px;
  font-weight: bold;
  background-color: #bd523fdd;
  width: 100px;
  height: 100px;
  color: #fff;
  border-radius: 10px;
  line-height: 100px;
}
.checkbox-orange input::before {
  height: 40px;
  border: 4px solid#ea7c69;
  width: 40px;
}
.checkbox-orange input {
  height: 40px;
  width: 40px;
}

.checkbox-orange input:checked::after {
  font-size: 22px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>


// drink > 49 +15
// food > 59 +15