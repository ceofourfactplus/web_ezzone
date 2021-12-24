<template>
    <div class="po-detail-popup">
      <!-- Nav -->
      <div class="row" style="width: 100%; height: 80px;">
        <div class="col-4"></div>
        <div class="col-5 popup-header">PO Detail</div>
        <div class="col-3">
          <img
            @click="$emit('show_status')"
            src="../../assets/icon/Union.png"
            style="
              top: 15px;
              right: 10px;
              position: absolute;
              width: 25px;
              height: 25px;
            "
          />
        </div>
      </div>
      <!-- Over Wrapper -->
      <div class="row over-wrapper">
        <div class="col-3" style="width: 261px; height: 270px;">
          <img src="../../assets/icon/star.png" class="po-detail-img">
        </div>
        <div class="col-9" style="width: 357px; height: 270px;">
          <div style="font-size: 30px; color: white; height: 39px; margin-top: 10px; text-align: left;">soda</div>
          <div style="font-size: 30px; color: #EA7C69; height: 42px; margin-top: 10px; text-align: left;">
            Remain&nbsp;:&nbsp;23&nbsp;ฟอง &nbsp;&nbsp;&nbsp; <img style="margin-bottom: 10px;" :src="$store.state.raw_material.status_image[2]">
          </div>
          <!-- Table Head -->
          <div class="table-head-in-po">
            <div class="row">
              <div class="col-3 item-in-table-head">Min</div>
              <div class="col-3 item-in-table-head">Avg</div>
              <div class="col-3 item-in-table-head">Max</div>
              <div class="col-3 item-in-table-head">Last</div>
            </div>
          </div>
          <!-- Table Item -->
          <div class="table-item-in-po">
            <div class="row">
              <div class="col-3 item-in-table-item" style="margin-top: 5px;">50</div>
              <div class="col-3 item-in-table-item" style="margin-top: 5px;">52</div>
              <div class="col-3 item-in-table-item" style="margin-top: 5px;">60</div>
              <div class="col-3 item-in-table-item" style="margin-top: 5px;">30</div>
            </div>
          </div>
        </div>
      </div>
      <!-- Below Wrapper -->
      <!-- Table -->
      <div class="table" style="width: 575px; margin-top: -10px;">
        <!-- Table Head -->
        <div class="table-header" style="width: 100%;">
          <div class="row">
            <div class="col-4" style="width: 100%;">Supplier</div>
            <div class="col-2" style="width: 100%;">Price</div>
            <div class="col-4" style="width: 100%;">Number</div>
            <div class="col-2" style="width: 100%; padding-right: 40px;">Map</div>
          </div>
        </div>
        <!-- Table Item -->
        <div class="table-item" style="width: 100%;">
          <div class="row" style="font-size: 30px;">
            <div class="col-4" style="width: 100%; text-align: left; margin-left: 20px;">Makro</div>
            <div class="col-2" style="width: 100%;">100</div>
            <div class="col-4" style="width: 100%;">xxx-xxx-xxxx</div>
            <div class="col-2" style="width: 100%;"><img style="width: 40px; height: 40px; margin: 0px 20px 10px 0px;" src="../../assets/icon/map-icon.png"></div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "PODetail",
  props: [],
  components: {},
  data() {
    return {
    };
  },
  mounted() {
  },
  methods: {
  },
};
</script>