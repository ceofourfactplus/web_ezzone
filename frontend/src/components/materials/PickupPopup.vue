<template>
  <div>
    <div class="show-pickup-popup">
      <!-- Nav -->
      <div class="row">
        <div class="col-3"></div>
        <div class="col-6 txt-for-add" style="width: 100%">Pickup</div>
        <div class="col-3">
          <img
            @click="$emit('show_status')"
            src="../../assets/icon/Union.png"
            style="
              top: 10px;
              right: 10px;
              position: absolute;
              width: 50px;
              height: 50px;
            "
          />
        </div>
      </div>
      <div class="content-wrapper">
        <div class="row">
          <div class="col-4">
            <!-- Select Image -->
            <div class="row">
              <div class="col-12" style="padding: 0px">
                <label id="select_img" for="file">
                  <img :src="show_img" class="image" v-if="show_img != null" />
                  <div class="edit-block">Edit</div>
                </label>
                <input
                  type="file"
                  @change="onFileChange"
                  style="display: none; width: "
                  id="file"
                  class="raw-image"
                />
              </div>
            </div>
          </div>
          <div class="col-8 right-wrapper">
            <!-- Name -->
            <div class="row" style="text-align: left">
              <div class="col-12">
                <p>Name&nbsp;&nbsp;: {{ item.name }}</p>
              </div>
            </div>
            <!-- Qty -->
            <div class="row" style="margin-top: 20px; text-align: left">
              <div class="col-12">
                <p>
                  Qty&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: {{ item.qty }}
                </p>
              </div>
            </div>
            <!-- Pickup Amount -->
            <div class="row" style="margin-top: 20px; text-align: left">
              <div class="col-12">
                <p>
                  Pickup&nbsp;:
                  <input
                    class="pickup-input"
                    type="text"
                    v-model="pickup_amount"
                    @click="pickup_amount = null"
                  />
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <button class="btn-confirm" @click="confirm">
          <span class="icon-save"></span>Confirm
        </button>
      </div>
    </div>
    <!-- Card Popup -->
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img src="../../assets/icon/btn-pass.png" alt="" />
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
      show_img: null,
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
          this.$emit("show_status")
        }, 2000);
        this.name = ''
        this.qty = 0
        this.pickup_amount = 0
    }
  },
};
</script>

<style scoped>
.card {
    width: 542px;
    height: 319px
}
.btn-confirm {
  width: 167px;
  height: 45px;
  margin-top: 15px;
  border: 1px solid #50d1aa;
  box-sizing: border-box;
  border-radius: 10px;
  font-size: 24px;
  color: #50d1aa;
  background: transparent;
}
span.icon-save {
  background: url("../../assets/icon/correct.png") no-repeat transparent;
  background-size: 30px;
  float: left;
  margin-left: 10px;
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
  margin: 25px 20px 0px 40px;
}
.content-wrapper {
  width: 575px;
  height: 260px;
  margin: 15px 20px 0px 20px;
  background: #303344;
  border-radius: 30px;
}
.show-pickup-popup {
  width: 616.86px;
  height: 406px;
  top: 7%;
  left: 7%;
  position: absolute;
  background-color: #252836;
  border: 2px solid #ea7c69;
  border-radius: 20px;
}
.image {
  width: 220px;
  height: 220px;
  border-radius: 25px;
}
#select_img {
  width: 220px;
  height: 220px;
  border-radius: 25px;
  margin: 20px 0px 0px 25px;
  background-color: #717171;
}
.txt-for-add {
  font-weight: bold;
  font-size: 48px;
  line-height: 56px;
  text-align: center;
  width: 100%;
  color: white;
}
.edit-block {
  position: absolute;
  width: 74px;
  height: 28.23px;
  left: 45px;
  top: 270px;
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