<template>
  <div>
    <div class="title">Manager</div>
    <div class="row1">
      <div class="block">
        <img class="image" src="../../src/assets/icon/order-box.png" />
        <p
          style="
            width: 80px;
            height: 36px;
            color: white;
            font-size: 28px;
            left: 45px;
            position: absolute;
          "
        >
          Orders
        </p>
      </div>
      <div class="block" style="margin-left: 180px;">
        <img class="image" src="../../src/assets/icon/drink.png" />
        <p
          style="
            width: 80px;
            height: 36px;
            color: white;
            font-size: 28px;
            left: 45px;
            position: absolute;
          "
        >
          Drink order
        </p>
      </div>
      <div class="block" style="margin-left: 360px;">
        <img class="image" src="../../src/assets/icon/food.png" />
        <p
          style="
            width: 80px;
            height: 36px;
            color: white;
            font-size: 28px;
            left: 45px;
            position: absolute;
          "
        >
          Food order
        </p>
      </div>
      <div class="block" style="margin-left: 540px;">
        <img class="image" src="../../src/assets/icon/order-detail.png" />
        <p
          style="
            width: 80px;
            height: 36px;
            color: white;
            font-size: 28px;
            left: 45px;
            position: absolute;
          "
        >
          Order detail
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  //   components: {

  //   },
  // mounted: {

  // },
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped>
.title {
  width: 100%;
  height: 59px;
  background-color: #2f414e;
  text-align: center;
  font-size: 36px;
  font-weight: 700;
  color: white;
}
.row1 {
  width: 100%;
  height: 168px;
  margin-top: 35px;
}
.block {
  width: 180px;
  height: 168px;
  position: absolute;
}
.image {
  width: 130px;
  height: 130px;
}
</style>