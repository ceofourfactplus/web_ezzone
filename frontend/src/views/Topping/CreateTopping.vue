<template>
  <div>
    <nav-app save="true" :url_name="'Topping'" @save="create_product"
      >New&#160;Topping&#160;</nav-app
    >
    <div class="container-f w-100">
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
              <label for="">Code&nbsp;&nbsp;&nbsp;:</label
              ><input type="text" style="width: 67%" v-model="code" />
            </div>
            <div class="col-12 h-25">
              <label for="">Name&nbsp;&nbsp;:</label
              ><input type="text" style="width: 66%" v-model="name" />
            </div>
            <div class="col-12 h-25">
              <label for=""
                >Status&nbsp;&nbsp;:&nbsp;<button
                  class="btn-y"
                  style="
                    width:  %;
                    display: inilne;
                    height: 36px;
                    line-height: 100%;
                    white-space:nowrap;
                  "
                  :class="{ 'btn-g': remain > minimum }"
                >
                  out of stock
                </button></label
              >
            </div>
            <div class="col-12 h-25">
              <label for="">Active&nbsp;&nbsp;:</label>
              <div class="switch">
                <Switch @switch="switch_active()" :value="active" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="frame f-2">
        <div class="row">
          <div class="col-6 label-input">
            <label for="">Qty&nbsp;&nbsp;:</label
            ><input type="number" style="width: 74%" v-model="remain" />
          </div>
          <div class="col-6 label-input">
            <label for="">Min&nbsp;Qty&nbsp;:</label
            ><input type="number" style="width: 55%" v-model="minimum" />
          </div>
          <div class="col-6 label-input m-15">
            <label for="unit">Unit&nbsp;&nbsp;:</label
            ><select
              name="unit"
              id="unit"
              style="width: 225px"
              v-model="unit_id"
            >
              <option v-for="unit in all_unit" :key="unit.id" :value="unit.id">
                {{ unit.unit }}
              </option>
            </select>
          </div>
          <div class="col-6 label-input m-15">
            <label for="">Max&nbsp;Qty&nbsp;:</label
            ><input type="number" style="width: 53%" v-model="maximum" />
          </div>
        </div>
      </div>
      <div class="frame f-2">
        <div class="row">
          <div class="col-5 label-input">
            <label for="flavour">Price&nbsp;:</label
            ><input type="number" v-model="price" style="width: 160px" />
          </div>
          <div class="col-7 label-input">
            <label for="stock">Stock :</label
            ><select id="type_topping" style="width: 260px" v-model="warehouse">
              <option value="0">not pickup</option>
              <option value="1">product</option>
              <option value="2">material</option>
            </select>
          </div>
          <div class="col-12 label-input m-15">
            <label for="type_topping">Topping Type : </label>
            <select
              id="type_topping"
              style="width: 445px"
              v-model="type_topping"
            >
              <option value="1">DRESSERT</option>
              <option value="2">DRINK</option>
              <option value="3">FOOD</option>
            </select>
          </div>
        </div>
      </div>
    </div>
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import SavePopup from "../../components/main_component/SavePopup.vue"
import { api_product } from "../../api/api_product";
import { api_raw_material } from "../../api/api_raw_material";
import { api_user } from "../../api/api_user";
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";

export default {
  components: { NavApp, Switch, SavePopup },
  mounted() {
    this.get_unit();
    this.get_user();
    this.get_category();
  },
  data() {
    return {
      show_img: null,
      alert: false,
      all_user: [],
      categories: [],
      all_unit: [],
      code: "",
      img: null,
      status: 1,
      active: true,
      unit_id: null,
      remain: 0,
      minimum: 0,
      maximum: 0,
      price: 0,
      name: "",
      warehouse: 0,
      type_topping: 0,
    };
  },
  methods: {
    get_user() {
      api_user.get("read-all/").then((response) => {
        this.all_product = response.data;
      });
    },
    get_category() {
      api_product.get("category/").then((response) => {
        this.categories = response.data;
      });
    },
    get_unit() {
      api_raw_material.get("unit").then((response) => {
        this.all_unit = response.data;
      });
    },
    onFileChange(e) {
      this.img = e.target.files[0];
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
    },
    create_product() {
      if (this.img != null) {
        const data = new FormData();
        data.append("code", this.code);
        data.append("category_id", this.category_id);
        data.append("unit_id", this.unit_id);
        data.append("status", this.status);
        data.append("is_active", this.active);
        data.append("remain", this.remain);
        data.append("minimum", this.minimum);
        data.append("maximum", this.maximum);
        data.append("price", this.price);
        data.append("name", this.name);
        data.append("warehouse", this.warehouse);
        data.append("type_topping", this.type_topping);
        data.append("create_by_id", 1);
        data.append("old_product_id", 1);
        api_product.post("topping/", data).then((response) => {
          const img = new FormData();
          img.append("img", this.img, this.img.name);
          api_product.put("get-topping/" + response.data.id, img).then(() => {
            this.alert = true
            setTimeout(() => {
              this.alert = false
              this.$router.push({ name: "Topping" });
            },)
          });
        });
      }
    },

    switch_flavour_level(val) {
      this.flavour_level = val;
    },
    switch_active() {
      this.active = !this.active;
    },
  },
  watch: {
    maximum(newData) {
      if (newData <= this.minimum) {
        this.maximum = this.minimum + 1;
      }
    },
    share(ND) {
      if (ND == 0) {
        this.percent = false;
      } else {
        this.percent = true;
      }
    },
  },
};
</script>

<style scoped>
.frame {
  margin: 15px auto 20px auto;
  background-color: #303344;
  border-radius: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 20px;
}
.f-1 {
  width: 680px;
  height: 300px;
}
.f-2 {
  width: 680px;
  height: 170px;
}
.container-f {
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
  height: 50px;
  width: 200px;
  color: #fff;
  border: 0px;
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
.h-25 {
  height: 20%;
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
  left: 100px;
  top: 340px;

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
  width: 260px;
  height: 260px;
  border-radius: 25px;
  margin-right: 12px;
  background-color: #717171;
}
.image {
  width: 260px;
  height: 260px;
  object-fit: cover;
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