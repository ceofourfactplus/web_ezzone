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
          <img :src="require(`../../../../backend${po_item.raw_material_set.img}`)" class="po-detail-img">
        </div>
        <div class="col-9" style="width: 357px; height: 270px;">
          <div style="font-size: 30px; color: white; height: 39px; margin-top: 10px; text-align: left;">{{ po_item.raw_material_set.name }}</div>
          <div style="font-size: 30px; color: #EA7C69; height: 42px; margin-top: 10px; text-align: left;">
            Remain&nbsp;:&nbsp;{{ po_item.raw_material_set.remain }}&nbsp;{{ po_item.unit_set.unit }} &nbsp;&nbsp;&nbsp; 
            <img style="margin-bottom: 10px;" :src="$store.state.raw_material.status_image[po_item.raw_material_set.status]['img']">
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
              <div class="col-3 item-in-table-item" style="margin-top: 5px;">{{ po_item.raw_material_set.minimum }}</div>
              <div class="col-3 item-in-table-item" style="margin-top: 5px;">{{ po_item.avg_price }}</div>
              <div class="col-3 item-in-table-item" style="margin-top: 5px;">{{ po_item.raw_material_set.maximum }}</div>
              <div class="col-3 item-in-table-item" style="margin-top: 5px;">{{ po_item.last_price }}</div>
            </div>
          </div>
        </div>
      </div>
      <!-- Below Wrapper -->
      <!-- Table -->
      <div class="table" style="width: 575px; margin-top: -10px;">
        <!-- Table Head -->
        <div class="table-header w-100">
          <div class="row">
            <div class="col-4 w-100">Supplier</div>
            <div class="col-2 w-100">Price</div>
            <div class="col-4 w-100">Number</div>
            <div class="col-2 w-100" style="padding-right: 40px;">Map</div>
          </div>
        </div>
        <!-- Table Item -->
        <div class="table-item w-100">
          <div class="row" style="position: relative; bottom: 10px;">
            <div class="col-4 w-100" style="text-align: left; margin-left: 20px;">{{ po_item.supplier_set.company_name }}</div>
            <div class="col-2 w-100">{{ po_item.last_price }}</div>
            <div class="col-4 w-100">{{ po_item.supplier_set.phone }}</div>
            <div class="col-2 w-100"><img style="width: 30px; height: 30px; margin: 0px 20px 0px -10px;" src="../../assets/icon/map-icon.png"></div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "PODetail",
  props: ['po_item'],
  components: {},
  data() {
    return {
    };
  },
  mounted() {
    console.log(this.po_item, 'po_item')
  },
  methods: {
  },
};
</script>

<style scoped>
.item-in-table-item {
  width: 100%;
  text-align: center;
}
.item-in-table-head {
  width: 100%;
  text-align: center;
}
.table-item-in-po {
  width: 100%;
  height: 59px;
  color: white;
  background: #303344;
  border-radius: 10px;
  margin-top: 10px;
  font-size: 30px;
}
.table-head-in-po {
  width: 100%;
  height: 59px;
  background: #889898;
  border-radius: 10px;
  margin-top: 10px;
  font-size: 30px;
  color: white;
}
.po-detail-img {
  width: 218px;
  height: 218px;
  margin: 20px 20px 20px 20px;
}
.over-wrapper {
  width: 619px;
  height: 271.11px;
}
.po-detail-popup {
  width: 619px;
  height: 640px;
  top: 20%;
  left: 100px;
  position: absolute;
  background-color: #252836;
  border: 2px solid #ea7c69;
  border-radius: 20px;
}
.popup-header {
  font-weight: 800;
  font-size: 48px;
  line-height: 56px;
  text-align: center;
  margin-top: 10px;
  width: 100%;
  color: white;
}
</style>