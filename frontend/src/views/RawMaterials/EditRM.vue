<template>
  <div>
    <div v-if="loading" style="color: white; font-size: 30px; margin-top: 20px">
      Loading ...
    </div>
    <div v-else>
      <nav-app :url_name="'RawMaterials'" save="true" @save="edit()">{{
        rm_item.raw_material_set.name
      }}</nav-app>
      <div class="container-f">
        <div class="frame" style="height: 250px">
          <div class="row h-100">
            <div class="col-5 w-100">
              <div class="row">
                <div class="col-12" style="padding: 0px">
                  <label
                    id="select_img"
                    for="file"
                    style="margin-top: 0px; margin-left: -25px"
                  >
                    <img
                      :src="
                        require(`../../../../backend${rm_item.raw_material_set.img}`)
                      "
                      class="image"
                    />
                    <div class="edit-block">Edit</div>
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
            <div class="col-7 w-100">
              <!-- Name -->
              <div class="col-12 h-25">
                <input
                  type="text"
                  style="
                    width: 95%;
                    margin: auto;
                    height: 50px;
                    background: #717171;
                  "
                  placeholder="Name"
                  v-model="rm_item.raw_material_set.name"
                />
              </div>
              <!-- Category -->
              <div class="col-12 h-25">
                <label for="">Category&nbsp;:</label>
                <select
                  name="category"
                  id="category"
                  v-model="rm_item.raw_material_set.category_id"
                  style="height: 40px; width: 180px; margin-left: 10px;"
                >
                  <option
                    v-for="category in categories"
                    :key="category.id"
                    :value="category.id"
                  >
                    {{ category.name }}
                  </option>
                </select>
              </div>
              <!-- Status -->
              <div class="col-12 h-25">
                <label for="" style="display: inline"
                  >Status&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:
                  <button
                    style="height: 50px"
                    :class="
                      $store.state.raw_material.status_image[
                        rm_item.raw_material_set.status
                      ]['class']
                    "
                  >
                    {{
                      $store.state.raw_material.status_image[
                        rm_item.raw_material_set.status
                      ]["txt"]
                    }}
                  </button>
                  <img
                    style="margin-left: 10px"
                    :src="
                      $store.state.raw_material.status_image[
                        rm_item.raw_material_set.status
                      ]['img']
                    "
                  />
                </label>
              </div>
              <!-- Fridge -->
              <div class="col-12 h-25">
                <label for=""
                  >Fridge&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</label
                >
                <div class="switch"><Switch :value="rm_item.raw_material_set.in_refrigerator" @switch="fridge" /></div>
              </div>
            </div>
          </div>
        </div>
        <div class="frame" style="height: 140px; padding-left: 0px">
          <!-- Head Of Section 2 -->
          <div class="row">
            <div class="col-5 w-100" style="margin-left: 20px">
              <div
                style="
                  width: 100%;
                  font-size: 24px;
                  color: white;
                  text-align: left;
                  margin-left: -10px;
                  margin-top: -10px;
                  margin-bottom: 20px;
                "
              >
                Smallest Unit Detail
              </div>
            </div>
          </div>
          <!-- First Row -->
          <div class="row">
            <div class="col-4 row-wrapper">
              <label style="margin-left: 30px"
                >Qty&nbsp;&nbsp;&nbsp;:&nbsp;</label
              >
              <input
                type="number"
                style="background: #717171; width: 100px; height: 50px"
                v-model="rm_item.raw_material_set.remain"
              />
            </div>
            <div class="col-4 row-wrapper">
              <label for="">Min&nbsp;Qty&nbsp;:&nbsp;</label
              ><input
                type="number"
                style="background: #717171; width: 100px; height: 50px"
                v-model="rm_item.raw_material_set.minimum"
              />
            </div>
            <div class="col-4 row-wrapper" style="margin-left: -12px;">
              <label for="">Max Qty&nbsp;:&nbsp;</label
              ><input
                type="number"
                style="background: #717171; width: 100px; height: 50px"
                v-model="rm_item.raw_material_set.maximum"
              />
            </div>
          </div>

          <!-- <div class="row" style="margin-top: 30px">
          <div class="col-6 row-wrapper">
            <label style="margin-left: 30px">Avg S&nbsp;:&nbsp;&nbsp;</label
            ><input
              type="number"
              class="avg-input"
              style="display: inline;"
              v-model="rm_item.raw_material_set.avg_s"
            />
            <p style="display: inline; font-size: 24px; margin-left: 10px;">บาท</p>
          </div>
          <div class="col-6 row-wrapper" style="margin-right: 20px">
            <label  style="margin-left: 35px;">Avg M&nbsp;:&nbsp;&nbsp;</label
            ><input
              type="number"
              class="avg-input"
              v-model="rm_item.raw_material_set.avg_m"
            />
            <p style="display: inline; font-size: 24px; margin-left: 10px;">บาท</p>
          </div>
        </div>
        <div class="row" style="margin-top: 30px">
          <div class="col-6 row-wrapper" style="margin-right: 20px">
            <label style="margin-left: 30px">Avg L&nbsp;:&nbsp;</label>
            <input
              type="number"
              class="avg-input"
              style="margin-left: -3px;"
              v-model="rm_item.raw_material_set.avg_l"
            />
            <p style="display: inline; font-size: 24px; margin-left: 10px;">บาท</p>
          </div>
          <div class="col-6 row-wrapper">
            <label for="">Supplier&nbsp;:&nbsp;&nbsp;</label>
            <select
              v-model="rm_item.supplier_id"
              class="i-25 ig"
              style="
                border-radius: 10px;
                width: 190px;
                margin-right: 0px;
                height: 50px;
              "
            >
              <option value="" selected disabled style="color: white">
                supplier
              </option>
              <option
                v-for="supplier in suppliers"
                :key="supplier.id"
                :value="supplier.id"
              >
                {{ supplier.company_name }}
              </option>
            </select>
          </div>
        </div> -->
        </div>
        <div class="frame" style="height: 230px">
          <!-- Head S M L -->
          <div
            class="row w-100"
            style="
              margin-top: -10px;
              border: 1px solid white;
              border-radius: 10px;
            "
          >
            <div class="col-3 w-100"></div>
            <div class="col-3 w-100 sml-txt">S</div>
            <div class="col-3 w-100 sml-txt">M</div>
            <div class="col-3 w-100 sml-txt">L</div>
          </div>
          <!-- Last Price -->
          <div class="row w-100" style="margin-top: 15px; margin-left: -6px;">
            <div class="col-3 w-100 lp-txt">Last</div>
            <div
              class="col-3 w-100 lp-txt"
              v-for="item in many_items"
              :key="item"
            >
              {{ item.last_price }}
            </div>
          </div>
          <!-- Supplier -->
          <div class="row w-100" style="margin-top: 15px; margin-left: -6px;">
            <div class="col-3 w-100 lp-txt">Supplier</div>
            <div class="col-3 w-100 lp-txt" v-for="(item, idx) in many_items" :key="idx">
              <select
                v-model="many_items[idx].supplier_id"
                style="width: 100%; height: 40px; border-radius: 10px;"
              >
                <option value="" selected disabled style="color: white">
                  supplier
                </option>
                <option v-for="supplier in suppliers" :key="supplier.id" :value="supplier.id">
                  {{ supplier.company_name }}
                </option>
              </select>
            </div>
          </div>
          <!-- Avg -->
          <div class="row w-100" style="margin-top: 15px; margin-left: -6px;">
            <div class="col-3 w-100 lp-txt">Avg</div>
            <div class="col-3 w-100 lp-txt">
              <input
                type="text"
                v-model="rm_item.raw_material_set.avg_s"
                style="width: 100%; background: #717171"
              />
            </div>
            <div class="col-3 w-100 lp-txt">
              <input
                type="text"
                v-model="rm_item.raw_material_set.avg_m"
                style="width: 100%; background: #717171"
              />
            </div>
            <div class="col-3 w-100 lp-txt">
              <input
                type="text"
                v-model="rm_item.raw_material_set.avg_l"
                style="width: 100%; background: #717171"
              />
            </div>
          </div>
        </div>
        <div class="frame" style="height: 205px">
          <!-- Head Of Section 3 -->
          <div class="row">
            <div class="col-12">
              <div
                style="
                  width: 100%;
                  font-size: 30px;
                  color: white;
                  text-align: left;
                  margin-top: -10px;
                  margin-bottom: 20px;
                "
              >
                Exchange Unit
              </div>
            </div>
          </div>
          <!-- First Row -->
          <div class="row" style="width: 99%; margin-left: -1px">
            <input
              type="number"
              class="i-25 g"
              v-model="rm_item.raw_material_set.s_to_m"
              placeholder="S Unit"
              style="
                text-align: right;
                border-radius: 10px;
                background: #717171;
              "
            />
            <input
              type="text"
              class="input-prepend"
              style="color: white; background: #717171"
              v-model="unit_s_name"
            />
            <select
              v-model="rm_item.raw_material_set.unit_s_id"
              @change="find_unit_s"
              class="ig select-append"
            >
              <option value="" selected disabled style="color: white">
                unit
              </option>
              <option v-for="unit in units" :key="unit.id" :value="unit.id">
                {{ unit.unit }}
              </option>
            </select>

            <span style="color: #fff; font-size: 30px">=</span>

            <input
              type="number"
              class="i-25 g"
              model="to_amount"
              value="1"
              readonly
              style="
                text-align: right;
                border-radius: 10px;
                background: #717171;
              "
            />
            <input
              type="text"
              class="input-prepend"
              style="color: white; background: #717171"
              v-model="unit_m_name"
            />
            <select
              v-model="rm_item.raw_material_set.unit_m_id"
              @change="find_unit_m"
              class="ig select-append"
            >
              <option value="" selected disabled style="color: white">
                unit
              </option>
              <option v-for="unit in units" :key="unit.id" :value="unit.id">
                {{ unit.unit }}
              </option>
            </select>
          </div>
          <!-- Second Row -->
          <div class="row m-15" style="width: 99%; margin-left: -1px">
            <input
              type="number"
              class="i-25 g"
              v-model="rm_item.raw_material_set.m_to_l"
              placeholder="M to L Unit"
              style="
                text-align: right;
                border-radius: 10px;
                background: #717171;
              "
            />
            <input
              type="text"
              class="input-prepend"
              style="color: white; background: #717171"
              v-model="unit_m_name"
            />
            <select
              v-model="rm_item.raw_material_set.unit_m_id"
              @change="find_unit_m"
              class="ig select-append"
            >
              <option value="" selected disabled style="color: white">
                unit
              </option>
              <option v-for="unit in units" :key="unit.id" :value="unit.id">
                {{ unit.unit }}
              </option>
            </select>

            <span style="color: #fff; font-size: 30px">=</span>

            <input
              type="number"
              value="1"
              class="i-25 g"
              style="
                text-align: right;
                border-radius: 10px;
                background: #717171;
              "
            />
            <input
              type="text"
              class="input-prepend"
              style="color: white; background: #717171"
              v-model="unit_l_name"
            />
            <select
              v-model="rm_item.raw_material_set.unit_l_id"
              @change="find_unit_l"
              class="ig select-append"
            >
              <option value="" selected disabled style="color: white">
                unit
              </option>
              <option v-for="unit in units" :key="unit.id" :value="unit.id">
                {{ unit.unit }}
              </option>
            </select>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import { api_raw_material } from "../../api/api_raw_material.js";
export default {
  components: { NavApp, Switch },
  data() {
    return {
      loading: false,
      new_img: false,
      unit_s_name: null,
      unit_m_name: null,
      unit_l_name: null,
      rm_item: {},
      many_items: [],
      categories: [],
      units: [],
      suppliers: [],
    };
  },
  methods: {
    fetchSuppliers() {
      api_raw_material.get("/supplier/").then((response) => {
        console.log(response.data, "suppliers");
        this.suppliers = response.data;
      });
    },
    fetchRawMaterials() {
      api_raw_material
        .get(`/raw-material/${this.$route.params.id}`)
        .then((response) => {
          console.log(response.data, "raw_material");
          this.rm_item = response.data[0];
          this.many_items = response.data;
          // api_raw_material.post('/pickup-raw-material/', {raw_material_id: response.data.id}).then((response) => {
          //   console.log(response.data, 'pick rm')
          // })
          console.log(this.rm_item, "rm_item");
        });
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
    fridge(val) {
      this.rm_item.raw_material_set.in_refrigerator = val;
    },
    async edit() {
      const data = new FormData();
      data.append("id", this.rm_item.raw_material_set.id);
      data.append("maximum", this.rm_item.raw_material_set.maximum);
      data.append("minimum", this.rm_item.raw_material_set.minimum);
      data.append("remain", this.rm_item.raw_material_set.remain);
      data.append("category_id", this.rm_item.raw_material_set.category_id);
      data.append("name", this.rm_item.raw_material_set.name);
      data.append(
        "in_refrigerator",
        this.rm_item.raw_material_set.in_refrigerator
      );
      data.append("supplier_id", this.rm_item.supplier_id);
      data.append("unit_l_id", this.rm_item.raw_material_set.unit_l_id);
      data.append("unit_m_id", this.rm_item.raw_material_set.unit_m_id);
      data.append("unit_s_id", this.rm_item.raw_material_set.unit_s_id);
      data.append("m_to_l", this.rm_item.raw_material_set.m_to_l);
      data.append("s_to_m", this.rm_item.raw_material_set.s_to_m);
      data.append("avg_l", this.rm_item.raw_material_set.avg_l);
      data.append("avg_m", this.rm_item.raw_material_set.avg_m);
      data.append("avg_s", this.rm_item.raw_material_set.avg_s);
      data.append("update_by_id", this.$store.state.auth.userInfo.id);
      data.append("create_by_id", this.$store.state.auth.userInfo.id);
      if (this.new_img) {
        user_data.append(
          "img",
          this.rm_item.raw_material_set.img,
          this.rm_item.raw_material_set.img.name
        );
      }
      await api_raw_material.put("rm-update/", data).then((response) => {
        console.log(response.data, "response data");
      });
      for (let index = 0; index < this.many_items.length; index++) {
        var prm_data = {
          id: this.many_items[index].id,
          avg_price: this.many_items[index].avg_price,
          last_price: this.many_items[index].last_price,
          raw_material_id: this.many_items[index].raw_material_id,
          supplier_id: this.many_items[index].supplier_id,
          unit_id: this.many_items[index].unit_id,
        }
        api_raw_material.put(`price-raw-material/`, prm_data).then((response) => {
          console.log(response.data, "response data");
        });
      }
      
      this.$router.push({ name: "RawMaterials" });
    },
    find_unit_s() {
      this.unit_s_name = this.units.find(
        (x) => x.id == this.rm_item.raw_material_set.unit_s_id
      ).unit;
    },
    find_unit_m() {
      this.unit_m_name = this.units.find(
        (x) => x.id == this.rm_item.raw_material_set.unit_m_id
      ).unit;
    },
    find_unit_l() {
      this.unit_l_name = this.units.find(
        (x) => x.id == this.rm_item.raw_material_set.unit_l_id
      ).unit;
    },
  },
  beforeMount() {
    this.fetchRawMaterials();
  },
  watch: {
    remain() {
      this.total_price = this.remain * this.avg_price;
    },
    avg_price() {
      this.total_price = this.remain * this.avg_price;
    },
  },
  computed: {
    status_am: function () {
      if (this.remain > this.minimum) {
        return "success";
      } else {
        return "minimum";
      }
    },
  },
  mounted() {
    this.fetchSuppliers();
    api_raw_material.get("category").then((response) => {
      this.categories = response.data;
    });
    this.loading = true;
    api_raw_material.get("unit").then((response) => {
      console.log(response.data, "unit");
      this.units = response.data;
      this.find_unit_s();
      this.find_unit_m();
      this.find_unit_l();
      this.loading = false;
    });
  },
};
</script>

<style scoped>
.lp-txt {
  font-size: 24px;
  color: white;
}
.sml-txt {
  font-size: 30px;
  color: white;
}
input {
  height: 40px;
}
label {
  font-size: 24px;
  bottom: 5px;
  position: relative;
}
.avg-input {
  width: 150px;
  height: 50px;
  margin-left: -10px;
  background: #717171;
}
.select-append {
  width: 0px;
  height: 40px;
  border-radius: 0px 10px 10px 0px;
}
.input-prepend {
  margin-right: 6px;
  border-radius: 10px 0px 0px 10px;
  width: 100px;
}
.row-wrapper {
  width: 100%;
  padding: 0px;
  margin-left: -10px;
}
::placeholder {
  text-align: left;
  color: white;
  font-size: 22px;
}
.i-25 {
  width: 140px;
  border-radius: 10px;
}
.frame {
  margin-top: 10px;
  margin-bottom: 0px;
  background-color: #303344;
  border-radius: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 20px;
}
.container-f {
  padding-left: 22px;
  margin-right: auto;
  margin-left: auto;
}

option {
  font-size: 20px;
}
raw-img {
  width: 236px;
  height: 235px;
}

::placeholder {
  text-indent: 5 px;
  color: #fff;
  font-size: 20px;
}
.h-25 {
  height: 25%;
  text-align: left;
}
.h-50 {
  height: 50%;
  text-align: left;
}

.h-1 {
  height: 50px;
}

.edit-block {
  position: absolute;
  width: 74px;
  height: 28.23px;
  left: 15px;
  top: 183px;
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
#select_img {
  width: 220px;
  height: 220px;
  border-radius: 25px;
  background-color: #717171;
}
.image {
  width: 220px;
  height: 220px;
  border-radius: 25px;
  right: 0px;
  position: absolute;
}
.switch {
  display: inline-block;
  top: 0px;
  left: 10px;
}
.label-input {
  text-align: left;
  margin-top: 5px;
  height: 50px;
  width: 100%;
}

.m-15 {
  margin-top: 20px;
}
.g {
  border-radius: 10px 0px 0px 10px;
  margin-right: 10px;
  width: 155px;
}
.ig {
  border-radius: 0px 10px 10px 0px;
  left: -3px;
  margin-left: -5px;
}
SELECT {
  background: url("data:image/svg+xml,<svg height='10px' width='10px' viewBox='0 0 16 16' fill='%23000000' xmlns='http://www.w3.org/2000/svg'><path d='M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z'/></svg>")
    no-repeat;
  background-position: calc(100% - 0.75rem) center !important;
  -moz-appearance: none !important;
  -webkit-appearance: none !important;
  appearance: none !important;
  padding-right: 2rem !important;
  background-color: #717171;
  width: 200px;
  font-size: 30px;
  color: #fff;
  border-radius: 10px;
  font-size: 24px;
  border: 0px;
  text-indent: 10px;
}
</style>