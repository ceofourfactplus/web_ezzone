<template>
  <div style="background-color: green;">
      <!-- Nav in Popup -->
      <div class="row" style="margin-left: 35px">
        <div class="col-3" @click="saveChange">
          <img
            src="../../assets/icon/save.png"
            style="
              top: 10px;
              left: 10px;
              position: absolute;
              width: 50px;
              height: 50px;
            "
          />
        </div>
        <div class="col-6 txt-for-add" style="width: 100%">+ Raw Material</div>
      </div>
      <!-- Section 1 -->
      <div class="row" style="margin-top: 10px">
        <div class="col-4">
          <!-- Select Image -->
          <div style="height: 0px">
            <img
              v-if="show_img == null"
              width="208"
              height="219"
              src="../../assets/img/BG.png"
              style="margin: 11px 0px 0px 22px"
              class="raw-image"
            />
            <img
              v-else
              :src="show_img"
              width="208"
              height="219"
              style="margin: 11px 0px 0px 22px"
              class="raw-image"
            />
            <label for="file">
              <div class="edit-block">
                <div class="row">
                  <div class="col-2">
                    <img
                      style="align-item: left; margin-left: 3px"
                      src="../../assets/icon/el_camera.png"
                    />
                  </div>
                  <div class="col-10">
                    <p style="font-size: 16px; margin-left: 10px">Edit</p>
                  </div>
                </div>
              </div>
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
        <div class="col-8">
          <div class="row" style="padding-right: 0px">
            <div class="col-12" style="padding-right: 0px">
              <div class="first-form-wrap">
                <input type="text" placeholder="Name" class="input-for-add" v-model="raw_material_item.name" />
                <!-- Category Line -->
                <div class="row" style="padding-right: 5px;">
                  <div class="col-12">
                    <label class="category-select-for-add">Category : </label>
                    <input
                      list="categories"
                      type="text"
                      v-model="raw_material_item.category"
                      class="select-input"
                    />
                    <datalist id="categories">
                      <option v-for="(cate, idx) in categories" :key="idx">
                        {{ cate }}
                      </option>
                    </datalist>
                  </div>
                </div>
                <!-- Status Line -->
                <div class="row">
                  <div class="col-12" style="margin-left: 22px">
                    <p
                      class="category-select-for-add"
                      style="display: inline; margin-left: -90px"
                    >
                      Status :
                    </p>
                    <div class="status-show" style="display: inline">
                      Minimum
                    </div>
                    <img
                      src="../../assets/icon/warning.png"
                      style="
                        position: relative;
                        left: 75px;
                        margin-bottom: 10px;
                      "
                    />
                  </div>
                </div>
                <!-- Fridge Line -->
                <div class="row">
                  <div class="col-12">
                    <p
                      class="category-select-for-add"
                      style="display: inline; margin-left: -175px"
                    >
                      Fridge :
                    </p>
                    <input type="checkbox" name="switch" id="switch" v-model="raw_material_item.in_refrigerator" />
                    <label
                      class="switch-label"
                      for="switch"
                      style="position: absolute; margin: -38px 0px 0px 200px"
                    ></label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Section 2 -->
      <div class="row">
        <div class="col-12">
          <div class="second-form-wrap">
            <!-- Qty & Min Qty Line -->
            <div class="row" style="padding-right: 0px">
              <div
                class="col-4"
                style="
                  display: flex;
                  justify-content: space-between;
                  margin: 0.5rem;
                  margin-top: 22px;
                  margin-left: 30px;
                "
              >
                <label for="qty" style="font-size: 30px; margin-top: -5px"
                  >Qty&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;
                </label>
                <input v-model="raw_material_item.qty" type="text" name="qty" id="qty" class="input-in-add" />
              </div>
              <div
                class="col-8"
                style="
                  display: flex;
                  justify-content: space-between;
                  margin: 0.5rem;
                  margin-top: 22px;
                  margin-left: 50px;
                "
              >
                <label
                  for="qty"
                  style="
                    font-size: 30px;
                    margin-top: -5px;
                    margin-right: -16px;
                    width: 100%;
                  "
                  >Min Qty&nbsp;&nbsp;:</label
                >
                <input
                  type="text"
                  name="qty"
                  id="qty"
                  v-model="min_qty"
                  class="input-in-add-sp"
                />
              </div>
            </div>
            <!-- Unit & Max Qty Line-->
            <div class="row" style="padding-right: 0px">
              <div
                class="col-4"
                style="
                  display: flex;
                  justify-content: space-between;
                  margin: 0.5rem;
                  margin-top: 22px;
                  margin-left: 30px;
                "
              >
                <label for="myBrowser" style="font-size: 30px; margin-top: -5px"
                  >Unit&nbsp;&nbsp;:&nbsp;&nbsp;</label
                >
                <input
                  class="unit-select-input"
                  v-model="unit"
                  type="text"
                  list="browsers"
                  id="myBrowser"
                  name="myBrowser"
                />
                <datalist id="browsers">
                  <option v-for="unit in units" :key="unit">{{ unit }}</option>
                </datalist>
              </div>
              <div
                class="col-8"
                style="
                  display: flex;
                  justify-content: space-between;
                  margin: 0.5rem;
                  margin-top: 22px;
                  margin-left: 50px;
                "
              >
                <label
                  for="qty"
                  style="
                    font-size: 30px;
                    margin-top: -5px;
                    margin-right: -16px;
                    width: 100%;
                  "
                  >Max Qty&nbsp;&nbsp;:</label
                >
                <input
                  type="text"
                  name="qty"
                  id="qty"
                  class="input-in-add-sp"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Section 3 -->
      <div class="row">
        <div class="col-12">
          <div class="third-form-wrap">
            <!-- Price & Min Price Line -->
            <div class="row" style="padding-right: 0px">
              <div
                class="col-4"
                style="
                  display: flex;
                  justify-content: space-between;
                  margin: 0.5rem;
                  margin-top: 22px;
                  margin-left: 30px;
                "
              >
                <label for="price" style="font-size: 30px; margin-top: -10px"
                  >Price&nbsp;:&nbsp;&nbsp;
                </label>
                <input
                  type="text"
                  name="price"
                  id="price"
                  v-model="raw_material_item.price"
                  style="width: 123px; height: 37px; background-color: #717171"
                />
              </div>
              <div
                class="col-8"
                style="
                  display: flex;
                  justify-content: space-between;
                  margin: 0.5rem;
                  margin-top: 22px;
                  margin-left: 50px;
                "
              >
                <label
                  for="min_price"
                  style="font-size: 30px; margin-top: -10px; width: 100%"
                  >Min Price&nbsp;&nbsp;:</label
                >
                <input
                  type="text"
                  name="min_price"
                  id="min_price"
                  v-model="raw_material_item.min_price"
                  class="input-in-third-section"
                />
              </div>
            </div>
            <!-- Total Cost & Max Price Line -->
            <div class="row" style="padding-right: 0px">
              <div class="col-4 w-100">
                <p style="font-size: 30px; margin: 12px 0px 0px 25px">
                  Total Cost :
                </p>
              </div>
              <div
                class="col-8"
                style="
                  display: flex;
                  justify-content: space-between;
                  margin: 0.5rem;
                  margin-top: 22px;
                  margin-left: 50px;
                "
              >
                <label
                  for="max_price"
                  style="font-size: 30px; margin-top: -10px; width: 100%"
                  >Max Price&nbsp;&nbsp;:</label
                >
                <input
                  type="text"
                  name="max_price"
                  id="max_price"
                  v-model="raw_material_item.max_price"
                  class="input-in-third-section"
                />
              </div>
            </div>
            <!-- Input & Average Price Line -->
            <div class="row" style="padding-right: 0px">
              <div class="col-4">
                <input type="text" class="last-input-in-add" />
              </div>
              <div
                class="col-8"
                style="
                  display: flex;
                  justify-content: space-between;
                  margin: 0.5rem;
                  margin-top: 22px;
                  margin-left: 50px;
                "
              >
                <label
                  for="avg_price"
                  style="font-size: 30px; margin-top: -10px; width: 100%"
                  >Avg Price&nbsp;&nbsp;:</label
                >
                <input
                  type="text"
                  name="avg_price"
                  id="avg_price"
                  v-model="raw_material_item.avg_price"
                  class="input-in-third-section"
                />
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
  mounted() {
    this.fetchRawMaterials()
  },
  data() {
    return {
      raw_material_item: {
        'img': '',
        'status': 1,
        'name': '',
        'category': '',
        'qty': null,
        'minimum': 1,
        'maximum': 10,
        'price': 0,
        'avg_price': null,
        'max_price': null,
        'min_price': null,
        'in_refrigerator': false,
      },
    };
  },
  methods: {
    fetchRawMaterials() {
      console.log('fetch raw materials')
    },
  },
};
</script>

<style scoped>
.card {
  width: 625px;
  height: 756px;
  top: 7%;
  left: 7%;
}
.unit-select-input {
  width: 150px;
  height: 40px;
  background-color: #2f414e;
  background-image: url("../../assets/icon/down-arrow.png");
  background-position: center right;
  background-size: 24px;
  background-repeat: no-repeat;
}
.select-input {
  width: 200px;
  height: 35px;
  background-color: #2f414e;
  color: white;
  margin: 17px -10px 0px 5px;
  background-image: url("../../assets/icon/down-arrow.png");
  background-position: center right;
  background-size: 24px;
  background-repeat: no-repeat;
}
input::-webkit-calendar-picker-indicator {
  opacity: 0;
}
.edit-block {
  position: absolute;
  top: 250px;
  left: 30px;
  width: 74px;
  height: 28.23px;
  background-color: #c4c4c4;
  border-radius: 5px;
}
.raw-image {
  position: fixed;
  border-radius: 30px;
}
.last-input-in-add {
  background-color: #717171;
  width: 217px;
  height: 37px;
  margin: 20px 0px 0px 20px;
}
.input-in-third-section {
  width: 150px;
  height: 37px;
  background-color: #717171;
  margin-right: -70px;
  margin-top: 0px;
}
.input-in-add {
  width: 150px;
  height: 40px;
  background-color: #717171;
}
#qty[data-v-8556b7f6] {
  width: 150px;
  height: 40px;
}
.input-in-add-sp {
  width: 300px;
  height: 40px;
  background-color: #717171;
  margin-right: -70px;
}
#qty {
  width: 130px;
  height: 40px;
}
.third-form-wrap {
  width: 597px;
  height: 215px;
  margin: 12px 0px 0px 15px;
  color: white;
  border-radius: 20px;
  background-color: #252836;
}
.second-form-wrap {
  width: 597px;
  height: 157px;
  margin: 265px 0px 0px 15px;
  color: white;
  border-radius: 20px;
  background-color: #252836;
}
input:checked + label {
  background-color: green;
}
input:checked + .switch-label:after {
  left: calc(100% - 5px);
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
  left: 5px;
  transition: 0.5s;
}
input[type="checkbox"] {
  width: 0;
  height: 0;
  visibility: hidden;
}
.status-show {
  width: 110px;
  height: 33px;
  font-weight: 600;
  font-size: 20px;
  margin: 0px -60px 0px 70px;
  background-color: #ffb572;
  border-radius: 3px;
}
.category-select-for-add {
  font-size: 30px;
  line-height: 56px;
  color: white;
  margin: 4px 0px 0px 6px;
  height: 57px;
  text-align: left;
}
.input-for-add {
  background-color: #c4c4c4;
  color: black;
  width: 340px;
  height: 46px;
  margin: 24px 0px 0px 0px;
}
.first-form-wrap {
  position: absolute;
  width: 60%;
  height: 255px;
  border-radius: 20px;
  margin: 0px 0px 0px 37px;
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
  width: 167px;
  height: 196px;
  margin: 42px 0px 0px 34px;
  border-radius: 20px;
  background-image: url("../../assets/img/warehouse.jpeg");
  background-repeat: no-repeat;
  background-size: contain;
}
::placeholder {
  color: #889898;
}
.popup-add-rm {
  width: 625px;
  height: 756px;
  top: 7%;
  left: 7%;
  position: absolute;
  background-color: #303344;
  border: 2px solid #ea7c69;
  border-radius: 20px;
}
.row {
  padding-right: 50px;
}
.btn-ghost {
  border-color: #65b0f6;
  color: #65b0f6;
  width: 119px;
  height: 45px;
  margin-left: 15px;
}

.wrap-search {
  min-width: 520px;
  width: fit-content;
  padding: 0px;
  margin-left: 45px;
}

.search-bar {
  background-size: contain;
  background-repeat: no-repeat;
  background-color: #3a3d49;
  text-indent: 65px;
  padding-left: 10px;
  margin-left: 3px;
  border-radius: 20px;
  width: 90%;
  height: 45px;
  background-image: url("../../assets/icon/Search-19x18-1.png");
  background-repeat: no-repeat;
  background-position: 2% 50%;
  /* Extra Styling */
}
</style>