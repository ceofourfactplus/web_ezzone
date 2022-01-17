<template>
  <div>
    <nav-app :url_name="'Promotion'" :save="true" @save="save">New Point</nav-app>
    <div class="card-content">
      <div class="row">
        <!-- Left -->
        <div class="col-6 w-100">
          <div
            class="col-12 w-100 txt-promotion"
            style="font-size: 36px; font-weight: bold"
          >
            Type
          </div>
          <div class="col-12 w-100 txt-promotion">Start Date</div>
          <div class="col-12 w-100 txt-promotion">End Date</div>
          <div class="col-12 w-100 txt-promotion">End Redeem</div>
          <div class="col-12 w-100 txt-promotion">Price per Point</div>
          <div class="col-12 w-100 txt-promotion">Status</div>
        </div>
        <!-- Middle -->
        <div class="col-1 w-100" style="margin-top: -4px; margin-left: -40px;">
          <div
            class="col-12 w-100 colon"
            style="font-size: 36px; font-weight: bold"
          >
            :
          </div>
          <div class="col-12 w-100 colon">:</div>
          <div class="col-12 w-100 colon">:</div>
          <div class="col-12 w-100 colon">:</div>
          <div class="col-12 w-100 colon">:</div>
          <div class="col-12 w-100 colon">:</div>
        </div>
        <!-- Right -->
        <div class="col-5 w-100" style="margin-left: -40px;">
          <div
            class="col-12 w-100 txt-promotion"
            style="font-size: 36px; font-weight: bold; margin-left: -20px"
          >
            <input
              type="text"
              style="width: 200px"
              class="input-promotion"
              placeholder="Name"
              v-model="promotion"
            />
          </div>
          <div class="col-12 w-100 txt-promotion" id="txt-right-side">
            {{ temp_start }}
            <input
              type="date"
              class="input-date"
              @change="format_date($event, 'start')"
            />
          </div>
          <div class="col-12 w-100 txt-promotion" id="txt-right-side">
            {{ temp_end }}
            <input
              type="date"
              class="input-date"
              @change="format_date($event, 'end')"
            />
          </div>
          <div class="col-12 w-100 txt-promotion" id="txt-right-side">
            {{ temp_end_redeem }}
            <input
              type="date"
              class="input-date"
              @change="format_date($event, 'endredeem')"
            />
          </div>
          <div class="col-12 w-100 txt-promotion" id="txt-right-side">
            <input
              type="text"
              class="input-promotion"
              style="width: 82px;"
              v-model="price_per_point"
            />
          </div>
          <div class="col-12 w-100 txt-promotion" id="txt-right-side">
            <Switch @switch="switch_active" style="margin-top: 7px" />
          </div>
        </div>
      </div>
    </div>
    <div class="description-card">
      <div class="row">
        <div
          class="col-12 w-100"
          style="
            color: white;
            font-size: 30px;
            text-align: left;
            margin: 10px 0px 10px 20px;
          "
        >
          Description :
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <textarea
            style="width: 600px; height: 80px; background: #717171"
            v-model="description"
          ></textarea>
        </div>
      </div>
    </div>
    <!-- Card Popup -->
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img
          src="../../assets/icon/btn-pass.png"
          style="width: 150px; height: 150px"
        />
      </div>
      <div class="main-text">Saved successfully</div>
    </div>
  </div>
</template>

<script>
import { api_promotion } from "../../api/api_promotion";
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";

export default {
  name: "NewPromotion",
  components: {
    NavApp,
    Switch,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
  },
  data() {
    return {
      is_staff: false,
      alert: false,
      promotion: null,
      start_promotion_date: null,
      temp_start: null,
      end_promotion_date: null,
      temp_end: null,
      end_reward_redemption: null,
      temp_end_redeem: null,
      price_per_point: null,
      point: 1,
      status: true,
      description: null,
    };
  },
  methods: {
    save() {
      const data = {
        promotion: this.promotion,
        start_promotion_date: this.start_promotion_date,
        end_promotion_date: this.end_promotion_date,
        end_reward_redemption: this.end_reward_redemption,
        price_per_point: this.price_per_point,
        point: 1,
        status: this.status,
        description: this.description,
        create_by_id: this.$store.state.auth.userInfo.id,
        update_by_id: this.$store.state.auth.userInfo.id,
      }
      api_promotion.post('point/', data).then((response) => {
        console.log(response.data)
        this.alert = true;
        setTimeout(() => {
          this.alert = false;
          this.$router.push({ name: "Promotion" });
        }, 2000);
      })
      
    },
    format_date(e, name) {
      if (name == "start") {
        this.start_promotion_date = e.target.value
        var temp_date = e.target.value.split("-");
        this.temp_start = `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
      }
      if (name == "end") {
        this.end_promotion_date = e.target.value
        var temp_date = e.target.value.split("-");
        this.temp_end = `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
      }
      if (name == "endredeem") {
        this.end_reward_redemption = e.target.value
        var temp_date = e.target.value.split("-");
        this.temp_end_redeem = `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
      }
    },
    switch_active(val) {
      this.status = val
    },
  },
};
</script>

<style scoped>
.colon {
  font-size: 30px;
  text-align: center;
  margin-top: 12px;
  color: white;
}

#txt-right-side {
  height: 45px;
  margin: 12px 0px 0px -20px;
  font-size: 24px;
  font-weight: normal;
}
.txt-promotion {
  font-size: 30px;
  color: white;
  text-align: left;
  margin: 12px 0px 0px 90px;
}
.card-content {
  width: 668px;
  height: 367px;
  background: #303344;
  border-radius: 20px;
  margin: 15px 0px 0px 27px;
}
</style>