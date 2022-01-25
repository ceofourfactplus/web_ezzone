<template>
  <div>
    <nav-app :url_name="'AllReward'">{{
      $store.state.promotion.reward_detail.reward
    }}</nav-app>

    <!-- AreaBlockItem -->
    <div
      class="table-item"
      style="
        margin-left: 27px;
        margin-right: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius: 20px;
        height: 820px;
        width: 762px;
      "
    >
      <!-- Select Bar -->
      <div class="row BlockItem" style="margin-left: 16px;">
        <div class="col-6 w-100">
          <input
            type="text"
            style="
              background: #717171;
              height: 50px;
              width: 282px;
              font-size: 28px;
              text-align: center;
            "
            readonly
            value="Pre-order"
            v-if="$store.state.promotion.reward_detail.is_per_order"
          />
          <input
            type="text"
            style="
              background: #717171;
              height: 50px;
              width: 282px;
              font-size: 28px;
              text-align: center;
            "
            readonly
            value="Received @ Counter"
            v-else
          />
        </div>
        <div class="col-6 w-100" style="padding: 0px">
          <div class="RedeemItem" @click="popup_status = true"><b>Redeem</b></div>
        </div>
      </div>
      <div class="row BlockImg" style="margin-left: 16px;">
        <div class="col-6 w-100">
          <img
            :src="
              $store.state.promotion.reward_detail.img
            "
            alt=""
            style="width: 282px; height: 298px; border-radius: 20px; border: 1px; solid"
          />
        </div>
        <div class="col-6 w-100 BlockRedeemPoint" style="padding: 0px">
          <div class="RedeemPointItem">
            <dir
              style="height: 60px; margin: 0px; padding: 0px; line-height: 55px"
            >
              <b>Redeem Point</b>
            </dir>
            <div class="table-item BlockPoint">
              <b>{{ $store.state.promotion.reward_detail.point }}</b>
            </div>
            <dir
              style="
                height: 60px;
                margin: 0px;
                padding: 0px;
                line-height: 55px;
                font-size: 28px;
              "
            >
              Value {{ $store.state.promotion.reward_detail.value.split('.')[0] }}&nbsp;฿
            </dir>
          </div>
        </div>
      </div>
      <div class="row AreaDescription">
        <div class="col-12 w-100" style="height: 50px; margin-left: 27px;">
          <b>Description :</b>
        </div>
        <div class="col-12 w-100 BlockDescription">
          {{ $store.state.promotion.reward_detail.description }}
        </div>
      </div>
    </div>
    <!-- Popup -->
    <Redeem v-if="popup_status" @close="popup_status = false" />
    
  </div>
</template>

<script>
export default {
  name: "RewardName",
  components: {
    NavApp,
    SearchBar,
    Redeem,
  },
  mounted() {
  },
  data() {
    return {
      popup_status: false,
      alert: false,
      reward_status: "",
    };
  },
  methods: {
    show_detail() {
        this.popup_status = true; 
    },
    search(val) {
      console.log(val);
    },
  },
};

import NavApp from "../../components/main_component/NavApp.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
import Redeem from "../../components/promotion/Redeem.vue";
</script>

<style scoped>
#clear {
  height: 100%;
  background: green;
  border: 1px solid transparent;
  color: white;
  font-weight: 600;
}
canvas#signature-pad {
  background: white;
  width: 100%;
  height: 100%;
  cursor: crosshair;
}
.wrapper {
  border: 1px solid black;
  border-right: 0;
}
.flex-row {
    margin-top: 20px;
  display: flex;
}

img {
  border-radius: 20px;
}

.BlockItem {
  position: relative;
  font-size: 23px;
  text-align: center;
  padding: 0px;
  margin: 0px;
  top: 30px;
}

.RedeemItem {
  color: #ea7c69;
  font-size: 30px;
  height: 50px;
  width: 308px;
  padding: 10px;
  border-radius: 10px;
  border: 2px solid #ea7c69;
  line-height: 20px;
  margin-left: 0px;
  margin-right: 20px;
}

.BlockImg {
  position: relative;
  font-size: 23px;
  text-align: center;
  padding: 0px;
  margin: 0px;
  top: 60px;
}

.RedeemPointItem {
  color: #fff;
  font-size: 30px;
  height: 298px;
  width: 308px;
  padding-left: 2px;
  padding-right: 2px;
  border-radius: 30px;
  background-color: #ea7c69;
  line-height: 20px;
  margin-left: 0px;
  margin-right: 20px;
}

.BlockPoint {
  height: 178px;
  margin: 0px;
  border-radius: 0px;
  font-size: 106px;
  line-height: 160px;
}

.AreaDescription {
  margin: 20px;
  color: aliceblue;
  width: 615px;
  position: relative;
  font-size: 30px;
  text-align: left;
  padding: 0px;
  margin-left: 27px;
  top: 70px;
}

.BlockDescription {
  height: 305px;
  border-radius: 20px;
  position: relative;
  font-size: 24px;
  text-align: left;
  padding: 0px;
  margin-left: 55px;
}

.AreaPopup {
  color: #fff;
  position: absolute;
  border-radius: 20px;
  width: 590px;
  height: 586px;
  background-color: #252836;
  top: 140px;
  left: 65px;
}

.HeadPopup {
  color: #fff;
  width: 590px;
  position: relative;
  font-size: 37px;
  text-align: center;
  padding: 0px;
  margin: 0px;
}

.AreaRedeemPopup {
  margin-left: 20px;
  margin-right: 20px;
  margin-bottom: 20px;
  width: 550px;
  height: 85%;
  padding: 20px;
}

.RedeemNamePhone {
  width: 243px;
  height: 50px;
  background-color: #717171;
  position: relative;
  font-size: 23px;
  padding: 0px;
  padding-left: 10px;
  margin-left: 12px;
  border-radius: 10px;
  line-height: 45px;
  text-align: left;
}

.RedeemImg {
  width: 243px;
  height: 100%;
  position: relative;
  font-size: 23px;
  text-align: center;
  padding: 0px;
  margin-left: 12px;
  border-radius: 25px;
}

.StatusBlock {
  color: #50d1aa;
  width: 243px;
  height: 50px;
  border-radius: 20px;
  border: 3px solid #50d1aa;
  width: 243px;
  height: 50px;
  position: relative;
  font-size: 23px;
  text-align: center;
  padding: 0px;
  margin-left: 12px;
}

.RedeemNameReward {
  width: 243px;
  height: 50px;
  position: relative;
  font-size: 30px;
  padding: 0px;
  margin-left: 12px;
  border-radius: 10px;
  line-height: 45px;
  padding-left: 10px;
  text-align: left;
}

.RedeemPoint {
  width: 243px;
  height: 50px;
  background-color: #ea7c69;
  position: relative;
  font-size: 26px;
  text-align: center;
  padding: 2px;
  margin-left: 12px;
  border-radius: 10px;
  line-height: 45px;
}

.DetailPoint {
  height: 100%;
  padding: 0px;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}

.AreaSign {
  margin-left: 10px;
  position: relative;
  text-align: left;
  background-color: #717171;
  border-radius: 15px;
  padding-left: 12px;
  padding-top: 5px;
  width: 510px;
  height: 130px;
  left: 12px;
  top: 20px;
  font-size: 28px;
}
</style>