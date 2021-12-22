
<template>
  <div class="detail-barsarabun-normal-alabaster-30px">
    <checked-off-size30-color-orange />
    <h1 class="titlevalign-text-middle">Item</h1>
    <div class="numbervalign-text-middle">1</div>
    <div class="unitvalign-text-middle">Unit</div>
    <div class="makrovalign-text-middle">makro</div>
    <property1-warning-icon />
  </div>
</template> 

<script>
import CheckedOffSize30ColorOrange from './new3.vue'
import Property1WarningIcon from './new4.vue'
export default {
  name: "DetailBar",
  components: { CheckedOffSize30ColorOrange, Property1WarningIcon },
};
</script> 

<style>
.detail-bar {
  align-items: center;
  background-color: var(--tuna);
  border-radius: 10px;
  display: flex;
  height: 60px;
  min-width: 677px;
  padding: 0 10px;
  position: relative;
}
.title {
  height: 39px;
  letter-spacing: 0;
  margin-left: 20px;
  min-width: 61px;
  text-align: center;
}
.number {
  height: 39px;
  letter-spacing: 0;
  margin-left: 196px;
  min-width: 17px;
  text-align: center;
}
.unit {
  height: 39px;
  letter-spacing: 0;
  margin-left: 41px;
  min-width: 55px;
}
.makro {
  height: 39px;
  letter-spacing: 0;
  margin-left: 34px;
  min-width: 83px;
}
</style> /