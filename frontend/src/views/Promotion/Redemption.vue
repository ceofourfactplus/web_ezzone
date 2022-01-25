<template>
  <div>
    <nav-app :url_name="'DashBoard'" :reward_menu="true">Redemption</nav-app>
    <!-- CustommerPhone Block -->
    <div
      class="row"
      style="
        line-height: 65px;
        border-radius: 10px;
        height: 70px;
        background-color: #303344;
        margin-left: 24px;
        margin-right: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
      "
    >
      <div
        class="col-4 w-100"
        style="font-size: 30px; padding: 0px; text-align: right; color: #ffffff"
      >
        Customer Phone
      </div>
      <div class="input col-8">

        <input type="text" v-model="input_customer" style="background: #717171; border-radius: 10px; width: 408px; height: 50px; margin-top: 10px; line-height: 50px;" />
        <!-- <input type="text" @input="find_customer($event)" :value="phone_number_layout($store.state.promotion.customer.phone_number)" style="background: #717171; border-radius: 10px; width: 408px; height: 50px; margin-top: 10px;" /> -->
        <ul class="selector" :class="{'d-none': selector_customer.length == 0}" v-if="selector_status">
          <li v-for="cus in selector_customer" :key="cus.id">
            <p style="font-size: 24px;" @click="select_customer(cus)"
              >{{ phone_number_layout(cus.phone_number) }} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;{{cus.nick_name}}</p
            >
          </li>
        </ul>
      </div>
    </div>

    <!-- Data Block -->
    <div
      v-if="Object.keys($store.state.promotion.customer).length != 0"
      class="row"
      style="
        line-height: 65px;
        background-color: #303344;
        margin-left: 24px;
        margin-right: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius: 10px;
        height: 245px;
      "
    >
      <!-- Picture Block -->
      <div
        class="col-4"
        style="
          background-color: #ffffff;
          border-radius: 10px;
          height: 200px;
          width: 200px;
          margin: 20px 10px 10px 20px;
          position: relative;
        "
      >
        <!-- <img
            :src="require(`../../../../backend${$store.state.promotion.customer.img}`)"
            style="
                height: 200px;
                width: 200px;
                left: -14px;
                top: -2px;
                position: relative;
            "
        /> -->
      </div>
      <!-- Description Block -->
      <div class="col-8 w-100" style="font-size: 30px; color: #ffffff">
        <!-- Point -->
        <div
          class="row"
          style="height: 68px; margin-top: 20px; line-height: 80px"
        >
          <div class="col-3 w-100" id="ColPoint">Point</div>
          <div class="col-1 w-100" id="DotPoint">:</div>
          <div
            v-if="$store.state.promotion.customer_point.length != 0"
            class="col-5 w-100"
            style="
              height: 64px;
              display: inline-block;
              font-size: 42px;
              line-height: 75px;
              padding-left: 10px;
              text-align: left;
              margin-left: 14px;
            "
          >
            {{ $store.state.promotion.customer_point[0].point }}
            <!-- {{ customer_point.reduce((x, y) => {x.point + y.point}) }} -->
          </div>
          <div
            v-else
            class="col-5 w-100"
            style="
              height: 64px;
              display: inline-block;
              font-size: 42px;
              line-height: 75px;
              padding-left: 10px;
              text-align: left;
              margin-left: 14px;
            "
          >
            0
            <!-- {{ customer_point.reduce((x, y) => {x.point + y.point}) }} -->
          </div>
          <div class="col-3 w-100" id="LinkHistory">
            <p style="color: #65B0F6; text-decoration: underline;" @click="$router.push({ name: 'History'})">History</p>
          </div>
        </div>
        <!-- Name -->
        <div
          class="row"
          style="height: 53px; margin-top: 10px; line-height: 50px"
        >
          <div
            class="col-3 w-100"
            id="ColName"
            style="height: 50px; display: inline-block; text-align: left"
          >
            Name
          </div>
          <div class="col-1 w-100" id="DotName">:</div>
          <div class="col-8 w-100" id="DetailName" style="margin-left: 14px;">
            {{ $store.state.promotion.customer.nick_name }}
          </div>
        </div>
        <!-- Birthdate -->
        <div
          class="row"
          style="height: 53px; margin-top: 10px; line-height: 50px"
        >
          <div class="col-3 w-100" style="padding-left: 14px;" id="ColBirthdate">Birthdate </div>
          <div class="col-1 w-100" style="padding-left: 43px;">:</div>
          <div class="col-8 w-100" id="DetailName">{{ format_date_show($store.state.promotion.customer.birth_date) }}</div>
        </div>
      </div>
    </div>
    <!-- Reward -->
    <div
      v-if="Object.keys($store.state.promotion.customer).length != 0"
      class="col-12"
      style="
        background-color: #303344;
        margin-left: 24px;
        margin-right: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius: 10px;
        height: 455px;
        width: 762px;">
        <!-- header Reward -->
            <div class="col-12 w-100" id="ColHeaderReward">
                <div class="row" 
                style="font-size:30px;
                height:45px;
                padding-top:5px;
                color: #FFFFFF;">
                    <div class="col-3 w-100" style="margin-left:21px;text-align:left;">Reward</div>
                    <div class="col-6 w-100"></div>
                    <div class="col-3 w-100" style="padding-right:0px;"><p style="color: #65B0F6; text-decoration: underline;" @click="$router.push({ name: 'AllReward'})">See All</p></div>
                </div>
            </div>
            
            <div id="ColItemReward">
                <div class="column" v-for="reward in rewards" :key="reward.id">
                  <img @click="see_detail(reward)" :src="reward.img" style="width: 100%; height: 100%; border-radius: 10px;">
                </div>
            </div>            
      </div>
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import InputTel from "../../components/main_component/InputTel.vue";
import { api_customer } from "../../api/api_customer";
import { api_promotion } from "../../api/api_promotion";
;

export default {
  name: "Redemption",
  components: {
    NavApp,
    InputTel,
  },
  data() {
    return {
      CustommerPhone: null,
      input_customer: "",
      temp_date: null,
      selector_status: false,
      selector_customer: [],
      customer_point: [],
      rewards: [],
      temp_rewards: [],
    };
  },
  methods: {
    fetchRewards() {
      api_promotion.get("reward/").then((response) => {
        console.log(response.data, "rewards");
        this.rewards = response.data;
        this.temp_rewards = response.data;
      });
    },
    see_detail(reward) {
        this.$store.state.promotion.reward_detail = reward
        this.$router.push({ name: "RewardName"})
    },
    select_customer(cus) {
      console.log(cus, "cus");
      this.selector_status = false;
      this.$store.state.promotion.customer = cus;
      api_promotion.get(`customer-point/${cus.id}`).then((response) => {
        console.log(response.data,' point')
        this.customer_point = response.data;
        this.$store.state.promotion.customer_point = response.data
      });
        this.input_customer = this.phone_number_layout(cus.phone_number)
        this.format_date_show(cus.birth_date);
    },
    format_date_show(date) {
      var temp_date = date.split("-");
      return `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
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
    find_customer(e) {
      if (e.target.value != "") {
        this.selector_status = true;
        api_customer
          .get("get-customer-by-phone-number/" + e.target.value)
          .then((response) => {
            this.selector_customer = response.data;
          });
      } else {
        this.selector_customer = [];
        this.selector_status = false;
      }
    },
  },
  watch: {
    input_customer(tel) {
      if (tel != "") {
        this.selector_status = true;
        api_customer
          .get("get-customer-by-phone-number/" + tel)
          .then((response) => {
            this.selector_customer = response.data;
          });
      } else {
        this.selector_customer = [];
        this.selector_status = false;
      }
    },
  },
  beforeMount() {
    this.fetchRewards()
  }
};
</script>

<style scoped>
.d-none {
  display: none;
}
.column {
  float: left;
  width: 100px;
  margin: 10px;
  height: 100px; 
  border-radius: 10px;
  background: #717171;
}
.selector {
  margin-top: 10px;
  background-color: #303344;
  position: absolute;
  list-style-type: none;
  border-radius: 0px 0px 10px 10px;
  text-align: left;
  padding-left: 10px;
  min-width: 400px;
  color: #fff;
  font-size: 20px;
  font-weight: 400;
  padding-bottom: 10px;
}
#DotPoint {
  height: 64px;
  display: inline-block;
  padding: 0px;
  text-align: right;
}

#DotName {
  height: 50px;
  display: inline-block;
  padding: 0px;
  text-align: right;
}

#ColPoint {
  height: 64px;
  display: inline-block;
  text-align: left;
}

#ColName {
  height: 50px;
  display: inline-block;
  text-align: left;
}

#ColBirthdate {
  height: 50px;
  display: inline-block;
  padding: 0px;
  text-align: right;
}

#DetailName {
  height: 50px;
  display: inline-block;
  padding-left: 10px;
  text-align: left;
}

#LinkHistory {
  height: 64px;
  display: inline-block;
  line-height: 0px;
  right: 10px;
  font-size: 30px;
  text-align: left;
  position: relative;
}

#ColHeaderReward {
  height: 45px;
  margin-top: 10px;
}

#ColItemReward {
  width: 632px;
  margin-left: 37px;
  margin-top: 25px;
  content: "";
  display: table;
  clear: both;
}

#BlockItem {
  position: relative;
  display: inline-block;
  height: 100px;
  width: 100px;
  border-radius: 10px;
  margin: 5px;
  left: 25px;
  background-color: #717171;
}
</style>