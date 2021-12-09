<template>
  <div class="card m-1" style="width: 200px;" v-if="product.status">
    <img
      :src="product.img"
      class="card-img-top"
      alt=""
      width="200"
      height="150"
    />
    <div class="card-body">
      <h5 class="card-title"># {{product.code}} {{ product.name }}</h5>
      <div v-for="price in product.price" :key="price">
        <p v-if="price.sale_channel_id == sale_channel_id" id="price" class="card-text"><span>ราคา</span> <span>{{price.price}} บาท</span></p>
      </div>
      
      <div class="btn-group" style="width: 100%">
        <button :class="{'disabled':sale_channel_id == undefined||table == ''}"
          class="btn btn-warning"
          @click="$emit('add_to_cart', product)"
        >
          add
        </button>
        <button :class="{'disabled':sale_channel_id == undefined}"
          class="btn btn-success"
          type="button"
          data-bs-toggle="modal"
          data-bs-target="#selectOptions"
          @click="$emit('select_product',product)"
        >
          topping
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["product", "sale_channel_id"],
  methods: {
    price() {
      for (const item of this.products.all_price) {
        if (item.sale_channel_id == this.sale_channel_id) {
          return item.price;
        }
      }
    },
  },
};
</script>

<style scoped>

</style>