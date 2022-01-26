<template>
  <div>
    <!-- Head -->
    <nav-app :url_name="'DashBoard'">Database Settings</nav-app>
    <div class="w-100" style="margin: auto">
      <!-- Content -->
      <div class="content">
        <!-- Change Setting -->
        <div class="row w-100" style="margin: 30px 0px 0px 0px">
          <div
            class="col-4 w-100 dbs-font ps-3"
            style="margin-top: 20px; text-align: left"
          >
            Change Setting
          </div>
          <div
            class="col-7 w-100 dbs-font"
            style="margin-top: 20px; padding: 0px"
          >
            <input
              v-model="dbs_item.change"
              type="text"
              style="
                left: 0px;
                width: 254px;
                height: 50px;
                background: #717171;
                display: inline;
              "
            />
            <p style="display: inline; margin-left: 6px">บาท</p>
          </div>
          <div class="col-1 w-100" style="margin-top: 20px">
            <div class="img-wrap">
              <img
                src="../../assets/icon/save.png"
                style="width: 30px; height: 30px; margin-top: 9px"
                @click="save"
              />
            </div>
          </div>
        </div>
        <!-- Change Setting -->
        <div class="row w-100" style="margin: 30px 0px 0px 0px">
          <div
            class="col-4 w-100 dbs-font ps-3"
            style="margin-top: 20px; text-align: left"
          >
            Pretty Cash
          </div>
          <div
            class="col-7 w-100 dbs-font"
            style="margin-top: 20px; padding: 0px"
          >
            <input
              v-model="dbs_item.pretty_cash"
              type="text"
              style="
                left: 0px;
                width: 254px;
                height: 50px;
                background: #717171;
                display: inline;
              "
            />
            <p style="display: inline; margin-left: 6px">บาท</p>
          </div>
          <div class="col-1 w-100" style="margin-top: 20px">
            <div class="img-wrap">
              <img
                src="../../assets/icon/save.png"
                style="width: 30px; height: 30px; margin-top: 9px"
                @click="save"
              />
            </div>
          </div>
        </div>
        <!-- Unit Setting -->
        <div class="row w-100" style="margin: 30px 0px 0px 0px">
          <div class="col-4 w-100 dbs-font ps-3" style="text-align: left">
            Unit Setting
          </div>
          <div class="col-1 w-100">
            <img
              src="../../assets/icon/edit-orange.png"
              style="width: 25px; height: 30px; margin-top: 5px"
              @click="$router.push({ name: 'RMUnit' })"
            />
          </div>
        </div>
      </div>

      <!-- Sale Channel setting -->
      <div class="BlockChannel">
        <!-- Sale Channel Setting -->
        <div class="row" id="Setting" style="margin-bottom: 5px">
          <div class="col-6 w-100 dbs-font">Sale Channel Setting</div>
          <div class="col-1 w-100">
            <img
              src="../../assets/icon/edit-orange.png"
              style="width: 25px; height: 30px; margin-top: -10px"
              @click="$router.push({ name: 'SaleChannel' })"
            />
          </div>
        </div>
        <div class="w-100" style="height: 140px; overflow-y: auto">
          <!-- Sale Channel 1 -->
          <div class="row w-100" style="margin: 0px">
            <div
              class="col-6 w-100"
              v-for="channel in channels"
              :key="channel.id"
            >
              <div class="row w-100" style="margin: 0px">
                <div class="col-3 w-100">
                  <img
                    :src="channel.img"
                    style="
                      display: inline;
                      width: 35px;
                      height: 35px;
                      object-fit: cover;
                      border-radius: 10px;
                    "
                  />
                </div>
                <div class="col-6 w-100" style="padding: 0px; text-align: left">
                  <p id="TextSaleChannel">{{ channel.sale_channel }}</p>
                </div>
                <div class="col-3 w-100" style="padding: 0px">
                  <div
                    v-if="channel.status"
                    class="sc-status"
                    style="
                      font-size: 12px;
                      line-height: 42px;
                      margin: 0px;
                      font-weight: bold;
                    "
                  >
                    ACTIVE
                  </div>
                  <div
                    v-else
                    class="r-status"
                    style="
                      font-size: 12px;
                      line-height: 42px;
                      margin: 0px;
                      font-weight: bold;
                    "
                  >
                    INACTIVE
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Payment Channel setting -->
      <div class="BlockChannel">
        <!-- Payment Channel Setting -->
        <div class="row" id="Setting" style="margin-bottom: 10px">
          <div class="col-7 w-100 dbs-font">Payment Channel Setting</div>
          <div class="col-1 w-100">
            <img
              src="../../assets/icon/edit-orange.png"
              style="width: 25px; height: 30px; margin-top: -9px"
              @click="$router.push({ name: 'Payments' })"
            />
          </div>
        </div>
        <!-- Payment Channel 1 -->
        <div class="w-100" style="height: 140px; overflow-y: auto">
          <div class="row w-100" style="margin: 0px">
            <div
              class="col-6 w-100 mb-2"
              v-for="payment in payments"
              :key="payment.id"
            >
              <div class="row w-100" style="margin: 0px">
                <div class="col-3 w-100">
                  <img
                    :src="payment.img"
                    style="
                      display: inline;
                      width: 35px;
                      height: 35px;
                      object-fit: cover;
                      border-radius: 10px;
                    "
                  />
                </div>
                <div
                  class="col-6 w-100"
                  style="padding-left: 0px; text-align: left"
                >
                  <p id="TextSaleChannel">{{ payment.payment }}</p>
                </div>
                <div class="col-3 w-100" style="padding: 0px">
                  <div
                    v-if="payment.is_active"
                    class="sc-status"
                    style="
                      font-size: 12px;
                      line-height: 42px;
                      margin: 0px;
                      font-weight: bold;
                    "
                  >
                    ACTIVE
                  </div>
                  <div
                    v-else
                    class="r-status"
                    style="
                      font-size: 12px;
                      line-height: 42px;
                      margin: 0px;
                      font-weight: bold;
                    "
                  >
                    INACTIVE
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- card pop up -->
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
// import { api_raw_material } from "../../api/api_raw_material";
import Tabs from "../../components/materials/Tabs.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";
import Table from "../../components/main_component/Table.vue";
import PickupPopup from "../../components/materials/PickupPopup.vue";
import SavePopup from "../../components/main_component/SavePopup.vue"
import { api_promotion } from "../../api/api_promotion";
import { api_product } from "../../api/api_product";
import { api_pos } from "../../api/api_pos";

export default {
  components: {
    Tabs,
    SearchBar,
    NavApp,
    Table,
    PickupPopup,
    SavePopup,
  },
  mounted() {
    api_promotion.get("dbs/").then((response) => {
      this.dbs_item = response.data;
    });
    api_product.get("read-sale-channel/").then((response) => {
      this.channels = response.data;
    });
    api_pos.get("payment/").then((response) => {
      this.payments = response.data;
    });
  },

  data() {
    return {
      channels: [],
      payments: [],
      alert: false,
      dbs_item: {
        change: null,
        pretty_cash: null,
      },
    };
  },
  methods: {
    save() {
      api_promotion.post("dbs/", this.dbs_item).then();
      this.alert = true;
      setTimeout(() => {
        this.alert = false;
      }, 2000);
    },
  },
};
</script>

<style scoped>
.r-status {
  width: 80px;
  height: 30px;
  display: inline;
  font-size: 12px;
  background: #ff7ca3;
  border-radius: 50px;
  padding: 4px 8px;
  margin-left: 10px;
}
.sc-status {
  width: 80px;
  height: 30px;
  display: inline;
  font-size: 12px;
  background: #50d1aa;
  border-radius: 50px;
  padding: 4px 8px;
  margin-left: 10px;
}
.dbs-font {
  font-size: 24px;
  color: white;
  font-weight: bold;
}
.img-wrap {
  width: 55px;
  height: 50px;
  border: 1px solid #ea7c69;
  box-sizing: border-box;
  border-radius: 5px;
  background: transparent;
  margin-right: 12px;
}
.content {
  width: 635px;
  height: 290px;
  margin: 20px auto 20px auto;
  background: #303344;
  border-radius: 20px;
}
.BlockChannel {
  width: 635px;
  height: 240px;
  margin: 20px auto 20px auto;
  background: #303344;
  border-radius: 20px;
}

#Setting {
  line-height: 80px;
  text-align: left;
  padding-left: 40px;
  height: 80px;
  margin: 10px auto 20px auto;
}

#SaleBlock {
  padding-left: 5px;
  margin: 10px auto 20px auto;
  position: relative;
  left: 10px;
}

#PaymentBlock {
  padding-left: 5px;
  margin-top: 0px;
  margin-bottom: 20px;
  position: relative;
  left: 20px;
}

#TextSaleChannel {
  display: inline;
  font-size: 24px;
  color: white;
  white-space: nowrap;
}

.IconPayment {
  height: 30px;
  width: 30px;
}
</style>