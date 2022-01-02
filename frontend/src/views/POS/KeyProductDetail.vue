<template>
  <div>
    <nav-app>{{ product.name }}</nav-app>
    <div class="frame">
      <div class="row mt-2 w-100" style="margin-left: 0px">
        <div class="col-4 w-100" style="margin: auto">
          <div class="container-img">
            <img
              v-if="product.img != null"
              class="img"
              :src="product.img"
              alt=""
            />
            <div v-else class="img" style="background-color: #c4c4c4"></div>
            <div class="code">
              {{ product.code }}
            </div>
          </div>
          <div class="price">
            29<sup>฿</sup>
            <!-- {{select_price(product.priceproduct_set)}}<sup>฿</sup> -->
          </div>
        </div>
        <div class="col-8 w-100" style="margin: auto; height: 90%">
          <div class="w-100" style="margin: auto; display: flex">
            <div class="total-price me-2">1990</div>
            <div class="baht me-4">฿</div>
            <button class="btn-ghost-g" style="display: inline">
              <img
                src="../../assets/icon/cart.png"
                style="width: 50px; height: 50px"
                alt=""
              />
            </button>
          </div>
          <div
            class="w-100"
            style="margin: auto; display: flex; overflow-y: scroll"
          >
            <button
              v-for="i in 10"
              :key="i"
              class="btn me-3"
              style="min-width: 70px; height: 70px"
            >
              {{ i }}
            </button>
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
  mounted() {
    api_product
      .get("product/" + this.$route.params.product_id)
      .then((response) => {
        this.product = response.data;
        console.log(response.data);
      });
  },
  data() {
    return {
      product: {},
    };
  },
};
</script>

<style scoped>
.frame {
  width: 672px;
  height: 805px;
  margin: auto;
  padding: 0px !important;
}
.img {
  height: 200px;
  width: 200px;
}
.code {
  position: absolute;
  bottom: 7px;
  right: 10px;
  color: #fff;
  font-size: 48px;
  font-weight: bold;
  text-shadow: rgb(0, 0, 0) 3px 0px 0px, rgb(0, 0, 0) 2.83487px 0.981584px 0px,
    rgb(0, 0, 0) 2.35766px 1.85511px 0px, rgb(0, 0, 0) 1.62091px 2.52441px 0px,
    rgb(0, 0, 0) 0.705713px 2.91581px 0px,
    rgb(0, 0, 0) -0.287171px 2.98622px 0px,
    rgb(0, 0, 0) -1.24844px 2.72789px 0px, rgb(0, 0, 0) -2.07227px 2.16926px 0px,
    rgb(0, 0, 0) -2.66798px 1.37182px 0px, rgb(0, 0, 0) -2.96998px 0.42336px 0px,
    rgb(0, 0, 0) -2.94502px -0.571704px 0px,
    rgb(0, 0, 0) -2.59586px -1.50383px 0px,
    rgb(0, 0, 0) -1.96093px -2.27041px 0px,
    rgb(0, 0, 0) -1.11013px -2.78704px 0px,
    rgb(0, 0, 0) -0.137119px -2.99686px 0px,
    rgb(0, 0, 0) 0.850987px -2.87677px 0px,
    rgb(0, 0, 0) 1.74541px -2.43999px 0px, rgb(0, 0, 0) 2.44769px -1.73459px 0px,
    rgb(0, 0, 0) 2.88051px -0.838247px 0px;
}
.container-img {
  position: relative;
}
.price {
  font-weight: bold;
  font-size: 72px;
  color: #889898;
}
sup {
  font-size: 36px;
  font-weight: 600;
  top: -2rem;
}
.total-price {
  color: #fff;
  background: #bd523f;
  border-radius: 15px;
  display: inline;
  font-weight: 500;
  font-size: 64px;
  line-height: 80px;
  width: 191px;
  height: 80px;
}
.baht {
  top: -50px;
  font-size: 40px;
  font-weight: 600;
  display: inline;
  color: #889898;
  margin-right: 35px;
}
.btn-ghost-g {
  width: 167px;
  height: 81px;
}
</style>