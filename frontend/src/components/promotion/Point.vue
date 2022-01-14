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
          <img
            src="../../assets/icon/edit.png"
            style="width: 25px; height: 30px"
            @click="
              $router.push({ name: 'PointDetail', params: { id: item.id } })
            "
          />
        </div>
        <div
          class="col-4 w-100"
          style="font-size: 30px; color: white; margin: 10px 0px 0px -10px"
        >
          Price per Point
        </div>
      </div>
      <div class="row">
        <div class="col-8 w-100">
          <div
            class="switch"
            style="
              font-size: 30px;
              color: white;
              line-height: 1;
              margin-top: 40px;
            "
          >
            <Switch :value="item.status" @switch="fridge" /> Point X2
          </div>
        </div>
        <div
          class="col-4 w-100"
          style="
            font-size: 100px;
            font-weight: bold;
            margin-top: -40px;
            color: white;
          "
        >
          {{ item.price_per_point }}
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
  </div>
</template>

<script>
import Switch from "../../components/main_component/Switch.vue";
import { api_promotion } from "../../api/api_promotion";

export default {
  name: "PointComponent",
  components: {
    Switch,
  },
  mounted() {
  },
  data() {
    return {
      point_promotions: [],
    };
  },
  methods: {
    fetchPointPromotion() {
      api_promotion.get("point/").then((response) => {
        console.log(response.data, "res");
        this.point_promotions = response.data;
      });
    },
    format_date(date) {
      var temp_date = date.split("-");
      return `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
    },
  },
  beforeMount() {
    this.fetchPointPromotion();
  }
};
</script>

<style scoped>
.card-content {
  width: 672px;
  height: 304px;
  background: #303344;
  border-radius: 20px;
  margin: 10px 0px 0px 25px;
}
</style>