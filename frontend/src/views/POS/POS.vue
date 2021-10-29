<template>
  <div class="container" id="sd">
    <NavbarPOS />
    <div class="row" style="background-color: rgb(253, 255, 151); height: 20vw">
      <div class="col-7" style="background-color: rgb(32, 2, 221)">
        <div class="card m-2" style="width: 17vw">
          <img src="" class="card-img-top" alt="" />
          <div class="card-body">
            <h5 class="card-title">ชานมไข่มุก</h5>
            <p id="price" class="card-text">
              <span>ราคา</span> <span>19.00บาท</span>
            </p>
            <div class="btn-group" style="width: 100%;">
              <button class="btn btn-warning">add</button>
              <button class="btn btn-success">topping</button>
            </div>
          </div>
        </div>
        <card-product/>
      </div>
      <div class="col-5" style="background-color: rgb(253, 25, 11)"></div>
    </div>
  </div>
</template>

<script>
import CardProduct from '../../components/CardProduct.vue';
import NavbarPOS from "../../components/NavPOS.vue";

export default {
  components: { NavbarPOS, CardProduct },
  name: "POS",
};
</script>

<style scoped>
#price{
  white-space: nowrap;
}
</style>
