<template>
  <PieChart
    :chartData="testData"
    :options="testOptions"
    :plugins="Plugins"
    :width="400"
    :height="400"
    style="margin: auto"
  />
</template>

<script>
import { PieChart } from "vue-chart-3";
import ChartDataLabels from "chartjs-plugin-datalabels";

export default {
  props:['data'],
  components: { PieChart },
  setup(props) {
    const testData = {
      labels: ["Food", "Drink", "Dressert", "Topping", "Consign"],
      datasets: [
        {
          data: props.data,
          backgroundColor: [
            "#FF6385",
            "#25A0E8",
            "#FFCE61",
            "#9B62FB",
            "#3CC0BF",
          ],
          borderWidth: 0,
        },
      ],
    };

    const testOptions = {
      plugins: {
        datalabels: {
          color: "#2F414E",
          textAlign: "center",
          font: {
            weight: "bold",
            size: 30,
            family: "Sarabun",
          },
          formatter: function (value, context) {
            return value + " ฿";
          },
        },
        legend: {
          display: false,
          labels: {
            color: "rgb(255, 99, 132)",
          },
        },
      },
    };
    const Plugins = [ChartDataLabels];
    return { testData, testOptions, Plugins };
  },
};
</script>

<style>
</style>