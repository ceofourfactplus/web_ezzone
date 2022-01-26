<template>
  <div>
    <nav-app :url_name="'Promotion'" :save="true" @save="edit">Voucher Detail</nav-app>
    <div class="card-content">
      <!-- Status & Code -->
      <div class="row">
        <div class="col-6 w-100 head-col">
          Status&nbsp;:&nbsp; <Switch :value="voucher_item.status" @switch="switch_active" style="top: 9px" />
        </div>
        <div class="col-6 w-100 head-col">
          Code&nbsp;:&nbsp;<input type="text" class="input-code" v-model="voucher_item.code" />
        </div>
      </div>
      <!-- Image -->
      <div class="row">
        <div class="col-12 w-100" style="padding: 0px; margin-top: 40px;">
          <label id="select_img" for="file" style="margin-top: 0px">
            <img :src="show_img" class="image" v-if="show_img != null" />
            <img :src="voucher_item.img" class="image" v-else />
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
        <div class="row" style="margin-top:5px">
          <div class="col-5 w-100 txt-promotion">Name</div>
          <div class="col-1 w-100 colon">:</div>
          <div class="col-6 w-100 txt-promotion-right" id="txt-right-side"><input type="text" class="input-right-side" style="width: 99%;" v-model="voucher_item.voucher"></div>
        </div>
        <div class="row">
          <div class="col-5 w-100 txt-promotion">Start Date</div>
          <div class="col-1 w-100 colon">:</div>
          <div class="col-6 w-100 txt-promotion-right" id="txt-right-side">{{ format_date_show(voucher_item.start_date) }}<input type="date" class="input-date" style="position:relative;display:inline-block;margin-left:2%;top:5px;margin-top:11px;" @change="format_date($event, 'start')" ></div>
        </div>
        <div class="row">
          <div class="col-5 w-100 txt-promotion">End Date</div>
          <div class="col-1 w-100 colon">:</div>
          <div class="col-6 w-100 txt-promotion-right" id="txt-right-side">{{ format_date_show(voucher_item.end_date) }}<input type="date" class="input-date" style="position:relative;display:inline-block;margin-left:2%;top:5px;margin-top:11px;" @change="format_date($event, 'end')" ></div>
        </div>
        <div class="row">
          <div class="col-5 w-100 txt-promotion">Qty</div>
          <div class="col-1 w-100 colon">:</div>
          <div class="col-6 w-100 txt-promotion-right" id="txt-right-side"><input type="text" class="input-right-side" style="width: 99%;" v-model="voucher_item.qty"></div>
        </div>
        <div class="row" style="margin-top:5px">
          <div class="col-5 w-100 txt-promotion">Discount</div>
          <div class="col-1 w-100 colon">:</div>
          <div class="col-6 w-100 txt-promotion-right" id="txt-right-side"><input type="text" class="input-right-side" style="width: 99%;" v-model="voucher_item.discount"></div>
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
              <textarea style="width: 700px; height: 80px; background: #717171;" v-model="voucher_item.description"></textarea>
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
  name: "VoucherDetail",
  components: {
    NavApp,
    Switch,
    SavePopup,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
  },
  data() {
    return {
      is_staff: false,
      alert: false,
      new_img: false,
      voucher_item: {},
      img: null,
      show_img: null,
    };
  },
  methods: {
    fetchVoucher() {
        api_promotion.get(`voucher/${this.$route.params.id}`).then((response) => {
            console.log(response.data, 'voucher')
            this.voucher_item = response.data[0]
        })
    },
    edit() {
      const data = new FormData();
      data.append("id", this.voucher_item.id);
      data.append("voucher", this.voucher_item.voucher);
      data.append("code", this.voucher_item.code);
    //   data.append("img", this.voucher_item.img, this.voucher_item.img.name); 
      data.append("discount", this.voucher_item.discount);
      data.append("start_date", this.voucher_item.start_date);
      data.append("end_date", this.voucher_item.end_date);
      data.append("description", this.voucher_item.description);
      data.append("qty", this.voucher_item.qty);
      data.append("status", this.voucher_item.status);
      data.append("update_by_id", this.$store.state.auth.userInfo.id);
      data.append("create_by_id", this.$store.state.auth.userInfo.id);
      if (this.new_img) {
        data.append("img", this.img, this.img.name);
      }
      console.log(data, 'data')
      api_promotion.put('voucher/', data).then((response) => {
        console.log(response.data)
        this.alert = true;
        setTimeout(() => {
          this.alert = false;
          this.$router.push({ name: "Promotion" });
        }, 2000);
      })
    },
    onFileChange(e) {
      console.log(e, "e");
      this.img = e.target.files[0];
      this.new_img = true;
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
      console.log(this.img, "img");
    },
    format_date(e, name) {
      if (name == "start") {
        this.voucher_item.start_date = e.target.value
        var temp_date = e.target.value.split("-");
        this.temp_start = `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
      }
      if (name == "end") {
        this.voucher_item.end_date = e.target.value
        var temp_date = e.target.value.split("-");
        this.temp_end = `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
      }
    },
    format_date_show(date) {
      var temp_date = date.split("-");
      return `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
    },
    switch_active(val) {
      this.voucher_item.status = val
    },
  },
  beforeMount() {
      this.fetchVoucher();
  }
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
.input-date {
  width: 30px;
  height: 30px;
  margin-left: 10px;
  background: white;
  background-image: url("../../assets/icon/calendar.png");
  background-size: 20px 20px;
  background-position: 50% 50%;
  background-repeat: no-repeat;
}
.colon {
  font-size: 30px;
  text-align: center;
  margin: 18px 0px 0px -40px;
  color: white;
}
.input-right-side {
  width: 220px;
  height: 50px;
  background: #717171;
  border-radius: 12px;
  color: white;
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