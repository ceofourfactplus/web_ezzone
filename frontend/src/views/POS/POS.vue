<template>
  <div class="container" id="sd">
    <NavbarPOS />
    <div class="row" style="height: 20vw">
      <div class="col-7">
        <div class="row">
          <div class="col-4"><card-product /></div>
          <div class="col-4"><card-product /></div>
          <div class="col-4"><card-product /></div>
          <div class="col-4"><card-product /></div>
          <div class="col-4"><card-product /></div>
          <div class="col-4"><card-product /></div>
          <div class="col-4"><card-product /></div>
          <div class="col-4"><card-product /></div>
          <div class="col-4"><card-product /></div>
          <div class="col-4"><card-product /></div>
          <div class="col-4"><card-product /></div>
          <div class="col-4"><card-product /></div>
        </div>
      </div>
      <div class="col-5">
        <bill/>
      </div>
    </div>
  </div>
</template>

<script>
import Bill from '../../components/Bill.vue';
import CardProduct from "../../components/CardProduct.vue";
import NavbarPOS from "../../components/NavPOS.vue";

export default {
  components: { NavbarPOS, CardProduct, Bill },
  name: "POS",
};
</script>

<style scoped>
#price {
  white-space: nowrap;
}
</style>
