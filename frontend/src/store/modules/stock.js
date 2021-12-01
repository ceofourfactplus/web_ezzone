import axios from "axios";

export default {
  namespace: true,
  state: {
    stock_select: {
      name: true,
      minstock: true,
      balance: true,
      avg_price: true,
      max_price: true,
      min_price: true,
      code: true,
      category_set: {
        name: true,
      },
      id: 1,
    },
    stock_data: [],
    supplier_data: [],
    unit_data: [],
    payer_data: [],
    OrderToBuy: [],
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
          state[models + "_data"] = response.data;
        });
    },
  },
  getters: {
    modal_id(state) {
      return "#" + state.modal_id;
    },
    stock_select(state) {
      return state.stock_select.name;
    },
  },
  actions: {
    refreshModels({ commit }, model) {
      commit("refreshModels", {
        models: model.models,
      });
    },
    opening({ context,state }) {
      const headers = {
        headers: {
          Authorization: `Bearer ${state.auth.accessToken}`,
        },
      };
      axios
        .get("http://127.0.0.1:8000/stock/stock/", headers)
        .then((response) => {
          context.commit(
            "updateStock",
            {
              stock: response.data,
            },
            { root: true }
          );
        });
      axios
        .get("http://127.0.0.1:8000/stock/unit/", headers)
        .then((response) => {
          context.commit(
            "updateUnit",
            {
              unit: response.data,
            },
            { root: true }
          );
        });
      axios
        .get("http://127.0.0.1:8000/stock/payer/", headers)
        .then((response) => {
          context.commit(
            "updatePayer",
            {
              payer: response.data,
            },
            { root: true }
          );
        });
      axios
        .get("http://127.0.0.1:8000/stock/supplier/", headers)
        .then((response) => {
          context.commit(
            "updateSupplier",
            {
              supplier: response.data,
            },
            { root: true }
          );
        });
    },
  },
};
