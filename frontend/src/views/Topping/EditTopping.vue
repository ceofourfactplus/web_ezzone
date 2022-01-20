<template>
  <div>
    <nav-app save="true" @save="create_product" :url_name="'Topping'">Edit&#160;Topping</nav-app>
    <div class="container-f w-100">
      <div class="frame f-1">
        <div class="row h-100">
          <div class="col-5 w-100">
            <div class="row">
              <div class="col-12" style="padding: 0px">
                <label id="select_img" for="fileimg" style="margin-top: 0px">
                  <img :src="show_img" class="image" v-if="show_img != null" />
                  <div class="edit-block">Edit</div>
                </label>
                <input
                  type="file"
                  @change="onFileChange"
                  style="display: none"
                  id="fileimg"
                  class="raw-image"
                />
              </div>
            </div>
          </div>
          <div class="col-7 w-100">
            <div class="col-12 h-25">
              <label for="">Code&nbsp;&nbsp;&nbsp;:</label
              ><input
                type="text"
                style="width: 67%"
                v-model="topping['code']"
              />
            </div>
            <div class="col-12 h-25">
              <label for="">Name&nbsp;&nbsp;:</label
              ><input
                type="text"
                style="width: 66%"
                v-model="topping['name']"
              />
            </div>
            <div class="col-12 h-25">
              <label for=""
                >Status&nbsp;&nbsp;:&nbsp;<button
                  class="btn-y"
                  style="white-space:nowrap;width:150px"
                  :class="{ 'btn-g': topping['remain'] > topping['minimum'] }"
                >
                status label
                </button></label
              >
            </div>
            <div class="col-12 h-25">
              <label for="">Active&nbsp;&nbsp;:</label>
              <div class="switch"><Switch @switch="switch_active" /></div>
            </div>
          </div>
        </div>
      </div>
      <div class="frame f-2">
        <div class="row">
          <div class="col-6 label-input">
            <label for="">Qty&nbsp;&nbsp;:</label
            ><input
              type="number"
              style="width: 74%"
              v-model="topping['remain']"
            />
          </div>
          <div class="col-6 label-input">
            <label for="">Min&nbsp;Qty&nbsp;:</label
            ><input
              type="number"
              style="width: 55%"
              v-model="topping['minimum']"
            />
          </div>
          <div class="col-6 label-input m-15">
            <label for="unit">Unit&nbsp;&nbsp;:</label
            ><select
              name="unit"
              id="unit"
              style="width: 225px"
              v-model="topping['unit_id']"
            >
              <option v-for="unit in all_unit" :key="unit.id" :value="unit.id">
                {{ unit.unit }}
              </option>
            </select>
          </div>
          <div class="col-6 label-input m-15">
            <label for="">Max&nbsp;Qty&nbsp;:</label
            ><input
              type="number"
              style="width: 53%"
              v-model="topping['maximum']"
            />
          </div>
        </div>
      </div>
      <div class="frame f-2">
        <div class="row">
          <div class="col-5 label-input">
            <label for="flavour">Price&nbsp;:</label
            ><input type="number" v-model="topping['price']" style="width: 160px" />
          </div>
          <div class="col-7 label-input">
            <label for="stock">Stock :</label
            ><select
              id="type_topping"
              style="width: 260px"
              v-model="topping['warehouse']"
            >
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
              v-model="topping['type_topping']"
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
import { api_product } from "../../api/api_product";
import { api_raw_material } from "../../api/api_raw_material";
import { api_user } from "../../api/api_user";
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import SavePopup from "../../components/main_component/SavePopup.vue"

export default {
  components: { NavApp, Switch, SavePopup },
  mounted() {
    this.get_unit();
    this.get_user();
    this.get_category();
    api_product.get("get-topping/" + this.$route.params.id).then((response) => {
      this.topping = response.data;
      this.topping['price'] = this.topping.pricetopping_set.filter(item=>{
        return item.sale_channel == this.$store.state.ezzone_id
      })[0].price
      this.show_img = response.data.img
    });
  },
  data() {
    return {
      alert: false,
      show_img: null,
      all_user: [],
      categories: [],
      all_unit: [],
      topping: {},
      img:null,
      change_img:false,
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
      this.topping['img'] = e.target.files[0];
      this.change_img = true
      if (this.topping['img']) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.topping['img']);
      }
    },
    create_product() {
      api_product.put("topping/"+this.$route.params.id, this.topping).then((response) => {
        if (this.change_img) {
          const data = new FormData();
          data.append("img", this.topping['img'], this.topping['img'].name);
          api_product.put('get-topping/'+response.data.id,data)
        }
        this.alert = true
        setTimeout(() => {
          this.alert = false
          this.$router.push({ name: "Topping" });
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
  top: 350px;

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
  object-fit: cover;
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