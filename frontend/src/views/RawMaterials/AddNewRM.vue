<template>
  <div style="background-color: green;">
      <div class="row" style="margin-left: 35px;">
        <div class="col-12 txt-for-add">
            Raw Material Detail
        </div>
      </div>
      <!-- First Section -->
      <div class="row">
        <div class="col-4">
          <div class="image-for-add"></div>
        </div>
        <div class="col-8">
          <div class="row" style="padding-right: 0px;">
            <div class="col-12" style="padding-right: 0px;">
              <div class="first-form-wrap">
                <input type="text" placeholder="Name" class="input-for-add" />
                <!-- Category Line -->
                <div class="row" style="padding-left: 20px;">
                  <div class="col-12">
                    <label class="category-select-for-add">Category : </label>
                    <input
                      list="categories"
                      type="text"
                      v-model="category"
                      style="
                        width: 160px;
                        height: 35px;
                        background-color: #889898;
                        color: white;
                        margin: 17px -50px 0px 90px;
                      "
                    />
                    <datalist id="categories">
                      <option v-for="(cate, idx) in categories" :key="idx">{{ cate }}</option>
                    </datalist>
                  </div>
                </div>
                <!-- Status Line -->
                <div class="row">
                  <div class="col-12" style="margin-left: -70px;">
                    <p class="category-select-for-add" style="display: inline; margin-left: -40px;">Status : </p>
                    <div class="status-show" style="display: inline;">Minimum</div>
                    <img src="../../assets/icon/Group95.png" style="position: relative; left: 150px; margin-bottom: 10px;">
                  </div>
                </div>
                <!-- Fridge Line -->
                <div class="row" style="padding-left: 25px;">
                  <div class="col-12">
                    <p class="category-select-for-add" style="display: inline; margin-left: -300px;">Fridge : </p>
                    <input type="checkbox" name="switch" id="switch">
                    <label class="switch-label" for="switch" style="position: absolute; margin: -38px 0px 0px 225px"></label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Second Section -->
      <div class="row">
        <div class="col-12">
          <div class="second-form-wrap">
            <!-- Qty & Min Qty Line -->
            <div class="row" style="padding-right: 0px;">
              <div class="col-4" style=" display: flex; justify-content: space-between; margin: .5rem; margin-top: 22px; margin-left: 30px;">
                <label for="qty" style="font-size: 30px; margin-top: -5px;">Qty&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp; </label>
                <input type="text" name="qty" id="qty" class="input-in-add">
              </div>
              <div class="col-8" style=" display: flex; justify-content: space-between; margin: .5rem; margin-top: 22px; margin-left: 50px;">
                <label for="qty" style="font-size: 30px; margin-top: -5px; width:100%;">Min Qty&nbsp;&nbsp;:</label>
                <input type="text" name="qty" id="qty" class="input-in-add-sp">
              </div>
            </div>
            <!-- Unit & Max Qty Line-->
            <div class="row" style="padding-right: 0px;">
              <div class="col-4" style=" display: flex; justify-content: space-between; margin: .5rem; margin-top: 22px; margin-left: 30px;">
                <label for="myBrowser" style="font-size: 30px; margin-top: -5px">Unit&nbsp;&nbsp;:&nbsp;&nbsp;</label>
                <input class="input-in-add" v-model="unit" type="text" list="browsers" id="myBrowser" name="myBrowser" />
                <datalist id="browsers">
                  <option v-for="unit in units" :key="unit">{{unit}}</option>
                </datalist>
              </div>
              <div class="col-8" style=" display: flex; justify-content: space-between; margin: .5rem; margin-top: 22px; margin-left: 50px;">
                <label for="qty" style="font-size: 30px; margin-top: -5px; width:100%;">Max Qty&nbsp;&nbsp;:</label>
                <input type="text" name="qty" id="qty" class="input-in-add-sp">
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Third Section -->
      <div class="row">
        <div class="col-12">
          <div class="third-form-wrap">
            <!-- Proce & Min Price Line -->
            <div class="row" style="padding-right: 0px;">
              <div class="col-4" style=" display: flex; justify-content: space-between; margin: .5rem; margin-top: 22px; margin-left: 30px;">
                <label for="price" style="font-size: 30px; margin-top: -5px;">Price&nbsp;:&nbsp; </label>
                <input type="text" name="price" id="price" style="width: 123px; height: 37px; background-color: #717171;">
              </div>
              <div class="col-8" style=" display: flex; justify-content: space-between; margin: .5rem; margin-top: 22px; margin-left: 50px;">
                <label for="min_price" style="font-size: 30px; margin-top: -5px; width:100%;">Min Price&nbsp;&nbsp;:</label>
                <input type="text" name="min_price" id="min_price" class="input-in-third-section">
              </div>
            </div>
            <!-- Total Cost & Max Price Line -->
            <div class="row" style="padding-right: 0px;">
              <div class="col-4">
                <p style="font-size: 30px; margin-top: 18px;">Total</p>
              </div>
              <div class="col-8" style=" display: flex; justify-content: space-between; margin: .5rem; margin-top: 22px; margin-left: 50px;">
                <label for="max_price" style="font-size: 30px; margin-top: -5px; width:100%;">Max Price&nbsp;&nbsp;:</label>
                <input type="text" name="max_price" id="max_price" class="input-in-third-section">
              </div>
            </div>
            <!-- Input & Average Price Line -->
            <div class="row" style="padding-right: 0px;">
              <div class="col-4">
                <input type="text" class="last-input-in-add">
              </div>
              <div class="col-8" style=" display: flex; justify-content: space-between; margin: .5rem; margin-top: 22px; margin-left: 50px;">
                <label for="avg_price" style="font-size: 30px; margin-top: -5px; width:100%;">Avg Price&nbsp;&nbsp;:</label>
                <input type="text" name="avg_price" id="avg_price" class="input-in-third-section">
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
// import api_raw_material from "../../api/api_raw_material"

export default {
  components: {},
  // mounted() {

  // },
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped>
.last-input-in-add {
  background-color: #717171;
  width: 217px;
  height: 37px;
  margin-left: 40px;
}
.input-in-third-section {
  width: 99.01px;
  height: 37px;
  background-color: #717171;
  margin-right: -65px;
}
.input-in-add {
   width: 130px; 
   height: 40px;
   background-color: #717171;
}
.input-in-add-sp {
   width: 130px; 
   height: 40px;
   background-color: #717171;
   margin-right: -50px;
}
#qty {
  width: 130px;
  height: 40px
}
.third-form-wrap {
  width: 565px;
  height: 250px;
  margin-top: 20px; 
  margin-left: 30px;
  color: white;
  border-radius: 20px;
  background-color: #252836;
}
.second-form-wrap {
  width: 685px;
  height: 157px;
  margin-top: 255px; 
  margin-left: 14px;
  color: white;
  border-radius: 20px;
  background-color: #252836;
}
input:checked + label {
   background-color: green;
   }
 input:checked + .switch-label:after {
   left: calc(100% - 10px);
   transform: translateX(-100%);
   }
.switch-label {
  display: block;
  width: 64px;
  height: 30px;
  background-color: #477a85;
  border-radius: 100px;
  position: relative;
  cursor: pointer;
  transition: 0.5s;
  box-shadow: 0 0 20px #477a8550;
}
.switch-label::after {
  content: "";
  width: 30px;
  height: 30px;
  background-color: #e8f5f7;
  position: absolute;
  border-radius: 70px;
  top: 0px;
  left: 0px;
  transition: 0.5s;
}
input[type="checkbox"] {
  width: 0;
  height: 0;
  visibility: hidden;
}
.status-show {
  width: 160px;
  height: 33px;
  font-weight: 600;
  font-size: 20px;
  margin: 0px -140px 0px 120px;
  background-color: #FFB572;
  border-radius: 3px;
}
.category-select-for-add {
  font-size: 30px;
  line-height: 56px;
  color: white;
  margin: 4px 0px 0px -70px;
  height: 57px;
  text-align: left;
}
.input-for-add {
  background-color: #c4c4c4;
  color: black;
  width: 317px;
  height: 46px;
  margin: 24px 0px 0px -70px;
}
.first-form-wrap {
  position: absolute;
  width: 60%;
  height: 245px;
  border-radius: 20px;
  margin: 0px 0px 0px 20px;
  background-color: #252836;
}
.txt-for-add {
  font-weight: bold;
  font-size: 36px;
  line-height: 56px;
  text-align: center;
  width: 100%;
  color: white;
}
.image-for-add {
  position: absolute;
  width: 228px;
  height: 220px;
  margin: 12px 0px 0px 22px;
  border-radius: 20px;
  background-image: url("../../assets/img/warehouse.jpeg");
  background-repeat: no-repeat;
  background-size: contain;
}
::placeholder {
  color: #889898;
}
.popup-add-rm {
  width: 725px;
  height: 9600px;
  top: 0%;
  left: 0%;
  position: absolute;
  background-color: aqua;
}
</style>