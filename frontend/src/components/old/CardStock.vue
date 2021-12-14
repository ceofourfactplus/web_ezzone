<template>
  <div class="card m-2" style="width: 20vw">
    <div class="card-header">
      <div class="row">
        <div class="col fw-bold fs-4">#{{ item.code }}</div>
      </div>
    </div>

    <div class="card-body text-center">
      <div class="row">
        <div class="col col-md-6 fw-bold fs-4">name :</div>
        <div class="col col-md-6 fw-bold fs-4">{{ item.name }}</div>
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
        @click="stock_select = item"
      >
        pick up</button
      ><button
        type="button"
        class="btn btn-danger fw-bold"
        data-bs-toggle="offcanvas"
        @click="select(item)"
        data-bs-target="#off-detail-stock"
      >
        detail
      </button>
    </div>
    <OFFDetailStock :data_labels="data_labels" />
    <pick-up-modal />
  </div>
</template>

<script>
import { mapState } from "vuex";
import OFFDetailStock from "./OFFDetailStock";
import axios from "axios";
import moment from "moment";
import PickUpModal from "./PickUpModal.vue";
export default {
  components: { OFFDetailStock, PickUpModal },
  props: ["item"],
  computed: mapState(['stock']),
  data() {
    return{
      data_labels:[]
    }
  },
  methods: {
    select(data) {
      this.$store.state.stock_select = data;
      axios
        .get("http://127.0.0.1:8000/stock/frequency/stock/" + data.id)
        .then((response) => {
          this.data_labels = this.getDaysBetweenDates(response.data);
        });
    },
    // To use this function startDate,endDate should be moment()
    getDaysBetweenDates(data) {
      var now = moment(data[0].create_at).clone();
      var dates = [];
      var endDate = moment(data.at(-1).create_at);
      var copy_end = endDate.add(1,'d');  
      console.log(data);
      console.log("start date:" + now.format("DD/MM/YY"));
      console.log("end date:" + endDate.format("DD/MM/YY"));
      while (now.isSameOrBefore(copy_end)) {
        console.log("while loop : " + now.format("DD/MM/YY"));
        var amount = 0
        for(var item of data){
          if(moment(item.create_at).format("DD/MM/YYYY") === now.format("DD/MM/YYYY")){
            console.log(item.amount)
            amount = amount+item.amount;
          }
        }
        dates.push({date:now.format("DD/MM/YY"),amount:amount});
        now.add(1, "d");
      }
      console.log(dates);
      console.log();
      return dates;
    },
  },
};
</script>
