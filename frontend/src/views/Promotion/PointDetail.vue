<template>
  <div>
    <nav-app :url_name="'Promotion'" :save="true" @save="edit">Point Detail</nav-app>
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
        <div class="col-1 w-100" style="margin-top: -4px; margin-left:-40px;">
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
        <div class="col-5 w-100" style="margin-left:-40px;">
          <div
            class="col-12 w-100 txt-promotion"
            style="font-size: 36px; font-weight: bold; margin-left: -20px"
          >
            <input
              type="text"
              style="width: 200px;"
              class="input-promotion"
              placeholder="Name"
              v-model="point_item.promotion"
            />
          </div>
          <div class="col-12 w-100 txt-promotion" id="txt-right-side">
            {{ format_date_show(point_item.start_promotion_date) }}
            <input
              type="date"
              class="input-date"
              @change="format_date($event, 'start')"
            />
          </div>
          <div class="col-12 w-100 txt-promotion" id="txt-right-side">
            {{ format_date_show(point_item.end_promotion_date) }}
            <input
              type="date"
              class="input-date"
              @change="format_date($event, 'end')"
            />
          </div>
          <div class="col-12 w-100 txt-promotion" id="txt-right-side">
            {{ format_date_show(point_item.end_reward_redemption) }}
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
              v-model="point_item.price_per_point"
            />
          </div>
          <div class="col-12 w-100 txt-promotion" id="txt-right-side">
            <Switch :value="point_item.status" style="margin-top: 7px" />
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
            margin-left: 34px;
          "
        >
          Description :
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <textarea
            style="width: 600px; height: 80px; background: #717171"
            v-model="point_item.description"
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
  name: "EditPoint",
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
      point_item: null,
    };
  },
  methods: {
    fetchPointPromotion() {
        api_promotion.get(`point/${this.$route.params.id}`).then((response) => {
            console.log(response.data)
            this.point_item = response.data
        })
    },
    edit() {
      api_promotion.put('point/', this.point_item).then((response) => {
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
        this.point_item.start_promotion_date = e.target.value
        var temp_date = e.target.value.split("-");
        this.temp_start = `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
      }
      if (name == "end") {
        this.point_item.end_promotion_date = e.target.value
        var temp_date = e.target.value.split("-");
        this.temp_end = `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
      }
      if (name == "endredeem") {
        this.point_item.end_reward_redemption = e.target.value
        var temp_date = e.target.value.split("-");
        this.temp_end_redeem = `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
      }
    },
    format_date_show(date) {
        var temp_date = date.split("-");
        return `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
    },
  },
  beforeMount() {
    this.fetchPointPromotion();
  },
};
</script>

<style scoped>
.input-date {
  width: 30px;
  height: 30px;
  background: white;
  background-image: url("../../assets/icon/calendar.png");
  background-size: 20px 20px;
  background-position: 50% 50%;
  background-repeat: no-repeat;
}
.colon {
  font-size: 30px;
  text-align: center;
  margin-top: 12px;
  color: white;
}
.input-right-side {
  width: 82px;
  height: 39px;
  background: #717171;
  border-radius: 5px;
  color: white;
}
#txt-right-side {
  margin-left: -20px;
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