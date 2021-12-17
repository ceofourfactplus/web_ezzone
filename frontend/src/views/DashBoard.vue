<template>
  <div>
    <div class="title">Manager</div>
    <!-- <div class="row" style="margin: auto; margin-left: 47px; margin-top: 20px">
      <div v-for="(dsh, idx) in dash_board_list" :key="idx">
        <div class="col-3" v-if="check_permission(dsh.permissions)" style="background-color: white">
          <div>
            <img class="image" :src="dsh.img" />
            <p class="content">{{ dsh.txt }}</p>
          </div>
        </div>
        <div v-else style="background-color: orange; padding-left: 0px; padding-right: 0px"></div>
      </div>
    </div> -->

    <div class="row" style="margin: auto; margin-left: 47px; margin-top: 20px">
      <div class="col-3" v-for="(dsh, idx) in main_dash_board_list" :key="idx">
        <img class="image" :src="dsh.img" />
        <p class="content">{{ dsh.txt }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  //   components: {

  //   },
  mounted() {
    var temp = [];
    this.dash_board_list.forEach((el) => {
      temp.push(el.permissions);
    });
    this.fist_check_permission(temp);
  },
  data() {
    return {
      dash_board_list: [
        {
          permissions: ["is_staff", "is_receptionist"],
          img: require("../../src/assets/icon/order-box.png"),
          txt: "Orders",
        },
        {
          permissions: ["is_staff", "is_barista"],
          img: require("../../src/assets/icon/drink.png"),
          txt: "Drink Order",
        },
        {
          permissions: ["is_staff", "is_chef"],
          img: require("../../src/assets/icon/food.png"),
          txt: "Food Order",
        },
        // {permissions: ['is_staff', ], img: require('../../src/assets/icon/order-detail.png'), txt: 'Order Detail'},
        {
          permissions: ["is_staff", "is_purchesing"],
          img: require("../../src/assets/icon/add-rm.png"),
          txt: "Add RM",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/raw-material.png"),
          txt: "Raw Material",
        },
        {
          permissions: ["is_staff", "is_cheff"],
          img: require("../../src/assets/icon/frame.png"),
          txt: "Pickup RM",
        },
        {
          permissions: ["is_staff", "is_cheff", "is_barista"],
          img: require("../../src/assets/icon/add-product.png"),
          txt: "Add Product",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/product.png"),
          txt: "Product",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/customer.png"),
          txt: "Customer",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/promotion.png"),
          txt: "Promotion",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/user-status.png"),
          txt: "User Status",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/report.png"),
          txt: "Report",
        },
      ],
      main_dash_board_list: [],
    };
  },
  methods: {
    check_permission(permissions) {
      console.log(permissions, "permissions");
      for (let index = 0; index < permissions.length; index++) {
        if (this.$store.state.auth.userInfo[permissions[index]]) {
          return true;
        }
      }
      return false;
    },
    fist_check_permission(permissions) {
      permissions.forEach((permission, idx) => {
        permission.forEach((el) => {
          if (this.$store.state.auth.userInfo[el]) {
            this.main_dash_board_list.push(this.dash_board_list[idx]);
          }
        });
      });
      console.log(this.main_dash_board_list)
      // for (let index = 0; index < dsh.length + 1; index++) {
      //   for (let idx = 1; idx < dsh.length; idx++) {
      //     console.log(dsh[index].txt, dsh[idx].txt, 'coordinates')
      //     if (dsh[index].txt == dsh[idx].txt) {
      //       console.log(dsh[index], index, idx)

      //       dsh.splice(index, 1)
      //     }
      //   }
      // }
    },
  },
};
</script>

<style scoped>
body {
  background-color: white;
}
.not_allowed {
  display: none;
  width: 0px;
  height: 0px;
}
.title {
  width: 100%;
  height: 59px;
  background-color: #2f414e;
  text-align: center;
  font-size: 36px;
  font-weight: 700;
  color: white;
}
.col-3 {
  width: 100%;
  margin-top: 60px;
  cursor: pointer;
}

.content {
  /* height: 36px; */
  color: white;
  font-size: 28px;
  position: absolute;
}
.row1 {
  width: 100%;
  height: 168px;
  margin-top: 29px;
}
.row2 {
  width: 100%;
  height: 168px;
  margin-top: 45px;
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
</style>