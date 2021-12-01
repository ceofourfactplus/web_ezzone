<template>
  <div class="btn-group" role="group">
    <button
      v-if="table != ''"
      type="button"
      class="btn btn-success"
      style="border-radius: 50px 0px 0px 50px"
      data-bs-toggle="modal"
      data-bs-target="#selectTable"
      @click="select = 1"
    >
      <img src="../../assets/eat-here.png" />
      <h5 class="mt-1">Eat Here</h5>
    </button>
    <button
      v-else
      type="button"
      class="btn"
      :class="{ 'btn-warning': select != 1, 'btn-danger': select == 1 }"
      style="border-radius: 50px 0px 0px 50px"
      data-bs-toggle="modal"
      data-bs-target="#selectTable"
      @click="select = 1"
    >
      <img src="../../assets/eat-here.png" />
      <h5 class="mt-1">Eat Here</h5>
    </button>

    <button
      type="button"
      class="btn btn-warning"
      @click="select = 2"
      data-bs-toggle="modal"
      data-bs-target="#selectSaleChannel"
      :class="{
        'btn-success': delivery != {} && select == 2,
        'btn-danger': select == 2,
      }"
    >
      <img src="../../assets/delivery.png" alt="" />
      <h5 class="mt-1">Delivery</h5>
    </button>
    <button
      type="button"
      class="btn btn-warning"
      :class="{ 'btn-danger': select == 3, 'btn-success': customer != {} }"
      @click="select = 3"
      style="border-radius: 0px 50px 50px 0px"
    >
      <img src="../../assets/customer.png" alt="" />
      <h5 class="mt-1">Customer</h5>
    </button>
  </div>
</template>

<script>
export default {
  props: ["customer", "table", "delivery"],
  data() {
    return {
      select: 0,
    };
  },
  watch: {},
};
</script>

<style scoped>
img {
  width: 50px;
  height: 50px;
}
</style>