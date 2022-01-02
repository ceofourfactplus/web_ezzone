<template>
  <div>
    <div v-if="loading" style="color: white; font-size: 30px; margin-top: 20px;">
      Loading ...
    </div>
    <div v-else>
      <nav-app save="true" @save="edit()">Edit&#160;RM</nav-app>
    <div class="container-f">
      <div class="frame f-1">
        <div class="row h-100">
          <div class="col-5 w-100">
            <div class="row">
              <div class="col-12" style="padding: 0px">
                <label id="select_img" for="file" style="margin-top: 0px">
                  <img :src="require(`../../../../backend${rm_item.raw_material_set.img}`)" class="image" />
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
                style="width: 350px; margin: auto"
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
                style="height: 50px; margin-top: 10px;"
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
            <div class="col-12 h-25" style="margin-top: 10px;">
              <label for="" style="display: inline"
                >Status&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:
                <img :src="$store.state.raw_material.status_image[rm_item.raw_material_set.status]">
                </label>
            </div>
            <!-- Fridge -->
            <div class="col-12 h-25">
              <label for="">Fridge&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</label>
              <div class="switch"><Switch @switch="fridge" /></div>
            </div>
          </div>
        </div>
      </div>
      <div class="frame f-2" style="height: 290px; padding-left: 0px">
        <!-- Head Of Section 2 -->
        <div class="row">
          <div class="col-12" style="margin-left: 20px">
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
        <!-- First Row -->
        <div class="row">
          <div class="col-4 row-wrapper">
            <label for="">Qty&nbsp;&nbsp;&nbsp;:&nbsp;</label>
            <input
              type="number"
              style="background: #717171; width: 100px; height: 50px"
              v-model="rm_item.raw_material_set.remain"
            />
          </div>
          <div class="col-4 row-wrapper">
            <label for="">Min&nbsp;Qty&nbsp;:</label
            ><input
              type="number"
              style="background: #717171; width: 100px; height: 50px"
              v-model="rm_item.raw_material_set.minimum"
            />
          </div>
          <div class="col-4 row-wrapper" style="margin-right: 20px">
            <label for="">Max Qty&nbsp;:</label
            ><input
              type="number"
              style="background: #717171; width: 100px; height: 50px"
              v-model="rm_item.raw_material_set.maximum"
            />
          </div>
        </div>
        <!-- Second Row -->
        <div class="row" style="margin-top: 30px">
          <div class="col-6 row-wrapper">
            <label for="">Avg S&nbsp;:&nbsp;&nbsp;</label
            ><input
              type="number"
              style="
                background: #717171;
                width: 220px;
                height: 50px;
                margin-left: -10px;
              "
              v-model="rm_item.raw_material_set.avg_s"
            />
          </div>
          <div class="col-6 row-wrapper" style="margin-right: 20px">
            <label for="">Avg M&nbsp;:&nbsp;&nbsp;</label
            ><input
              type="number"
              style="
                background: #717171;
                width: 200px;
                height: 50px;
                margin-right: -40px;
              "
              v-model="rm_item.raw_material_set.avg_m"
            />
          </div>
        </div>
        <!-- Third Row -->
        <div class="row" style="margin-top: 30px">
          <div class="col-6 row-wrapper" style="margin-right: 20px">
            <label for="">Avg L&nbsp;:&nbsp;</label
            ><input
              type="number"
              style="background: #717171; width: 220px; height: 50px"
              v-model="rm_item.raw_material_set.avg_l"
            />
          </div>
          <div class="col-6 row-wrapper">
            <label for="">Supplier&nbsp;:&nbsp;&nbsp;</label>
            <select
              v-model="rm_item.supplier_id"
              class="i-25 ig"
              style="
                border-radius: 10px;
                width: 190px;
                margin-right: -30px;
                height: 50px;
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
      <div class="frame f-2" style="height: 230px">
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
        <div class="row" style="width: 99%; margin-left: 5px;">
          <input
            type="number"
            class="i-25 g"
            v-model="rm_item.raw_material_set.s_to_m"
            placeholder="S Unit"
            style="text-align: right; border-radius: 10px; background: #717171"
          />
          <select
            v-model="rm_item.raw_material_set.unit_s_id"
            class="i-25 ig"
            style="border-radius: 10px; width: 170px;"
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
            style="text-align: right; border-radius: 10px; background: #717171"
          />
          <select
            name=""
            id=""
            v-model="rm_item.raw_material_set.unit_m_id"
            class="i-25 ig"
            style="border-radius: 10px; width: 170px;"
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
        <div class="row m-15" style="width: 99%; margin-left: 5px;">
          <input
            type="number"
            class="i-25 g"
            v-model="rm_item.raw_material_set.m_to_l"
            placeholder="M to L Unit"
            style="text-align: right; border-radius: 10px; background: #717171"
          />
          <select
            v-model="rm_item.raw_material_set.unit_m_id"
            class="i-25 ig"
            style="border-radius: 10px; color: white; width: 170px;"
          >
            <option value="" selected disabled style="color: white">
              unit
            </option>
            <option
              v-for="unit in units"
              :key="unit.id"
              :value="unit.id"
            >
              {{ unit.unit }}
            </option>
          </select>

          <span style="color: #fff; font-size: 30px">=</span>

          <input
            type="number"
            value="1"
            class="i-25 g"
            style="text-align: right; border-radius: 10px; background: #717171"
          />
          <select
            name=""
            id=""
            v-model="rm_item.raw_material_set.unit_l_id"
            class="i-25 ig"
            style="border-radius: 10px; width: 170px;"
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
      rm_item: {},
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
      this.loading = true
      api_raw_material.get(`/raw-material/${this.$route.params.id}`).then((response) => {
        console.log(response.data, "raw_material");
        this.rm_item = response.data;
        this.loading = false
        console.log(this.rm_item, 'rm_item')
      });
    },
    onFileChange(e) {
      console.log(e, "e");
      this.img = e.target.files[0];
      this.new_img = true
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
    edit() {
      const data = new FormData();
      data.append("id", this.rm_item.raw_material_set.id);
      data.append("maximum", this.rm_item.raw_material_set.maximum);
      data.append("minimum", this.rm_item.raw_material_set.minimum);
      data.append("remain", this.rm_item.raw_material_set.remain);
      data.append("category_id", this.rm_item.raw_material_set.category_id);
      data.append("name", this.rm_item.raw_material_set.name);
      data.append("is_refrigerator", this.rm_item.raw_material_set.is_refrigerator);
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
        user_data.append("img", this.rm_item.raw_material_set.img, this.rm_item.raw_material_set.img.name);
      }
      api_raw_material.put("rm-update/", data).then((response) => {
        console.log(response.data, "response data");
      });
    },
  },
  beforeMount () {
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
    api_raw_material.get("unit").then((response) => {
      console.log(response.data, "unit");
      this.units = response.data;
    });
  },
};
</script>

<style scoped>
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
  margin-top: 16px;
  margin-bottom: 0px;
  background-color: #303344;
  border-radius: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 20px;
}
.f-1 {
  width: 725px;
  height: 270px;
}
.f-2 {
  width: 725px;
  height: 170px;
}
.f-3 {
  width: 725px;
  height: 230px;
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
  left: 70px;
  top: 320px;

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
  width: 236px;
  height: 235px;
  border-radius: 25px;
  margin-right: 12px;
  background-color: #717171;
}
.image {
  width: 236px;
  height: 235px;
  border-radius: 25px;
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
  width: 145px;
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