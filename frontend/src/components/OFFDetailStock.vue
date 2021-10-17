<template>
  <div
    class="offcanvas offcanvas-end"
    tabindex="-1"
    id="off-detail-stock"
    aria-labelledby="offcanvasRightLabel"
  >
    <div class="offcanvas-header">
      <h5 id="offcanvasRightLabel">
        details of {{ $store.state.stock_select.name }}
      </h5>
      <button
        type="button"
        class="btn-close text-reset"
        data-bs-dismiss="offcanvas"
        aria-label="Close"
      ></button>
    </div>
    <div class="offcanvas-body">
      <div class="row">
        <div class="col">
          <h5>code:{{ $store.state.stock_select.code }}</h5>
          <h5>name:{{ $store.state.stock_select.name }}</h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState(["stock_select"]),
  },
};
</script>

<style>
</style>