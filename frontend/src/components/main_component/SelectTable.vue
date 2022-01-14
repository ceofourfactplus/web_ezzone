<template>
  <div v-if="show">
    <div class="dark" @click="$emit('hide')"></div>
    <div class="table-select">
      <div class="row w-100" style="margin-left: 0px">
        <div class="col-6 w-100" style="margin:auto" @click="$emit('select_table','-')">-</div>
        <div class="col-6"></div>
        <div class="col-6 w-100" style="margin: auto" v-for="i in 10" :key="i" @click="$emit('select_table',i)">
          {{ i }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["show"],
};
</script>

<style scoped>
.dark {
  background-color: #00000099;
  width: 100%;
  height: 100%;
  top: 0px;
  left: 0px;
  position: fixed;
  display: block;
}
.table-select {
  top: 16%;
  left: 58%;
  position: absolute;
  background-color: #303344;
  width: 234px;
  height: 461.18px;
  border: 1.13592px solid #ea7c69;
  border-radius: 10px;
  display: flex;
  color: #ffffff;
  font-weight: bold;
  font-size: 40px;
}
</style>