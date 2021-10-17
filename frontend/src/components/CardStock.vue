<template>
  <div class="card m-2" style="width: 16rem">
    <div class="card-header">
      <div class="row">
        <div class="col fw-bold fs-4">#{{ item.code }}</div>
      </div>
    </div>

    <div class="card-body text-center">
      <div class="row">
        <div class="col fw-bold fs-4">name :</div>
        <div class="col fw-bold fs-4">{{ item.name }}</div>
      </div>
      <hr />
      <div class="row fw-bold">
        <div class="col">remain</div>
        <div class="col">{{ item.balance }} {{ item.unit_set.unit }}</div>
      </div>
      <div class="row fw-bold">
        <div class="col">avg price</div>
        <div class="col">{{ item.avg_price }}</div>
      </div>
    </div>
    <div class="card-footer bg-transparent btn-group btn-block">
      <button
        type="button"
        class="btn btn-warning fw-bold"
        data-bs-toggle="modal"
        data-bs-target="#pick-up"
        @click="$store.state.stock_select = item"
      >
        pick up</button
      ><button
        type="button"
        class="btn btn-danger fw-bold"
        data-bs-toggle="offcanvas"
        @click="$store.state.stock_select = item"
        data-bs-target="#off-detail-stock"
      >
        detail
      </button>
    </div>
    <OFFDetailStock/>
  </div>
</template>

<script>
import OFFDetailStock from './OFFDetailStock.vue';
export default {
  components: { OFFDetailStock },
  props: ["item"],
};
</script>
