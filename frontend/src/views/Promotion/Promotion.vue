<template>
  <div>
    <nav-app :url_name="'DashBoard'">{{ $store.state.promotion.tab }}</nav-app>
    <!-- Head -->
    <div class="row" style="width94%;margin-left:3%;margin-right:3%;">
      <div class="col-9 w-100 p-0 pe-1">
        <SearchBar @search="search_by_typing" />
      </div>
      <div style="padding: 0px" class="col-3 w-100">
        <button
          v-if="$store.state.promotion.tab == 'Point'"
          class="w-100 btn-ghost"
          style="margin-right: 0%; text-align: center"
          @click="$router.push({ name: 'NewPoint' })"
        >
          + Point
        </button>
        <button
          v-if="$store.state.promotion.tab == 'Voucher'"
          class="w-100 btn-ghost"
          style="margin-right: 0%; text-align: center; padding-left: 8%"
          @click="$router.push({ name: 'NewVoucher' })"
        >
          + Voucher
        </button>
        <button
          v-if="$store.state.promotion.tab == 'Package'"
          class="w-100 btn-ghost"
          style="margin-right: 0%; text-align: center; padding-left: 8%"
          @click="$router.push({ name: 'NewPackage' })"
        >
          + Package
        </button>
        <button
          v-if="$store.state.promotion.tab == 'Rewards'"
          class="w-100 btn-ghost"
          style="margin-right: 0%; text-align: center; padding-left: 10%"
          @click="$router.push({ name: 'NewReward' })"
        >
          + Reward
        </button>
      </div>
    </div>
    <!-- Tabs -->
    <div
      style="width94%;margin-left:3%;margin-right:3%;height: 50px;"
      class="row mt-2"
    >
      <div class="col-12" style="padding: 0%">
        <button
          v-for="(item, idx) in ['Point', 'Voucher', 'Package', 'Rewards']"
          :key="idx"
          @click="select_item(item)"
          style="width: 24.45%; height: 100%"
          class="btn-gray me-1"
          :class="{ 'tab-selected': item == $store.state.promotion.tab }"
        >
          {{ item }}
        </button>
      </div>
    </div>
    <!-- Point Promotion -->
    <div
      style="width: 94%; margin-left: 3%; margin-right: 3%"
      v-if="$store.state.promotion.tab == 'Point'"
    >
      <!-- Card Content -->
      <div
        class="card-content"
        style="width100%;margin-left:0%;margin-right:0%;"
        v-for="item in point_promotions"
        :key="item.id"
      >
        <div class="row" style="width100%;margin:0%">
          <div
            class="col-8 w-100"
            style="
              font-size: 48px;
              color: #ea7c69;
              font-weight: bold;
              margin-left: 15px;
              text-align: left;
            "
          >
            {{ item.promotion }}&nbsp;&nbsp;&nbsp;
          </div>
          <div class="col-4 w-100">
            <SmallSwitch
              :value="item.status"
              @switch="change_status(item)"
              style="margin: 25px 0px 0px 80px"
            />
          </div>
        </div>

        <div class="row" style="line-height: 110px;width100%;margin:0%;">
          <div
            v-if="!used_point_promotions_id.includes(item.id)"
            class="col-2 w-100"
            style="margin-left: 15px"
            @click="delete_confirm(item)"
          >
            <img
              src="../../assets/icon/gold-bin.png"
              style="width: 64px; height: 64px"
            />
          </div>
          <div class="col-2 w-100" style="margin-left: 15px" v-else></div>
          <div class="col-1 w-100">
            <img
              src="../../assets/icon/edit.png"
              style="width: 53px; height: 64px"
              @click="
                $router.push({ name: 'PointDetail', params: { id: item.id } })
              "
            />
          </div>
          <div class="col-4 w-100"></div>
          <div
            class="col-3 w-100"
            style="
              font-size: 100px;
              font-weight: bold;
              color: white;
              text-align: right;
              margin-left: -20px;
            "
          >
            {{ item.price_per_point }}
          </div>
          <div
            class="col-2 w-100"
            style="
              min-width: 126px;
              font-size: 30px;
              font-weight: bold;
              color: #ffb572;
              line-height: 56px;
              position: relative;
              right: 23px;
            "
          >
            Baht <br />
            /&nbsp;{{ item.point }}
            <img
              src="../../assets/icon/point_star.png"
              style="width: 40px; height: 40px; margin-bottom: 5px"
            />
          </div>
        </div>
        <div class="row" style="margin-top: 10px">
          <div class="col-4 w-100">
            <div class="col-12 w-100" style="font-size: 24px; color: white">
              Start Date
            </div>
            <div
              class="col-12 w-100"
              style="font-size: 28px; color: white; margin-top: 15px"
            >
              {{ format_date(item.start_promotion_date) }}
            </div>
          </div>
          <div class="col-4 w-100">
            <div class="col-12 w-100" style="font-size: 24px; color: white">
              End Date
            </div>
            <div
              class="col-12 w-100"
              style="font-size: 28px; color: white; margin-top: 15px"
            >
              {{ format_date(item.end_promotion_date) }}
            </div>
          </div>
          <div class="col-4 w-100">
            <div class="col-12 w-100" style="font-size: 24px; color: white">
              End Redeem
            </div>
            <div
              class="col-12 w-100"
              style="font-size: 28px; color: white; margin-top: 15px"
            >
              {{ format_date(item.end_reward_redemption) }}
            </div>
          </div>
        </div>
      </div>

      <!-- Delete Card -->
      <div class="blur" v-if="delete_status">
        <div class="delete-card" v-if="delete_status">
          <div
            class="row"
            style="font-size: 36px; color: white; margin-top: 30px"
          >
            <div class="col-12 w-100">
              <img src="../../assets/icon/bin.png" /> Are you sure
            </div>
            <div class="col-12 w-100">you want to delete ?</div>
          </div>
          <div class="row" style="margin: 20px 0px 0px -19px">
            <div class="col-1 w-100"></div>
            <div class="col-5 w-100">
              <button class="btn-ghost-cancel" @click="delete_status = false">
                <img src="../../assets/icon/incorrect.png" />
              </button>
            </div>
            <div class="col-5 w-100" @click="delete_point_pro()">
              <button class="btn-ghost-correct">
                <img src="../../assets/icon/correct.png" />
              </button>
            </div>
            <div class="col-1 w-100"></div>
          </div>
        </div>
        <div class="delete-card" v-if="correct_status">
          <img
            src="../../assets/icon/correct.png"
            style="width: 150px; height: 150px; margin-top: 35px"
          />
          <div class="row">
            <div
              class="col-12 w-100"
              style="color: white; font-size: 36px; font-weight: bold"
            >
              Delete successfully
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Voucher -->
    <div
      class="table"
      style="margin-top: 10px; width: 100%"
      v-else-if="$store.state.promotion.tab == 'Voucher'"
    >
      <div
        class="table-header row"
        style="
          width: 94%;
          margin-left: 3%;
          margin-right: 3%;
          font-size: 24px;
          font-weight: bold;
          color: white;
          line-height: 150%;
        "
      >
        <div class="col-4 w-100">Name</div>
        <div class="col-1 w-100">Qty</div>
        <div class="col-2 w-100">Discount</div>
        <div class="col-2 w-100">End</div>
        <div class="col-2 w-100">Status</div>
        <div class="col-1 w-100"></div>
      </div>
      <div
        class="table-item"
        style="width: 94%; margin-left: 3%; margin-right: 3%"
        v-for="voucher in vouchers"
        :key="voucher.id"
      >
        <div class="row" style="font-size: 20px; color: white; line-height: 1">
          <div
            class="col-4 w-100"
            style="
              padding-left: 10%;
              text-align: left;
              white-space: nowrap;
              overflow-x: auto;
            "
          >
            {{ voucher.voucher }}
          </div>
          <div class="col-1 w-100">{{ voucher.qty }}</div>
          <div class="col-2 w-100" v-if="voucher.is_percent">
            {{ format_percent(voucher.discount) }}
          </div>
          <div class="col-2 w-100" v-else>{{ parseInt(voucher.discount) }}</div>
          <div class="col-2 w-100">{{ format_date(voucher.end_date) }}</div>
          <div class="col-2 w-100">
            <SmallSwitch
              :value="voucher.status"
              @switch="switch_active(voucher, 'voucher')"
            />
          </div>
          <div class="col-1 w-100">
            <img
              src="../../assets/icon/edit.png"
              style="width: 23px; height: 30px; margin: -3px 10px 20px 0px"
              @click="
                $router.push({
                  name: 'VoucherDetail',
                  params: { id: voucher.id },
                })
              "
            />
          </div>
        </div>
      </div>
    </div>
    <!-- Package -->
    <div
      class="table"
      style="margin-top: 10px; width: 100%"
      v-else-if="$store.state.promotion.tab == 'Package'"
    >
      <div
        class="table-header row"
        style="
          font-size: 24px;
          font-weight: bold;
          color: white;
          width: 94%;
          margin-left: 3%;
          margin-right: 3%;
          line-height: 150%;
        "
      >
        <div class="col-5 w-100">Name</div>
        <div class="col-2 w-100">Norm.P.</div>
        <div class="col-2 w-100">Disc.P.</div>
        <div class="col-2 w-100">Status</div>
        <div class="col-1 w-100"></div>
      </div>
      <div
        class="table-item"
        style="width: 760px; margin-left: 3%"
        v-for="item in packages"
        :key="item.id"
      >
        <div class="row" style="font-size: 20px; color: white; line-height: 1">
          <div class="col-5 w-100" style="margin-left: 10px; text-align: left">
            {{ item.promotion }}
          </div>
          <div class="col-2 w-100">
            {{ get_price(item).normal_price }}
          </div>
          <div class="col-2 w-100">
            {{ get_price(item).discount_price }}
          </div>

          <div class="col-2 w-100">
            <SmallSwitch
              :value="item.status"
              @switch="switch_active(item, 'package')"
            />
          </div>
          <div class="col-1 w-100">
            <img
              @click="
                $router.push({ name: 'PackageDetail', params: { id: item.id } })
              "
              src="../../assets/icon/edit.png"
              style="width: 23px; height: 30px; margin: -3px 10px 20px 0px"
            />
          </div>
        </div>
      </div>
    </div>
    <!-- Reward -->
    <div class="table" style="margin-top: 10px; width: 100%" v-else>
      <div
        class="table-header row"
        style="
          font-size: 24px;
          font-weight: bold;
          color: white;
          width: 94%;
          margin-left: 3%;
          margin-right: 3%;
          line-height: 150%;
        "
      >
        <div class="col-5 w-100">Name</div>
        <div class="col-2 w-100">Point</div>
        <div class="col-2 w-100">Qty</div>
        <div class="col-2 w-100">Status</div>
        <div class="col-1 w-100"></div>
      </div>

      <div
        class="table-item row"
        style="
          width: 94%;
          margin-left: 3%;
          margin-right: 3%;
          font-size: 20px;
          color: white;
          line-height: 180%;
        "
        v-for="reward in rewards"
        :key="reward.id"
      >
        <div class="col-5 w-100" style="margin-left: 10px; text-align: left">
          {{ reward.reward }}
        </div>
        <div class="col-2 w-100">{{ reward.point }}</div>
        <div class="col-2 w-100">{{ reward.qty }}</div>
        <div class="col-2 w-100">
          <SmallSwitch
            :value="reward.status"
            @switch="switch_active(reward, 'reward')"
          />
        </div>
        <div class="col-1 w-100">
          <img
            @click="
              $router.push({
                name: 'RewardDetail',
                params: { id: reward.id },
              })
            "
            src="../../assets/icon/edit.png"
            style="width: 95%; height: 80%; margin-top: -5%"
          />
        </div>
      </div>
    </div>

    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import SavePopup from "../../components/main_component/SavePopup.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import SmallSwitch from "../../components/main_component/SmallSwitch.vue";
import { api_promotion } from "../../api/api_promotion";

export default {
  name: "Point",
  components: {
    SearchBar,
    NavApp,
    Switch,
    SavePopup,
    SmallSwitch,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
  },
  data() {
    return {
      delete_status: false,
      correct_status: false,
      is_staff: false,
      alert: false,
      point_item: {},
      used_point_promotions_id: [],
      point_promotions: [],
      temp_point_promotions: [],
      vouchers: [],
      temp_vouchers: [],
      packages: [],
      temp_packages: [],
      rewards: [],
      temp_rewards: [],
    };
  },
  methods: {
    change_status(item) {
      console.log(item, "item");
      if (item.status) {
        item.status = false;
        const data = { status: item.status };
        api_promotion.put(`point/${item.id}`, data).then(() => {});
      } else {
        if (!this.point_promotions.some((x) => x.status == true)) {
          item.status = true;
          const data = { status: item.status };
          api_promotion.put(`point/${item.id}`, data).then(() => {});
        }
      }
    },
    switch_active(item, promotion) {
      item.status = !item.status;
      const data = new FormData();
      data.append("status", item.status);
      api_promotion.put(`${promotion}/${item.id}`, data).then(() => {});
    },
    select_item(item) {
      this.$store.state.promotion.tab = item;
    },
    get_price(item) {
      if (item.pricepackage_set.length > 0) {
        return item.pricepackage_set.filter((i) => {
          return i.sale_channel == this.$store.state.ezzone_id;
        })[0];
      } else {
        return { discount_price: 0, normal_price: 0 };
      }
    },
    search_by_typing(txt) {
      var temp = [];
      if (txt == "") {
        if (this.$store.state.promotion.tab == "Point") {
          this.point_promotions = this.temp_point_promotions;
        }
        if (this.$store.state.promotion.tab == "Voucher") {
          this.vouchers = this.temp_vouchers;
        }
        if (this.$store.state.promotion.tab == "Package") {
          this.packages = this.temp_packages;
        }
        if (this.$store.state.promotion.tab == "Rewards") {
          this.rewards = this.temp_rewards;
        }
      } else {
        if (this.$store.state.promotion.tab == "Point") {
          this.temp_point_promotions.forEach((element) => {
            if (element.promotion.indexOf(txt) + 1 != 0) {
              temp.push(element);
            }
          });
          this.point_promotions = temp;
        }
        if (this.$store.state.promotion.tab == "Voucher") {
          this.temp_vouchers.forEach((element) => {
            if (element.voucher.indexOf(txt) + 1 != 0) {
              temp.push(element);
            }
          });
          this.vouchers = temp;
        }
        if (this.$store.state.promotion.tab == "Package") {
          this.temp_packages.forEach((element) => {
            if (element.promotion.indexOf(txt) + 1 != 0) {
              temp.push(element);
            }
          });
          this.packages = temp;
        }
        if (this.$store.state.promotion.tab == "Rewards") {
          this.temp_rewards.forEach((element) => {
            if (element.reward.indexOf(txt) + 1 != 0) {
              temp.push(element);
            }
          });
          this.rewards = temp;
        }
      }
    },
    fetchPackage() {
      api_promotion.get("package/").then((response) => {
        console.log(response.data, "package");
        this.packages = response.data;
        this.temp_packages = response.data;
      });
    },
    fetchRewards() {
      api_promotion.get("reward/").then((response) => {
        console.log(response.data, "rewards");
        this.rewards = response.data;
        this.temp_rewards = response.data;
      });
    },
    fetchVoucher() {
      api_promotion.get("voucher/").then((response) => {
        this.vouchers = response.data;
        this.temp_vouchers = response.data;
        console.log(response.data, "voucher");
      });
    },
    fetchPointPromotion() {
      api_promotion.get("point/").then((response) => {
        console.log(response.data, "res");
        this.point_promotions = response.data;
        this.temp_point_promotions = response.data;
      });
      api_promotion.get("customer-point/").then((response) => {
        this.used_point_promotions_id = response.data.map(
          (x) => x.point_promotion_id
        );
      });
    },
    format_date(date) {
      var temp_date = date.split("-");
      return `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
    },
    format_percent(discount) {
      var temp = discount.split(".");
      return `${temp[0]}%`;
    },
    delete_confirm(item) {
      console.log(item, "item");
      this.point_item = item;
      this.delete_status = true;
    },
    delete_point_pro() {
      api_promotion.delete(`point/${this.point_item.id}`).then(() => {
        this.correct_status = true;
        setTimeout(() => {
          this.correct_status = false;
          this.delete_status = false;
        }, 1000);
      });
    },
  },
  mounted() {
    this.fetchPointPromotion();
    this.fetchVoucher();
    this.fetchPackage();
    this.fetchRewards();
  },
};
</script>

<style scoped>
.btn-ghost-cancel {
  background: transparent;
  border-color: #ff7ca3;
  color: #ff7ca3;
  width: 180px;
  height: 56px;
  border-radius: 10px;
}
.btn-ghost-correct {
  background: transparent;
  border-color: #50d1aa;
  color: #50d1aa;
  width: 180px;
  height: 56px;
  border-radius: 10px;
}
.delete-card {
  width: 440px;
  height: 280px;
  background: #252836;
  border: 2px solid #ea7c69;
  border-radius: 15.5833px;
  position: absolute;
  top: 25%;
  left: 20%;
}
.card-content {
  width: 765px;
  height: 304px;
  background: #303344;
  border-radius: 20px;
  margin: 10px 0px 0px 25px;
}
.tab-selected {
  color: white;
}
.btn-ghost {
  border-color: #50d1aa;
  color: #50d1aa;
  width: 133px;
  height: 45px;
  margin: 0px 35px 0px 0px;
  white-space: nowrap;
}
.wrap-search {
  min-width: 610px;
  width: fit-content;
  padding: 0%;
  margin: 0%;
}
.tab {
  width: 100%;
  height: 46px;
  margin: auto;
}

.tab-item {
  background-color: #2f3446;
  color: gray;
  border: none;
  outline: none;
  cursor: pointer;
  padding-top: 6px;
  transition: 0.3s;
  font-size: 26.5px;
  font-style: normal;
  border-radius: 15px 15px 0px 0px;
  margin-top: 0px;
  margin-bottom: 1em;
  height: 59px;
  width: 150px;
  block-size: fit-content;
  text-decoration: none;
  line-height: 31px;
}
</style>