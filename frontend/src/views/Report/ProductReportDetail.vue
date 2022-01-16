<template>
  <div>
    <nav-app>Food Report</nav-app>
    <div class="row" style="width: 90%; margin: auto">
      <div class="col-12" style="text-align: right">
        <select
          style="
            background-color: #717171;
            width: 174px;
            height: 43px;
            font-weight: 700;
            margin-right: 10px;
          "
          v-model="day"
        >
          <option value="Monday">Monday</option>
        </select>
        <select
          style="
            background-color: #717171;
            width: 174px;
            height: 43px;
            font-weight: 700;
          "
          v-model="day"
        >
          <options value="Monday">Monday</options>
          <options value="Tuesday">Tuesday</options>
          <options value="Wednesday">Wednesday</options>
          <options value="Thursday">Thursday</options>
          <option value="Friday">Friday</option>
          <option value="Saturday">Saturday</option>
          <option value="Sunday">Sunday</option>
        </select>
      </div>
      <div class="col-12 frame" style="height: 800px; overflow-y: auto">
        <product-chart></product-chart>
      </div>
    </div>
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import ProductChart from "./ProductChart.vue";
export default {
  components: { ProductChart, NavApp },
  mounted() {
  },
  data() {
    return {
      category: [],
    };
  },
};
</script>

<style>
</style>