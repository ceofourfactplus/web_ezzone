<template>
  <div>
    <nav-app :url_name="'KeyOrder'">{{ topping.topping_set.name }}</nav-app>
    <div class="frame">
      <div class="row mt-2 w-100" style="margin-left: 0px">
        <div class="col-4 mt-3 w-100" style="margin: auto">
          <div class="container-img">
            <img
              v-if="topping.topping_set.img != null"
              class="img"
              :src="topping.topping_set.img"
              alt=""
            />
            <div v-else class="img" style="background-color: #c4c4c4"></div>
            <div class="code">
              {{ topping.topping_set.code }}
            </div>
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
          <div
            class="w-100"
            style="margin: auto; display: flex; margin-top: 30px"
          >
            <div class="price">
              {{ get_price_product(topping.topping_set.pricetopping_set)
              }}<sup>฿</sup>
            </div>
            <div style="line-height: 100px; margin-left: 40px">
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
      <div
        class="mb-4 w-100"
        style="margin-left: 0px; display: flex; margin-top: 70px"
      >
        <div style="width: 133px; margin: auto" v-for="i in 5" :key="i">
          <div
            class="square"
            :class="{ 'bg-o': topping.amount == i }"
            @click="topping.amount = i"
          >
            {{ i }}
          </div>
        </div>
      </div>
      <div
        class="w-100"
        style="margin-left: 0px; display: flex; margin-top: 50px"
      >
        <div
          style="width: 133px; margin: auto"
          v-for="i in [6, 7, 8, 9, 10]"
          :key="i"
        >
          <div
            class="square"
            :class="{ 'bg-o': topping.amount == i }"
            @click="topping.amount = i"
          >
            {{ i }}
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
      <div class="col-12">{{ this.topping.code }}</div>
    </div>
    <!-- note -->
    <div class="blur" v-if="blur">
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
              v-model="topping.description"
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
              style="width: 165px; height: 65px; font-size: 30px"
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
    if (this.is_edit_topping) {
      this.topping = this.edit_topping;
    } else {
      api_product
        .get("get-topping/" + this.$route.params.topping_id)
        .then((response) => {
          this.topping.topping_set = response.data;
          this.topping.topping = response.data.id;
        });
    }
  },
  data() {
    return {
      topping: {
        code: "",
        topping: 0,
        price_item: 0,
        total_price: 0,
        description: "",
        amount: 1,
        topping_set: {
          img: "",
          name: "",
          pricetopping_set: [],
          topping_category_set: [{ settopping_set: [] }],
        },
      },
      blur: false,
      description_list: [
        "ไข่ไม่สุก",
        "ขอซอสเพิ่ม",
        "ไม่รับถุง",
        "ขอช้อนส้อม",
      ],
      select_description: [],
    };
  },
  methods: {
    clear() {
      this.blur = false;
      this.select_description = [];
      this.topping.description = "";
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
        this.topping.price_item = price;
        return price;
      }
    },
    total_price() {
      var description = "";
      var p = this.topping;
      description = p.topping_set.name;
      if (this.select_description.length != 0 || p.description != "") {
        var select_d = "";
        for (var content of this.select_description) {
          select_d += content + " ";
        }
        description =
          description + " + (" + p.description + " " + select_d + ")";
      }
      p.code = description;
      p.total_price = p.price_item * p.amount;
      return p.total_price;
    },
    add_to_cart() {
      if (this.select_description.length != 0) {
        var select_d = "";
        for (var content of this.select_description) {
          select_d += content + " ";
        }
        this.topping.description = this.topping.description + " " + select_d;
      }
      if (this.is_edit_topping) {
        this.$store.dispatch("pos/confirm_topping", this.topping);
        this.$router.push({ name: "OrderReceipt" });
      } else {
        this.$store.dispatch("pos/add_product", this.topping);
        this.$router.push({
          name: "KeyOrder",
        });
      }
    },
    back() {
      if (this.is_edit_topping) {
        this.$router.push({ name: "OrderReceipt" });
      } else {
        this.$router.push({ name: "KeyOrder" });
      }
    },
  },
  computed: {
    ...mapGetters({
      edit_topping: "pos/edit_topping",
      is_edit_topping: "pos/is_edit_topping",
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
  height: 502px;
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
.bg-o {
  background-color: #bd523f;
  color: #fff !important;
  width: 70%;
  margin: auto;
  border-radius: 15px;
}
.btn-ghost-g {
  width: 165px;
  height: 80px;
}
.square {
  height: 70px;
  font-size: 52px;
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