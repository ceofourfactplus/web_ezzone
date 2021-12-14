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
    <hr />
    <div class="offcanvas-body">
      <div class="row">
        <div class="col text-start">
          <div class="card mb-3" style="width: 100%">
            <div class="card-header fw-bold">Basic Details</div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <span>CODE : </span>
                <span> #{{ $store.state.stock_select.code }}</span>
              </li>
              <li class="list-group-item">
                <span>NAME : </span>
                <span> {{ $store.state.stock_select.name }}</span>
              </li>
              <li class="list-group-item">
                <span>REMAIN : </span>
                <span> {{ $store.state.stock_select.balance }}</span>
              </li>
              <li class="list-group-item">
                <span>MIN_STOCK : </span>
                <span> {{ $store.state.stock_select.minstock }}</span>
              </li>
              <li class="list-group-item">
                <span>CATEGORY : </span>
                <span> {{ $store.state.stock_select.category_set.name }}</span>
              </li>
            </ul>
          </div>
          <div class="card" style="width: 100%">
            <div class="card-header fw-bold">Manager Details</div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <span>AVG_PRICE : </span>
                <span> {{ $store.state.stock_select.avg_price }}</span>
              </li>
              <li class="list-group-item">
                <span>MIN_PRICE : </span>
                <span> {{ $store.state.stock_select.min_price }}</span>
              </li>
              <li class="list-group-item">
                <span>MAX_PRICE : </span>
                <span> {{ $store.state.stock_select.max_price }}</span>
              </li>
              <li class="list-group-item">
                CHART COMING SOON
                <Chart :data_labels="data_labels" />
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import Chart from './ChartOfPickUp.vue';
export default {
  name: "OffCanvasDetailOfPickUp",
  components: { Chart },
  computed: {
    ...mapState(["stock"]),
  },
  props:['data_labels'],
  methos:{
    chart_data() {
      var chart_data = [];
      for(var item in this.stock.stock_select.frequency_data) {
        chart_data.push(item.date)
      }
      console.log('this is chart-data : '+chart_data)
    }
  }
};
</script>

<style>
</style>