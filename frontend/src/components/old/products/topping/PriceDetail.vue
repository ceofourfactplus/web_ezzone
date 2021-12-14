<template>
  <div
    class="offcanvas offcanvas-end"
    tabindex="-1"
    id="price-detail"
    aria-labelledby="offcanvasRightLabel"
  >
    <div class="offcanvas-header">
      <h5 id="offcanvasRightLabel">Price Topping Detail</h5>
      <button
        type="button"
        class="btn-close text-reset"
        data-bs-dismiss="offcanvas"
        aria-label="Close"
      ></button>
    </div>
    <hr>
    <div class="offcanvas-body">
      <div class="row">
        <div class="col-12 fw-bold fs-3" v-for="price in all_price" :key="price">
          <span class="text-dark">{{ price.sale_channel.sale_channel.toUpperCase() }}</span> : {{price.price}}.-
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  props:['all_price'],
  methods:{
    getSaleChannel(id){
      axios.get('http://127.0.0.1:8000/product/sale-channel/'+id+'/').then((response)=>{
        console.log(response.data.sale_channel)
        return response.data.sale_channel
      })
    }
  }
};
</script>

<style>
</style>