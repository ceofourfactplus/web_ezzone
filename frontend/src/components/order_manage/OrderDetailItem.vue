<template>
  <div v-if="order != null">
    <div class="dark" @click="$emit('close')"></div>
    <div class="order-detail">
      <div class="row w-100" style="text-align: center; margin: 0px">
        <div class="col-12">
          <div class="row header">
            <div class="col-2 w-100" style="font-size: 30px">
              #{{ order.order_number }}
            </div>
            <div
              class="col-3 w-100"
              style="font-size: 30px"
              v-if="order.table != null"
            >
              <img
                src="../../assets/icon/table-white.png"
                style="
                  width: 35px;
                  height: 35px;
                  object-fit: cover;
                  border-radius: 10px;
                  margin-right: 10px;
                "
              />{{ order.table }}
            </div>
            <div class="col-3 w-100" v-else>
              <img
                :src="order.sale_channel_set.img"
                style="
                  width: 34px;
                  height: 30px;
                  object-fit: cover;
                  line-height: 30px;
                "
              />
            </div>
            <div class="col-3 w-100" style="display: flex">
              <div style="font-size: 24px">
                <img
                  src="../../assets/icon/clock.png"
                  style="width: 34px; height: 34px"
                />
                {{ get_date(order.create_at) }}
              </div>
            </div>
            <div class="col-4 w-100">
              <button
                class="btn"
                :style="{
                  'background-color': get_status(order.status_order).color,
                }"
                style="height: 40px"
              >
                {{ get_status(order.status_order).text }}
              </button>
            </div>
          </div>
        </div>

        <div
          class="col-10 w-100"
          style="hieght: 45px !important; line-height: 45px"
        >
          รายการ
        </div>
        <div
          class="col-2 w-100"
          style="hieght: 45px !important; text-align: center; line-height: 45px"
        >
          จำนวน
        </div>
        <div class="col-12">
          <div
            class="row"
            v-for="(item, index) in order.orderitem_set"
            :key="item.id"
          >
            <div
              class="col-10 w-100"
              v-if="item.status_order < 2 && item.package == null"
              style="text-align: left; line-height: 45px"
              :class="{
                odd: (index + 1) % 2 != 0,
                'last-l': last_f(index),
              }"
            >
              {{ index + 1 }}. {{ get_code(item) }}
              <span style="color: #ff7ca3" v-if="item.description != ''">
                / {{ item.description }}</span
              >
            </div>

            <div
              class="col-10 w-100 red"
              v-else-if="item.status_order == 2 && item.package == null"
              style="text-align: left; line-height: 45px"
              @click="serve_order(item.id)"
              :class="{
                odd: (index + 1) % 2 != 0,
                'last-l': last_f(index),
              }"
            >
              {{ index + 1 }}. {{ get_code(item) }}
              <span style="color: #ff7ca3" v-if="item.description != ''">
                / {{ item.description }}</span
              >
            </div>

            <div
              class="col-10 w-100 green"
              v-else-if="(item.status_order == 3 || !item.item_in_package)&&(item.package == null)"
              style="text-align: left; line-height: 45px"
              :class="{
                odd: (index + 1) % 2 != 0,
                'last-l': last_f(index),
              }"
            >
              {{ index + 1 }}. {{ get_code(item) }}
              <span style="color: #ff7ca3" v-if="item.description != ''">
                / {{ item.description }}</span
              >
            </div>
            <div
              class="col-2 w-100"
              style="text-align: center; line-height: 45px"
              v-if="item.status_order < 2 && item.package == null"
              :class="{
                odd: (index + 1) % 2 != 0,
                'last-r': last_f(index),
              }"
            >
              {{ item.amount }}
            </div>
            <div
              class="col-2 w-100 red"
              v-else-if="item.status_order == 2 && item.package == null"
              style="text-align: center; line-height: 45px"
              :class="{
                odd: (index + 1) % 2 != 0,
                'last-r': last_f(index),
              }"
            >
              {{ item.amount }}
            </div>
            <div
              class="col-2 w-100 green"
              v-else-if="item.status_order == 3 && item.package == null"
              style="text-align: center; line-height: 45px"
              :class="{
                odd: (index + 1) % 2 != 0,
                'last-r': last_f(index),
              }"
            >
              {{ item.amount }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import moment from "moment";
import { api_pos } from "../../api/api_pos";
export default {
  props: ["order"],
  data() {
    return {};
  },
  methods: {
    get_date(data) {
      var date = moment(data);
      var now = moment();
      if (now.diff(date, "day") == 0) {
        if (now.diff(date, "hour") == 0) {
          return now.diff(date, "minute") + " Mins";
        }
        return now.diff(date, "hour") + " Hour";
      }
      return now.diff(date, "day") + " Day";
    },
    get_status(status) {
      if (status == 0) {
        return { text: "Waiting", color: "#FFF500" };
      }
      if (status == 1) {
        return { text: "On Cooking", color: "#FF7CA3" };
      }
      if (status == 2) {
        return { text: "On Serve", color: "#FFB572" };
      }
      if (status == 3) {
        return { text: "Finished", color: "#50D1AA" };
      }
      if (status == 4) {
        return { text: "Cancel", color: "#FFB572" };
      }
    },
    get_code(p) {
      var description = "";
      console.log(p);
      if (p.topping == null) {
        description = p.product_set.name;
        if (p.flavour_level == 3) {
          description += "(S+)";
        } else if (p.flavour_level == 1) {
          description += "(S-)";
        } else if (p.flavour_level == 0) {
          description += "(Sx)";
        }
        if (p.size == "L") {
          description = description + "(L)";
        }
        for (var topping of p.orderitemtopping_set) {
          if (topping.amount > 1) {
            description +=
              " + " + topping.topping_set.name + "(" + topping.amount + ")";
          } else {
            description += " + " + topping.topping_set.name;
          }
        }
      } else {
        description = p.topping_set.name;
      }

      return description;
    },
    last_f(index) {
      if (index == this.order.orderitem_set.length - 1) {
        return true;
      } else {
        return false;
      }
    },
    serve_order(id) {
      this.order.orderitem_set.forEach((item) => {
        if (item.id == id) {
          item.status_order = 3;
        }
      });
      api_pos.put("change-status-order/order/0/3/" + id);
    },
  },
};
</script>

<style scoped>
.header {
  background-color: #bd523f;
  height: 55px;
  border-radius: 10px 10px 0px 0px;
  line-height: 33px;
  text-align: center;
  padding: 7px;
}
div .col-10,
.col-2 {
  height: 45px;
}
.red {
  background-color: #ffb57280 !important;
}
.green {
  background-color: #50d1aa80 !important;
}
.dark {
  background-color: #000000c9;
  width: 100%;
  height: 100%;
  top: 0px;
  left: 0px;
  position: fixed;
  display: block;
}
.order-detail {
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
  background-color: #303344;
  width: 620px;
  border: 1.2px solid #bd523f;
  border-radius: 15px;
  display: flex;
  color: #ffffff;
  font-weight: bold;
  font-size: 20px;
}
.odd {
  background-color: #252836;
}
.last-l {
  border-radius: 0px 0px 0px 15px;
}
.last-r {
  border-radius: 0px 0px 15px 0px;
}
.btn {
  font-size: 24px;
  font-weight: bolder;
  line-height: 25px;
  color: #252836;
  border-radius: 10px;
}
</style>