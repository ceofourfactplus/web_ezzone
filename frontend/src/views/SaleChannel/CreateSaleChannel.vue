<template>
  <div>
    <nav-app :save="true" @save="create_sale_channel">New Sale Channel</nav-app>
    <div class="row" style="margin-top: 20px">
      <div class="col-4 w-100" style="margin: auto">
        <label id="select_img" for="file" style="margin-top: 0px">
          <img
            :src="show_img"
            style="width: 150px; height: 132px"
            class="image"
            v-if="show_img != null"
          />
          <img
            v-else
            src="../../assets/icon/View.png"
            style="width: 150px"
            alt=""
          />
        </label>
        <input
          type="file"
          @change="onFileChange"
          style="display: none"
          id="file"
          class="raw-image"
        />
      </div>
      <div class="col-8 w-100">
        <div style="display: flex" class="mb-2">
          <label class="col-3" for="name">Name </label>
          <input
            v-model="sale_channel_set.sale_channel"
            class="input"
            type="text"
            id="name"
          />
        </div>
        <div style="display: flex">
          <label class="col-3" for="gp">GP% </label>
          <input
            style="width: 120px"
            class="input"
            v-model="sale_channel_set.gp"
            type="number"
            id="gp"
          />
          <div class="status ms-1">
            Status :
            <div class="switch"><Switch @switch="status_switch" /></div>
          </div>
        </div>
      </div>
      <div class="col-12" style="padding: 0px">
        <hr />
        <div class="col-12" style="margin-top: 10px">
          <div style="display: flex">
            <div class="col-3 product" style="text-align: left">Product</div>
            <div class="col-9">
              <button
                class="btn-ghost-b me-3"
                style="width: 202px; height: 50px"
                @click="$router.push({ name: 'CreateCustomer' })"
              >
                +&#160;New Product</button
              ><button
                class="btn-ghost-r"
                style="width: 235px; height: 50px"
                @click="$router.push({ name: 'CreateCustomer' })"
              >
                <img
                  src="../../assets/icon/bin.png"
                  width="20"
                  alt=""
                />&#160;Delete Product
              </button>
            </div>
          </div>
        </div>
        <div class="col-12" style="margin-top: 8px">
          <search-bar />
        </div>
      </div>

      <!-- select product -->
      <div class="col-12 mt-2" style="text-align: left; padding: 0px">
        <button
          :class="{ 'btn-gray-active': type_item == 3 }"
          @click="type_item = 3"
          class="btn-gray me-2"
        >
          FOOD
        </button>
        <button
          :class="{ 'btn-gray-active': type_item == 2 }"
          @click="type_item = 2"
          class="btn-gray me-2"
        >
          DRINK
        </button>
        <button
          :class="{ 'btn-gray-active': type_item == 1 }"
          @click="type_item = 1"
          class="btn-gray me-2"
        >
          DRESSERT
        </button>
        <button
          :class="{ 'btn-gray-active': type_item == 4 }"
          @click="type_item = 4"
          class="btn-gray me-2"
        >
          TOPPING
        </button>
        <button
          :class="{ 'btn-gray-active': type_item == 5 }"
          @click="type_item = 5"
          class="btn-gray"
        >
          CONSIGNMENT
        </button>
      </div>
    </div>
    <div class="table" style="margin-top: 10px">
      <div class="table-header" style="line-height: 40px; font-size: 24px">
        <div class="row">
          <div
            class="col-5 w-100"
            style="margin-left: 10px; text-align: left; line-height: 100%"
          >
            Product Name
          </div>
          <div
            class="col-3 w-100"
            style="margin-left: 10px; text-align: left; line-height: 100%"
          >
            Sale Price
          </div>
          <div
            class="col-4 w-100"
            style="margin: auto; margin-left: -10px; line-height: 100%"
          >
            Net Price
          </div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 430px">
        <div class="table-item" v-for="item in items" :key="item.id">
          <div class="row" style="width: 100%">
            <div class="col-4 w-100" style="margin: auto; line-height: 100%">
              {{ item.name }}
            </div>
            <div
              class="col-4 w-100"
              style="margin: auto; text-align: left; line-height: 100%"
            ></div>
            <div
              class="col-4 w-100"
              style="
                margin: auto;
                width: 175px;
                text-align: left;
                line-height: 100%;
              "
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_product } from "../../api/api_product";
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
export default {
  components: { NavApp, Switch, SearchBar },
  data() {
    return {
      show_img: null,
      img: null,
      sale_channel_set: {
        sale_channel: "hello",
        gp: 0,
        create_by: 1,
        price_product: [
          {
            product: 1,
            price: 19,
          },
        ],
        price_topping: [
          {
            topping: 1,
            price: 19,
          },
        ],
      },
      type_item: 1,
      items: [],
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
    create_sale_channel() {
      api_product.post("sale-channel/create/", this.sale_channel_set);
      // const data = new FormData();
      // data.append("img", this.sale_channel_set.img,this.img.name)
    },
    status_switch(val) {
      this.sale_channel_set.status = val;
    },
    get_price(list_price) {
      list_price.forEach((item) => {
        if (item.sale_channel == this.$store.state.ezzone_id) {
          console.log(item.price);
          return item.price;
        }
      });
    },
  },
  watch: {
    type_item(new_type) {
      if (new_type == 1) {
        this.items = this.sale_channel_set;
        this.items.filter((item) => {
          item;
        });
        dress;
      }
    },
  },
};
</script>

<style scoped>
.row {
  width: 90%;
  margin: auto;
}
.input {
  width: 300px;
  margin: auto;
  background-color: #717171;
}
label {
  color: #ea7c69;
  font-weight: 800;
  display: inline-block;
  text-align: left;
}
input {
  display: inline-block;
}
.status {
  color: #ea7c68;
  text-align: left;
  font-size: 30px;
  font-weight: 800;
}
hr {
  background-color: #717171;
  height: 3px;
  opacity: 1;
}
.product {
  font-size: 36px;
  color: #fff;
  font-weight: 800;
}
button {
  font-weight: 500;
}

.switch {
  display: inline-block;
  top: 10px;
}

.btn-gray {
  font-weight: 700;
}
</style>
