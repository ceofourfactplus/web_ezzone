import { createStore } from "vuex";
import axios from "axios";
import auth from "./modules/auth"

export default createStore({
  state: {
    stock_data: [],
    supplier_data: [],
    unit_data: [],
    payer_data: [],
    OrderToBuy: [],
    stock_select:{
      name: true
    },
    confirm_pass:false,
    modal_id:'',
  },
  mutations: {
    updateStock(state, { stock }) {
      state.stock_data = stock;
    },
    updateSupplier(state, { supplier }) {
      state.supplier_data = supplier;
    },
    updateUnit(state, { unit }) {
      state.unit_data = unit;
    },
    updatePayer(state, { payer }) {
      state.payer_data = payer;
    },
    updateOrderToBuy(state, { order }) {
      state.OrderToBuy = order;
    },
    refreshModels(state, { models }) {
      const headers = {
        headers: {
          Authorization: `Bearer ${state.auth.accessToken}`,
        },
      };
      axios
        .get("http://127.0.0.1:8000/stock/" + models + "/", headers)
        .then((response) => {
          state[models+"_data"] = response.data;
        });
    },
  },
getters: {
    modal_id(state){
      return '#'+state.modal_id;
    },
    stock_select(state){
      return state.stock_select.name;
    }    
  },
  actions: {
    refreshModels({ commit },model) {
      commit("refreshModels",{
        models: model.models
      });
    },
  },
  modules: {
    auth,
  },
});
