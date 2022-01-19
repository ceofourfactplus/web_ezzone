<template>
  <div>
    <nav-app save="true" @save="create_product">New&#160;Product&#160;Detail</nav-app>
    <div class="container-f">
      <div class="frame f-1">
        <div class="row h-100">
          <div class="col-5 w-100">
            <div class="row">
              <div class="col-12 mb-4">
                <label for="">Code :</label
                ><input type="text" v-model="code" style="width: 150px" />
              </div>
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
            <div class="col-12 h-20">
              <input
                type="text"
                style="width: 350px; margin: auto"
                placeholder="Product Name"
                v-model="name"
              />
            </div>
            <div class="col-12 h-20">
              <label for="">Category&nbsp;:</label
              ><select v-model="category_id" name="category" id="category">
                <option
                  v-for="category in categories"
                  :key="category.id"
                  :value="category.id"
                >
                  {{ category.category }}
                </option>
              </select>
            </div>
            <div class="col-12 h-20">
              <label for=""
                >Status&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;<button
                  class="btn-y"
                  style="width: 100px; display: inilne; height: 50px"
                  :class="{ 'btn-g': remain > minimum }"
                >
                  {{ status_label }}
                </button></label
              >
            </div>
            <div class="col-12 h-20">
              <label for="">Active&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</label>
              <div class="switch"><Switch @switch="switch_active" /></div>
            </div>
            <div class="col-12 h-20">
              <label for="owner"
                >Owner&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</label
              >
              <select name="owner" id="owner" v-model="consignment_id">
                <option value="form_ezzone">EZ Zone</option>
                <option
                  v-for="user in all_user"
                  :key="user.id"
                  :value="user.id"
                >
                  {{ user.nick_name }}
                </option>
              </select>
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
      <div class="frame f-3">
        <div class="row">
          <div class="col-6 label-input">
            <label for="">Price&nbsp;&nbsp;:</label
            ><input type="number" style="width: 69%" v-model="price" />
          </div>
          <div class="col-6 label-input">
            <label for="">Share&nbsp;(%)&nbsp;&nbsp;:</label
            ><input type="number" style="width: 47%" v-model="share" />
          </div>
          <div class="col-6 label-input m-15">
            <label for="flavour">Flavour:</label
            ><select id="flavour" v-model="flavour">
              <option value="2">Sweet</option>
              <option value="1">Spicy</option>
            </select>
          </div>
          <div class="col-6 label-input m-15">
            <label for="stock">Stock:</label
            ><select id="stock" style="width: 220px" v-model="stock">
              <option value="0">No Stock</option>
              <option value="1">Product</option>
              <option value="2" disabled>Material</option>
            </select>
          </div>
          <div class="col-6 label-input m-15">
            <label for="type_topping">Type Topping:</label
            ><select
              id="type_topping"
              style="width: 125px"
              v-model="type_topping"
            >
              <option value="0">not use</option>
              <option value="1">ROTI</option>
              <option value="2">DRINK</option>
              <option value="3">FOOD</option>
            </select>
          </div>
          <div class="col-6 label-input m-15">
            <label for="">Flavour Level&nbsp;&nbsp;:</label
            ><Switch @switch="switch_flavour_level" />
          </div>
        </div>
      </div>
    </div>
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import { api_product } from "../../api/api_product";
import { api_raw_material } from "../../api/api_raw_material";
import { api_user } from "../../api/api_user";
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import SavePopup from "../../components/main_component/SavePopup.vue"


export default {
  components: { NavApp, Switch, SavePopup},
  mounted() {
    this.get_unit();
    this.get_user();
    this.get_category();
  },
  data() {
    return {
      alert: false,
      show_img: null,
      all_user: [],
      categories: [],
      all_unit: [],
      code: "",
      img: null,
      category_id: null,
      status: 1,
      active: true,
      consignment_id: "form_ezzone",
      unit_id: null,
      remain: 0,
      minimum: 0,
      maximum: 0,
      price: 0,
      flavour: 0,
      flavour_level: false,
      price: 0,
      percent: false,
      share: 0,
      show_img: null,
      name: "",
      stock: 0,
      type_topping: 0,
    };
  },
  methods: {
    get_user() {
      api_user.get("read-all/").then((response) => {
        this.all_user = response.data;
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
      this.show_img = e.target.files[0];
      if (this.show_img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.show_img);
      }
    },
    create_product() {
      const data = new FormData();
      data.append("code", this.code);
      if (this.img != null) {
        data.append("img", this.img, this.img.name);
      }
      data.append("category", this.code);
      data.append("unit", this.unit_id);
      if (this.consignment_id != "form_ezzone") {
        data.append("consignment", this.consignment_id);
      }
      data.append("status", this.status);
      data.append("is_active", this.active);
      data.append("remain", this.remain);
      data.append("minimum", this.minimum);
      data.append("maximum", this.maximum);
      data.append("price", this.price);
      data.append("flavour", this.flavour);
      data.append("flavour_level", this.flavour_level);
      data.append("share", this.share);
      data.append("name", this.name);
      data.append("warehouse", this.stock);
      data.append("type_topping", this.type_topping);
      data.append("create_by", 1);

      api_product.post("product/", data).then(() => {
        this.alert = true
        setTimeout(() => {
          this.alert = false
          this.$router.push({ name: "Product" });
        }, 2000)
      });
    },
    switch_flavour_level(val) {
      this.flavour_level = val;
    },
    switch_active(val) {
      this.active = val;
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
  height: 375px;
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
.h-20 {
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
  left: 60px;
  top: 420px;

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