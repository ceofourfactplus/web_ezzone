<template>
  <div>
    <nav-app
      v-if="raw_material.name.length > 23"
      :url_name="'RawMaterials'"
      save="true"
      @save="create_raw_material()"
      >{{ raw_material.name.slice(0, 22) }}...
    </nav-app>
    <nav-app
      v-else
      :url_name="'RawMaterials'"
      save="true"
      @save="create_raw_material()"
      >{{ raw_material.name }}
    </nav-app>

    <div style="width: 95%; margin: auto">
      <div class="frame row mb-2 w-100 m-0" style=":padding: 20px">
        <div class="col-5 w-100" style="height: 235px">
          <label
            id="select_img"
            for="file"
            style="margin-top: 0px; margin-left: -25px"
          >
            <img :src="show_img" class="image" v-if="show_img != null" />
            <div class="image" style="background-color: #717171" v-else></div>
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
        <!-- data -->
        <div class="col-7 w-100">
          <div class="row w-100 h-100" style="margin: 0px">
            <div class="col-12 w-100">
              <input
                v-model="raw_material.name"
                type="text"
                style="height: 60px"
                class="w-100 m-0"
              />
            </div>
            <div class="col-12 w-100">
              <label for="">Category</label>:
              <select v-model="raw_material.category_id" style="width: 65%">
                <option value="">category</option>
                <option
                  v-for="category in categories"
                  :key="category.id"
                  :value="category.id"
                >
                  {{ category.name }}
                </option>
              </select>
            </div>
            <div class="col-12 w-100">
              <label for="">Status</label>:
              <button
                v-if="raw_material.remain == 0"
                class="btn-r ms-1"
                style="
                  width: fit-content;
                  position: relative;
                  color: #000;
                  white-space: nowrap;
                  height: 40px;
                "
              >
                Out of stock
              </button>
              <button
                v-else
                :class="{
                  'btn-y': raw_material.remain <= this.raw_material.minimum,
                  'btn-g': raw_material.remain > this.raw_material.minimum,
                }"
                class="ms-1"
                style="
                  position: relative;
                  color: #000;
                  white-space: nowrap;
                  height: 40px;
                "
              >
                {{ status_t }}
              </button>
            </div>
            <div class="col-12 w-100">
              <label for="">Fridge</label>:
              <Switch
                style="top: 12px"
                class="ms-2"
                :value="raw_material.in_refrigerator"
                @switch="
                  raw_material.in_refrigerator = !raw_material.in_refrigerator
                "
              />
            </div>
          </div>
        </div>
      </div>
      <!-- qty -->
      <div class="frame mb-2" style="padding: 20px">
        <h2>Smallest Unit Detail</h2>
        <div class="row w-100" id="qty">
          <div class="col-4 w-100">
            Qty :
            <input
              v-model="raw_material.remain"
              type="number"
              style="width: 86px"
            />
          </div>
          <div class="col-4 w-100">
            Min Qty:
            <input
              v-model="raw_material.minimum"
              type="number"
              style="width: 86px"
            />
          </div>
          <div class="col-4 w-100">
            Max Qty:
            <input
              v-model="raw_material.maximum"
              type="number"
              style="width: 86px"
            />
          </div>
        </div>
      </div>
      <div class="frame mb-2" style="padding: 20px">
        <div
          class="row"
          style="
            width: 99%;
            margin: auto;
            border: 2px solid #fff;
            border-radius: 10px;
            font-size: 30px;
            color: #fff;
          "
        >
          <div class="col-3"></div>
          <div class="col-3 w-100">S</div>
          <div class="col-3 w-100">M</div>
          <div class="col-3 w-100">L</div>
        </div>
        <!-- price -->
        <div class="row mt-2 w-100">
          <div class="col-3 w-100 lp-txt">Last</div>
          <div class="col-3 w-100">
            <input
              type="number"
              v-model="options_s.last_price"
              style="text-align: right; padding-right: 10px"
            />
          </div>
          <div class="col-3 w-100">
            <input
              type="number"
              v-model="options_m.last_price"
              style="text-align: right; padding-right: 10px"
            />
          </div>
          <div class="col-3 w-100">
            <input
              type="number"
              v-model="options_l.last_price"
              style="text-align: right; padding-right: 10px"
            />
          </div>
        </div>
        <!-- supplier -->
        <div class="row mt-2 w-100">
          <div class="col-3 w-100 lp-txt">Supplier</div>
          <div class="col-3 w-100">
            <select v-model="options_s.supplier">
              <option value="" selected>None</option>
              <option
                v-for="supplier in suppliers"
                :key="supplier.id"
                :value="supplier.id"
              >
                {{ supplier.company_name }}
              </option>
            </select>
          </div>
          <div class="col-3 w-100">
            <select v-model="options_m.supplier">
              <option selected>None</option>
              <option
                v-for="supplier in suppliers"
                :key="supplier.id"
                :value="supplier.id"
              >
                {{ supplier.company_name }}
              </option>
            </select>
          </div>
          <div class="col-3 w-100">
            <select v-model="options_l.supplier">
              <option selected>None</option>
              <option
                v-for="supplier in suppliers"
                :key="supplier.id"
                :value="supplier.id"
              >
                {{ supplier.company_name }}
              </option>
            </select>
          </div>
        </div>
        <!-- remain -->
        <div class="row mt-2 w-100">
          <div class="col-3 w-100 lp-txt">Avg</div>
          <div class="col-3 w-100">
            <input
              type="number"
              v-model="options_s.avg_price"
              style="text-align: right; padding-right: 10px"
            />
          </div>
          <div class="col-3 w-100">
            <input
              type="number"
              v-model="options_m.avg_price"
              style="text-align: right; padding-right: 10px"
            />
          </div>
          <div class="col-3 w-100">
            <input
              type="number"
              v-model="options_l.avg_price"
              style="text-align: right; padding-right: 10px"
            />
          </div>
        </div>
      </div>
      <div class="frame">
        <h2 class="mb-2">Exchange Unit</h2>
        <div class="row" style="width: 100%">
          <div class="col-3 w-100">
            <input type="text" class="i-25" v-model="raw_material.s_to_m" />
          </div>
          <div class="col-4 w-100" style="display: flex">
            <input
              type="text"
              class="input-prepend"
              v-model="raw_material.unit_s_name"
            />
            <select class="ig select-append" v-model="raw_material.unit_s_name">
              <option value="" selected disabled style="color: white">
                unit
              </option>
              <option v-for="unit in units" :key="unit.unit" :value="unit.unit">
                {{ unit.unit }}
              </option>
            </select>
          </div>
          <div class="col-2 equal w-100">=</div>
          <div class="col-3 w-100" style="display: flex">
            <input
              type="text"
              class="input-prepend"
              v-model="raw_material.unit_m_name"
            />
            <select class="ig select-append" v-model="raw_material.unit_m_name">
              <option value="" selected disabled style="color: white">
                unit
              </option>
              <option v-for="unit in units" :key="unit.unit" :value="unit.unit">
                {{ unit.unit }}
              </option>
            </select>
          </div>

          <div class="col-3 w-100 mt-3">
            <input type="number" class="i-25" v-model="raw_material.m_to_l" />
          </div>
          <div class="col-4 mt-3 w-100" style="display: flex">
            <input
              type="text"
              class="input-prepend"
              v-model="raw_material.unit_m_name"
            />
            <select class="ig select-append" v-model="raw_material.unit_m_name">
              <option value="" selected disabled style="color: white">
                unit
              </option>
              <option v-for="unit in units" :key="unit.unit" :value="unit.unit">
                {{ unit.unit }}
              </option>
            </select>
          </div>
          <div class="col-2 equal w-100 mt-3">=</div>
          <div class="col-3 mt-3 w-100" style="display: flex">
            <input
              type="text"
              class="input-prepend"
              v-model="raw_material.unit_l_name"
            />
            <select class="ig select-append" v-model="raw_material.unit_l_name">
              <option value="" selected disabled style="color: white">
                unit
              </option>
              <option v-for="unit in units" :key="unit.unit" :value="unit.unit">
                {{ unit.unit }}
              </option>
            </select>
          </div>
        </div>
      </div>
    </div>

    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import { api_raw_material } from "../../api/api_raw_material.js";
import SavePopup from "../../components/main_component/SavePopup.vue";

export default {
  components: { NavApp, Switch, SavePopup },
  data() {
    return {
      show_img: null,
      img: null,
      units: [],
      categories: [],
      suppliers: [],
      alert: false,
      raw_material: {
        maximum: 0,
        minimum: 0,
        category_id: null,
        name: "",
        remain: 0,
        in_refrigerator: false,
        unit_l_name: "",
        unit_m_name: "",
        unit_s_name: "",
        m_to_l: 0,
        s_to_m: 0,
        create_by_id: 1,
        status: 1,
        pricerawmaterial_set: [
          //   {
          //     last_price: 0,
          //     supplier: 1,
          //     unit: 23,
          //   },
        ],
      },
      options_s: {
        price: 0,
        supplier: null,
        remain: 0,
      },
      options_m: {
        price: 0,
        supplier: null,
        remain: 0,
      },
      options_l: {
        price: 0,
        supplier: null,
        remain: 0,
      },
      change_img: false,
    };
  },
  methods: {
    onFileChange(e) {
      this.raw_material.img = e.target.files[0];
      if (this.raw_material.img) {
        this.change_img = true;
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.raw_material.img);
      }
    },
    check_option() {
      console.log("in check");
      this.raw_material.pricerawmaterial_set = [];
      for (var option of ["options_s", "options_m", "options_l"]) {
        console.log(option);
        if (this[option].supplier != null && this[option].last_price != "") {
          var data = this[option];
          const name = "unit_" + option.charAt(option.length - 1) + "_name";
          data["unit_name"] = this.raw_material[name];
          this.raw_material.pricerawmaterial_set.push(
            JSON.parse(JSON.stringify(data))
          );
        }
      }
      if (this.raw_material.pricerawmaterial_set.length != 0) {
        return true;
      } else {
        return false;
      }
    },
    create_raw_material() {
      if (this.check_option()) {
        api_raw_material
          .put("edit-rm/" + this.$route.params.id, this.raw_material)
          .then((response) => {
            if (this.change_img) {
              console.log(response.data.id);
              const data = new FormData();
              data.append(
                "img",
                this.raw_material.img,
                this.raw_material.img.name
              );
              api_raw_material
                .put("rm-img/" + response.data.id, data)
                .then(() => {
                  this.$router.push({ name: "RawMaterials" });
                });
            } else {
              this.$router.push({ name: "RawMaterials" });
            }
          });
      }
    },
  },
  mounted() {
    api_raw_material
      .get("unit/")
      .then((response) => (this.units = response.data));
    api_raw_material
      .get("category/")
      .then((response) => (this.categories = response.data));
    api_raw_material
      .get("supplier/")
      .then((response) => (this.suppliers = response.data));
    api_raw_material
      .get("raw-material/" + this.$route.params.id)
      .then((response) => {
        this.raw_material = response.data;
        this.show_img = response.data.img;
        if(response.data.m_to_l == null){
          this.raw_material.m_to_l = 0
        }
        if(response.data.s_to_m == null){
          this.raw_material.s_to_m = 0
        }
        for (const price of response.data.pricerawmaterial_set) {
          for (var option of ["options_s", "options_m", "options_l"]) {
            const unit_set = this.units.filter((unit) => {
              return (
                unit.id ==
                response.data[
                  "unit_" + option.charAt(option.length - 1) + "_id"
                ]
              );
            })[0];
            if (unit_set != undefined) {
              this.raw_material[
                "unit_" + option.charAt(option.length - 1) + "_name"
              ] = unit_set.unit;
            } else {
              this.raw_material[
                "unit_" + option.charAt(option.length - 1) + "_name"
              ] = "";
            }
            if (
              response.data[
                "unit_" + option.charAt(option.length - 1) + "_id"
              ] == price.unit
            ) {
              this[option] = JSON.parse(JSON.stringify(price));
            }
          }
        }
      });
  },
  watch: {
    "raw_material.remain": function (re) {
      if (re == ""||re<0) {
        this.raw_material.remain = 0;
      }
    },
    "raw_material.s_to_m": function (re) {
      if (re == "") {
        this.raw_material.s_to_m = 0;
      }
    },
    "raw_material.m_to_l": function (re) {
      if (re == "") {
        this.raw_material.m_to_l = 0;
      }
    },
  },
  computed: {
    status_t() {
      if (this.raw_material.remain == 0) {
        this.raw_material.status = 3;
        return "Out of stock";
      } else if (this.raw_material.remain > this.raw_material.minimum) {
        this.raw_material.status = 2;
        return "In stock";
      } else if (this.raw_material.remain <= this.raw_material.minimum) {
        this.raw_material.status = 1;
        return "Min stock";
      }
    },
  },
};
</script>

<style scoped>
input,
select {
  background-color: #717171;
  height: 45px;
  margin-left: 5px;
}
label {
  width: 30%;
  text-align: left;
}
.col-7 .row .col-12 {
  padding: 0px 5px;
  text-align: left;
  color: #fff !important;
  font-size: 30px;
}
.equal {
  text-align: center;
  color: #fff !important;
  font-size: 30px;
  line-height: 30px;
}
.col-3 input,
select {
  width: 100%;
}

.edit-block {
  position: absolute;
  width: 74px;
  height: 28.23px;
  left: 93px;
  top: 295px;
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
h2 {
  color: #fff;
  text-align: left;
}
#qty .col-4 {
  color: #fff !important;
  font-size: 30px;
  width: 100%;
}

.i-25 {
  width: 160px;
  text-align: right;
  border-radius: 10px;
  height: 40px;
  padding-right: 10px;
}
.lp-txt {
  font-size: 24px;
  color: white;
  text-align: center;
}
.input-prepend {
  margin-right: 6px;
  border-radius: 10px 0px 0px 10px;
  width: 150px;
  height: 40px;
}
.select-append {
  width: 0px;
  height: 40px;
  border-radius: 0px 10px 10px 0px;
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
  background-color: #717171;
  padding-right: 2rem !important;
  border-radius: 10px;
  font-size: 24px;
  border: 0px;
  text-indent: 10px;
}
.image {
  width: 220px;
  height: 220px;
  border-radius: 25px;
  object-fit: cover;
  left: 80px;
  position: absolute;
  top: 118px;
}
</style>