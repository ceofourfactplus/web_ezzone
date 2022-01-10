<template>
  <div>
    <nav-app :save="true" @save="save">New Package</nav-app>
    <div class="card-content">
      <div class="row">
        <!-- Left Side -->
        <div class="col-8 w-100">
          <!-- Input -->
          <div class="row">
            <div class="col-12 w-100">
              <input type="text" class="input-top" />
            </div>
          </div>
          <!-- Start Date -->
          <div class="row" style="margin-top: 20px">
            <div class="col-12 w-100 txt">
              Start
              Date&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;23/1/2565&nbsp;&nbsp;<input
                type="text"
                class="input-date"
              />
            </div>
          </div>
          <!-- Amount Day -->
          <div class="row" style="margin-top: 20px">
            <div class="col-12 w-100 txt" style="margin-left: 8px">
              Amount Day&nbsp;:&nbsp;<input
                type="text"
                class="input-promotion"
                style="width: 204px"
              />
            </div>
          </div>
          <!-- Description -->
          <div class="row" style="margin-top: 20px">
            <div class="col-12 w-100 txt" style="margin-left: 7px">
              <textarea
                style="
                  width: 428px;
                  height: 110px;
                  background: #717171;
                  borde-radius: 10px;
                  margin-left: 24px;
                "
                placeholder="Description"
              ></textarea>
            </div>
          </div>
        </div>
        <!-- Right Side -->
        <div class="col-4 w-100">
          <div
            class="col-12 w-100"
            style="color: white; margin: 15px 10px 0px 0px"
          >
            Status&nbsp;:&nbsp; <Switch style="top: 9px" />
          </div>
          <div class="col-12 w-100" style="margin-top: 30px">
            <!-- Image -->
            <label id="select_img" for="file" style="margin-top: 0px">
              <img :src="show_img" class="image" v-if="show_img != null" />
            </label>
            <input
              type="file"
              @change="onFileChange"
              style="display: none"
              id="file"
              class="raw-image"
            />
          </div>
        </div>
      </div>
    </div>
    <!-- Product in Package -->
    <div class="row" style="margin-top: 15px; margin-left: -40px">
      <div
        class="col-7 w-100"
        style="font-size: 36px; font-weight: bold; color: white"
      >
        Product in Package
      </div>
      <div class="col-2 w-100"><button class="btn-ghost">+ New</button></div>
      <div class="col-3 w-100">
        <button class="btn-save" @click="edit()">
          <span class="icon-save"></span>Delete
        </button>
      </div>
    </div>
    <!-- Table -->
    <div class="table" style="margin-top: 10px">
      <div class="table-header">
        <div
          class="row"
          style="font-size: 24px; font-weight: bold; color: white"
        >
          <div class="col-1 w-100">
            <div class="checkbox-white">
              <input
                type="checkbox"
                :value="true"
                style="margin-top: 4px; right: 0px; left: 23px; bottom: 3px"
              />
            </div>
          </div>
          <div class="col-5 w-100">Product</div>
          <div class="col-3 w-100">Topping</div>
          <div class="col-1 w-100">Qty</div>
          <div class="col-2 w-100">Price</div>
        </div>
      </div>
      <div class="table-item">
        <div class="row" style="font-size: 20px; color: white; line-height: 1">
          <div class="col-1 w-100">
            <div class="checkbox-orange">
              <input
                type="checkbox"
                style="margin-top: -2px; left: 23px;"
              />
            </div>
          </div>
          <div class="col-5 w-100" style="margin-left: 10px; text-align: left">
            กะเพราไก่
          </div>
          <div class="col-3 w-100">ไข่ข้น</div>
          <div class="col-1 w-100">69</div>
          <div class="col-2 w-100">39</div>
        </div>
      </div>
      <!-- Total -->
      <div class="table-item">
        <div
          class="row"
          style="font-size: 24px; color: white; line-height: 14px"
        >
          <div class="col-6 w-100"></div>
          <div class="col-4 w-100" style="text-align: right;">Total</div>
          <div class="col-2 w-100">100</div>
        </div>
      </div>
      <!-- Discount Total Price -->
      <div class="table-item">
        <div
          class="row"
          style="font-size: 24px; color: white; line-height: 14px"
        >
        <div class="col-6 w-100"></div>
          <div class="col-4 w-100" style="text-align: right;">Discount Total Price</div>
          <div class="col-2 w-100">100</div>
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
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";

export default {
  name: "NewPackage",
  components: {
    NavApp,
    Switch,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
  },
  data() {
    return {
      is_staff: false,
      alert: false,
      id: null,
      promotion: null,
      start_date: null,
      img: null,
      amount_day: null,
      discount_price: null,
      normal_price: null,
      status: null,
      total_amount: null,
      description: null,
      img: null,
      show_img: null,
    };
  },
  methods: {
    save() {
      this.alert = true;
      setTimeout(() => {
        this.alert = false;
        this.$router.push({ name: "Point" });
      }, 2000);
    },
    onFileChange(e) {
      console.log(e, "e");
      this.img = e.target.files[0];
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
      console.log(this.img, "img");
    },
  },
};
</script>

<style scoped>
.btn-ghost {
  border-color: #65b0f6;
  color: #65b0f6;
  width: 119px;
  height: 50px;
  margin: 0px 25px 0px 0px;
}
.btn-save {
  font-size: 24px;
  color: #ff7ca3;
  border-color: #ff7ca3;
  border-radius: 10px;
  text-align: center;
  background: transparent;
  line-height: 21px;
  width: 140px;
  height: 50px;
}
span.icon-save {
  background: url("../../assets/icon/bin.png") no-repeat transparent;
  background-size: 18px;
  float: left;
  margin-left: 17px;
  width: 19px;
  height: 27px;
}
#select_img {
  width: 170px;
  height: 170px;
  border-radius: 20px;
  margin-right: 12px;
  background-color: #c4c4c4;
}
.image {
  width: 170px;
  height: 170px;
  border-radius: 20px;
}
.colon {
  font-size: 30px;
  text-align: center;
  margin: 20px 0px 0px -40px;
  color: white;
}
.input-top {
  width: 215px;
  height: 50px;
  background: rgb(113, 113, 113);
  border-radius: 12px;
  color: white;
  float: left;
  margin: 10px 0px 0px 20px;
}
.input-code {
  width: 167px;
  height: 53px;
  background: #717171;
  border-radius: 10px;
  color: white;
}
#txt-right-side {
  margin-left: -40px;
}
.txt {
  font-size: 30px;
  font-weight: bold;
  color: white;
  /* text-align: left;
  margin: 20px 0px 0px 120px; */
}
.card-content {
  width: 670px;
  height: 342px;
  background: #303344;
  border-radius: 20px;
  margin: 15px 0px 0px 27px;
  font-size: 30px;
  font-weight: bold;
}
.checkbox-white input:checked::after {
  font-size: 20px;
  top: 1px;
  left: 1px;
}
.checkbox-white input::before {
  height: 30px;
  width: 30px;
}
.checkbox-white input {
  height: 28px;
  width: 28px;
}
.checkbox-orange input:checked::after {
  font-size: 20px;
  top: 4px;
  left: 4px;
}
.checkbox-orange input::before {
  height: 30px;
  width: 30px;
}
.checkbox-orange input {
  height: 28px;
  width: 28px;
}
</style>