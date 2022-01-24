<template>
  <div>
    <nav-app :url_name="'DashBoard'">Drink Order</nav-app>
    <div class="row" style="width: 90%; margin: auto">
      <div
        class="col-12 w-100"
        style="
          border: 3px solid #bd523f;
          font-size: 30px;
          border-radius: 10px;
          color: #fff;
          display: flex;
          font-weight: bold;
        "
      >
        <div style="text-align: left; width: 320px">
          Finished Order : {{ finished_order }}
        </div>
        <div style="text-align: right; width: 320px">
          Remain Order : {{ remain_order }}
        </div>
      </div>
      <!-- tab -->
      <div class="col-12 mt-2 w-100 p-0" style="display: flex">
        <div
          @click="get_order_by_type('1')"
          class="btn-gray me-2"
          style="width: 24%; opacity: 0.6"
          :class="{
            active: type_order == '1',
          }"
        >
          On going
        </div>
        <div
          @click="get_order_by_type('4')"
          class="btn-gray me-2"
          style="width: 24%; opacity: 0.6"
          :class="{
            active: type_order == '4',
          }"
        >
          Cancel
        </div>
        <div
          @click="get_order_by_type('3')"
          class="btn-gray me-2"
          style="width: 24%; opacity: 0.6"
          :class="{
            active: type_order == '3',
          }"
        >
          Completed
        </div>
        <div
          @click="get_order_by_type('5')"
          class="btn-gray me-2"
          style="width: 24%; opacity: 0.6"
          :class="{
            active: type_order == '5',
          }"
        >
          all
        </div>
      </div>
      <div class="col-12 mt-3" style="padding: 0px">
        <div style="height: 715px; overflow-y: auto">
          <div v-for="order in all_order" :key="order.id" class="mb-2">
            <div class="row w-100 header" style="padding: 0px; margin: 0px">
              <div class="col-2 w-100" style="font-size: 30px">
                #{{ order.order_number }}
              </div>
              <div
                class="col-3 w-100"
                style="font-size: 30px; line-height: 30px"
              >
                <img
                  src="../../assets/icon/table-white.png"
                  style="
                    width: 35px;
                    height: 35px;
                    object-fit: cover;
                    border-radius: 10px;
                    margin-right: 10px;
                    margin-top: 5px;
                  "
                />{{ order.table }}
              </div>
              <!-- <div class="col-3 w-100" v-else>
              <img
                style="
                  width: 34px;
                  height: 30px;
                  object-fit: cover;
                  line-height: 30px;
                "
              />
            </div> -->
              <div class="col-3 w-100" style="display: flex">
                <div style="font-size: 24px; line-height: 40px">
                  <img
                    src="../../assets/icon/clock.png"
                    style="width: 34px; height: 34px; margin-right: 10px"
                  />{{ get_date(order.create_at) }}
                </div>
              </div>
              <div style="line-height: 32px" class="col-4 w-100">
                <button
                  v-if="order.status_order == 4"
                  class="btn btn-y"
                  style="background-color: #717171 !important;border:0px;"
                >
                  Cancel
                </button>
                <button
                  v-else-if="order.status_drink == 0"
                  @click="accept(order)"
                  class="btn-y btn"
                >
                  Waiting</button
                ><button
                  v-else-if="order.status_drink == 1"
                  @click="finish_order(order.id)"
                  class="btn-r btn"
                >
                  On Cooking
                </button><button
                  v-else-if="order.status_drink == 2"
                  @click="finish_order(order.id)"
                  class="btn-y btn"
                >
                  On Serve
                </button>
                <button v-else-if="order.status_drink == 3" class="btn-g btn">
                  Completed
                </button>
              </div>
            </div>
            <div
              class="row w-100 sub-header"
              style="margin: 0px"
              v-if="order.status_drink != 0"
            >
              <div class="col-9">รายการ</div>
              <div class="col-3 w-100">จำนวน</div>
            </div>
            <div
              class="w-100"
              v-if="order.status_drink != 0"
              style="margin: 0px"
            >
              <div v-for="(item, index) in order.orderitem_set" :key="item.id">
                <div
                  class="row body w-100"
                  style="margin: 0px"
                  v-if="is_drink(item)"
                  :class="{
                    'last-b': last_f(index, order.orderitem_set),
                  }"
                >
                  <div
                    v-if="item.status_order == 1"
                    class="col-9 w-100"
                    @click="finish_item(item.id, order.id)"
                    style="overflow-x: auto; white-space: nowrap"
                    :class="{
                      odd: (index + 1) % 2 != 0,
                      'last-l': last_f(index, order.orderitem_set),
                    }"
                  >
                    {{ index + 1 }}. {{ get_code(item) }}
                    <span style="color: #ff7ca3" v-if="item.description != ''">
                      / {{ item.description }}</span
                    >
                  </div>
                  <div
                    v-else-if="item.status_order == 2"
                    class="col-9 w-100 red"
                    style="overflow-x: auto; white-space: nowrap"
                    :class="{
                      odd: (index + 1) % 2 != 0,
                      'last-l': last_f(index, order.orderitem_set),
                    }"
                  >
                    {{ index + 1 }}. {{ get_code(item) }}
                    <span style="color: #ff7ca3" v-if="item.description != ''">
                      / {{ item.description }}</span
                    >
                  </div>
                  <div
                    v-else-if="item.status_order == 3"
                    @click="finish_item(item.id, order.id)"
                    class="col-9 w-100 green"
                    style="overflow-x: auto; white-space: nowrap"
                    :class="{
                      odd: (index + 1) % 2 != 0,
                      'last-l': last_f(index, order.orderitem_set),
                    }"
                  >
                    {{ index + 1 }}. {{ get_code(item) }}
                    <span style="color: #ff7ca3" v-if="item.description != ''">
                      / {{ item.description }}</span
                    >
                  </div>
                  <div
                    class="col-3 w-100"
                    v-if="item.status_order == 1"
                    :class="{
                      odd: (index + 1) % 2 != 0,
                      'last-r': last_f(index, order.orderitem_set),
                    }"
                  >
                    {{ item.amount }}
                  </div>

                  <div
                    class="col-3 w-100 red"
                    @click="finish_item(item.id, order.id)"
                    v-if="item.status_order == 2"
                    :class="{
                      odd: (index + 1) % 2 != 0,
                      'last-r': last_f(index, order.orderitem_set),
                    }"
                  >
                    {{ item.amount }}
                  </div>
                  <div
                    class="col-3 w-100 green"
                    @click="finish_item(item.id, order.id)"
                    v-if="item.status_order == 3"
                    :class="{
                      odd: (index + 1) % 2 != 0,
                      'last-r': last_f(index, order.orderitem_set),
                    }"
                  >
                    {{ item.amount }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_pos } from "../../api/api_pos";
import NavApp from "../../components/main_component/NavApp.vue";
import moment from "moment";
var audio = new Audio(require("./short-alert.mp3"));
export default {
  components: { NavApp },
  mounted() {
    this.get_order();
    this.loader;
  },
  unmounted() {
    clearInterval(this.loader);
  },
  data() {
    return {
      all_order: [],
      loader: window.setInterval(() => {
        this.get_order();
      }, 5000),
      remain_order: 0,
      finished_order: 0,
      type_order: 1,
    };
  },
  methods: {
    find_waiting_order(order_list) {
      var wait = order_list.filter((item) => {
        return item.status_drink == 0;
      });
      console.log(wait.length);
      if (wait.length != 0 && audio.paused) {
        audio.play();
      }
    },
    get_order() {
      api_pos.get("counter/today").then((response) => {
        if (this.type_order == 1) {
          this.all_order = response.data.order;
        }
        this.remain_order = response.data.remain_order;
        this.finished_order = response.data.finish_order;
        this.find_waiting_order(response.data.order);
      });
    },
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
      if (status == 4) {
        return { text: "On Serve", color: "#717171" };
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
      if (p.product_set != null) {
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
    last_f(index, all) {
      if (index == all.length - 1) {
        return true;
      } else {
        return false;
      }
    },
    accept(order) {
      api_pos.put("change-status-order/counter/1/1/" + order.id).then(() => {
        this.get_order();
      });
    },
    finish_order(order_id) {
      this.all_order.forEach((order) => {
        if (order.id == order_id) {
          order.status_drink = 2;
        }
      });
      api_pos.put("change-status-order/counter/1/2/" + order_id);
    },
    finish_item(item_id, order_id) {
      this.all_order.forEach((order) => {
        if (order.id == order_id) {
          order.orderitem_set.forEach((item) => {
            if (item.id == item_id) {
              item.status_order = 2;
            }
          });
        }
      });
      api_pos.put("change-status-order/counter/0/2/" + item_id);
    },
    is_drink(item) {
      if (item.topping_set != null) {
        return item.topping_set.type_topping == 2;
      }
      if (item.product_set != null) {
        return item.product_set.type_product == 2;
      }
    },
    get_order_by_type(type) {
      this.type_order = type;
      if (type == 1) {
        this.get_order();
      } else {
        api_pos.get("counter/" + type).then((response) => {
          this.all_order = response.data;
        });
      }
    },
  },
};
</script>

<style scoped>
.header {
  background-color: #bd523f;
  height: px;
  border-radius: 10px 10px 0px 0px;
  line-height: 45px;
  text-align: center;
  padding: 7px;
  font-weight: bold;
  font-size: 30px;
  color: #fff;
}
.red {
  background-color: #FFB57280 !important;
}
.green {
  background-color: #50d1aa80 !important;
}
.btn {
  font-size: 20px;
  font-weight: bolder;
  line-height: 15px;
  color: #252836;
  border-radius: 10px;
  height: 30px;
}
.active {
  color: #fff;
  opacity: 1 !important;
}
.sub-header {
  font-weight: bold;
  font-size: 24px;
  color: #fff;
  height: 45px;
  line-height: 45px;
  background-color: #303344;
}
.body {
  background-color: #303344;
  color: #fff;
  font-size: 24px;
  font-weight: bold;
  height: 45px;
  line-height: 45px;
}
.odd {
  background-color: #252836;
}

.body .col-9 {
  text-align: left;
}
.last-l {
  border-radius: 0px 0px 0px 15px;
}
.last-r {
  border-radius: 0px 0px 15px 0px;
}
.last-b {
  border-radius: 0px 0px 15px 15px;
}
.btn-gray {
  line-height: 56px;
}
</style>