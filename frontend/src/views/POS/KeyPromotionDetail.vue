<template>
  <div>
    <nav-app :url_name="'KeyOrder'">{{
      this.package.package_set.promotion
    }}</nav-app>
    <div class="frame">
      <div class="row mt-2 w-100" style="margin-left: 0px">
        <div class="col-4 mt-3 w-100" style="margin: auto">
          <div class="container-img">
            <img
              v-if="this.package.package_set.img != null"
              class="img"
              :src="this.package.package_set.img"
              alt=""
            />
            <div v-else class="img" style="background-color: #c4c4c4"></div>
            <div class="code">
              {{ this.package.package_set.code }}
            </div>
          </div>
          <div class="price">
            {{ this.package.price_item }}<sup>฿</sup>
            <!-- {{select_price(package.pricepackage_set)}}<sup>฿</sup> -->
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
                v-if="this.package.amount == i"
                class="btn square"
                style="color: #fff !important; line-height: 1px"
              >
                {{ i }}
              </button>
              <div v-else class="square" @click="this.package.amount = i">
                {{ i }}
              </div>
            </div>
          </div>
          <div
            class="w-100"
            style="margin: auto; display: flex; margin-top: 30px"
          >
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

      <h2
        style="
          color: #fff;
          font-size: 30px;
          text-align: left;
          padding-left: 20px;
        "
      >
        Package Detail
      </h2>
      <div
        class="row w-100 table-header"
        style="width: 90%; margin: auto; padding-top: 5px"
      >
        <div class="col-4 w-100">
          Food <img class="type" src="../../assets/icon/fork-active.png" />
        </div>
        <div class="col-4 w-100">
          Drink <img class="type" src="../../assets/icon/drink-active.png" />
        </div>
        <div class="col-4 w-100">
          Dessert
          <img class="type" src="../../assets/icon/dressert-active.png" />
        </div>
      </div>
      <div class="row w-100">
        <div class="col-4 w-100">
          <div
            v-for="item in food"
            :key="item.id"
            class="w-100"
            style="
              font-size: 24px;
              color: #fff;
              text-align: left;
              margin: 10px 0px 10px 10px;
              overflow-x: auto;
              white-space: nowrap;
            "
          >
            {{ item.product_set.name }}
            <div
              class="w-100 ps-4"
              v-for="top in item.itemtopping_set"
              :key="top.id"
            >
              - {{ top.topping_set.name }}
            </div>
          </div>
        </div>
        <div class="col-4 w-100">
          <div
            v-for="item in drink"
            :key="item.id"
            class="w-100"
            style="
              font-size: 24px;
              color: #fff;
              text-align: left;
              margin: 10px 0px 10px 10px;
              overflow-x: auto;
              white-space: nowrap;
            "
          >
            {{ item.product_set.name }}
            <div
              class="w-100 ps-4"
              v-for="top in item.itemtopping_set"
              :key="top.id"
            >
              - {{ top.topping_set.name }}
            </div>
          </div>
        </div>
        <div class="col-4 w-100">
          <div
            v-for="item in dessert"
            :key="item.id"
            class="w-100"
            style="
              font-size: 24px;
              color: #fff;
              text-align: left;
              margin: 10px 0px 10px 10px;
              overflow-x: auto;
              white-space: nowrap;
            "
          >
            {{ item.product_set.name }}
            <div
              class="w-100 ps-4"
              v-for="top in item.itemtopping_set"
              :key="top.id"
            >
              - {{ top.topping_set.name }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- code -->
    <hr class="mt-2" />
    <div
      class="row mt-2"
      style="
        width: 90%;
        margin: auto;
        color: #fff;
        height: 100px;
        font-size: 24px;
        white-space: normal;
        overflow-y: auto;
        text-align: left;
      "
    >
      <div class="col-12">{{ this.package.code }}</div>
    </div>
    <div v-if="blur">
      <div class="blur" @click="blur = false"></div>
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
              v-model="this.package.description"
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
              style="
                width: 165px;
                height: 65px;
                font-size: 30px;
                white-space: nowrap;
              "
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
import { api_promotion } from "../../api/api_promotion";
import { mapGetters } from "vuex";
import NavApp from "../../components/main_component/NavApp.vue";
export default {
  components: { NavApp },
  mounted() {
    if (this.is_edit_package) {
      this.package = this.edit_package;
      this.separate();
    } else {
      api_promotion
        .get("package-pos/" + this.$route.params.package_id)
        .then((response) => {
          this.package.package_set = response.data;
          this.package.package = response.data.id;
          this.get_price_product(this.package.package_set.pricepackage_set);
          this.separate();
        });
    }
  },
  data() {
    return {
      package: {
        code: "",
        flavour_level: 2,
        package: 0,
        price_item: 0,
        total_price: 0,
        size: "M",
        description: "",
        amount: 1,
        package_set: {
          pricepackage_set: [],
          topping_category_set: [{ settopping_set: [] }],
        },
      },
      topping: null,
      blur: false,
      description_list: [
        "แยกน้ำแข็ง",
        "ไม่โรยน้ำตาล",
        "ข้าวน้อย",
        "ขอช้อนส้อม",
      ],
      select_description: [],
      dessert: [],
      food: [],
      drink: [],
    };
  },
  methods: {
    get_price_product(price_list) {
      if (price_list[0] != undefined) {
        const price = parseInt(
          price_list.filter((item) => {
            return (
              item.sale_channel == this.$store.state.pos.order.sale_channel_id
            );
          })[0].discount_price
        );
        this.package.price_item = parseInt(price);
        return price;
      }
    },
    separate() {
      this.package.package_set.packageitem_set.forEach((item) => {
        console.log(item);
        if (item.product_set.type_product == 3) {
          this.food.push(JSON.parse(JSON.stringify(item)));
        }
        if (item.product_set.type_product == 2) {
          this.drink.push(JSON.parse(JSON.stringify(item)));
        }
        if (item.product_set.type_product == 1) {
          this.dessert.push(JSON.parse(JSON.stringify(item)));
        }
      });
    },
    clear() {
      this.blur = false;
      this.select_description = [];
      this.package.description = "";
    },
    total_price() {
      var p = this.package;
      var description = p.package_set.promotion;
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
      p.total_price = parseInt(this.get_price_product(p.package_set.pricepackage_set)) * p.amount;
      return p.total_price;
    },
    add_to_cart() {
      if (this.select_description.length != 0) {
        var select_d = "";
        for (var content of this.select_description) {
          select_d += content + " ";
        }
        this.package.description = this.package.description + " " + select_d;
      }
      if (this.$store.state.pos.select_index != null) {
        this.$store.dispatch("pos/confirm_product", this.package);
        this.$router.push({ name: "OrderReceipt" });
      } else {
        this.$store.dispatch("pos/add_product", this.package);
        this.$router.push({
          name: "KeyOrder",
        });
      }
    },
    back() {
      if (this.is_edit_package) {
        this.$router.push({ name: "OrderReceipt" });
      } else {
        this.$router.push({ name: "KeyOrder" });
      }
    },
    get_code(item) {
      var description = item.product_set.name;
      for (const tops of item.itemtopping_set) {
        description += " + " + tops.topping_set.name;
      }
      return description;
    },
  },
  computed: {
    ...mapGetters({
      edit_package: "pos/edit_package",
      is_edit_package: "pos/is_edit_package",
    }),
  },
};
</script>

<style scoped>
.type {
  height: 35px;
  width: 35px;
  object-fit: contain;
}
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