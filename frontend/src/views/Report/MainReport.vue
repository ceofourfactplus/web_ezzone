<template>
  <div>
    <nav-app :url_name="'SelectReport'"
      ><span style="text-transform: capitalize">{{ $route.params.type }}</span>
      Report</nav-app
    >
    <div class="row" style="width: 85%; margin: auto">
      <div class="col-12 w-100 header" style="display: flex">
        <h1>Total Balance Report</h1>
        <select v-model="day" @change="select_date()">
          <option value="1">Monday</option>
          <option value="2">Tuesday</option>
          <option value="3">Wednesday</option>
          <option value="4">Thursday</option>
          <option value="5">Friday</option>
          <option value="6">Saturday</option>
          <option value="0">Sunday</option>
        </select>
      </div>
      <div
        class="col-12 mt-2"
        style="background-color: #303344; border-radius: 10px; padding: 0px"
      >
        <div class="row w-100">
          <div class="col-9 w-100" style="height: 240px">
            <div
              class="row border-y"
              style="
                height: 200px;
                width: 97%;
                margin: 20px 0px 20px 12px;
                border-right: 5px solid #73e4c2;
              "
            >
              <div class="col-12" style="display: inline">
                <div class="total-balance">
                  <img
                    src="../../assets/icon/wallet-mini.png"
                    style="vertical-align: text-bottom"
                  />
                  {{ check_value(report.total_balance__sum) }} ฿
                </div>
                <br />
                <span class="total-balance-title">Total Balance</span>
              </div>
              <div class="col-6 h-100 w-100">
                <img
                  src="../../assets/icon/counter.png"
                  style="vertical-align: bottom"
                />
                <span class="total-mini"
                  >{{ check_value(report.total_cash) }} ฿</span
                >
                <br />
                <span class="mini-title">Cash Drawer</span>
              </div>
              <div class="col-6 h-100 w-100" style="margin-top: 25px">
                <img src="../../assets/icon/viza.png" alt="" />
                <span class="total-mini"
                  >{{ check_value(report.total_transfer) }} ฿</span
                >
                <br />
                <span class="mini-title">Transfer Amount</span>
              </div>
            </div>
          </div>
          <div class="col-3 w-100" style="height: 240px; padding: 0px">
            <div style="height: 200px; width: 95%; margin: 20px auto">
              <div class="w-100 h-50" style="left: -5px; position: relative">
                <img src="../../assets/icon/order-bill.png" alt="" />
                <span class="total-mini">{{
                  check_value(report.total_order)
                }}</span>
                <br />
                <span class="mini-title">Total Order</span>
              </div>
              <div class="w-100 h-50" style="left: -5px; position: relative">
                <img src="../../assets/icon/customer-icon.png" alt="" />
                <span class="total-mini">{{
                  check_value(report.total_customer)
                }}</span>
                <br />
                <span class="mini-title">Total Customer</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-3 p-1 header">Channel</div>
      <div class="col-6 p-1 header">Cost</div>
      <div class="col-3 p-1 header">Best Seller</div>
      <div class="col-3 space">
        <div
          class="w-100 mb-3"
          style="text-align: left"
          v-for="(channel, index) in report.sale_channel_total_price"
          :key="index"
        >
          <img
            style="
              width: 40px;
              height: 40px;
              object-fit: cover;
              border-radius: 10px;
            "
            :src="channel.sale_channel_set.img"
          /><span class="mini-title ms-2">{{
            check_value(channel.total_price)
          }}</span>
        </div>
      </div>
      <div class="col-6 space">
        <div class="row" style="text-align: left">
          <div
            class="col-12 total-mini mt-1"
            style="display: inline; margin-left: 0px"
          >
            <img
              src="../../assets/icon/gift.png"
              style="padding-left: 20px"
              alt=""
            />
            Promotion
            <br />
            <div class="total-mini" style="text-align: center">1,123</div>
          </div>
          <div
            class="col-12 total-mini mt-3"
            style="display: inline; margin-left: 0px"
          >
            <img
              src="../../assets/icon/raw_material_total.png"
              style="padding-left: 20px"
            />
            Raw Material
            <br />
            <div class="total-mini" style="text-align: center">1,123</div>
          </div>
          <div
            class="col-12 total-mini mt-3"
            style="display: inline; margin-left: 0px"
          >
            <img
              src="../../assets/icon/employee.png"
              style="padding-left: 20px"
              alt=""
            />
            Employee
            <br />
            <div class="total-mini" style="text-align: center">0</div>
          </div>
        </div>
        <div class="w-100 total-mini" style="display: inline"></div>
      </div>
      <div class="col-3 space">
        <div class="w-100 mini-title mb-2">
          <img src="../../assets/icon/top-drink.png" alt="" />
          Drink
        </div>
        <div
          class="w-100 list"
          v-for="(product, index) in report.top_drink"
          :key="product.id"
        >
          {{ index + 1 }}. {{ product.name }}
        </div>
        <div class="w-100 mini-title mb-2 mt-3">
          <img src="../../assets/icon/top-drink.png" alt="" />
          Food
        </div>
        <div
          class="w-100 list"
          v-for="(product, index) in report.top_food"
          :key="product.id"
        >
          {{ index + 1 }}. {{ product.name }}
        </div>
        <div class="w-100 mini-title mb-2 mt-3">
          <img src="../../assets/icon/top-drink.png" alt="" />
          Dressert
        </div>
        <div
          class="w-100 list"
          v-for="(product, index) in report.top_dressert"
          :key="product.id"
        >
          {{ index + 1 }}. {{ product.name }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_pos } from "../../api/api_pos";
import NavApp from "../../components/main_component/NavApp.vue";
export default {
  components: { NavApp },
  mounted() {
    var dateObj = new Date();
    var month = dateObj.getUTCMonth() + 1;
    var day = dateObj.getUTCDate();
    var year = dateObj.getUTCFullYear();
    this.day = dateObj.getDay();
    api_pos
      .get("report/daily/" + year + "/" + month + "/" + day)
      .then((response) => {
        this.report = response.data;
      });
  },
  data() {
    return {
      report: {},
      day: 0,
    };
  },
  methods: {
    check_value(value) {
      if (value == null) {
        return 0;
      }
      return value;
    },
    select_date() {
      var getDaysArray = function (s, e) {
        for (var a = [], d = new Date(s); d <= e; d.setDate(d.getDate() + 1)) {
          a.push(new Date(d));
        }
        return a;
      };

      Date.prototype.backDays = function (days) {
        var date = new Date(this.valueOf());
        date.setDate(date.getDate() - days);
        return date;
      };

      var dateObj = new Date();
      var next_week = new Date().backDays(7);
      var range_date = getDaysArray(next_week, dateObj);

      for (const date of range_date) {
        if (date.getDay() == this.day) {
          console.log(date);
        }
      }
      
    },
  },
};
</script>

<style scoped>
h1 {
  color: #fff;
  margin: auto;
  font-weight: bold;
  font-size: 36px;
  margin-bottom: 0px;
  line-height: 48px;
  margin-left: 20px;
  margin-top: -9px;
}
.header {
  background-color: #bd523f;
  height: 55px;
  border-radius: 10px;
  font-weight: bold;
  font-size: 24px;
  color: #ffffff;
  line-height: 45px;
  white-space: nowrap;
  padding-top: 8px;
}
select {
  width: 175px;
  height: 40px;
  background-color: #717171;
  margin-right: -4px;
}
.row .header {
  width: 95%;
  margin: auto;
  margin-top: 10px;
}
.row .col-6 {
  margin: auto;
  margin-top: 10px;
}
.row .space {
  width: 95%;
  margin: auto;
  background-color: #303344;
  margin-top: 10px;
  height: 445px;
  border-radius: 10px;
  padding-top: 10px;
}
.border-y {
  border-left: 5px solid yellow;
}
.total-balance {
  font-weight: bold;
  font-size: 36px;
  color: #fff;
  margin-left: 10px;
  display: inline;
}
.total-balance-title {
  font-size: 30px;
  color: #fff;
  white-space: nowrap;
}
.total-mini {
  font-weight: bold;
  font-size: 24px;
  color: #fff;
  margin-left: 10px;
}
.mini-title {
  font-size: 23px;
  color: #fff;
  white-space: nowrap;
}
.list {
  font-weight: bold;
  font-size: 18px;
  color: #fff;
  text-align: left;
}
.total-mini img {
  margin-right: 10px;
}
img {
  vertical-align: top;
}
</style>