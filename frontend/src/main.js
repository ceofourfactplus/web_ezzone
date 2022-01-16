import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./assets/style/component.css";
import moment from "moment";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

createApp(App).use(store).use(router).use(moment).mount("#app");
