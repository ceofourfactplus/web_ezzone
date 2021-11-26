import { createStore } from "vuex";
// import axios from "axios";
import auth from "./modules/auth";
import stock from "./modules/stock";
import product from "./modules/product";

export default createStore({
  state: {
    confirm_pass: false,
    modal_id: "",
    chart_pickup_data: [],
    chart_dates_data: [],
  },
  mutations: {},
  getters: {},
  actions: {},
  modules: {
    auth,
    stock,
    product,
  },
});
