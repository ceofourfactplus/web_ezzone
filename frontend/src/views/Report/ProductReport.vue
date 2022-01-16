<template>
  <div>
    <nav-app>Daily Product Report</nav-app>
    <div class="row" style="width: 90%; margin: auto">
      <div class="col-12 frame">
        <div class="row">
          <div class="col-8 w-100" style="height: 420px">
            <pie-chart-product
              :data="data_total_price"
              style="margin: auto"
            ></pie-chart-product>
          </div>
          <div class="col-4 w-100">
            <select
              style="
                background-color: #717171;
                width: 174px;
                height: 43px;
                font-weight: 700;
              "
              v-model="day"
            >
              <option value="Monday">Monday</option>
              <option value="Tuesday">Tuesday</option>
              <option value="Wednesday">Wednesday</option>
              <option value="Thursday">Thursday</option>
              <option value="Friday">Friday</option>
              <option value="Saturday">Saturday</option>
              <option value="Sunday">Sunday</option>
            </select>
            <ul class="w-100">
              <li>
                <div class="color" style="background-color: #ff6385"></div>
                Food
              </li>
              <li>
                <div class="color" style="background-color: #25a0e8"></div>
                Drink
              </li>
              <li>
                <div class="color" style="background-color: #ffce61"></div>
                Dressert
              </li>
              <li>
                <div class="color" style="background-color: #9b62fb"></div>
                Topping
              </li>
              <li>
                <div class="color" style="background-color: #3cc0bf"></div>
                Consign
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="col-12" style="padding: 0px">
        <div
          class="row w-100"
          style="margin: 0px; overflow-y: auto; height: 385px"
        >
          <!-- food -->
          <div
            class="col-12 table-item mt-2 w-100 table"
            style="padding-left: 10px; font-weight: bold; text-align: left"
            @click="
              router.push({ name: 'ProductReportDetail', params: { type: 3 } })
            "
          >
            Top 10 Food
            <img
              src="../../assets/icon/fork-active.png"
              style="height: 30px"
              alt=""
            />
          </div>
          <div
            class="col-2 w-100 mt-2"
            v-for="(food, index) in report_product.top_food"
            :key="food.id"
            style="color: #fff"
          >
            <div class="container-img">
              <img v-if="food.img != null" class="img" :src="food.img" alt="" />
              <div v-else class="img" style="background-color: #717171"></div>
              <div class="no">{{ index + 1 }}</div>
            </div>
            {{ food.name }}
          </div>

          <!-- drink -->
          <div
            class="col-12 table-item mt-2 w-100 table"
            style="padding-left: 10px; font-weight: bold; text-align: left"
          >
            Top 10 Drink
            <img
              src="../../assets/icon/fork-active.png"
              style="height: 30px"
              alt=""
            />
          </div>
          <div
            class="col-2 w-100 mt-2"
            v-for="(food, index) in report_product.top_drink"
            :key="food.id"
            style="color: #fff"
          >
            <div class="container-img">
              <img v-if="food.img != null" class="img" :src="food.img" alt="" />
              <div v-else class="img" style="background-color: #717171"></div>
              <div class="no">{{ index + 1 }}</div>
            </div>
            {{ food.name }}
          </div>

          <!-- dressert -->
          <div
            class="col-12 table-item mt-2 w-100 table"
            style="padding-left: 10px; font-weight: bold; text-align: left"
          >
            Top 10 Dressert
            <img
              src="../../assets/icon/fork-active.png"
              style="height: 30px"
              alt=""
            />
          </div>
          <div
            class="col-2 w-100 mt-2"
            v-for="(food, index) in report_product.top_dressert"
            :key="food.id"
            style="color: #fff"
          >
            <div class="container-img">
              <img v-if="food.img != null" class="img" :src="food.img" alt="" />
              <div v-else class="img" style="background-color: #717171"></div>
              <div class="no">{{ index + 1 }}</div>
            </div>
            {{ food.name }}
          </div>

          <!-- topping -->
          <div
            class="col-12 table-item mt-2 w-100 table"
            style="padding-left: 10px; font-weight: bold; text-align: left"
          >
            Top 10 Food
            <img
              src="../../assets/icon/fork-active.png"
              style="height: 30px"
              alt=""
            />
          </div>
          <div
            class="col-2 w-100 mt-2"
            v-for="(food, index) in report_product.top_food"
            :key="food.id"
            style="color: #fff"
          >
            <div class="container-img">
              <img v-if="food.img != null" class="img" :src="food.img" alt="" />
              <div v-else class="img" style="background-color: #717171"></div>
              <div class="no">{{ index + 1 }}</div>
            </div>
            {{ food.name }}
          </div>

          <!-- consign  -->
          <div
            class="col-12 table-item mt-2 w-100 table"
            style="padding-left: 10px; font-weight: bold; text-align: left"
          >
            Top 10 dressert
            <img
              src="../../assets/icon/fork-active.png"
              style="height: 30px"
              alt=""
            />
          </div>
          <div
            class="col-2 w-100 mt-2"
            v-for="(food, index) in report_product.top_food"
            :key="food.id"
            style="color: #fff"
          >
            <div class="container-img">
              <img v-if="food.img != null" class="img" :src="food.img" alt="" />
              <div v-else class="img" style="background-color: #717171"></div>
              <div class="no">{{ index + 1 }}</div>
            </div>
            {{ food.name }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import { api_pos } from "../../api/api_pos";
import PieChartProduct from "./PieChartProduct.vue";

export default {
  components: { NavApp, PieChartProduct },
  data() {
    return {
      data_total_price: [50, 50],
      report_product: {},
      day: "",
    };
  },
  mounted() {
    api_pos.get("report/all-product").then((response) => {
      this.report_product = response.data;
      this.data_total_price[0] = response.data.total_price_food;
      this.data_total_price[1] = response.data.total_price_drink;
      this.data_total_price[2] = response.data.total_price_dressert;
    });
  },
};
</script>

<style scoped>
.color {
  width: 24px;
  height: 24px;
  background-color: #fff;
  border-radius: 50%;
}
ul {
  list-style: None;
  padding-left: 0px;
  margin: 50px auto;
}
li {
  display: flex;
  line-height: 25px;
  color: #fff;
  margin: 20px 0px 0px 20px;
  font-size: 24px;
  font-weight: bold;
}
li .color {
  margin-right: 20px;
}
.container-img {
  color: #fff;
  position: relative;
}
.container-img .img {
  width: 90px;
  height: 87px;
  object-fit: cover;
  border-radius: 15px;
}
.no {
  position: absolute;
  bottom: 3px;
  right: 0px;
  width: 25px;
  height: 25px;
  font-weight: 700;
  border-radius: 50%;
  background-color: #ea7c69;
}
</style>