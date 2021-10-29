<template>
  <div>
    <BarChart ref="doughnutRef" :chartData="mainData" :options="options" />
  </div>
</template>

<script>
import { computed, defineComponent, ref, watch } from "vue";
import { BarChart } from "vue-chart-3";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

export default defineComponent({
  props: ["data_labels"],
  components: { BarChart },
  setup(props) {
    const data = ref([]);
    const labels = ref([]);
    const doughnutRef = ref();

    const options = ref({
      responsive: true,
      plugins: {
        legend: {
          position: "top",
        },
        title: {
          display: true,
          text: "Chart.js Doughnut Chart",
        },
      },
    });

    watch(
      () => props.data_labels,
      (props) => {
        for(var item of props.data_labels) {
          data.value.push(item.amount);
          labels.value.push(item.dates);
        }
        console.log(data.value,labels.value);
      }
    );

    const mainData = computed(() => ({
      labels: labels.value,
      datasets: [
        {
          data: data.value,
          backgroundColor: [
            "#77CEFF",
            "#0079AF",
            "#123E6B",
            "#97B0C4",
            "#A5C8ED",
          ],
        },
      ],
    }));

    return { mainData, doughnutRef, options };
  },
});
</script>