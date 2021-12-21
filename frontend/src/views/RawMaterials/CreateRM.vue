<template>
  <div>
    <nav-app save="true">New&#160;RM</nav-app>
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
              <label for="">Category&nbsp;:</label
              ><select name="category" id="category" v-model="category_id">
                <option
                  v-for="category in categories"
                  :key="category.id"
                  :value="category.id"
                >
                  {{ category.category }}
                </option>
              </select>
            </div>
            <div class="col-12 h-25">
              <label for="">Status&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</label>
              <div></div>
            </div>
            <div class="col-12 h-25">
              <label for="">Fridge&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</label>
              <div class="switch"><Switch @switch="fridge" /></div>
            </div>
          </div>
        </div>
      </div>
      <div class="frame f-2">
        <div class="row">
          <div class="col-6 label-input">
            <label for="">Qty&nbsp;&nbsp;:</label
            ><input type="text" style="width: 74%" v-model="remain" />
          </div>
          <div class="col-6 label-input">
            <label for="">Min&nbsp;Qty&nbsp;:</label
            ><input type="text" style="width: 55%" v-model="minimum" />
          </div>
          <div class="col-6 label-input m-15">
            <label for="units">Unti&nbsp;&nbsp;:</label
            ><input
              type="text"
              style="width: 70%"
              v-model="unit"
              id="units"
              list="unit"
            />
            <datalist id="unit">
              <option v-for="unit in units" :key="unit.id">
                {{ unit.unit }}
              </option>
            </datalist>
          </div>
          <div class="col-6 label-input m-15">
            <label for="">Max&nbsp;Qty&nbsp;:</label
            ><input type="text" style="width: 53%" v-model="maximum" />
          </div>
        </div>
      </div>
      <div class="frame f-3">
        <div class="row">
          <div class="col-6 label-input">
            <label for="">Min&nbsp;Price&nbsp;&nbsp;:</label>
            <input type="number" style="width: 47%" v-model="min_price" />
          </div>
          <div class="col-6 label-input">
            <label for="">Max&nbsp;Price&nbsp;:</label
            ><input type="number" style="width: 48%" v-model="maximum" />
          </div>
          <div class="col-6 label-input m-15">
            <label for="">Total&nbsp;Cost&nbsp;:</label
            ><input type="number" style="width: 5p;0%" v-model="total_price" />
          </div>
          <div class="col-6 label-input m-15">
            <label for="">Avg&nbsp;Price&nbsp;&nbsp;:</label
            ><input type="number" style="width: 48%" v-model="avg_price" />
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
      category_id: null,
      status: true,
      remain: null,
      unit: null,
      minimum: null,
      maximum: null,
      avg_price: null,
      min_price: null,
      max_price: null,
      img: null,
      is_refrigerator: false,
      min_price_supplier: null,
      max_price_supplier: null,
      name: "",
      total_price: 0,
      show_img: null,
      categories: [],
      units: [],
    };
  },
  methods: {
    onFileChange(e) {
      this.img = e.target.files[0];
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.show_img);
      }
    },
    fridge(val) {
      this.is_refrigerator = val;
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
  mounted() {
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
.frame {
  margin-top: 15px;
  margin-bottom: 20px;
  background-color: #303344;
  border-radius: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 20px;
}
.f-1 {
  width: 680px;
  height: 270px;
}
.f-2 {
  width: 680px;
  height: 170px;
}
.f-3 {
  width: 680px;
  height: 235px;
}
.container-f {
  padding-left: 22px;
  margin-right: auto;
  margin-left: auto;
}
input {
  background-color: #717171;
  width: 150px;
  height: 50px;
  margin-left: 10px;
}
select {
  background-color: #303344;
  margin-left: 10px;
  width: 200px;
  font-size: 30px;
  color: #fff;
  border: 0px;
}
raw-img {
  width: 236px;
  height: 235px;
}

label {
  color: #fff;
  font-size: 30px;
}

::placeholder {
  text-indent: 10 px;
  color: #fff;
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
  left: 80px;
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
</style>