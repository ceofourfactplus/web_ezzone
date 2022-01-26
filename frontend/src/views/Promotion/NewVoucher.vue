<template>
  <div>
    <nav-app :url_name="'Promotion'" :save="true" @save="save">New Voucher</nav-app>
    <div class="card-content">
      <!-- Status & Code -->
      <div class="row">
        <div class="col-6 w-100 head-col">
          Status&nbsp;:&nbsp; <Switch :value="status" @switch="switch_active" style="top: 9px" />
        </div>
        <div class="col-6 w-100 head-col">
          Code&nbsp;:&nbsp;<input type="text" style="width: 167px;" class="input-promotion" v-model="code" />
        </div>
      </div>
      <!-- Image -->
      <div class="row">
        <div class="col-12 w-100" style="padding: 0px; margin-top: 40px;">
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
      <div class="AreaRow">
        <div class="row ">
          <div class="col-5 w-100 txt-promotion">Name</div>
          <div class="col-1 w-100 colon">:</div>
          <div class="col-6 w-100 txt-promotion-right" id="txt-right-side"><input type="text" class="input-promotion" style="width: 99%;" v-model="voucher"></div>
        </div>
        <div class="row">
          <div class="col-5 w-100 txt-promotion">Start Date</div>
          <div class="col-1 w-100 colon">:</div>
          <div class="col-6 w-100 txt-promotion-right" id="txt-right-side">{{ temp_start }}<input type="date" class="input-date" style="position:relative;display:inline-block;margin-left:2%;top:5px;margin-top:11px;" @change="format_date($event, 'start')" ></div>
        </div>
        <div class="row">
          <div class="col-5 w-100 txt-promotion">End Date</div>
          <div class="col-1 w-100 colon">:</div>
          <div class="col-6 w-100 txt-promotion-right" id="txt-right-side">{{ temp_end }}<input type="date" class="input-date" style="position:relative;display:inline-block;margin-left:2%;top:5px;margin-top:11px;" @change="format_date($event, 'end')" ></div>
        </div>
        <div class="row">
          <div class="col-5 w-100 txt-promotion">Qty</div>
          <div class="col-1 w-100 colon">:</div>
          <div class="col-6 w-100 txt-promotion-right" id="txt-right-side"><input type="text" class="input-promotion" style="width: 99%;" v-model="qty"></div>
        </div>
        <div class="row" style="margin-top:5px">
          <div class="col-5 w-100 txt-promotion">Discount</div>
          <div class="col-1 w-100 colon">:</div>
          <div class="col-6 w-100 txt-promotion-right" id="txt-right-side"><input type="text" class="input-promotion" style="width: 99%;" v-model="discount"></div>
        </div>
            
      </div>
    </div>
    <div class="description-card">
      <div class="row">
        <div
          class="col-12 w-100"
          style="color: white; font-size: 30px; text-align: left; margin-left: 34px; margin-top:1%"
        >
          Description :
        </div>
      </div>
      <div class="row">
          <div class="col-12" style="margin-top:2%">
              <textarea style="width: 700px; height: 80px; background: #717171;" v-model="description"></textarea>
          </div>
      </div>
    </div>
    <!-- Card Popup -->
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import SavePopup from "../../components/main_component/SavePopup.vue"
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import { api_promotion } from "../../api/api_promotion"

export default {
  name: "NewVoucher",
  components: {
    SavePopup,
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
      voucher: null,
      code: null,
      img: null,
      discount: null,
      start_date: null,
      temp_start: null,
      end_date: null,
      temp_end: null,
      is_percent: false,
      description: null,
      qty: null,
      status: true,
      show_img: null,
    };
  },
  methods: {
    save() {
      if (this.discount.endsWith('%')) {
        this.is_percent = true
        this.discount = parseInt(this.discount.replace('%', ''))
      }
      const data = new FormData();
      data.append("voucher", this.voucher);
      data.append("code", this.code);
      data.append("img", this.img, this.img.name);
      data.append("discount", this.discount);
      data.append("start_date", this.start_date);
      data.append("end_date", this.end_date);
      data.append("qty", this.qty);
      data.append("is_percent", this.is_percent);
      data.append("status", this.status);
      data.append("update_by_id", this.$store.state.auth.userInfo.id);
      data.append("create_by_id", this.$store.state.auth.userInfo.id);

      api_promotion.post('voucher/', data).then((response) => {
        console.log(response.data)
        this.alert = true;
        setTimeout(() => {
          this.alert = false;
          this.$router.push({ name: "Promotion" });
        }, 2000);
      })
    },
    onFileChange(e) {
      console.log(e.target, "e");
      this.img = e.target.files[0];
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
      console.log(this.img, "img");
    },
    format_date(e, name) {
      if (name == "start") {
        this.start_date = e.target.value
        var temp_date = e.target.value.split("-");
        this.temp_start = `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
      }
      if (name == "end") {
        this.end_date = e.target.value
        var temp_date = e.target.value.split("-");
        this.temp_end = `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
      }
    },
    switch_active() {
      this.status = !this.status
    },
  },
};
</script>

<style scoped>
#select_img {
  width: 170px;
  height: 170px;
  border-radius: 25px;
  margin-right: 12px;
  background-color: #c4c4c4;
}
.image {
  width: 170px;
  height: 170px;
  border-radius: 25px;
}
.head-col {
  color: white;
  font-size: 36px;
  font-weight: bold;
  margin-top: 18px;
}
.colon {
  font-size: 32px;
  text-align: center;
  margin: 18px 0px 0px -40px;
  color: white;
  
}
#txt-right-side {
  margin-left: -40px;
}
.txt-promotion {
  font-size: 32px;
  color: white;
  text-align: left;
  margin-top: 20px;
  padding-left: 40%;
  font-weight: bold;
}
.txt-promotion-right {
  width: 100%;
  font-size: 30px;
  color: white;
  text-align: left;
  margin: 17px 0px 0px 0px;
}
.card-content {
  width: 765px;
  height: 675px;
  background: #303344;
  border-radius: 20px;
  margin: 15px 0px 0px 27px;
}
body {
  color: white;
}
</style>