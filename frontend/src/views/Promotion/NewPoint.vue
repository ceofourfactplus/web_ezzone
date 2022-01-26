<template>
  <div>
    <nav-app :url_name="'Promotion'" :save="true" @save="save">New Point</nav-app>
    <div class="card-content">
      <div class="row">
        <!-- Left -->
        <div class="col-5 w-100">
          <div
            class="col-12 w-100 txt-promotion"
            style="font-size: 36px; font-weight: bold"
          >
            Type
          </div>
          <div class="col-12 w-100 txt-promotion">Start Date</div>
          <div class="col-12 w-100 txt-promotion">End Date</div>
          <div class="col-12 w-100 txt-promotion">End Redeem</div>
          <div class="col-12 w-100 txt-promotion">Price / Point</div>
          <div class="col-12 w-100 txt-promotion">Point</div>
          <div class="col-12 w-100 txt-promotion">Status</div>
        </div>
        <!-- Middle -->
        <div class="col-1 w-100">
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
          <div class="col-12 w-100 colon">:</div>
        </div>
        <!-- Right -->
        <div class="col-6 w-100">
          <div
            class="col-12 w-100"
            id="txt-right-side"
            style="font-size: 36px; font-weight: bold;"
          >
            <input
              type="text"
              style="width: 200px;"
              class="input-promotion"
              placeholder="Name"
              v-model="promotion"
            />
          </div>
          <div class="col-12 w-100" id="txt-right-side" >
            {{ temp_start }}
            <input
              type="date"
              class="input-date"
              style="margin-top:7px"
              @change="format_date($event, 'start')"
            />
          </div>
          <div class="col-12 w-100" id="txt-right-side" >
            {{ temp_end }}
            <input
              type="date"
              class="input-date"
              style="margin-top:7px"
              @change="format_date($event, 'end')"
            />
          </div>
          <div class="col-12 w-100" id="txt-right-side" >
            {{ temp_end_redeem }}
            <input
              type="date"
              class="input-date"
              style="margin-top:7px"
              @change="format_date($event, 'endredeem')"
            />
          </div>
          <div class="col-12 w-100" id="txt-right-side">
            <input
              type="text"
              class="input-promotion"
              style="width: 82px;"
              v-model="price_per_point"
            />
          </div>
          <div class="col-12 w-100" id="txt-right-side">
            <input
              type="text"
              class="input-promotion"
              style="width: 82px;"
              v-model="point"
            />
          </div>
          <div v-if="!point_promotions.some(x => x.status == true)" class="col-12 w-100" id="txt-right-side">
            <Switch @switch="switch_active" style="margin-top: 10px" />
          </div>
          <div v-else class="col-12 w-100" id="txt-right-side">
            .....
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
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import SavePopup from "../../components/main_component/SavePopup.vue"
import { api_promotion } from "../../api/api_promotion";
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";

export default {
  name: "NewPromotion",
  components: {
    SavePopup,
    NavApp,
    Switch,
  },
  mounted() {
    this.fetchPointPromotion()
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
      point_promotions: [],
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
        point: this.point,
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
    fetchPointPromotion() {
      api_promotion.get("point/").then((response) => {
        console.log(response.data, "res");
        this.point_promotions = response.data;
      });
    },
  },
};
</script>

<style scoped>
.false-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #fff;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

.false-slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: #ccc;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}
.false-slider.false-round {
  border-radius: 34px;
}

.false-slider.false-round:before {
  top: 1px;
  border-radius: 50%;
}

.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 28px;
  margin-top: 8px;
}

.colon {
  height: 55px;
  font-size: 30px;
  text-align: center;
  margin-top: 12px;
  color: white;
}

#txt-right-side {
  height: 55px;
  font-size: 30px;
  color: white;
  margin: 12px 0px 0px 0px;
  text-align: left;
}
.txt-promotion {
  height: 55px;
  font-size: 30px;
  color: white;
  text-align: right;
  margin: 12px 0px 0px 0px;
}
.card-content {
  width: 765px;
  height: 477px;
  background: #303344;
  border-radius: 20px;
  margin: 15px 0px 0px 27px;
}
.input-date {
  width: 30px;
  height: 30px;
  background: white;
  background-image: url("../../assets/icon/calendar.png");
  background-size: 20px 20px;
  background-position: 50% 50%;
  background-repeat: no-repeat;
  position:relative;
  top: 5px;
  margin-top:12px;
  line-height: 10px;
  display: inline-block;
}
</style>