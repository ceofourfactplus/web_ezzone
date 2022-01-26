<template>
  <div>
    <nav-app :url_name="'Promotion'" :save="true" @save="edit">Point Detail</nav-app>
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
              style="width: 340px;"
              class="input-promotion"
              placeholder="Name"
              v-model="point_item.promotion"
            />
          </div>
          <div class="col-12 w-100" id="txt-right-side">
            {{ format_date_show(point_item.start_promotion_date) }}
            <input
              type="date"
              class="input-date"
              @change="format_date($event, 'start')"
            />
          </div>
          <div class="col-12 w-100" id="txt-right-side">
            {{ format_date_show(point_item.end_promotion_date) }}
            <input
              type="date"
              class="input-date"
              @change="format_date($event, 'end')"
            />
          </div>
          <div class="col-12 w-100" id="txt-right-side">
            {{ format_date_show(point_item.end_reward_redemption) }}
            <input
              type="date"
              class="input-date"
              @change="format_date($event, 'endredeem')"
            />
          </div>
          <div class="col-12 w-100" id="txt-right-side">
            <input
              type="text"
              class="input-promotion"
              style="width: 82px;"
              v-model="point_item.price_per_point"
            />
          </div>
          <div class="col-12 w-100" id="txt-right-side">
            <input
              type="text"
              class="input-promotion"
              style="width: 82px;"
              v-model="point_item.point"
            />
          </div>
          <div class="col-12 w-100" id="txt-right-side">
            <Switch :value="point_item.status" style="margin-top: 10px" />
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
            margin-top: 5px;
          "
        >
          Description :
        </div>
      </div>
      <div class="row">
        <div class="col-12" style="margin-top:17px;">
          <textarea
            style="width: 700px; height: 80px; background: #717171"
            v-model="point_item.description"
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
  name: "EditPoint",
  components: {
    SavePopup,
    NavApp,
    Switch,
  },
  mounted() {
    this.fetchPointPromotions()
  },
  data() {
    return {
      is_staff: false,
      alert: false,
      point_item: null,
      point_promotions: [],
    };
  },
  methods: {
    fetchPointPromotions() {
      api_promotion.get("point/").then((response) => {
        console.log(response.data, "res");
        this.point_promotions = response.data;
      });
    },
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
    change_status(item) {
      if(item.status) {
        item.status = false
      } else {
        if(!this.point_promotions.some(x => x.status == true)) {
          item.status = true
        }
      }
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
  position:relative;
  top: 5px;
  margin-top: 6px;
  display: inline-block;

}
.colon {
  height: 55px;
  font-size: 30px;
  text-align: center;
  margin-top: 12px;
  color: white;
}
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

.input-right-side {
  width: 82px;
  height: 39px;
  background: #717171;
  border-radius: 5px;
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
</style>