import router from "../../router/index";
import { api_pos } from "../../api/api_pos.js";
export default {
  namespaced: true,
  state: {
    order: {
      order_number: 0,
      address: "",
      nick_name: "",
      phone_number: "",
      status_delivery: 1,
      total_price: 0,
      total_amount: 0,
      sale_channel_id: null,
      sale_channel_set: {},
      description: "",
      status_order: 0,
      payment_status: 1,
      payment_id: 1,
      orderitem_set: [],
      create_by: 1,
      delivery_price: 0,
      table: null,
      total_balance: 0,
      discount: 0,
      discount_percent: false,
      select_index: null,
      cash: null,
      change: null,
      voucher_id: null,
      point_promotion_id: null,
      point: null,
    },
    customer_set: {
      addresscustomer_set: [],
    },
    voucher_set: null,
    point_promotion: {},
    category: 1,
    type_product: 2,
    select_index: null,
    is_edit_product: false,
    is_edit_promotion: false,
    is_edit_toppig: false,
    is_edit: false,
  },
  mutations: {
    note_input(state, input) {
      state.order.description = input;
    },
    cal_total_price(state) {
      state.order.total_price = 0;
      state.order.total_amount = 0;
      for (var item of state.order.orderitem_set) {
        item.total_price = parseInt(item.total_price);
        state.order.total_price += item.total_price;
        state.order.total_amount += item.amount;
      }
      if (state.order.discount_percent) {
        state.order.total_balance =
          (state.order.total_price * (100 - state.order.discount)) / 100;
      } else {
        state.order.total_balance =
          state.order.total_price - state.order.discount;
      }

      if (state.voucher_set != null) {
        if (state.voucher_set.is_percent) {
          state.order.total_balance -=
            (state.order.total_price * parseInt(state.voucher_set.discount)) /
            100;
        } else {
          state.order.total_balance =
            state.order.total_balance - parseInt(state.voucher_set.discount);
        }
      }

      if (state.order.phone_number != "" && state.point_promotion != null) {
        state.order.point =
          Math.floor(
            (state.order.total_balance - state.order.delivery_price) /
              parseInt(state.point_promotion.price_per_point)
          ) * parseInt(state.point_promotion.point);
        state.order.point_promotion_id = state.point_promotion.id;
      }
      state.order.total_balance += parseInt(state.order.delivery_price);
      state.order.total_balance = Math.round(state.order.total_balance);
    },
    discount(state, result) {
      if (result != "") {
        if (result.indexOf("%") != -1) {
          state.order.discount_percent = true;
          state.order.discount = parseInt(result.slice(0, result.indexOf("%")));
        } else {
          state.order.discount_percent = false;
          state.order.discount = parseInt(result);
        }
      } else {
        state.order.discount = 0;
        state.order.discount_percent = false;
      }
    },
    delivery(state, result) {
      if (result != "") {
        state.order.delivery_price = parseInt(result);
      } else {
        state.order.delivery_price = 0;
      }
    },
    remove_product(state, index) {
      state.order.orderitem_set.splice(index, 1);
    },
    select_product(state, index) {
      state.select_index = index;
      state.is_edit_product = true;
    },
    select_topping(state, index) {
      state.select_index = index;
      state.is_edit_topping = true;
    },
    select_package(state, index) {
      state.select_index = index;
      state.is_edit_package = true;
    },
    confirm_product(state, product) {
      state.order.orderitem_set[state.select_index] = JSON.parse(
        JSON.stringify(product)
      );
      state.select_index = null;
      state.is_edit_product = false;
    },
    confirm_topping(state, product) {
      state.order.orderitem_set[state.select_index] = JSON.parse(
        JSON.stringify(product)
      );
      state.select_index = null;
      state.is_edit_topping = false;
    },
    table(state, table) {
      state.order.table = table;
    },
    address_customer(state, address) {
      state.order.address = address;
    },
    phone_number(state, phone) {
      state.order.phone_number = phone;

      if (state.order.phone_number != "" && state.point_promotion != null) {
        state.order.point =
          Math.floor(
            (state.order.total_balance - state.order.delivery_price) /
              parseInt(state.point_promotion.price_per_point)
          ) * parseInt(state.point_promotion.point);
        state.order.point_promotion_id = state.point_promotion.id;
      }
    },
    customer_set(state, customer) {
      state.customer_set = customer;
      state.order.nick_name = customer.nick_name;
      state.order.phone_number = customer.phone_number;
      if (state.order.phone_number != "" && state.point_promotion != null) {
        state.order.point =
          Math.floor(
            (state.order.total_balance - state.order.delivery_price) /
              parseInt(state.point_promotion.price_per_point)
          ) * parseInt(state.point_promotion.point);
        state.order.point_promotion_id = state.point_promotion.id;
      }
    },
    clear_order(state) {
      state.order = {
        order_number: 0,
        address: "",
        nick_name: "",
        phone_number: "",
        status_delivery: 1,
        total_price: 0,
        total_amount: 0,
        sale_channel_id: null,
        sale_channel_set: {},
        description: "",
        status_order: 0,
        payment_status: 1,
        payment_id: 1,
        orderitem_set: [],
        create_by: 1,
        delivery_price: 0,
        table: null,
        total_balance: 0,
        discount: 0,
        discount_percent: false,
        select_index: null,
        cash: null,
        change: null,
        voucher_id: null,
        point_promotion_id: null,
        point: null,
      };
      state.is_edit = false;
      state.voucher_set = null;
    },
    cash(state, cash) {
      state.order.cash = cash;
      state.order.change = state.order.cash - state.order.total_balance;
    },
    payment(state, data) {
      state.order.payment_id = data;
    },
    clear_voucher(state) {
      state.voucher_set = null;
    },
  },
  actions: {
    add_product(context, product) {
      context.state.order.orderitem_set.push(
        JSON.parse(JSON.stringify(product))
      );
      context.commit("cal_total_price");
    },
    discount(context, result) {
      context.commit("discount", result);
      context.commit("cal_total_price");
    },
    delivery(context, result) {
      context.commit("delivery", result);
      context.commit("cal_total_price");
    },
    remove_product(context, index) {
      context.commit("remove_product", index);
      context.commit("cal_total_price");
    },
    edit_product(context, index) {
      context.commit("select_product", index);
      router.push({
        name: "KeyProductDetail",
        params: {
          product_id: context.state.order.orderitem_set[index].product,
        },
      });
    },
    edit_topping(context, index) {
      context.commit("select_topping", index);
      router.push({
        name: "KeyToppingDetail",
        params: {
          topping_id: context.state.order.orderitem_set[index].topping,
        },
      });
    },
    edit_package(context, index) {
      context.commit("select_package", index);
      router.push({
        name: "KeyPromotionDetail",
        params: {
          package_id: context.state.order.orderitem_set[index].package,
        },
      });
    },
    confirm_product(context, product) {
      context.commit("confirm_product", product);
      context.commit("cal_total_price");
    },
    confirm_topping(context, product) {
      context.commit("confirm_topping", product);
      context.commit("cal_total_price");
    },
    clear_order(context) {
      context.commit("clear_order");
      router.push({ name: "SelectSaleChannel" });
    },
    create_order(context) {
      if (context.state.is_edit) {
        api_pos
          .put(
            "order/" + context.state.order.id + "/",
            context.getters.get_data
          )
          .then((response) => {
            console.log(response.data);
            context.commit("clear_order");
            router.push({
              name: "OrderDetail",
            });
            context.state.is_edit = false;
            context.commit("clear_order");
          });
      } else {
        api_pos.post("order/", context.getters.get_data).then((response) => {
          console.log(response.data);
          context.commit("clear_order");
          router.push({
            name: "OrderDetail",
          });
        });
      }
    },
    clear_voucher(context) {
      context.commit("clear_voucher");
      context.commit("cal_total_price");
    },
    re_order(context, order) {
      context.state.order = order;
      context.state.is_edit = true;
      if (order.customer_set != null) {
        context.state.order["nick_name"] =
          context.state.order.customer_set.nick_name;
        context.state.order["phone_number"] =
          context.state.order.customer_set.phone_number;
        if (order.address_id != null) {
          context.state.order["address"] = order.address_set.address;
        } else {
          context.state.order["address"] = "";
        }
      } else {
        context.state.order["nick_name"] = "";
        context.state.order["phone_number"] = "";
        context.state.order["address"] = "";
      }
      router.push({ name: "OrderReceipt" });
    },
  },
  getters: {
    img_sale_channel: (state) => {
      return state.order.sale_channel_set.img;
    },
    orderitem_list: (state) => {
      return state.order.orderitem_set;
    },
    total_price: (state) => {
      return state.order.total_price;
    },

    // orderitemtopping_set orderitemtopping_set
    cash: (state) => {
      if (state.order.cash != null) {
        return state.order.cash.toLocaleString(undefined);
      } else {
        return 0;
      }
    },
    change: (state) => {
      if (state.order.cash != null) {
        return state.order.change.toLocaleString(undefined);
      } else {
        return 0;
      }
    },
    discount: (state) => {
      var discount = "";
      if (state.order.discount_percent) {
        discount = state.order.discount.toString() + "%";
      } else if (state.order.discount != 0) {
        discount = state.order.discount;
      } else {
        discount = "-";
      }
      return discount;
    },
    discount_price: (state) => {
      var discount = "";
      if (state.order.total_balance - state.order.total_price != 0) {
        discount = state.order.total_price - state.order.total_balance;
      } else {
        discount = "-";
      }
      return discount;
    },
    total_balance: (state) => {
      return parseInt(state.order.total_balance);
    },
    total_amount: (state) => {
      return parseInt(state.order.total_amount);
    },
    delivery_price: (state) => {
      if (state.order.delivery_price == 0) {
        return "-";
      } else {
        return state.order.delivery_price;
      }
    },
    edit_product: (state) => {
      return state.order.orderitem_set[state.select_index];
    },
    is_edit_product: (state) => {
      return state.is_edit_product;
    },
    edit_topping: (state) => {
      return state.order.orderitem_set[state.select_index];
    },
    is_edit_topping: (state) => {
      return state.is_edit_topping;
    },
    edit_package: (state) => {
      return state.order.orderitem_set[state.select_index];
    },
    is_edit_package: (state) => {
      return state.is_edit_promotion;
    },
    table: (state) => {
      return state.order.table;
    },
    description: (state) => {
      return state.order.description;
    },
    address: (state) => {
      if (state.order.address_set != null) {
        return state.order.address_set.address;
      }
      return "";
    },
    phone_number: (state) => {
      return state.order.phone_number;
    },
    customer_name: (state) => {
      return state.order.nick_name;
    },
    customer_set: (state) => {
      return state.customer_set;
    },
    get_data: (state) => {
      return state.order;
    },
    voucher: (state) => {
      if (state.voucher_set != null) {
        if (state.voucher_set.is_percent) {
          return parseInt(state.voucher_set.discount).toString() + "%";
        } else {
          return parseInt(state.voucher_set.discount);
        }
      }
      return "-";
    },
  },
};
