<template>
  <div>
    <div class="title">Manager</div>
    <div class="row" style="margin: auto; margin-left: 30px; margin-right: 30px; margin-top: 0px;">
      <div class="col-3" v-for="(dsh, idx) in main_dash_board_list" :key="idx">
        <img class="image" :src="dsh.img" />
        <p :style="dsh.margin" class="content">{{ dsh.txt }}</p>
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
    this.first_check_permission(temp);
  },
  data() {
    return {
      dash_board_list: [
        {
          permissions: ["is_staff", "is_receptionist"],
          img: require("../../src/assets/icon/order-box.png"),
          margin: 'margin-left: 33px',
          txt: "Orders",
        },
        {
          permissions: ["is_staff", "is_barista"],
          img: require("../../src/assets/icon/drink.png"),
          margin: 'margin-left: 0px',
          txt: "Drink Order",
        },
        {
          permissions: ["is_staff", "is_chef"],
          img: require("../../src/assets/icon/food.png"),
          margin: 'margin-left: 0px',
          txt: "Food Order",
        },
        {
          permissions: ["is_staff", "is_purchesing"],
          img: require("../../src/assets/icon/add-rm.png"),
          margin: 'margin-left: 30px',
          txt: "Add RM",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/raw-material.png"),
          margin: 'margin-left: 0px',
          txt: "Raw Material",
        },
        {
          permissions: ["is_staff", "is_cheff"],
          img: require("../../src/assets/icon/frame.png"),
          margin: 'margin-left: 8px',
          txt: "Pickup RM",
        },
        {
          permissions: ["is_staff", "is_cheff", "is_barista"],
          img: require("../../src/assets/icon/add-product.png"),
          margin: 'margin-left: 0px',
          txt: "Add Product",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/product.png"),
          margin: 'margin-left: 30px',
          txt: "Product",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/customer.png"),
          margin: 'margin-left: 14px',
          txt: "Customer",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/promotion.png"),
          margin: 'margin-left: 5px',
          txt: "Promotion",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/user-status.png"),
          margin: 'margin-left: 4px',
          txt: "User Status",
        },
        {
          permissions: ["is_staff"],
          img: require("../../src/assets/icon/report.png"),
          margin: 'margin-left: 33px',
          txt: "Report",
        },
      ],
      main_dash_board_list: [],
    };
  },
  methods: {
    first_check_permission(permissions) {
      permissions.forEach((permission, idx) => {
        permission.forEach((el) => {
          if (this.$store.state.auth.userInfo[el]) {
            this.main_dash_board_list.push(this.dash_board_list[idx]);
          }
        });
      });
      this.main_dash_board_list = [...new Set(this.main_dash_board_list)]
      console.log(this.main_dash_board_list)
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
  text-align: center;
  font-size: 48px;
  font-weight: 800;
  line-height: 80px;
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