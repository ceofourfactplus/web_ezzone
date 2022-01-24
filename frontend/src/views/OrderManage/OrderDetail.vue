<template>
  <div>
    <nav-app :url_name="'DashBoard'">Order Detail</nav-app>
    <div class="row" style="width: 90%; margin: auto">
      <div class="col-9 w-100" style="padding: 0px">
        <search-bar></search-bar>
      </div>
      <div class="col-3 w-100" style="padding: 0px; padding-left: 10px">
        <button
          class="btn-ghost-b w-100"
          style="height: 45px; font-size: 28px; line-height: 40px"
          @click="$router.push({ name: 'SelectSaleChannel' })"
        >
          + Order
        </button>
      </div>
      <div
        class="col-12 w-100"
        style="
          display: flex;
          justify-content: space-between;
          padding: 7px 0px;
          margin: auto;
        "
      >
        <button
          style="width: 24%; padding: 0px"
          class="btn-gray"
          :class="{ 'g-act': selected_status == '1' }"
          @click="select_status('on_going')"
        >
          On going
        </button>
        <button
          style="width: 24%; padding: 0px"
          class="btn-gray"
          :class="{ 'g-act': selected_status == '3' }"
          @click="select_status('completed')"
        >
          Completed
        </button>
        <button
          style="width: 24%; padding: 0px"
          class="btn-gray"
          :class="{ 'g-act': selected_status == '4' }"
          @click="select_status('void')"
        >
          Cancel
        </button>
        <button
          style="width: 24%; padding: 0px"
          class="btn-gray"
          :class="{ 'g-act': selected_status == 'all' }"
          @click="select_status('all')"
        >
          All
        </button>
      </div>
    </div>
    <div class="table">
      <div class="table-header">
        <div class="row w-100" style="margin: auto">
          <div class="col-2">Order No.</div>
          <div class="col-2">Total</div>
          <div class="col-3">Status</div>
          <div class="col-2">Time</div>
          <div class="col-2">Payment</div>
        </div>
      </div>
      <div style="height: 715px; overflow-y: auto">
        <div v-for="order in all_order" :key="order" class="table-item">
          <div
            class="row w-100"
            style="margin: auto; line-height: 100%; padding: 3px"
          >
            <div class="col-1" @click="selected_order = order">
              <img
                :src="order.sale_channel_set.img"
                style="height: 33px; width: 33px; object-fit: cover"
                id="sale_channel"
              />
            </div>
            <div
              class="col-1"
              @click="selected_order = order"
              style="text-align: left; line-height: 30px"
            >
              #{{ order.order_number }}
            </div>
            <div
              class="col-2"
              @click="selected_order = order"
              style="line-height: 30px"
            >
              {{ parseInt(order.total_balance) }}
            </div>
            <div
              class="col-3"
              style="
                display: flex;
                margin: auto;
                width: 160px;
                line-height: 30px;
                justify-content: space-between;
              "
              @click="selected_order = order"
            >
              <div
                class="status me-1"
                :class="{
                  cooking: order.status_food == 1,
                  serve: order.status_food == 2,
                  paid: order.status_food == 3,
                  none: order.status_food == null,
                }"
              >
                Food
              </div>
              <div
                class="status"
                :class="{
                  cooking: order.status_drink == 1,
                  serve: order.status_drink == 2,
                  paid: order.status_drink == 3,
                  none: order.status_drink == null,
                }"
              >
                Drink
              </div>
            </div>
            <div
              class="col-2"
              style="line-height: 30px"
              @click="selected_order = order"
            >
              {{ get_date(order.create_at) }}
            </div>
            <div class="col-2">
              <div
                v-if="order.status_order == 4"
                class="payment"
                style="background-color: #ffb572"
              >
                Cancel
              </div>
              <div
                v-else-if="order.payment_status < 3"
                class="payment"
                @click="$store.dispatch('pos/re_order', order)"
              >
                {{ payment(order) }}
              </div>
              <div v-else class="payment paid">
                {{ payment(order) }}
              </div>
            </div>
            <div
              class="col-1"
              v-if="order.payment_status < 3 && order.status_order != 4"
            >
              <img
                @click="selected_cancel = order"
                src="../.././assets/icon/bin.png"
                style="width: 30px; height: 30px"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <change-payment
      :order="pay_order"
      @hide="pay_order = null"
      @cash="cash"
      @payment_status="change_status"
      @update_order="update_order"
    />
    <cancel-order
      :show="selected_cancel != null"
      @close="selected_cancel = null"
      @cancel_order="cancel_order"
      @re_order="re_order"
    />
    <order-detail-item :order="selected_order" @close="selected_order = null" />
  </div>
</template>

<script>
import { api_pos } from "../../api/api_pos";
import NavApp from "../../components/main_component/NavApp.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
import moment from "moment";
import OrderDetailItem from "../../components/order_manage/OrderDetailItem.vue";
import ChangePayment from "../../components/payment/ChangePayment.vue";
import CancelOrder from "../../components/order_manage/CancelOrder.vue";
var song = new Audio(require("./short-alert.mp3"));
export default {
  components: {
    NavApp,
    SearchBar,
    OrderDetailItem,
    ChangePayment,
    CancelOrder,
  },
  mounted() {
    this.get_order_all_today();
    this.w;
  },
  unmounted() {
    window.clearInterval(this.w);
  },
  data() {
    return {
      w: window.setInterval(() => {
        this.get_status(this.selected_status);
      }, 5000),
      all_order: [],
      selected_status: "1",
      selected_order: null,
      pay_order: null,
      selected_cancel: null,
    };
  },
  methods: {
    get_order_all_today() {
      api_pos.get("order/today/on-going").then((response) => {
        this.all_order = response.data;
      });
    },
    cash(cash) {
      this.pay_order.cash = parseInt(cash);
      this.pay_order.change = parseInt(cash - this.pay_order.total_balance);
    },
    get_date(data) {
      var date = moment(data);
      var now = moment();
      if (now.diff(date, "day") == 0) {
        if (now.diff(date, "hour") == 0) {
          return now.diff(date, "minute") + " Mins";
        }
        return now.diff(date, "hour") + " Hour";
      }
      return now.diff(date, "day") + " Day";
    },
    payment(order) {
      if (order.payment_status == 1) {
        return "COD";
      } else if (order.payment_status == 2) {
        return "Credit";
      } else if (order.payment_status == 3) {
        return "Cash";
      } else if (order.payment_status == 4) {
        return order.payment_set.payment;
      }
    },
    select_pay(order) {
      this.pay_order = order;
    },
    get_status(status) {
      if (status == "1") {
        api_pos.get("order/today/on-going").then((response) => {
          this.all_order = response.data;
        });
      }
      if (status == "2") {
        api_pos.get("order/today/unpaid").then((response) => {
          this.all_order = response.data;
        });
      }
      if (status == "3") {
        api_pos.get("order/today/completed").then((response) => {
          this.all_order = response.data;
        });
      }
      if (status == "4") {
        api_pos.get("order/today/void").then((response) => {
          this.all_order = response.data;
        });
      }
      if (status == "5") {
        api_pos.get("order/today/").then((response) => {
          this.all_order = response.data;
        });
      }
    },
    select_status(status) {
      if (status == "on_going") {
        this.selected_status = "1";
        api_pos.get("order/today/on-going").then((response) => {
          this.all_order = response.data;
        });
      }
      if (status == "unpaid") {
        this.selected_status = "2";
        api_pos.get("order/today/unpaid").then((response) => {
          this.all_order = response.data;
        });
      }
      if (status == "completed") {
        this.selected_status = "3";
        api_pos.get("order/today/completed").then((response) => {
          this.all_order = response.data;
        });
      }
      if (status == "void") {
        this.selected_status = "4";
        api_pos.get("order/today/void").then((response) => {
          this.all_order = response.data;
        });
      }
      if (status == "all") {
        this.selected_status = "all";
        api_pos.get("order/today/").then((response) => {
          this.all_order = response.data;
        });
      }
    },
    change_status(i) {
      this.pay_order.payment_status = i;
    },
    update_order() {
      if (this.pay_order.customer != null) {
        this.pay_order.customer_id = this.pay_order.customer.id;
      } else {
        this.pay_order.customer_id = null;
      }
      api_pos
        .put("order/" + this.pay_order.id + "/", this.pay_order)
        .then(() => {
          this.select_status(this.selected_status);
        });
    },
    re_order(reason) {
      console.log(reason);
      this.$store.dispatch("pos/re_order", this.selected_cancel);
    },
    cancel_order(reason) {
      api_pos
        .put("order/cancel/" + this.selected_cancel.id + "/", reason)
        .then(() => {
          this.select_status(this.selected_status);
          this.selected_cancel = null;
        });
    },
  },
};
</script>

<style scoped>
.btn-gray {
  padding: 10px 24px;
  opacity: 0.5;
  height: 50px;
}
.g-act {
  opacity: 1;
  color: #fff;
}
.col-12 {
  justify-content: space-between;
  margin: 10px 0px;
}
.finish {
}
div {
  white-space: nowrap;
  /* line-height: 30px; */
}
.table-header .row div {
  text-align: center;
  width: 100%;
}
.col-1 {
  width: 100%;
}
.col-2 {
  width: 100%;
}
.col-3 {
  width: 100%;
}
.col-4 {
  width: 100%;
}
.col-5 {
  width: 100%;
}
.col-6 {
  width: 100%;
}
#sale_channel {
  object-fit: cover;
  border-radius: 7px;
}
.col-7 {
  width: 100%;
}
.col-8 {
  width: 100%;
}
.status {
  width: 69px;
  height: 30px;
  background: #fff500;
  line-height: 30px;
  color: #000;
  border-radius: 70px;
  font-weight: bold;
  font-size: 20px;
}
.payment {
  width: 85px;
  height: 30px;
  background: #fff500;
  line-height: 30px;
  color: #000;
  border-radius: 10px;
  font-weight: bold;
  margin-top: 2px;
  font-size: 20px;
}
.cooking {
  background-color: #ff7ca3 !important;
}
.paid {
  background-color: #50d1aa !important;
}
.none {
  background-color: #717171 !important;
}
.serve {
  background-color: #FFB572 !important;
}
</style>