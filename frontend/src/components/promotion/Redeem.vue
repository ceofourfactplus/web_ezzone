<template>
  <div>
    <!-- Popup -->
    <div class="AreaPopup">
      <div class="HeadPopup" style="left: 20px">
        <b>Redeem</b>
        <img
          src="../../assets/img/btn-close.png"
          alt=""
          style="right: -176px; position: relative"
          @click="$emit('close')"
        />
      </div>
      <div class="table-item AreaRedeemPopup">
        <div class="row">
          <div class="col-6 StatusBlock" style="color: #FF7CA3; border: 3px solid #FF7CA3;" v-if="$store.state.promotion.customer_point[0].point < $store.state.promotion.reward_detail.point"><b>Not enough points</b></div>
          <div class="col-6 StatusBlock" @click="save" v-else><b>Confirm Redeem</b></div>
          <div class="col-6 RedeemNamePhone" style="margin-bottom: 5px">
            {{ $store.state.promotion.customer.nick_name }}
          </div>
        </div>
        <div class="row" style="height: 250px; padding-top: 10px">
          <div class="col-6 RedeemImg" style="background-color: #717171">
            <img
              :src="
                require(`../../../../backend${$store.state.promotion.reward_detail.img}`)
              "
              style="height: 245px; width: 243px"
            />
          </div>
          <div class="col-6 RedeemImg">
            <div
              class="RedeemNamePhone"
              style="margin: 0px; margin-bottom: 15px"
            >
              {{
                phone_number_layout(
                  $store.state.promotion.customer.phone_number
                )
              }}
            </div>
            <div
              class="RedeemNameReward"
              style="margin: 0px; margin-bottom: 15px"
            >
              <b>{{ $store.state.promotion.reward_detail.reward }}</b>
            </div>
            <div
              class="row RedeemPoint"
              style="margin: 0px; margin-bottom: 15px"
            >
              <div
                class="col-6 w-100 DetailPoint"
                style="background-color: #303344"
              >
                <b>{{ $store.state.promotion.reward_detail.point }}</b>
              </div>
              <div class="col-6 w-100 DetailPoint"><b>Point</b></div>
            </div>
            <div class="RedeemNamePhone" style="margin: 0px">
              <select
                v-model="$store.state.promotion.reward_detail.is_pre_order"
                style="background: #717171; height: 50px; width: 233px"
              >
                <option :value="false">Received @ Counter</option>
                <option :value="true">Pre-order</option>
              </select>
            </div>
          </div>
        </div>
        <!-- Sign Here -->
        <div class="flex-row">
          <div class="wrapper">
            <canvas id="signature-pad" width="510"></canvas>
            <img
              src="../../assets/icon/eraser.png"
              id="clear"
              style="
                position: absolute;
                height: 50px;
                padding: 0px;
                right: 40px;
              "
            />
          </div>
        </div>
      </div>
    </div>
    <!-- Card Popup -->
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img
          src="../../assets/icon/btn-pass.png"
          style="width: 150px; height: 150px"
        />
      </div>
      <div class="main-text">Saved successfully</div>
    </div>
  </div>
</template>

<script>
import { api_promotion} from "../../api/api_promotion"
export default {
  name: "Redeem",
  data() {
    return {
        alert: false,
    };
  },
  mounted() {
    this.signature_pad();
  },
  methods: {
    signature_pad() {
      var canvas = document.getElementById("signature-pad");
      function resizeCanvas() {
        var ratio = Math.max(window.devicePixelRatio || 1, 1);
        canvas.width = canvas.offsetWidth * ratio;
        canvas.height = canvas.offsetHeight * ratio;
        canvas.getContext("2d").scale(ratio, ratio);
      }
      window.onresize = resizeCanvas;
      resizeCanvas();

      var signaturePad = new SignaturePad(canvas, {
        backgroundColor: "rgb(250,250,250)",
      });
      document.getElementById("clear").addEventListener("click", function () {
        signaturePad.clear();
      });
    },
    save() {
      var canvas = document.getElementById("signature-pad");
      canvas.toBlob((blob) => {
          const data = new FormData();
            data.append("customer_id", this.$store.state.promotion.customer.id);
            data.append("reward_id", this.$store.state.promotion.reward_detail.id);
            data.append("signature", blob, `${this.$store.state.promotion.customer.email.split('@')[0]}-signature.png`);
            data.append("point", this.$store.state.promotion.reward_detail.point);
            data.append("qty", this.$store.state.promotion.reward_detail.qty);
            data.append("update_by_id", this.$store.state.auth.userInfo.id);
            data.append("create_by_id", this.$store.state.auth.userInfo.id);

            api_promotion.post('exchange-history/', data).then((response) => {
                this.alert = true
                setTimeout(() => {
                    this.alert = false
                    this.$emit('close')
                }, 2000)
                console.log(response.data)
            })
      });
    },
    phone_number_layout(phone) {
      if (phone != null) {
        return (
          phone.substr(0, 3) +
          "-" +
          phone.substr(3, 3) +
          "-" +
          phone.substr(6, 4)
        );
      } else {
        return "";
      }
    },
  },
};
</script>
<style scoped>
canvas#signature-pad {
  background: white;
  width: 100%;
  height: 140px;
  cursor: crosshair;
}
.wrapper {
  border: 1px solid black;
  border-right: 0;
  width: 510px;
}
.flex-row {
  margin-top: 20px;
  display: flex;
}

img {
  border-radius: 20px;
}

.BlockItem {
  width: 672px;
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
  width: 672px;
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
  width: 100%;
  height: 305px;
  border-radius: 20px;
  position: relative;
  font-size: 24px;
  text-align: left;
  padding: 0px;
  margin-left: 14px;
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