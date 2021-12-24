<template>
  <div>
    <nav-app save="true" @save="save()">New&#160;RM</nav-app>
    <div class="container-f">
      <div class="frame f-1">
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
            <div class="col-12 h-25">
              <input
                type="text"
                style="width: 350px; margin: auto"
                placeholder="Name"
                v-model="name"
              />
            </div>
            <div class="col-12 h-25">
              <label for="">Category&nbsp;:</label>
              <select
                name="category"
                id="category"
                v-model="category_id"
                style="height: 50px"
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
            <div class="col-12 h-25">
              <label for="" style="display: inline"
                >Status&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:
                <button
                  class="btn-y"
                  style="width: 100px; display: inilne"
                  :class="{ 'btn-g': remain > minimum }"
                >
                  {{ status_am }}
                </button></label
              >
            </div>
            <div class="col-12 h-25">
              <label for="">Fridge&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</label>
              <div class="switch"><Switch @switch="fridge" /></div>
            </div>
          </div>
        </div>
      </div>
      <div class="frame f-2" style="height: 220px; padding-left: 0px">
        <!-- Head Of Section 2 -->
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
              Smallest Unit Detail
            </div>
          </div>
        </div>
        <!-- Content -->
        <div class="row">
          <div class="col-4" style="width: 100%; padding: 0px;">
            <label for="">Qty&nbsp;:</label>
            <input type="number" style="background: #717171; width: 100px; height: 50px;" v-model="remain" />
          </div>
          <div class="col-4" style="width: 100%; padding: 0px;">
            <label for="">Min&nbsp;Qty&nbsp;:</label
            ><input type="number" style="background: #717171; width: 100px; height: 50px;" v-model="minimum" />
          </div>
          <div class="col-4" style="width: 100%; padding: 0px;">
            <label for="">Max Qty&nbsp;:</label
            ><input type="number" style="background: #717171; width: 100px; height: 50px;" v-model="maximum" />
          </div>
        </div>
        <div class="row" style="margin-top: 30px;">
          <div class="col-6" style="width: 100%; padding: 0px;">
            <label for="">Price&nbsp;:</label
            ><input type="number" style="background: #717171; width: 234px; height: 50px; margin-left: -10px" v-model="maximum" />
          </div>
          <div class="col-6" style="width: 100%; padding: 0px;">
            <label for="">Supplier&nbsp;:</label
            ><input type="number" style="background: #717171; width: 234px; height: 50px;" v-model="maximum" />
          </div>
        </div>
      </div>
      <div class="frame f-2" style="height: 286px">
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
        <div class="row" style="width: 99%">
          <input
            type="number"
            class="i-25 g"
            v-model="s_to_m"
            placeholder="S Unit"
            style="text-align: right; border-radius: 10px; background: #717171;"
          />
          <select v-model="unit_s_id" class="i-25 ig" style="border-radius: 10px">
            <option value="" selected disabled style="color: white;">unit</option>
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
            style="text-align: right; border-radius: 10px; background: #717171;"
          />
          <select
            name=""
            id=""
            v-model="unit_m_id"
            class="i-25 ig"
            style="border-radius: 10px"
          >
            <option value="" selected disabled style="color: white;">unit</option>
            <option v-for="unit in units" :key="unit.id" :value="unit.id">
              {{ unit.unit }}
            </option>
          </select>
        </div>
        <!-- Second Row -->
        <div class="row m-15" style="width: 99%">
          <input
            type="number"
            class="i-25 g"
            v-model="m_to_l"
            placeholder="M to L Unit"
            style="text-align: right; border-radius: 10px; background: #717171;"
          />
          <select
            v-model="unit_m_id"
            class="i-25 ig"
            style="border-radius: 10px; color: white;"
          >
            <option value="" selected disabled style="color: white;">unit</option>
            <option v-for="unit in units" :key="unit.id" :value="unit.id">
              {{ unit.unit }}
            </option>
          </select>

          <span style="color: #fff; font-size: 30px">=</span>

          <input
            type="number"
            value="1"
            class="i-25 g"
            style="text-align: right; border-radius: 10px; background: #717171;"
          />
          <select
            name=""
            id=""
            v-model="unit_l_id"
            class="i-25 ig"
            style="border-radius: 10px"
          >
            <option value="" selected disabled style="color: white;">unit</option>
            <option v-for="unit in units" :key="unit.id" :value="unit.id">
              {{ unit.unit }}
            </option>
          </select>
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
      img: null,
      status: null,
      name: null,
      minimum: null,
      remain: null,
      maximum: null,
      in_refrigerator: null,
      create_by_id: null,
      update_by_id: null,
      category_id: null,
      unit_l_id: null,
      unit_m_id: null,
      unit_s_id: null,
      m_to_l: null,
      s_to_m: null,
      avg_l: null,
      avg_m: null,
      avg_s: null,
      unit_id: null,
      total_price: 0,
      show_img: null,
      avg: null,
      categories: [],
      to_unit_id: null,
      next_unit_id: null,
      to_amount: 1,
      next_amount: 0,
      units: [],
    };
  },
  methods: {
    onFileChange(e) {
      console.log(e, 'e')
      this.img = e.target.files[0];
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
      console.log(this.img, 'img')
    },
    fridge(val) {
      this.is_refrigerator = val;
    },
    save() {
      const data = new FormData();
      data.append("maximum", this.maximum);
      data.append("minimum", this.minimum);
      data.append("remain", this.remain);
      data.append("category_id", this.category_id);
      data.append("name", this.name);
      data.append("is_refrigerator", this.is_refrigerator);
      data.append("img", this.img, this.img.name);
      data.append("to_unit_id", this.to_unit_id);
      data.append("next_unit_id", this.next_unit_id);
      data.append("to_amount", this.to_amount);
      data.append("next_amount", this.next_amount);
      data.append("unit_l_id", this.unit_l_id);
      data.append("unit_m_id", this.unit_m_id);
      data.append("unit_s_id", this.unit_s_id);
      data.append("m_to_l", this.m_to_l);
      data.append("s_to_m", this.s_to_m);
      data.append("avg_l", this.avg_l);
      data.append("avg_m", this.avg_m);
      data.append("avg_s", this.avg_s);
      data.append("update_by_id", this.$store.state.auth.userInfo.id);
      data.append("create_by_id", this.$store.state.auth.userInfo.id);

      api_raw_material.post("raw-material/", data).then((response) => {
        console.log(response.data, 'response data')
        this.$router.push({ name: "CreateRM" });
      });
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
        return "success";
      } else {
        return "ไม่พอ";
      }
    },
  },
  mounted() {
    api_raw_material.get("category").then((response) => {
      this.categories = response.data;
    });
    api_raw_material.get("unit").then((response) => {
      console.log(response.data, 'unit')
      this.units = response.data;
    });
  },
};
</script>

<style scoped>
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