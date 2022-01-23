<template>
  <div>
    <nav-app
      :url_name="'KeyOrder'"
      :trash="true"
      @trash="$store.dispatch('pos/clear_order')"
      >Order Receipt</nav-app
    >
    <div class="row" style="width: 96%; margin: auto; margin-top: 15px">
      <div class="col-9 w-100">
        <div style="display: flex">
          <img :src="img_channel" class="sale-channel-img" alt="" />
          <span
            style="
              white-space: pre;
              color: #fff;
              font-size: 20px;
              margin: 0px 10px;
            "
            ># {{ $store.state.pos.order.order_number}}</span
          >
          <label for="tel">Tel.</label>
          <div
            style="
              width: 172px;
              background-color: #303344;
              height: 40px;
              border-radius: 5px;
              color: #fff;
              line-height: 40px;
              text-align: left;
              padding-left: 5px;
              font-size: 20px;
              margin-right: 10px;
            "
            @click="input_tel = true"
          >
            {{ phone_number_layout(phone_number) }}
          </div>
          <img
            src="../../assets/icon/promotion_no_case.png"
            style="
              width: 50px;
              top: -5px;
              position: relative;
              margin-right: 15px;
            "
          />
          <span style="font-size: 24px; color: #ea7c69">999</span>
        </div>
        <div style="display: flex">
          <label for="name">Name&#160;&#160;&#160; :</label>
          <input
            type="text"
            id="name"
            style="margin-right: 15px; width: 241px"
            v-model="cus_name"
          />
          <img
            v-if="
              this.$store.state.pos.order.sale_channel_set.sale_channel ==
              'EZ Zone'
            "
            src="../../assets/icon/table-white.png"
            style="height: 40px; margin-right: 15px"
            alt=""
          />
          <div
            v-if="
              this.$store.state.pos.order.sale_channel_set.sale_channel ==
              'EZ Zone'
            "
            @click="select_table_s = true"
            style="
              width: 56px;
              height: 40px;
              background: #303344;
              border-radius: 5px;
              color: #fff;
              line-height: 40px;
              font-size: 24px;
            "
          >
            {{ table }}
          </div>
        </div>
      </div>
      <div class="col-3 w-100 h-100" style="text-align: right">
        <button
          class="btn-ghost-g"
          style="width: 110px; height: 90px"
          @click="select_payment = true"
        >
          <img
            src="../../assets/icon/cash-coin.png"
            style="width: 60px; margin-top: 8px"
            alt=""
          />
        </button>
      </div>
      <div class="col-12">
        <div style="display: flex; margin-top: 10px">
          <label for="address" style="margin-right: 13px">Address :</label>
          <textarea
            id="address"
            v-model="address"
            @click="select_address = true"
          ></textarea>
        </div>
      </div>
      <div class="col-12 mt-2">
        <div style="display: flex">
          <label for="note" class="note">Note &#160; &#160; &#160;:</label>
          <input type="text" v-model="note" class="note-input" id="note" />
        </div>
      </div>
      <div class="col-12 mt-3">
        <div class="table-header" style="margin: auto; height: 40px">
          <div class="row w-100" style="line-height: 40px; margin: 0px">
            <div class="col-6 w-100" style="margin: auto">Order Details</div>
            <div class="col-2 w-100" style="margin: auto">Qty</div>
            <div class="col-1 w-100" style="margin: auto">Price</div>
            <div class="col-2 w-100" style="margin: auto">Total</div>
          </div>
        </div>
        <div
          class="frame"
          style="height: 355px;margin-top:15px;padding 10px 0px 0px 0px;overflow-y:auto;"
        >
          <div
            v-for="(item, index) in orderitem_list"
            :key="index"
            class="row w-100 mb-2"
            style="margin: 0px; color: #fff; font-size: 20px"
          >
            <div
              v-if="is_topping(item)"
              class="col-6 w-100"
              style="text-align: left; overflow-x: auto"
              @click="$store.dispatch('pos/edit_topping', index)"
            >
              {{ item.code }}
            </div>
            <div
              v-else
              class="col-6 w-100"
              style="text-align: left; overflow-x: auto"
              @click="$store.dispatch('pos/edit_product', index)"
            >
              {{ cal_code(item) }}
            </div>
            <div
              class="col-2 w-100"
              style="text-align: left; padding-left: 35px; font-weight: 700"
            >
              {{ item.amount }}
            </div>
            <div
              class="col-1 w-100"
              style="text-align: center; font-weight: 700"
            >
              {{ item.total_price / item.amount }}
            </div>
            <div
              class="col-2 w-100"
              style="text-align: center; font-weight: 700"
            >
              {{ item.total_price }}
            </div>
            <div class="col-1 w-100" style="text-align: left">
              <img
                src="../../assets/icon/bin.png"
                style="height: 25px"
                alt=""
                @click="$store.dispatch('pos/remove_product', index)"
              />
            </div>
          </div>
        </div>
        <div
          class="frame"
          style="
            height: 180px;
            margin-top: 15px;
            padding-top: 10px;
            padding-right: 15px;
          "
        >
          <div class="row" style="color: #fff">
            <div class="col-6 w-100" style="display: flex; margin-bottom: 20px">
              <div class="event-text">Vouncher&#160; :</div>
              <div class="select-event" @click="VouncherPopup = true">-</div>
            </div>
            <div class="col-1"></div>
            <div class="col-5 w-100">
              <div class="total">Total : {{ total_price }}</div>
            </div>
            <div class="col-6 w-100" style="display: flex; margin-bottom: 20px">
              <div class="event-text">Discount&#160;&#160; :</div>
              <div class="select-event" @click="select_discount()">
                {{ discount }}
              </div>
            </div>
            <div class="col-1"></div>
            <div class="col-5 w-100">
              <div class="discount">Discount : {{ discount_price }}</div>
            </div>
            <div class="col-6 w-100" style="display: flex">
              <div class="event-text">Delivery &#160;&#160; :</div>
              <div class="select-event" @click="select_deli()">
                {{ delivery_price }}
              </div>
            </div>
            <div class="col-1"></div>
            <div class="col-5 w-100">
              <div class="balance">Total Balance : {{ total_balance }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Popup Vouncher -->
    <div class="AreaPopup" v-if="VouncherPopup">

      <div class="dark" @click="VouncherPopup=false">
        <div class="AreaRowVouncher">
          <div class="RowPopupVouncher">

            <div class="PopupVouncher" v-for="voucher in vouchers" :key="voucher" >
                  <img :src="voucher.img" style="width:200px;height:200px;border-radius: 10%;object-fit:cover;">
            </div>          
          
          </div>
        </div>
      </div>
      

    </div>
      
      
    <calculator
      :show_cal="show_cal"
      @hide_cal="show_cal = false"
      @submit="submit"
      :selected="select_cal"
    />
    <input-tel :show="input_tel" @submit="submit_tel" @hide="hide_tel" />
    <select-table
      :show="select_table_s"
      @select_table="select_table"
      @hide="select_table_s = false"
    />
    <select-address
      :show="select_address"
      :customer="customer_set"
      @hide="select_address = false"
      @save="address_save"
    />
    <select-payment
      :show="select_payment"
      @hide="select_payment = false"
      @select_payment="payment"
    />
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import { mapGetters } from "vuex";
import Calculator from "../../components/main_component/Calculator.vue";
import { api_customer } from "../../api/api_customer";
import InputTel from "../../components/main_component/InputTel.vue";
import SelectTable from "../../components/main_component/SelectTable.vue";
import SelectAddress from "../../components/main_component/SelectAddress.vue";
import SelectPayment from "../../components/payment/SelectPayment.vue";
import { api_promotion } from "../../api/api_promotion";
export default {
  components: {
    NavApp,
    Calculator,
    InputTel,
    SelectTable,
    SelectAddress,
    SelectPayment,
  },
  mounted() {
    this.note = this.description;
    this.fetchVoucher();
  },
  data() {
    return {
      note: "",
      show_cal: false,
      select_cal: "",
      selected_customer: {},
      input_tel: false,
      cus_name: "",
      select_table_s: false,
      select_address: false,
      select_payment: false,
      selected_payment: {},
      vouchers: [],
      VouncherPopup: false,
    };
  },
  methods: {
    is_topping(product) {
      console.log("topping" in product);
      if ("topping" in product) {
        return true;
      }
      return false;
    },
    payment(payment) {
      this.selected_payment = payment;
      this.select_payment = false;
    },
    address_save(address_t) {
      this.$store.commit("pos/address_customer", address_t);
      this.select_address = false;
    },
    select_table(i) {
      if (i == "-") {
        this.$store.commit("pos/table", null);
      } else {
        this.$store.commit("pos/table", i);
      }
      this.select_table_s = false;
    },
    submit(result) {
      if (this.select_cal == "discount") {
        this.$store.dispatch("pos/discount", result);
      } else {
        this.$store.dispatch("pos/delivery", result);
      }
      this.show_cal = false;
    },
    submit_tel({ tel, customer }) {
      if (customer != null) {
        this.$store.commit("pos/phone_number", customer.phone_number);
        this.$store.commit("pos/customer_set", customer);
        this.$store.commit("pos/customer_name", customer.first_name);
        this.input_tel = false;
        if (customer.addresscustomer_set.legnth != 0) {
          this.$store.commit(
            "pos/address_customer",
            customer.addresscustomer_set[0].address
          );
        }
      } else {
        this.$store.commit("pos/phone_number", tel);
      }
    },
    select_deli() {
      this.select_cal = "delivery";
      this.show_cal = true;
    },
    select_discount() {
      this.select_cal = "discount";
      this.show_cal = true;
    },
    cal_code(p) {
      var description = "";
      description = p.product_set.name;
      if (p.flavour_level == 3) {
        description += "(S+)";
      } else if (p.flavour_level == 1) {
        description += "(S-)";
      } else if (p.flavour_level == 0) {
        description += "(Sx)";
      }
      if (p.size == "L") {
        description = description + "(L)";
      }
      for (var topping of p.orderitemtopping_set) {
        if (topping.amount > 1) {
          description +=
            " + " + topping.topping_set.name + "(" + topping.amount + ")";
        } else {
          description += " + " + topping.topping_set.name;
        }
      }
      if (p.description != "") {
        description += " + " + "(" + p.description + ")";
      }
      return description;
    },
    hide_tel(tel) {
      this.phone_number = tel;
      this.$store.commit("pos/phone_number", tel);
      this.input_tel = false;
    },
    phone_number_layout(phone) {
      if (phone != null) {
        return (
          phone.substr(0, 3) +
          "-" +
          phone.substr(3, 3) +
          "-" +
          phone.substr(6, 4)
        );
      } else {
        return "";
      }
    },
    fetchVoucher() {
      api_promotion.get("voucher/").then((response) => {
        this.vouchers = response.data;
        console.log(response.data, "voucher");
      });
    },
  },
  computed: {
    ...mapGetters({
      img_channel: "pos/img_sale_channel",
      orderitem_list: "pos/orderitem_list",
      total_price: "pos/total_price",
      discount: "pos/discount",
      discount_price: "pos/discount_price",
      total_balance: "pos/total_balance",
      delivery_price: "pos/delivery_price",
      table: "pos/table",
      description: "pos/description",
      address: "pos/address",
      phone_number: "pos/phone_number",
      customer_name: "pos/customer_name",
      customer_set: "pos/customer_set",
    }),
  },
  watch: {
    customer_name(new_name){
      this.cus_name = new_name    
    },
    note(newData) {
      this.$store.commit("pos/note_input", newData);
    },
    phone_number(newTel) {
      if (newTel != "") {
        api_customer
          .get("get-customer-by-phone-number/" + newTel)
          .then((response) => {
            this.selector_customer = response.data;
          });
      }
    },
    cus_name(new_name) {
      this.$store.state.pos.order.customer_set.nick_name = new_name
    },
    
  },
};
</script>

<style scoped>
.frame {
  border-radius: 10px;
}
.sale-channel-img {
  object-fit: cover;
  width: 40px;
  height: 40px;
  border-radius: 5px;
}
textarea {
  width: 100%;
  height: 64px;
  border-radius: 5px;
  font-size: 20px;
  text-indent: 0px;
  padding-left: 10px;
  padding-right: 20px;
  background-image: url("../../assets/icon/edit-orange.png");
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: 97% 50%;
}
input {
  border-radius: 5px;
  height: 40px;
  width: 175px;
}
label {
  white-space: nowrap;
  font-size: 20px !important;
  margin-right: 15px;
}
.note {
  background-color: #303344;
  font-weight: 800;
  font-size: 20px;
  color: #ff92b2;
  padding-left: 5px;
  border-radius: 5px 0px 0px 5px;
  padding-top: 3px;
  padding-right: 10px;
  margin-right: 0px;
}
.note-input {
  border-radius: 0px 5px 5px 0px;
  background-color: #fafafacc;
  width: 100%;
  color: black;
}
div {
  white-space: nowrap;
}
.select-event {
  margin-left: 10px;
  border: 1px solid #ea7c69;
  width: 170px;
  height: 40px;
  border-radius: 10px;
  line-height: 34px;
  font-weight: 700;
  font-size: 24px;
}
.event-text {
  color: #fafafa;
  font-weight: 700;
  font-size: 24px;
}
.total {
  color: #ffb572;
  font-weight: bold;
  font-size: 24px;
  text-align: left;
}
.discount {
  color: #ff7ca3;
  font-weight: bold;
  font-size: 24px;
  text-align: left;
}

.balance {
  color: #50d1aa;
  font-weight: bold;
  font-size: 24px;
  text-align: left;
}

/* Popup Vouncher */
.AreaRowVouncher {

  width: 100%;
  height: 100%;
  top: 0%;
  position: fixed;
  
}

.RowPopupVouncher {
  width: 100%;
  height: 10%;
  padding:0%;
  padding-left:7%;
  padding-right:7%;
  margin: 0%;
  margin-top:20%;
  display:grid;
  justify-content: center;
  grid-gap: 40% 10%;
  grid-template-columns: auto auto auto;

}

.PopupVouncher {
  border-radius: 20%;
  width: 100%;
  height: 80%;
  padding:0%;

}
</style>
