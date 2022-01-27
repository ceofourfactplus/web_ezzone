<template>
  <div>
    <div class="title">
      Dashboard
      <router-link :to="{ name: 'Login' }">
        <img src="../assets/icon/exit.png" class="hamburger" alt=""
      /></router-link>
    </div>

    <div v-for="category in select_list" :key="category">
      <h2>{{ category.title }}</h2>
      <div style="margin-left: 50px; margin-right: 50px">
        <div class="row" style="background-color: #303344; border-radius: 10px">
          <div
            v-for="(dsh, idx) in category.btn"
            :key="idx"
            class="col-2 w-100"
            style="padding-left: 0px; padding-right: 0px"
          >
            <div style="padding-top: 10px; height: 120px; width: 100%">
              <router-link
                style="height: 120px"
                class="w-100"
                v-if="
                  ['Point', 'Voucher', 'Package', 'Reward'].some((el) => {
                    return el === dsh.txt;
                  })
                "
                :to="{ name: 'Promotion' }"
                @click="$store.state.promotion.tab = dsh.link"
              >
                <img class="image" :src="dsh.img" />
                <div class="content">
                  {{ dsh.txt }}
                </div>
              </router-link>
              <router-link
                style="height: 120px"
                class="w-100"
                :to="{ name: dsh.link }"
                v-else
              >
                <img class="image" :src="dsh.img" />
                <div class="content">
                  {{ dsh.txt }}
                </div>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="row"
      style="margin-left: 40px; margin-right: 40px"
      v-if="$store.state.auth.userInfo.is_staff"
    >
      <div
        v-for="(category, index) in setting_else"
        :key="category"
        class="col-6 w-100"
        :class="{ 'pe-1': index == 0, 'ps-1': index == 1 }"
      >
        <div>
          <h2 class="else">{{ category.title }}</h2>
          <div
            class="row"
            :class="{ 'me-1-i': index == 0, 'ms-1-i': index == 1 }"
            style="background-color: #303344; border-radius: 10px"
          >
            <div
              v-for="(dsh, idx) in category.btn"
              :key="idx"
              class="col-4 w-100"
              style="padding-left: 0px; padding-right: 0px"
            >
              <div style="padding-top: 10px; height: 120px">
                <router-link :to="{ name: dsh.link }">
                  <img class="image" :src="dsh.img" />
                  <div class="content">
                    {{ dsh.txt }}
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.dash_board_list.forEach((element) => {
      if (this.has_permission(element.permissions)) {
        var btn_t = [];
        element.btn.forEach((item) => {
          if (this.has_permission(item.permissions)) {
            btn_t.push(item);
          }
        });
        this.select_list.push({ title: element.title, btn: btn_t });
      }
    });
  },
  data() {
    return {
      dash_board_list: [
        // order
        {
          permissions: [
            "is_staff",
            "is_receptionist",
            "is_chef",
            "is_bartender",
          ],
          title: "Order",
          btn: [
            {
              permissions: ["is_staff", "is_receptionist"],
              img: require("../../src/assets/icon/order-box.png"),
              txt: "Orders",
              link: "SelectSaleChannel",
            },
            {
              permissions: ["is_staff", "is_receptionist"],
              img: require("../../src/assets/icon/order-detail.png"),
              txt: "Order Detail",
              link: "OrderDetail",
            },
            {
              permissions: ["is_staff", "is_bartender"],
              img: require("../../src/assets/icon/drink.png"),
              txt: "Drink Order",
              link: "DrinkOrder",
            },
            {
              permissions: ["is_staff", "is_chef"],
              img: require("../../src/assets/icon/food.png"),
              txt: "Food Order",
              link: "FoodOrder",
            },
          ],
        },
        // promotion
        {
          permissions: ["is_staff"],
          title: "Promotion",
          btn: [
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/promotion.png"),
              txt: "Point",
              link: "Point",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/voucher.png"),
              txt: "Voucher",
              link: "Voucher",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/package.png"),
              txt: "Package",
              link: "Package",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/reward.png"),
              txt: "Reward",
              link: "Reward",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/redemtion.png"),
              txt: "Redemption",
              link: "Redemption",
            },
          ],
        },
        // stock
        {
          permissions: [
            "is_staff",
            "is_purchesing",
            "is_barista",
            "is_chef",
            "is_receptionist",
          ],
          title: "Stock",
          btn: [
            {
              permissions: [
                "is_staff",
                "is_purchesing",
                "is_receptionist",
                "is_barista",
                "is_chef",
              ],
              img: require("../../src/assets/icon/raw-material-2.png"),
              txt: "Raw Material",
              link: "RawMaterials",
            },
            {
              permissions: ["is_staff", "is_purchesing"],
              img: require("../../src/assets/icon/PO.png"),
              txt: "PO Notice",
              link: "PONotice",
            },
            {
              permissions: ["is_staff", "is_purchesing"],
              img: require("../../src/assets/icon/product.png"),
              txt: "Products",
              link: "Product",
            },
          ],
        },
        // people
        {
          permissions: ["is_staff", "is_receptionist", "is_purchesing"],
          title: "People",
          btn: [
            {
              permissions: ["is_staff", "is_receptionist"],
              img: require("../../src/assets/icon/customer.png"),
              txt: "Customer",
              link: "Customer",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/user-status.png"),
              txt: "User Status",
              link: "UserStatus",
            },
            {
              permissions: ["is_staff", "is_purchesing"],
              img: require("../../src/assets/icon/supplier.png"),
              txt: "Supplier",
              link: "Supplier",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/consigner.png"),
              txt: "Consigner",
              link: "DashBoard",
            },
          ],
        },
      ],
      setting_else: [
        // report
        {
          permissions: ["is_staff"],
          title: "Report",
          btn: [
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/report.png"),
              txt: "Report",
              link: "SelectReport",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/wallet.png"),
              txt: "Wallet",
              link: "DashBoard",
            },
          ],
        },
        // setting
        {
          permissions: ["is_staff"],
          title: "Setting",
          btn: [
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/app.png"),
              txt: "App",
              link: "DashBoard",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/database.png"),
              txt: "DataBase",
              link: "DataBaseSettings",
            },
          ],
        },
      ],
      select_list: [],
    };
  },
  methods: {
    has_permission(array) {
      for (const item of array) {
        if (this.$store.state.auth.userInfo[item]) {
          return true;
        }
      }
      return false;
    },
  },
};
</script>

<style scoped>
h2 {
  color: #fff;
  font-weight: 700;
  text-align: left;
  margin-top: 5px;
  margin-left: 40px;
  margin-bottom: 10px;
}
body {
  background-color: white;
}
.container-box {
  display: none;
  width: 0px;
  height: 0px;
}
.title {
  width: 100%;
  height: 59px;
  text-align: center;
  font-size: 48px;
  font-weight: 800;
  line-height: 80px;
  color: white;
}
.content {
  /* height: 36px; */
  color: white;
  font-size: 16px;
  width: 120px;
  position: absolute;
}
.block {
  width: 180px;
  height: 168px;
  position: absolute;
}
.image {
  width: 75px;
  height: 75px;
}
.hamburger {
  top: 30px;
  right: 20px;
  position: absolute;
}
.ms-1-i {
  margin-left: 3px;
}
.me-1-i {
  margin-right: 3px;
}
.else {
  text-align: left;
  margin-left: 0px;
}
</style>