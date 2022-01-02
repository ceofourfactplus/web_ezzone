<template>
  <div>
    <nav-app>Drink</nav-app>
    <div class="frame-pos">
      <!-- select type product -->
      <div class="row w-100">
        <div class="col-2 w-100">
          <button v-if="select_type_product == 1" class="btn-gray active">
            <img src="../../assets/icon/drink-active.png" />
          </button>
          <button v-else @click="select_type_product = 1" class="btn-gray">
            <img src="../../assets/icon/drink-gray.png" />
          </button>
        </div>
        <div class="col-2 w-100">
          <button v-if="select_type_product == 2" class="btn-gray active">
            <img src="../../assets/icon/fork-active.png" />
          </button>
          <button v-else class="btn-gray" @click="select_type_product = 2">
            <img src="../../assets/icon/fork.png" />
          </button>
        </div>
        <div class="col-2 w-100">
          <button v-if="select_type_product == 3" class="btn-gray active">
            <img src="../../assets/icon/dressert-active.png" />
          </button>
          <button v-else class="btn-gray" @click="select_type_product = 3">
            <img src="../../assets/icon/dressert.png" />
          </button>
        </div>
        <div class="col-2 w-100">
          <button v-if="select_type_product == 4" class="btn-gray active">
            <img src="../../assets/icon/promotion-gray-active.png" />
          </button>
          <button class="btn-gray" @click="select_type_product = 4" v-else>
            <img src="../../assets/icon/promotion-gray.png" />
          </button>
        </div>
        <div class="col-2 w-100">
          <button v-if="select_type_product == 5" class="btn-gray active">
            <img src="../../assets/icon/consignment-active.png" />
          </button>
          <button v-else class="btn-gray" @click="select_type_product = 5">
            <img src="../../assets/icon/consignment.png" />
          </button>
        </div>
        <div class="col-2 w-100">
          <button class="btn-gray active" v-if="select_type_product == 6">
            <img src="../../assets/icon/topping-active.png" />
          </button>
          <button v-else class="btn-gray" @click="select_type_product = 6">
            <img src="../../assets/icon/topping.png" />
          </button>
        </div>
      </div>

      <!-- select category -->
      <div
        style="
          display: flex;
          height: 50px;
          overflow-x: auto;
          margin: auto;
          width: 99.5%;
        "
        class="mt-2"
      >
        <button
          v-for="category in categories"
          :key="category.id"
          class="btn-gray category me-1"
          style="min-width: 165px; white-space: nowrap"
          :class="{
            active: select_category == category.id,
            'text-active': select_category == category.id,
          }"
          @click="select_category = category.id"
        >
          {{ category.category }}
        </button>
      </div>

      <!-- select product -->
      <div class="frame-1">
        <div class="row w-100" style="margin:0px">
          <div
            v-for="product in products"
            :key="product.id"
            @click="$router.push({name:'KeyProductDetail',params:{product_id:product.id,sale_channel_id:$route.params.sale_channel_id}})"
            class="col-3 w-100 card-product"
          >
            <img v-if="product.img != null" class="img" :src="product.img" alt="" />
            <div v-else class="img" style="background-color:#c4c4c4" ></div>
            <p>{{ product.name }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_product } from "../../api/api_product";
import NavApp from "../../components/main_component/NavApp.vue";
export default {
  components: { NavApp },
  data() {
    return {
      header: "",
      select_type_product: 0,
      select_category: 0,
      select_product:{},
      categories: [],
      products: [],
    };
  },
  mounted() {
    api_product.get("category/").then((response) => {
      this.categories = response.data;
    });
  },
  watch: {
    select_type_product(newType) {
      if (newType == 6) {
        // api_product.get()
        this.products = [];
      } else if (newType == 5) {
        this.products = [];
      } else if (newType == 4) {
        this.products = [];
      } else {
        api_product.get("category-by-type/" + newType).then((response) => {
          this.categories = response.data;
        });
      }
    },
    select_category(newCategory) {
      if (this.select_type_product == 6) {
        // api_product.get()
        this.products = [];
      } else if (this.select_type_product == 5) {
        this.products = [];
      } else if (this.select_type_product == 4) {
        this.products = [];
      } else {
        api_product.get("product/category/" + newCategory).then((response) => {
          this.products = response.data;
        });
      }
    },
  },
  methods: {},
};
</script>

<style scpoed>
.frame-pos {
  width: 90%;
  margin: auto;
}
p{
  color:#abbbc2;
  font-size: 19px;
}

.frame-1 {
  width: 100%;
  height: 753px;
  background-color: #303344;
}

button {
  width: 105px;
  height: 70px;
  border-radius: 10px !important;
}
.btn-gray {
  opacity: 0.5;
  display: inline;
}
img {
  height: 40px;
}
.img {
  height: 150px;
  width: 150px;
  border-radius: 10px;
  margin-top: 15px;
}
.active {
  opacity: 1;
}
.text-active {
  color: #ea7c69 !important;
}
.card-product {
  margin: auto;
  white-space: nowrap;
}
.category {
  border-radius: 10px 10px 0px 0px !important;
  height: 50px !important;
  font-size: 36px !important;
  font-weight: 400 !important;
}
</style>