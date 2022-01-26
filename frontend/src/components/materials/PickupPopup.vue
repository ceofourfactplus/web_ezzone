<template>
  <div>
    <div class="show-pickup-popup">
      <!-- Nav -->
      <div class="row" style="margin-top: 10px;">
        <div class="col-11 w-100 txt-for-add" style="width: 100%; white-space: nowrap; overflow-x: auto;">{{item.name}}</div>
        <div class="col-1 w-100">
          <img
            @click="$emit('show_status')"
            src="../../assets/icon/Union.png"
            style="
              top: 15px;
              right: 10px;
              position: absolute;
              width: 25px;
              height: 25px;
            "
          />
        </div>
      </div>
      <div class="content-wrapper">
        <div class="row">
          <div class="col-5 w-100">
            <!-- Select Image -->
            <label id="select_img">
              <img :src="show_img" class="image" />
            </label>
          </div>
          <div class="col-7 w-100 right-wrapper">
            <!-- Qty -->
            <div class="row" style="margin-top: 20px;">
              <div class="col-12">
                <p class="font-pickup-popup">
                  <span style="font-size: 28px;">Qty</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {{ item.remain }}&nbsp;&nbsp;&nbsp;&nbsp; {{ item.unit_set.unit }}
                </p>
              </div>
            </div>
            <!-- Pickup Amount -->
            <div class="row" style="margin-top: 20px;">
              <div class="col-12">
                <p class="font-pickup-popup">
                  <span style="font-size: 28px;">Pickup</span>&nbsp;:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <input
                    class="pickup-input"
                    type="text"
                    :disabled="item.remain == 0"
                    v-model="pickup_amount"
                    @click="pickup_amount = null"
                  />
                </p>
              </div>
            </div>
            <p v-if="parseInt(pickup_amount) > item.remain" style="color: #ff6d6d; font-size: 20px; margin: -5px 0px 0px 60px;">Not Enough Stuff</p>
          </div>
        </div>
      </div>
      <div>
        <button :disabled="parseInt(this.pickup_amount) > item.remain" class="btn-confirm" @click="confirm">
          <span class="icon-save"></span>Confirm
        </button>
      </div>
    </div>
    <!-- Card Popup -->
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img src="../../assets/icon/btn-pass.png" />
      </div>
      <div class="main-text">Pickup successfully</div>
    </div>
  </div>
</template>


<script>
export default {
  name: "PickupPopup",
  props: ["item"],
  data() {
    return {
      show_status: false,
      alert: false,
      show_img: this.item.img,
      name: "",
      qty: 0,
      pickup_amount: 0,
    };
  },
  mounted() {},
  methods: {
    onFileChange(e) {
      this.show_img = e.target.files[0];
      if (this.show_img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.show_img);
      }
    },
    confirm() {
        this.alert = true
        setTimeout(() => {
          this.alert = false;
        }, 2000);
        this.$emit("confirm", this.pickup_amount, this.item)
        this.name = ''
        this.qty = 0
        this.pickup_amount = 0
    }
  },
};
</script>

<style scoped>
.font-pickup-popup {
  font-size: 24px;
  font-weight: bold;
  text-align: left;
}
.card {
    width: 542px;
    height: 319px
}
.btn-confirm {
  white-space: nowrap;
  width: 167px;
  height: 45px;
  margin-top: 15px;
  border: 1px solid #50d1aa;
  box-sizing: border-box;
  border-radius: 10px;
  font-size: 24px;
  padding-right: 3%;
  color: #50d1aa;
  background: transparent;
  text-align: right;
  line-height: 27px;
}
span.icon-save {
  background: url("../../assets/icon/correct.png") no-repeat transparent;
  transform: rotate(180deg);
  background-size: 30px;
  float: left;
  margin-left: -4px;
  width: 30px;
  height: 30px;
}
.pickup-input {
  width: 121px;
  height: 50px;
  background: #717171;
  border-radius: 10px;
}
.right-wrapper {
  text-align: left;
  width: 299px;
  height: 210px;
  font-size: 30px;
  color: white;
  margin: 20px 20px 0px -10px;
}
.content-wrapper {
  width: 575px;
  height: 205px;
  margin: 20px 20px 5px 20px;
  background: #303344;
  border-radius: 30px;
}
.show-pickup-popup {
  width: 616.86px;
  height: 385px;
  top: 20%;
  left: 12%;
  position: absolute;
  background-color: #252836;
  border: 2px solid #ea7c69;
  border-radius: 20px;
}
.image {
  width: 160px;
  height: 160px;
  border-radius: 25px;
}
#select_img {
  width: 160px;
  height: 160px;
  border-radius: 25px;
  margin: 20px 0px 0px -10px;
  background-color: #717171;
}
.txt-for-add {
  font-weight: bold;
  font-size: 36px;
  line-height: 56px;
  text-align: center;
  width: 85%;
  color: white;
  white-space: nowrap;
  overflow-x: auto;
  margin-left: 12%;
}
.edit-block {
  position: absolute;
  width: 74px;
  height: 28.23px;
  left: 55px;
  top: 280px;
  background-color: #c4c4c4;
  border-radius: 5px;
  background-image: url("../../assets/icon/el_camera.png");
  background-position: 10% 50%;
  background-size: contain;
  background-repeat: no-repeat;
  font-size: 18px;
  color: #000000;
  font-weight: bold;
  text-indent: 30px;
  background-size: 25px;
}
</style>