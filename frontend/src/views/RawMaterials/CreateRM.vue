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
            <label for="units">Unit&nbsp;&nbsp;:</label
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
      <div class="frame f-2">
        <div class="row" style="width: 99%">
          <input type="number" class="i-25" style="text-align: right" />
          <select name="" id="" class="i-25">
            <option value="" selected>unit</option>
            <option v-for="unit in units" :key="unit.id" value="">
              {{ unit.unit }}
            </option>
          </select>
          <span style="color: #fff; font-size: 30px">&#160;&#160;=</span>
          <input type="number" class="i-25" style="text-align: right" />
          <select name="" id="" class="i-25">
            <option value="" selected>unit</option>
            <option v-for="unit in units" :key="unit.id" value="">
              {{ unit.unit }}
            </option>
          </select>
        </div>
        <div class="row m-15" style="width: 99%">
          <input type="number" class="i-25" style="text-align: right" />
          <select name="" id="" class="i-25">
            <option value="" selected>unit</option>
            <option v-for="unit in units" :key="unit.id" value="">
              {{ unit.unit }}
            </option>
          </select>
          <span style="color: #fff; font-size: 30px">&#160;&#160;=</span>
          <input type="number" class="i-25" style="text-align: right" />
          <select name="" id="" class="i-25">
            <option value="" selected>unit</option>
            <option v-for="unit in units" :key="unit.id" value="">
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
      category_id: null,
      status: true,
      remain: null,
      unit: null,
      minimum: null,
      maximum: null,
      img: null,
      is_refrigerator: false,
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
        reader.readAsDataURL(this.img);
      }
    },
    fridge(val) {
      this.is_refrigerator = val;
    },
    save() {
      const data = new FormData();
      data.append("maximum", this.maximum);
      data.append("minimum", this.minimum);
      data.append("remain", this.remain);
      data.append("category", this.category);
      data.append("name", this.name);
      data.append("is_refrigerator", this.is_refrigerator);
      data.append("img", this.img, this.img.name);
      data.append("unit", this.unit);
      data.append("update_by_id", this.$store.state.auth.userInfo.id);
      data.append("create_by_id", this.$store.state.auth.userInfo.id);
      api_raw_material.post("raw-material/", data).then((response) => {
        this.$router.push({name:'CreateRM'});
        console.log(response)
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
.i-25 {
  width: 140px;
}
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
  height: 230px;
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

option {
  font-size: 20px;
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