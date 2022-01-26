<template>
  <div>
    <nav-app
      :url_name="'SelectSaleChannel'"
      :cart="true"
      :amount="$store.state.pos.order.orderitem_set.length"
      >{{ header }}</nav-app
    >
    <div class="frame-pos">
      <!-- select type product -->
      <div class="row w-100">
        <div class="col-2 w-100">
          <button v-if="select_type_product == 2" class="btn-gray active">
            <img src="../../assets/icon/drink-active.png" />
          </button>
          <button v-else @click="select_type_product = 2" class="btn-gray">
            <img src="../../assets/icon/drink-gray.png" />
          </button>
        </div>
        <div class="col-2 w-100">
          <button v-if="select_type_product == 3" class="btn-gray active">
            <img src="../../assets/icon/fork-active.png" />
          </button>
          <button v-else class="btn-gray" @click="select_type_product = 3">
            <img src="../../assets/icon/fork.png" />
          </button>
        </div>
        <div class="col-2 w-100">
          <button v-if="select_type_product == 1" class="btn-gray active">
            <img src="../../assets/icon/dressert-active.png" />
          </button>
          <button v-else class="btn-gray" @click="select_type_product = 1">
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
          overflow-y: hidden;
        "
        class="mt-2"
      >
        <button
          v-for="category in categories"
          :key="category.id"
          class="btn-gray category me-1"
          style="min-width: fit-content; white-space: nowrap; padding: 0px 5px;"
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
      <div class="frame-1" style="overflow-y: auto;">
        <div class="row w-100" style="margin: 0px">
          <div
            v-for="product in products"
            :key="product.id"
            class="w-100 card-product"
            :class="{
              'col-3': product.type_product != 3,
              'col-6': product.type_product == 3,
            }"
          >
            <img
              v-if="'promotion' in product"
              :src="product.img"
              alt=""
              class="img-s"
              @click="
                $router.push({
                  name: 'KeyPromotionDetail',
                  params: {
                    package_id: product.id,
                  },
                })
              "
            />
            <img
              v-else-if="!('type_topping' in product)"
              :class="{
                'img-s': product.type_product != 3,
                'img-l': product.type_product == 3,
              }"
              :src="product.img"
              alt=""
              @click="
                $router.push({
                  name: 'KeyProductDetail',
                  params: {
                    product_id: product.id,
                  },
                })
              "
            />
            <img
              v-else-if="is_topping(product)"
              class="img-s"
              :src="product.img"
              alt=""
              @click="
                $router.push({
                  name: 'KeyToppingDetail',
                  params: {
                    topping_id: product.id,
                  },
                })
              "
            />
            <div
              v-else
              @click="
                $router.push({
                  name: 'KeyProductDetail',
                  params: {
                    product_id: product.id,
                  },
                })
              "
              :class="{
                'img-s': product.type_product != 3,
                'img-l': product.type_product == 3,
              }"
              style="background-color: #c4c4c4"
            ></div>
            <p v-if="('promotion' in product)">{{ product.promotion }}</p>
            <p v-else>{{ product.name }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_product } from "../../api/api_product";
import { api_promotion } from "../../api/api_promotion";
import NavApp from "../../components/main_component/NavApp.vue";
export default {
  components: { NavApp },
  data() {
    return {
      header: "",
      select_type_product: 0,
      select_category: 0,
      select_product: {},
      categories: [],
      products: [],
    };
  },
  mounted() {
    this.select_type_product = this.$store.state.pos.type_product;
  },
  watch: {
    select_type_product(newType) {
      this.$store.state.pos.type_product = newType;
      if (newType == 6) {
        this.header = "Topping";
        this.categories = [
          {
            id: 1,
            category: "Dressert",
          },
          {
            id: 2,
            category: "Drink",
          },
          {
            id: 3,
            category: "Food",
          },
        ];
        this.select_category = 1
      } else if (newType == 5) {
        this.categories = []
        this.header = "Consignment";
        this.products = [];
      } else if (newType == 4) {
        this.header = "Promotion";
        this.categories = [
          {
            id: 1,
            category: "Package",
          },]
        this.select_category = 10
      } else {
        api_product.get("category-by-type/" + newType).then((response) => {
          this.categories = response.data;
          this.select_category = response.data[0].id;
        });
      }
      if (newType == 1) {
        this.header = "Dessert";
      }
      if (newType == 2) {
        this.header = "Drink";
      }
      if (newType == 3) {
        this.header = "Food";
      }
    },
    select_category(newCategory) {
      this.$store.state.pos.category = newCategory
      if (this.select_type_product == 6) {
        api_product
          .get(
            "get-topping-by-sale-channel/" +
              this.$store.state.pos.order.sale_channel_id +
              "/" +
              newCategory
          )
          .then((response) => {
            this.products = response.data;
          });
      } else if (this.select_type_product == 5) {
        this.products = [];
      } else if (this.select_type_product == 4) {
        api_promotion.get('package-by-sale-channel/'+this.$store.state.pos.order.sale_channel_id).then((response) => {
          this.products = response.data;
        })
      } else {
        api_product
          .get(
            "get-product-by-sale-channel/" +
              this.$store.state.pos.order.sale_channel_id +
              "/" +
              newCategory
          )
          .then((response) => {
            this.products = response.data;
          });
      }
    },

  },
  methods: {
    is_topping(product){
      console.log('type_topping' in product)
      if ('type_topping' in product){
        return true
      }return false
    }
  },
};
</script>

<style scoped>
.frame-pos {
  width: 90%;
  margin: auto;
}
p {
  color: #abbbc2;
  font-size: 19px;
  margin-bottom: 0px;
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
.img-s {
  height: 150px;
  width: 150px;
  border-radius: 10px;
  margin-top: 10px;
  object-fit: cover;
}
.img-l {
  height: 150px;
  width: 300px;
  border-radius: 10px;
  margin-top: 10px;
  object-fit: cover;
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
img {
  height: 48px;
}
</style>