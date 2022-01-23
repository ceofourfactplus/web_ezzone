<template>
  <div>
    <nav-app save="true" @save="create_product" :url_name="'Product'"
      >Edit&#160;Product</nav-app
    >
    <div class="container-f w-100">
      <div class="frame f-1">
        <div class="row h-100">
          <div class="col-5 w-100">
            <div class="row">
              <div class="col-12 mb-4">
                <label for="">Code :</label
                ><input
                  type="text"
                  v-model="product.code"
                  style="width: 150px"
                />
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
                v-model="product.name"
              />
            </div>
            <div class="col-12 h-20">
              <label for="">Category&nbsp;:</label
              ><select
                v-model="product.category_id"
                style="width: 210px"
                name="category"
                id="category"
              >
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
              <label for="">Type Product&nbsp;:&nbsp;</label>
              <select
                id="type_topping"
                style="width: 160px; margin-left: 0px"
                v-model="product['type_product']"
              >
                <option value="1">DRESSERT</option>
                <option value="2">DRINK</option>
                <option value="3">FOOD</option>
              </select>
            </div>
            <div class="col-12 h-20">
              <label for="">Active&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</label>
              <div class="switch"><Switch @switch="product.is_active = !product.is_active" :value="product.is_active" /></div>
            </div>
            <div class="col-12 h-20">
              <label for="">Price&nbsp;&nbsp;:</label
              ><input
                type="number"
                style="width: 69%"
                v-model="product.price"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="frame f-2">
        <div class="row">
          <div class="col-6 label-input">
            <label for="">Qty&nbsp;&nbsp;:</label
            ><input type="number" style="width: 74%" v-model="product.remain" />
          </div>
          <div class="col-6 label-input">
            <label for="">Min&nbsp;Qty&nbsp;:</label
            ><input
              type="number"
              style="width: 55%"
              v-model="product.minimum"
            />
          </div>
          <div class="col-6 label-input m-15">
            <label for="unit">Unit&nbsp;&nbsp;:</label
            ><select
              name="unit"
              id="unit"
              style="width: 225px"
              v-model="product.unit_id"
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
              v-model="product.maximum"
            />
          </div>
        </div>
      </div>
      <div class="frame f-2">
        <div class="row">
          <div class="col-6 label-input">
            <label for="flavour">Flavour:</label
            ><select id="flavour" v-model="product.flavour">
              <option value="2">Sweet</option>
              <option value="1">Spicy</option>
            </select>
          </div>
          <div class="col-6 label-input">
            <label for="stock">Stock:</label
            ><select
              id="stock"
              style="width: 210px"
              v-model="product.warehouse"
            >
              <option value="0">No Stock</option>
              <option value="1">Product</option>
              <option value="2" disabled>Material</option>
            </select>
          </div>
          <div class="col-5 label-input m-15">
            <label for="">Flavour Level&nbsp;&nbsp;:</label
            ><Switch @switch="product.flavour_level = !product.flavour_level" :value="product.flavour_level" />
          </div>
          <div class="col-7 label-input m-15">
            <label for="type_topping">Type Topping:</label
            ><select
              id="type_topping"
              style="width: 165px"
              v-model="product.topping_category_id"
            >
              <option
                v-for="topcate in topping_categories"
                :key="topcate.id"
                :value="topcate.id"
              >
                {{ topcate.category }}
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
    this.get_product();
    this.get_topping_categories();
  },
  data() {
    return {
      alert: false,
      show_img: null,
      all_user: [],
      categories: [],
      all_unit: [],
      product: {},
      topping_categories: [],
      change_img: false,
    };
  },
  methods: {
    get_topping_categories() {
      api_product.get("topping/category/").then((response) => {
        this.topping_categories = response.data;
      });
    },
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
    get_product() {
      api_product
        .get("product/" + this.$route.params.id + "/")
        .then((response) => {
          this.product = response.data;
          this.show_img = response.data.img;
          this.product["price"] = this.product.priceproduct_set.filter(
            (item) => {
              return item.sale_channel == this.$store.state.ezzone_id;
            }
          )[0].price;
        });
    },
    onFileChange(e) {
      this.product["img"] = e.target.files[0];
      this.change_img = true;
      if (this.product["img"]) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.product["img"]);
      }
    },
    create_product() {
      api_product
        .put("update-product/" + this.$route.params.id + "/", this.product)
        .then(() => {
          this.alert = true
          setTimeout(() => {
            this.alert = false
            this.$router.push({ name: "Product" });
          }, 2000)
        });
      if (this.change_img) {
        const data = new FormData();
        data.append("img", this.product["img"], this.product["img"].name);
        api_product.put(
          "update-img-product/" + this.$route.params.id + "/",
          data
        );
      }
    },
    switch_flavour_level(val) {
      this.product.flavour_level = val;
    },
    switch_active(val) {
      this.product.active = val;
    },
  },
  watch: {
    "product.maximum": function (newData) {
      if (newData <= this.product.minimum) {
        this.product.maximum = this.product.minimum + 1;
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
  height: 375px;
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
  left: 100px;
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