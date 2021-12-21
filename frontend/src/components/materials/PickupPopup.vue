<template>
  <div>
    <div class="show-pickup-popup">
      <div class="row">
        <div class="col-3">
        </div>
        <div class="col-6 txt-for-add" style="width: 100%">Pickup</div>
        <div class="col-3">
          <img
            @click="show_status = false"
            src="../../assets/icon/Union.png"
            style="
              top: 10px;
              right: 10px;
              position: absolute;
              width: 50px;
              height: 50px;
            "
          />
        </div>
      </div>
      <div class="content-wrapper">

      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "PickupPopup",
  props: [],
  data() {
    return {
        show_status: false,
    };
  },
  mounted() {
  },
};
</script>

<style scoped>
.content-wrapper {
    width: 575px;
    height: 260px;
    background: #303344;
    border-radius: 30px;
}
.show-pickup-popup {
  width: 616.86px;
  height: 406px;
  top: 7%;
  left: 7%;
  margin: 15px 20px 0px 20px;
  position: absolute;
  background-color: #252836;
  border: 2px solid #ea7c69;
  border-radius: 20px;
}
.txt-for-add {
  font-weight: bold;
  font-size: 48px;
  line-height: 56px;
  text-align: center;
  width: 100%;
  color: white;
}
</style>