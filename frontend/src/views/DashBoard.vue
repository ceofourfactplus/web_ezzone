<template>
  <div>
    <div class="title">
      Manager
      <router-link :to="{ name: 'Login' }">
        <img src="../assets/icon/exit.png" class="hamburger" alt=""
      /></router-link>
    </div>

    <div v-for="category in dash_board_list" :key="category">
      <div v-if="has_permission(category.permissions)">
        <h1>{{ category.title }}</h1>
        <div style="margin-left: 50px; margin-right: 50px">
          <div class="row">
            <div
              v-for="(dsh, idx) in category.btn"
              :key="idx"
              class="col-3 w-100"
              style="padding-left: 0px; padding-right: 0px;"
            >
              <div
                v-if="has_permission(dsh.permissions)"
                style="padding: 0px; height: 180px"
              >
                <router-link :to="{ name: dsh.link }">
                  <img class="image" :src="dsh.img" />
                  <p class="content">
                    {{ dsh.txt }}
                  </p>
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
  data() {
    return {
      dash_board_list: [
        {
          permissions: ["is_staff", "is_barista", "is_chef"],
          title: "Display",
          btn: [
            {
              permissions: ["is_staff", "is_barista", "is_chef"],
              img: require("../../src/assets/icon/drink.png"),
              txt: "Drink Order",
              link: "DashBoard",
            },
            {
              permissions: ["is_staff", "is_barista", "is_chef"],
              img: require("../../src/assets/icon/order-box.png"),
              txt: "Food Order",
              link: "DashBoard",
            },
          ],
        },
        {
          permissions: ["is_staff", "is_receptionist"],
          title: "Order",
          btn: [
            {
              permissions: ["is_staff", "is_receptionist"],
              img: require("../../src/assets/icon/order-box.png"),
              txt: "Orders",
              link: "DashBoard",
            },
            {
              permissions: ["is_staff", "is_receptionist"],
              img: require("../../src/assets/icon/order-detail.png"),
              txt: "Order Status",
              link: "DashBoard",
            },
          ],
        },
        {
          permissions: ["is_staff"],
          title: "Promotion",
          btn: [
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/promotion.png"),
              txt: "Point",
              link: "DashBoard",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/package.png"),
              txt: "Package",
              link: "DashBoard",
            },
          ],
        },
        {
          permissions: ["is_staff", "is_purchesing", "is_barista", "is_chef"],
          title: "Raw Material",
          btn: [
            {
              permissions: [
                "is_staff",
                "is_purchesing",
                "is_receptionist",
                "is_barista",
                "is_chef",
              ],
              img: require("../../src/assets/icon/RM.png"),
              txt: "Raw Material",
              link: "RawMaterials",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/NewRM.png"),
              txt: "New RM",
              link: "DashBoard",
            },
            {
              permissions: ["is_staff", "is_purchesing"],
              img: require("../../src/assets/icon/PO.png"),
              txt: "PO",
              link: "PO",
            },
            {
              permissions: ["is_staff", "is_purchesing"],
              img: require("../../src/assets/icon/add_RM.png"),
              txt: "Add RM",
              link: "DashBoard",
            },
            {
              permissions: [
                "is_staff",
                "is_purchesing",
                "is_barista",
                "is_chef",
                "is_receptionist",
              ],
              img: require("../../src/assets/icon/pick_up.png"),
              txt: "RMUnit",
              link: "RMUnit"
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/category_rm.png"),
              txt: "Categories",
              link: "RawMaterialCategory",
            },
          ],
        },
        {
          permissions: ["is_staff", "is_barista", "is_chef", "is_receptionist"],
          title: "Products",
          btn: [
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/product.png"),
              txt: "Products",
              link: "Product",
            },
            {
              permissions: [
                "is_staff",
                "is_barista",
                "is_chef",
                "is_receptionist",
              ],
              img: require("../../src/assets/icon/add_product.png"),
              txt: "Add Qty",
              link: "DashBoard",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/category_product.png"),
              txt: "Categories",
              link: "DashBoard",
            },
          ],
        },
        {
          permissions: ["is_staff"],
          title: "Contacts",
          btn: [
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/customer.png"),
              txt: "Customers",
              link: "Customer",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/supplier.png"),
              txt: "Supplier",
              link: "Supplier",
            },
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/user-status.png"),
              txt: "User Status",
              link: "UserStatus",
            },
          ],
        },
        {
          permissions: ["is_staff"],
          title: "Report",
          btn: [
            {
              permissions: ["is_staff"],
              img: require("../../src/assets/icon/report.png"),
              txt: "Report",
              link: "DashBoard",
            },
          ],
        },
      ],
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
h1 {
  font-size: 40px;
  text-align: left;
  margin-left: 20px;
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
  font-size: 28px;
  width: 160px;
  position: absolute;
}
.block {
  width: 180px;
  height: 168px;
  position: absolute;
}
.image {
  width: 130px;
  height: 130px;
}
.hamburger {
  top: 30px;
  right: 20px;
  position: absolute;
}
</style>