<template>
  <div class="container">
    <!-- if have stock-data -->
    <div v-if="stock.stock_data.length != 0" class="row mt-2">
      <div class="col-3" v-for="data in stock.stock_data" :key="data.id">
        <card-stock :item="data" />
      </div>
    </div>
    <!-- if don`t have stock-data -->
    <div v-else class="position-absolute top-50 start-50 translate-middle">
      <h1 class="text-center text-light">don`t have stock</h1>
    </div>
  </div>
</template>

<script>
import {mapState} from "vuex"
import CardStock from "../../components/CardStock.vue";
export default {
  name: "AllStock",
  components: {
    CardStock,
  },
  computed: mapState(["stock"])
};
</script>

<style>
</style>