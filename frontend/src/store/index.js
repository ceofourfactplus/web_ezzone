import { createStore } from "vuex";
// import axios from "axios";
import auth from "./modules/auth";
import stock from "./modules/stock";
import product from "./modules/product";
import sale_channel from "./modules/sale_channel";
import raw_material from "./modules/raw_material";
import promotion from "./modules/promotion";
import pos from "./modules/pos"


export default createStore({
  state: {
    confirm_pass: false,
    modal_id: "",
    chart_pickup_data: [],
    chart_dates_data: [],
    ezzone_id:null
  },
  mutations: {},
  getters: {},
  actions: {},
  modules: {
    auth,
    stock,
    pos,
    product,
    raw_material,
    sale_channel,
    promotion,
  },
});
