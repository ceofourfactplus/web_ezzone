<template>
  <div>
    <!-- Card Content -->
    <div class="card-content" v-for="item in point_promotions" :key="item.id">
      <div class="row">
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
        <div
          class="col-4 w-100"
          style="margin: 10px 0px 0px -10px"
        >
          <label class="switch">
              <input type="checkbox" v-model="item.status" @input="change_status(item)" />
              <span class="slider round"></span>
          </label>
        </div>
      </div>
      <div class="row" style="line-height: 110px;">
        <div class="col-2 w-100" style="margin-left: 15px;" @click="delete_confirm(item)">
          <img src="../../assets/icon/gold-bin.png" style="width: 64px; height: 64px;">
        </div>
        <div class="col-1 w-100">
          <img src="../../assets/icon/edit.png" style="width: 53px; height: 64px;" @click="$router.push({ name: 'PointDetail', params: { id: item.id } })">
        </div>
        <div class="col-4 w-100"></div>
        <div
          class="col-3 w-100"
          style="
            font-size: 100px;
            font-weight: bold;
            color: white;
          "
        >
          {{ item.price_per_point }}
        </div>
        <div
          class="col-2 w-100"
          style="
            font-size: 30px;
            font-weight: bold;
            color: #FFB572;
            line-height: 56px;
            position: relative;
            right: 23px;
          "
        >
          Baht <br> /Point
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
        <div class="row" style="font-size: 36px; color: white; margin-top: 30px;">
          <div class="col-12 w-100">
            <img src="../../assets/icon/bin.png"> Are you sure
          </div>
          <div class="col-12 w-100">
            you want to delete ?
          </div>
        </div>
        <div class="row" style="margin: 20px 0px 0px -19px;">
          <div class="col-1 w-100"></div>
          <div class="col-5 w-100">
            <button class="btn-ghost-cancel" @click="delete_status = false">
              <img src="../../assets/icon/incorrect.png">
            </button>
          </div>
          <div class="col-5 w-100" @click="delete_point_pro()">
            <button class="btn-ghost-correct">
              <img src="../../assets/icon/correct.png">
            </button>
          </div>
          <div class="col-1 w-100"></div>
        </div>
      </div>
      <div class="delete-card" v-if="correct_status">
        <img src="../../assets/icon/correct.png" style="width: 150px; height: 150px; margin-top: 35px;">
        <div class="row">
          <div class="col-12 w-100" style="color: white; font-size: 36px; font-weight: bold;">
            Delete successfully
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Switch from "../../components/main_component/Switch.vue";
import{ api_promotion } from "../../api/api_promotion"

export default {
  name: "PointComponent",
  props: ["items"],
  components: {
    Switch,
  },
  mounted() {
  },
  data() {
    return {
      delete_status: false,
      correct_status: false,
      point_promotions: this.items,
      point_item: {},
    };
  },
  methods: {
    format_date(date) {
      var temp_date = date.split("-");
      return `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
    },
    change_status(item) {
      item.status = !item.status
      const data = {status: item.status}
      api_promotion.put(`point/${item.id}`, data).then(() => {})
    },
    delete_confirm(item) {
      console.log(item, "item")
      this.point_item = item
      this.delete_status = true
    },
    delete_point_pro() {
      api_promotion.delete(`point/${this.point_item.id}`).then(() => {
        this.correct_status = true
        setTimeout(() => {
          this.correct_status = false
          this.delete_status = false
        }, 1000)
      })
    },
    fetchPointPromotion() {
      api_promotion.get("point/").then((response) => {
        console.log(response.data, "res");
        this.point_promotions = response.data;
      });
    },
  },
  beforeMount() {
    // this.fetchPointPromotion()
  }
};
</script>

<style scoped>
.btn-ghost-cancel {
  background: transparent;
  border-color: #FF7CA3;
  color: #FF7CA3;
  width: 180px;
  height: 56px;
}
.btn-ghost-correct {
  background: transparent;
  border-color: #50D1AA;
  color: #50D1AA;
  width: 180px;
  height: 56px;
}
.delete-card {
  width: 440px;
  height: 280px;
  background: #252836;
  border: 2px solid #EA7C69;
  border-radius: 15.5833px;
  position: absolute;
  top: 25%;
  left: 20%;
}
.card-content {
  width: 672px;
  height: 304px;
  background: #303344;
  border-radius: 20px;
  margin: 10px 0px 0px 25px;
}
.switch {
  position: relative;
  display: inline-block;
  right: -3px;
  top: 14px;
  width: 60px;
  height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
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

.slider:before {
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

input:checked + .slider {
  background-color: #c5ffed;
}

input:focus + .slider {
  box-shadow: 0 0 1px #c5ffed;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
  background-color: #50d1aa;
}
/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>