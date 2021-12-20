import { createStore } from "vuex";
// import axios from "axios";
import auth from "./modules/auth";
import stock from "./modules/stock";
import product from "./modules/product";
import raw_material from "./modules/raw_material";


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
    raw_material,
  },
});
