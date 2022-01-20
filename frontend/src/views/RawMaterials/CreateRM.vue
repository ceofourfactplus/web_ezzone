<template>
  <div>
    <nav-app :url_name="'RawMaterials'" save="true" @save="save()"
      >New&#160;RM</nav-app
    >
    <div class="container-f">
      <div class="frame">
        <div class="row h-100">
          <div class="col-5 w-100">
            <div class="row">
              <div class="col-12" style="padding: 0px">
                <label id="select_img" for="file" style="margin-top: 0px">
                  <img :src="show_img" class="image" v-if="show_img != null" />
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
                  background: #717171;
                  height: 50px;
                "
                placeholder="Name"
                v-model="name"
              />
            </div>
            <!-- Category -->
            <div class="col-12 h-25" style="margin-top: 10px">
              <label for="">Category&nbsp;:</label>
              <select
                name="category"
                id="category"
                v-model="category_id"
                style="height: 40px; width: 180px"
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
                  style="width: 180px; height: 50px; display: inilne"
                  :class="{
                    'btn-g': remain > minimum,
                    'btn-r': remain == 0 || remain == '' || remain == null,
                    'btn-y': remain < minimum || remain == minimum,
                  }"
                >
                  {{ status_txt }}
                </button></label
              >
            </div>
            <!-- Fridge -->
            <div class="col-12 h-25" style="line-height: 60px">
              <label for="">Fridge&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</label>
              <div class="switch"><Switch @switch="fridge" /></div>
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
                font-size: 30px;
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
        <!-- Min & Max -->
        <div class="row">
          <div class="col-6 row-wrapper" style="margin-left: 0.5px">
            <label for="">Min&nbsp;Qty&nbsp;:&nbsp;</label
            ><input
              type="number"
              style="background: #717171; width: 180px; height: 40px"
              v-model="minimum"
            />
          </div>
          <div class="col-6 w-100" style="margin-left: 3px">
            <label for="">Max Qty&nbsp;:&nbsp;</label
            ><input
              type="number"
              style="background: #717171; width: 180px; height: 40px"
              v-model="maximum"
            />
          </div>
        </div>
      </div>
      <div class="frame" style="height: 160px; padding-left: 0px">
        <!-- Price & Qty -->
        <div class="row" style="margin-top: 0px; line-height: 50px">
          <div class="col-4">
            <input type="text">
          </div>
          <!-- <div class="col-6 w-100" style="margin-left: 10px">
            <label for="price" style="display: inline; margin-left: -100px"
              >Price&nbsp;:&nbsp;</label
            >
            <input
              v-model="price"
              type="text"
              id="price"
              name="price"
              style="display: inline; width: 240px; margin-right: -110px"
            />
          </div>
          <div
            class="col-1 w-100"
            style="
              color: white;
              font-size: 36px;
              height: 100%;
              position: relative;
              bottom: 4px;
              right: 10px;
            "
          >
            /
          </div>
          <div class="col-2 w-100">
            <input
              type="text"
              placeholder="Qty"
              style="width: 100%; margin-top: 5px"
              @input="remain_func($event)"
            />
          </div>
          <div class="col-3 w-100" style="margin-left: -17px">
            <select
              @change="calc_status_rm"
              v-model="unit_price_id"
              class="i-25 ig"
              style="
                border-radius: 10px;
                color: white;
                width: 100%;
                height: 40px;
                margin-top: 5px;
              "
            >
              <option value="" selected disabled style="color: white">
                unit
              </option>
              <option v-for="unit in units" :key="unit.id" :value="unit.id">
                {{ unit.unit }}
              </option>
            </select>
          </div> -->
        </div>
        <!-- Supplier -->
        <div class="row" style="margin-top: 20px">
          <div class="col-12 row-wrapper">
            <label style="margin-left: -2px">Supplier&nbsp;:&nbsp;&nbsp;</label>
            <select
              v-model="supplier_id"
              class="i-25 ig"
              style="
                border-radius: 10px;
                width: 655px;
                margin-right: -25px;
                height: 40px;
              "
            >
              <option value="" selected disabled style="color: white">
                unit
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
        </div>
      </div>
      <div class="frame" style="height: 210px">
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
            class="g"
            v-model="s_to_m"
            @input="makeAvgList(s_to_m, unit_s_id)"
            placeholder="S Unit"
            style="text-align: right; border-radius: 10px; background: #717171"
          />
          <input
            type="text"
            class="input-prepend"
            style="color: white; background: #717171"
            v-model="unit_s_name"
          />
          <select
            v-model="unit_s_id"
            @change="find_unit_s"
            class="ig select-append"
          >
            <option value="" selected style="color: white">
              <input type="text" />
            </option>
            <option v-for="unit in units" :key="unit.id" :value="unit.id">
              {{ unit.unit }}
            </option>
          </select>

          <span
            style="
              color: #fff;
              font-size: 30px;
              position: relative;
              bottom: 7px;
            "
            >=</span
          >

          <input
            type="number"
            class="i-25 g"
            model="to_amount"
            value="1"
            readonly
            style="text-align: right; border-radius: 10px; background: #717171"
          />
          <input
            type="text"
            class="input-prepend"
            style="color: white; background: #717171"
            v-model="unit_m_name"
          />
          <select
            name=""
            id=""
            v-model="unit_m_id"
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
            v-model="m_to_l"
            @input="makeAvgList(m_to_l, unit_m_id)"
            placeholder="M to L Unit"
            style="text-align: right; border-radius: 10px; background: #717171"
          />
          <input
            type="text"
            class="input-prepend"
            style="color: white; background: #717171"
            v-model="unit_m_name"
          />
          <select
            v-model="unit_m_id"
            @change="find_unit_m"
            class="ig select-append"
          >
            <option value="" selected disabled style="color: white">
              unit
            </option>
            <option
              v-for="unit in units"
              :key="unit.id"
              :value="unit.id"
              @click="console.log(unit.unit)"
            >
              {{ unit.unit }}
            </option>
          </select>

          <span
            style="
              color: #fff;
              font-size: 30px;
              position: relative;
              bottom: 7px;
            "
            >=</span
          >

          <input
            type="number"
            value="1"
            class="i-25 g"
            style="text-align: right; border-radius: 10px; background: #717171"
          />
          <input
            type="text"
            class="input-prepend"
            style="color: white; background: #717171"
            v-model="unit_l_name"
          />
          <select
            v-model="unit_l_id"
            @change="find_unit_l"
            class="ig select-append"
          >
            <option
              value=""
              selected
              disabled
              style="color: white; width: 50px"
            >
              unit
            </option>
            <option v-for="unit in units" :key="unit.id" :value="unit.id">
              {{ unit.unit }}
            </option>
          </select>
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
import SavePopup from "../../components/main_component/SavePopup.vue"

export default {
  components: { NavApp, Switch, SavePopup },
  data() {
    return {
      status_txt: "Out of Stock",
      raw_material_id: null,
      img: null,
      status: null,
      name: null,
      minimum: null,
      remain: null,
      temp_remain: null,
      maximum: null,
      in_refrigerator: null,
      supplier_id: null,
      price: null,
      alert: false,
      create_by_id: null,
      category_id: null,
      unit_price_id: null,
      unit_l_name: null,
      unit_m_name: null,
      unit_s_name: null,
      price_s: 0,
      price_m: 0,
      price_l: 0,
      m_to_l: "",
      s_to_m: "",
      avg_l: 0,
      avg_s: 0,
      avg_m: 0,
      unit_id: null,
      total_price: 0,
      show_img: null,
      avg: null,
      categories: [],
      to_unit_id: null,
      next_unit_id: null,
      to_amount: 1,
      next_amount: 0,
      selected_unit_id: [],
      selected_units: [],
      units: [],
      suppliers: [],
      unit_price_list: [],
    };
  },
  methods: {
    fetchSuppliers() {
      api_raw_material.get("/supplier/").then((response) => {
        console.log(response.data, "suppliers");
        this.suppliers = response.data;
      });
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
    fridge(val) {
      this.is_refrigerator = val;
    },
    async save() {
      if (this.unit_price_id == this.unit_m_id) {
        this.remain = this.temp_remain * this.s_to_m;
      } else if (this.unit_price_id == this.unit_l_id) {
        this.remain = this.temp_remain * this.m_to_l * this.s_to_m;
      }
      const data = {
        maximum: this.maximum,
        minimum: this.minimum,
        category_id: this.category_id,
        name: this.name,
        is_refrigerator: this.is_refrigerator,
        to_amount: this.to_amount,
        supplier_id: this.supplier,
        unit_l_name: this.unit_l_name,
        unit_m_name: this.unit_m_name,
        unit_s_name: this.unit_s_name,
        m_to_l: this.m_to_l,
        s_to_m: this.s_to_m,
        create_by: 1,
        pricerawmaterial_set: this.pricerawmaterial_set,
      };
      api_raw_material.post("raw-material/", data).then(() => {
        this.$router.push({ name: "RawMaterials" });
      });
    },
    makeAvgList() {
      if (this.s_to_m != "" && this.unit_s_id != "") {
        if (this.selected_unit_id.indexOf(this.unit_s_id) + 1 != 0) {
        } else {
          this.selected_unit_id.push(this.unit_s_id);
        }
      }
      if (this.m_to_l != "" && this.unit_m_id != "") {
        if (this.selected_unit_id.indexOf(this.unit_m_id) + 1 != 0) {
        } else {
          this.selected_unit_id.push(this.unit_m_id);
        }
      }

      if (this.m_to_l != "" && this.unit_l_id != "") {
        if (this.selected_unit_id.indexOf(this.unit_l_id) + 1 != 0) {
        } else {
          this.selected_unit_id.push(this.unit_l_id);
        }
      }

      this.units.forEach((element) => {
        if (this.selected_unit_id.indexOf(element.id) + 1 != 0) {
          if (this.selected_units.indexOf(element) + 1 == 0) {
            this.selected_units.push(element);
          }
        }
      });
    },
    makeUnitPrice() {
      this.unit_price_list.push({
        price: this.price,
        unit: this.units.find((x) => x.id == this.unit_price_id).unit,
        unit_id: this.unit_price_id,
      });
      this.price = null;
      this.unit_price_id = null;
    },
    find_unit_s() {
      this.unit_s_name = this.units.find((x) => x.id == this.unit_s_id).unit;
      this.calc_status_rm();
      this.status_am;
    },
    find_unit_m() {
      this.unit_m_name = this.units.find((x) => x.id == this.unit_m_id).unit;
      this.calc_status_rm();
      this.status_am;
    },
    find_unit_l() {
      this.unit_l_name = this.units.find((x) => x.id == this.unit_l_id).unit;
      this.calc_status_rm();
      this.status_am;
    },
    remain_func(e) {
      this.temp_remain = e.target.value;
      this.calc_status_rm();
    },
    calc_status_rm() {
      if (this.unit_price_id == this.unit_m_id) {
        this.remain = this.temp_remain * this.s_to_m;
      } else if (this.unit_price_id == this.unit_l_id) {
        this.remain = this.temp_remain * this.m_to_l * this.s_to_m;
      } else if (this.unit_price_id == this.unit_s_id) {
        this.remain = this.temp_remain;
      }
      this.status_am;
    },
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
        this.status_txt = "In Stock";
      } else if (this.remain == 0 || this.remain == "" || this.remain == null) {
        this.status_txt = "Out of Stock";
      } else {
        this.status_txt = "Minimum";
      }
    },
  },
  mounted() {
    this.fetchSuppliers();
    setInterval(() => {
      this.makeAvgList();
    }, 2000);
    api_raw_material.get("category").then((response) => {
      this.categories = response.data;
    });
    api_raw_material.get("unit").then((response) => {
      this.units = response.data;
    });
  },
};
</script>

<style scoped>
label {
  font-size: 24px;
  bottom: 5px;
  position: relative;
}
input {
  height: 40px;
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
  width: 130px;
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
  position: relative;
  width: 74px;
  height: 28.23px;
  left: 15px;
  top: 180px;
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
  margin-right: 12px;
  background-color: #717171;
}
.image {
  width: 220px;
  height: 220px;
  border-radius: 25px;
  right: 0px;
  object-fit: cover;
  position: absolute;
}
.switch {
  display: inline-block;
  top: 10px;
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
  width: 175px;
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
  margin-left: 10px;
  width: 200px;
  font-size: 30px;
  color: #fff;
  border-radius: 10px;
  font-size: 24px;
  border: 0px;
  text-indent: 10px;
}
</style>