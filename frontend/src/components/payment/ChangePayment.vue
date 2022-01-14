<template>
  <div v-if="order != null">
    <div class="dark" @click="$emit('hide')"></div>
    <div class="payment-select">
      <div class="row w-100" style="margin: 0px">
        <div class="col-12" style="margin-top: 15px; height: 90px">
          <p style="font-size: 40px">Payment Channel</p>
          <img
            src="../../assets/icon/delete.png"
            style="position: absolute; height: 30px; top: 15px; right: 15px"
            @click="$emit('hide')"
            alt=""
          />
        </div>

        <div class="col-3 w-100" style="height: 150px">
          <button
            class="btn-ghost-y"
            style="width: 126.25px; height: 133.52px"
            @click="select_payment({ payment: 'cod' })"
          >
            <img
              src="../../assets/icon/pod.png"
              style="width: 80px; margin-top: 10px"
            />
            <p style="font-size: 24px; margin-bottom: 5px">COD</p>
          </button>
        </div>
        <div
          class="col-3 w-100"
          style="height: 150px"
          v-for="channel in payment"
          :key="channel.id"
        >
          <button
            class="btn-ghost-g"
            style="width: 126.25px; height: 133.52px"
            @click="select_payment(channel)"
          >
            <img :src="channel.img" style="width: 80px; margin-top: 10px" />
            <p style="font-size: 24px; margin-bottom: 5px">
              {{ channel.payment }}
            </p>
          </button>
        </div>
      </div>
    </div>

    <!-- trasfer -->
    <div v-if="transfer">
      <div class="dark" @click="transfer = false"></div>
      <div class="transfer">
        <div class="row w-100" style="margin: 0px; line-height: 100px">
          <div class="col-12 w-100" style="height: 100px; text-align: center">
            Transfer
          </div>
          <div
            class="col-12 w-100"
            style="font-weight: normal; font-size: 72px; height: 105px"
          >
            {{ order.total_balance }}
          </div>
          <div class="col-12 line"></div>
          <div class="col-4 w-100" style="height: 110px">
            <button
              class="btn-ghost-r"
              style="width: 113px; height: 56px; line-height: 100%"
              @click="transfer = false"
            >
              <img
                src="../../assets/icon/cancel.png"
                style="width: 30px"
                alt=""
              />
            </button>
          </div>
          <div class="col-4 w-100" style="height: 110px">
            <button
              class="btn-ghost-b"
              style="width: 113px; height: 56px; line-height: 100%"
            >
              <img
                src="../../assets/icon/print.png"
                style="width: 30px"
                alt=""
              />
            </button>
          </div>
          <div class="col-4 w-100" style="height: 110px">
            <button
              class="btn-ghost-g"
              style="width: 113px; height: 56px; line-height: 100%"
              @click="update_order()"
            >
              <img
                src="../../assets/icon/correct-bold.png"
                style="width: 30px"
                alt=""
              />
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- payment summary -->
    <div v-if="payment_summary">
      <div class="dark" @click="payment_summary = false"></div>
      <div class="payment_summary">
        <div
          class="row w-100"
          style="margin: 0px; height: 600px; padding-bottom: 15px"
        >
          <div class="col-12">Payment Summary</div>
          <div class="col-7" style="color: #9290fe">Total Qty :</div>
          <div class="col-5" style="color: #9290fe">
            {{ order.total_amount }}
          </div>
          <div class="col-7" style="color: #ea7c69">Cash :</div>
          <div class="col-5" style="color: #ea7c60">{{ cash }}</div>
          <div class="col-7" style="color: #ffb572">Total :</div>
          <div class="col-5" style="color: #ffb572">
            {{ order.total_price }}
          </div>
          <div class="col-7" style="color: #ff7ca3">Discount :</div>
          <div
            class="col-5"
            style="color: #ff7ca3"
            v-if="order.discount_percent"
          >
            {{ (order.discount * order.total_price) / 100 }}
          </div>
          <div class="col-5" style="color: #ff7ca3" v-else>
            {{ order.discount }}
          </div>
          <div class="col-7" style="color: #50d1aa">Total Balance :</div>
          <div class="col-5" style="color: #50d1aa">
            {{ order.total_balance }}
          </div>
          <div class="col-12 line mt-2 mb-3"></div>
          <div class="col-12">Change</div>
          <div class="col-12" style="font-size: 72px; font-weight: 400">
            {{ order.total_balance - cash }}
          </div>
          <div class="col-12 line mb-3 mt-4"></div>
          <div class="col-4 w-100" style="padding-right: 0px">
            <button
              class="btn-ghost-r"
              style="width: 113px; height: 56px; line-height: 100%"
              @click="payment_summary = false"
            >
              <img
                src="../../assets/icon/cancel.png"
                style="width: 30px"
                alt=""
              />
            </button>
          </div>
          <div class="col-4 w-100">
            <button
              class="btn-ghost-b"
              style="width: 113px; height: 56px; line-height: 100%"
            >
              <img
                src="../../assets/icon/print.png"
                style="width: 30px"
                alt=""
              />
            </button>
          </div>
          <div class="col-4 w-100" style="padding-left: 0px">
            <button
              class="btn-ghost-g"
              style="width: 113px; height: 56px; line-height: 100%"
              @click="cash_order()"
            >
              <img
                src="../../assets/icon/correct-bold.png"
                style="width: 30px"
                alt=""
              />
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- payment summary cod -->
    <div v-if="cod_summary">
      <div class="dark" @click="cod_summary = false"></div>
      <div class="payment_summary">
        <div
          class="row w-100"
          style="margin: 0px; height: 600px; padding-bottom: 15px"
        >
          <div class="col-12">Payment Summary</div>
          <div class="col-7" style="color: #9290fe">Total Qty :</div>
          <div class="col-5" style="color: #9290fe">
            {{ order.total_amount }}
          </div>
          <div class="col-7" style="color: #ffb572">Total :</div>
          <div class="col-5" style="color: #ffb572">
            {{ order.total_price }}
          </div>
          <div class="col-7" style="color: #ff7ca3">Discount :</div>
          <div
            class="col-5"
            style="color: #ff7ca3"
            v-if="order.discount_percent"
          >
            {{ (order.discount * order.total_price) / 100 }}
          </div>
          <div class="col-5" style="color: #ff7ca3" v-else>
            {{ order.discount }}
          </div>
          <div class="col-7" style="color: #50d1aa">Total Balance :</div>
          <div class="col-5" style="color: #50d1aa">
            {{ order.total_balance }}
          </div>
          <div class="col-12 line mt-2 mb-3"></div>
          <div class="col-12">Prepare Change</div>
          <div class="col-7" style="color: #ea7c60">1,000 ฿ :</div>
          <div class="col-5">{{ 1000 - order.total_balance }}</div>
          <div class="col-7" style="color: #ea7c69">500 ฿ :</div>
          <div class="col-5">{{ 500 - order.total_balance }}</div>
          <div class="col-7" style="color: #ea7c60">200 ฿ :</div>
          <div class="col-5">{{ 200 - order.total_balance }}</div>
          <div class="col-7" style="color: #ea7c60">100 ฿ :</div>
          <div class="col-5">{{ 100 - order.total_balance }}</div>
          <div class="col-12 line mb-3 mt-4"></div>
          <div class="col-12 w-100" style="padding-right: 0px">
            <button
              class="btn-ghost-r"
              style="width: 113px; height: 56px; line-height: 100%"
              @click="cod_summary = false"
            >
              <img
                src="../../assets/icon/cancel.png"
                style="width: 30px"
                alt=""
              />
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- total cal cash -->
    <cal-cash
      :show_cal="calculate_cash"
      :total_price="order.total_balance"
      @hide_cal="calculate_cash = false"
      @submit_c="cash_c"
    />
  </div>
</template>

<script>
import CalCash from "./CalCash.vue";
import { api_pos } from "../../api/api_pos.js";
export default {
  props: ["order"],
  components: { CalCash },
  mounted() {
    api_pos.get("payment/").then((response) => {
      this.payment = response.data;
    });
  },
  data() {
    return {
      payment: [],
      selected_payment: {},
      transfer: false,
      calculate_cash: false,
      payment_summary: false,
      cod_summary: false,
      cash: 0,
    };
  },
  methods: {
    select_payment(payment) {
      this.selected_payment = payment;
      if (payment.id == undefined) {
        this.$store.commit("pos/payment", null);
      } else {
        this.$store.commit("pos/payment", payment.id);
      }
      if (payment.payment == "cash") {
        this.calculate_cash = true;
      } else if (payment.payment == "cod") {
        this.cod_summary = true;
      } else if (payment.payment == "transfer") {
        this.transfer = true;
      } else {
        this.transfer = true;
      }
      this.seleted_payment = payment;
    },
    cash_c(cash_i) {
      this.cash = cash_i;
      this.calculate_cash = false;
      this.payment_summary = true;
    },
    cash_order() {
      var data = {
        cash: this.cash,
      };
      api_pos.put(
        "order/payment-channel/" +
          this.order.id +
          "/" +
          this.selected_payment.id,
        data
      );
      this.transfer = false;
      this.payment_summary = false;
      this.cod_summary = false;
      this.$emit("hide");
    },
    update_order() {
      api_pos.put(
        "order/payment-channel/" +
          this.order.id +
          "/" +
          this.selected_payment.id
      );
      this.transfer = false;
      this.payment_summary = false;
      this.cod_summary = false;
      this.$emit("hide");
    },
  },
};
</script>

<style scoped>
.dark {
  background-color: #000000aa;
  width: 100%;
  height: 100%;
  top: 0px;
  left: 0px;
  position: fixed;
  display: block;
}
.payment-select {
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
  background-color: #303344;
  width: 632px;
  border: 1.2px solid #ea7c69;
  border-radius: 10px;
  display: flex;
  color: #ffffff;
  font-weight: bold;
  font-size: 30px;
}
.transfer {
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
  background-color: #303344;
  width: 450px;
  /* height: 320px; */
  border-radius: 15px;
  display: flex;
  color: #ffffff;
  font-weight: bold;
  font-size: 36px;
}
.payment_summary {
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
  background-color: #303344;
  width: 400px;
  border-radius: 15px;
  display: flex;
  color: #ffffff;
  font-weight: bold;
  font-size: 36px;
}
.credit {
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
  background-color: #303344;
  width: 439px;
  border-radius: 15px;
  display: flex;
  color: #ffffff;
  font-weight: bold;
  font-size: 36px;
}
.line {
  height: 2.5px;
  margin: auto;
  width: 90%;
  background-color: #ea7c69;
}
p {
  font-weight: bold;
  font-size: 30px;
  text-align: center;
}
.payment_summary .row .col-7 {
  text-align: right;
  width: 100%;
  font-size: 24px;
}
.payment_summary .row .col-5 {
  text-align: left;
  width: 100%;
  padding-left: 5px;
  font-size: 24px;
}
</style>