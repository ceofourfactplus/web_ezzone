<template>
  <BarChart
    :chartData="testData"
    :options="testOptions"
    :plugins="Plugins"
    :width="700"
    :height="800"
    style="margin: auto"
  />
</template>

<script>
import { BarChart } from "vue-chart-3";
import ChartDataLabels from "chartjs-plugin-datalabels";

export default {
  props: ["data"],
  components: { BarChart },
  setup(props) {
    const testData = {
      labels: [
        "Food",
        "Drink",
        "Dresxvdfdddsaff",
        "Topping",
        "Cosdfsdfsnsign",
        "Drsdfsdfsink",
      ],
      datasets: [
        {
          data: [
            30, 60, 30, 50, 20, 60, 30, 50, 20
          ],
          backgroundColor: [
            "#FF6385",
            "#25A0E8",
            "#FFCE61",
            "#9B62FB",
            "#3CC0BF",
          ],
          datalabels: {
            labels: {},
          },
          borderWidth: 0,
          borderRadius: {
            topLeft: 0,
            topRight: 20,
            botttomLeft: 0,
            bottomRight: 20,
          },
          barPercentage: 0.6,
        },
      ],
    };

    const testOptions = {
      scales: {
        y: {
          ticks: {
            enabled:true,
            font: {
              size: 20,
            },
            color: "#fff",
          },
        },
        x: {
          ticks: {
            enabled:true,
            font: {
              size: 20,
            },
            color: "#fff",
          },
          grid: {
            drawBorder: false,
            color: function (context) {
              return "#ffffff80";
            },
          },
        },
      },
      responsive: false,
      aspectRatio: 1,
      indexAxis: "y",
      plugins: {
        datalabels: {
          color: "#fff",
          textAlign: "center",
          font: {
            weight: "bold",
            size: 30,
            family: "Sarabun",
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
