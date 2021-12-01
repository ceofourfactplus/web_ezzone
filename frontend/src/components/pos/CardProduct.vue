<template>
  <div class="card m-1" style="width: 245px;" v-if="product.status">
    <img
      :src="product.img"
      class="card-img-top"
      alt=""
      width="245"
      height="150"
    />
    <div class="card-body">
      <h5 class="card-title">{{ product.name }}</h5>
      <p id="price" class="card-text"><span>ราคา</span> <span>19 บาท</span></p>
      <div class="btn-group" style="width: 100%">
        <button
          class="btn btn-warning"
          @click="$emit('add_to_cart', product)"
        >
          add
        </button>
        <button
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