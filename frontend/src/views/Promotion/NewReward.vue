<template>
  <div>
    <nav-app :save="true" @save="save">New Reward</nav-app>
    <div class="card-content">
      <div class="row">
        <!-- Left Side -->
        <div class="col-8 w-100" style="margin-left: 15px;">
          <!-- Input -->
          <div class="row">
            <div class="col-12 w-100">
              <input type="text" class="input-top" />
            </div>
          </div>
          <!-- Value -->
          <div class="row" style="margin-top: 15px;">
            <div class="col-8 w-100">
              <div class="row">
                  <div class="col-6 w-100 txt">Value</div>
                  <div class="col-1 w-100 txt">:</div>
                  <div class="col-5 w-100"><input type="text" class="input-promotion" style="width: 298px;"></div>
              </div>
            </div>
          </div>
          <!-- Cost -->
          <div class="row" style="margin-top: 15px;">
            <div class="col-8 w-100">
              <div class="row">
                  <div class="col-6 w-100 txt">Cost</div>
                  <div class="col-1 w-100 txt">:</div>
                  <div class="col-5 w-100"><input type="text" class="input-promotion" style="width: 298px;"></div>
              </div>
            </div>
          </div>
          <!-- Qty -->
          <div class="row" style="margin-top: 15px;">
            <div class="col-8 w-100">
              <div class="row">
                  <div class="col-6 w-100 txt">Qty</div>
                  <div class="col-1 w-100 txt">:</div>
                  <div class="col-5 w-100"><input type="text" class="input-promotion" style="width: 298px;"></div>
              </div>
            </div>
          </div>
          <!-- Point -->
          <div class="row" style="margin-top: 15px;">
            <div class="col-8 w-100">
              <div class="row">
                  <div class="col-6 w-100 txt">Point</div>
                  <div class="col-1 w-100 txt">:</div>
                  <div class="col-5 w-100"><input type="text" class="input-promotion" style="width: 298px;"></div>
              </div>
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
    <!-- PP Name -->
    <div class="description-card">
      <div class="row">
        <div
          class="col-12 w-100"
          style="color: white; font-size: 30px; text-align: left; margin-left: 34px;"
        >
          PP Name :
        </div>
      </div>
      <div class="row">
          <div class="col-12">
              <textarea style="width: 600px; height: 80px; background: #717171;"></textarea>
          </div>
      </div>
    </div>
    <!-- Desciption -->
    <div class="description-card">
      <div class="row">
        <div
          class="col-12 w-100"
          style="color: white; font-size: 30px; text-align: left; margin-left: 34px;"
        >
          Description :
        </div>
      </div>
      <div class="row">
          <div class="col-12">
              <textarea style="width: 600px; height: 80px; background: #717171;"></textarea>
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
      start_date: null,
      end_date: null,
      end_redeem: null,
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
  width: 428px;
  height: 50px;
  background: rgb(113, 113, 113);
  border-radius: 12px;
  color: white;
  float: left;
  margin: 10px 0px 0px 0px;
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
  color: white;
  text-align: left;
}
.card-content {
  width: 670px;
  height: 322px;
  background: #303344;
  border-radius: 20px;
  margin: 15px 0px 0px 27px;
  font-size: 30px;
  font-weight: bold;
}
template {
  color: white;
}
</style>