<template>
  <div v-if="show">
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
            class="btn-ghost-g"
            style="width: 126.25px;hieght:80px; height: 133.52px"
            @click="select_payment({ payment: 'COD' })"
          >
            <img
              src="../../assets/icon/give-money.png"
              style="width: 80px;height:80px; margin-top: 10px;object-fit: contain"
            />
            <p style="font-size: 24px; margin-bottom: 5px">COD</p>
          </button>
        </div>
        <div class="col-3 w-100" style="height: 150px">
          <button
            class="btn-ghost-g"
            style="width: 126.25px; height: 133.52px"
            @click="select_payment({ payment: 'Credit' })"
          >
            <img
              src="../../assets/icon/time-is-money.png"
              style="width: 80px;hieght:80px; margin-top: 10px;object-fit: cover"
            />
            <p style="font-size: 24px; margin-bottom: 5px">Credit</p>
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
            <img :src="channel.img" style="width: 80px;hieght:80px; margin-top: 10px;object-fit: cover" />
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
            {{selected_payment.payment }}
          </div>
          <div
            class="col-12 w-100"
            style="font-weight: normal; font-size: 72px; height: 105px"
          >
            {{ total_balance }}
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
              @click="$store.dispatch('pos/create_order')"
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
          <div class="col-5" style="color: #9290fe">{{ total_amount }}</div>
          <div class="col-7" style="color: #ea7c69">Cash :</div>
          <div class="col-5" style="color: #ea7c60">{{ cash }}</div>
          <div class="col-7" style="color: #ffb572">Total :</div>
          <div class="col-5" style="color: #ffb572">{{ total_price }}</div>
          <div class="col-7" style="color: #ff7ca3">Discount :</div>
          <div class="col-5" style="color: #ff7ca3">{{ discount }}</div>
          <div class="col-7" style="color: #50d1aa">Total Balance :</div>
          <div class="col-5" style="color: #50d1aa">{{ total_balance }}</div>
          <div class="col-12 line mt-2 mb-3"></div>
          <div class="col-12">Change</div>
          <div class="col-12" style="font-size: 72px; font-weight: 400">
            {{ change }}
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
              @click="$store.dispatch('pos/create_order')"
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
          <div class="col-5" style="color: #9290fe">{{ total_amount }}</div>
          <div class="col-7" style="color: #ffb572">Total :</div>
          <div class="col-5" style="color: #ffb572">{{ total_price }}</div>
          <div class="col-7" style="color: #ff7ca3">Discount :</div>
          <div class="col-5" style="color: #ff7ca3">{{ discount }}</div>
          <div class="col-7" style="color: #50d1aa">Total Balance :</div>
          <div class="col-5" style="color: #50d1aa">{{ total_balance }}</div>
          <div class="col-12 line mt-2 mb-3"></div>
          <div class="col-12">Prepare Change</div>
          <div class="col-7" v-if="(1000 - total_balance)>0" style="color: #ea7c60">1,000 ฿ :</div>
          <div class="col-5" v-if="(1000 - total_balance)>0">{{ 1000 - total_balance }}</div>
          <div class="col-7" v-if="(500 - total_balance)>0" style="color: #ea7c69">500 ฿ :</div>
          <div class="col-5" v-if="(500 - total_balance)>0">{{ 500 - total_balance }}</div>
          <div class="col-7" v-if="(200 - total_balance)>0" style="color: #ea7c60">200 ฿ :</div>
          <div class="col-5" v-if="(200 - total_balance)>0">{{ 200 - total_balance }}</div>
          <div class="col-7" v-if="(100 - total_balance)>0" style="color: #ea7c60">100 ฿ :</div>
          <div class="col-5" v-if="(100 - total_balance)>0">{{ 100 - total_balance }}</div>
          <div class="col-12 line mb-3 mt-4"></div>
          <div class="col-4 w-100" style="padding-right: 0px">
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
              @click="$store.dispatch('pos/create_order')"
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

    <!-- total cal cash -->
    <cal-cash
      :show_cal="calculate_cash"
      :total_price="total_balance"
      @hide_cal="calculate_cash = false"
      @submit_c="cash_c"
    />

    <!-- credit conf -->
    <div v-if="credit">
      <div class="dark" @click="credit = false"></div>
      <div class="credit">
        <div class="row">
          <div
            class="col-12"
            style="white-space: normal; width: 75%; margin: 20px auto"
          >
            <img
              src="../../assets/icon/credit.png"
              style="width: 50px"
              class="me-2"
            />
            Are you sure you want to credit?
          </div>

          <div class="col-6 w-100" style="padding-right: 0px; height: 90px">
            <button
              class="btn-ghost-r"
              style="width: 179.5px; height: 56px; line-height: 100%"
              @click="credit = false"
            >
              <img
                src="../../assets/icon/cancel.png"
                style="width: 30px"
                alt=""
              />
            </button>
          </div>
          <div class="col-6 w-100" style="padding-left: 0px; height: 90px">
            <button
              class="btn-ghost-g"
              style="width: 179.5px; height: 56px; line-height: 100%"
              @click="$store.dispatch('pos/create_order')"
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
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import CalCash from "./CalCash.vue";
import { api_pos } from "../../api/api_pos.js";
export default {
  props: ["show"],
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
      credit: false,
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
      if (payment.payment == "Cash") {
        this.$store.state.pos.order.payment_status = 3;
        this.calculate_cash = true;
      } else if (payment.payment == "COD") {
        this.$store.state.pos.order.payment_status = 1;
        this.cod_summary = true;
      } else if (payment.payment == "Credit") {
        this.$store.state.pos.order.payment_status = 2;
        this.credit = true;
      } else {
        this.$store.state.pos.order.payment_status = 4;
        this.transfer = true
      }
    },
    cash_c(cash) {
      this.$store.commit("pos/cash", parseInt(cash));
      this.calculate_cash = false;
      this.payment_summary = true;
    },
  },
  computed: {
    ...mapGetters({
      total_price: "pos/total_price",
      total_amount: "pos/total_amount",
      discount: "pos/discount",
      cash: "pos/cash",
      change: "pos/change",
      total_balance: "pos/total_balance",
      get_data: "pos/get_data",
    }),
  },
};
</script>

<style scoped>
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