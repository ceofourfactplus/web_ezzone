<template>
  <div v-if="show">
    <div class="dark" @click="$emit('hide', input_customer)"></div>
    <div class="input">
      <form @submit="enter()">
        <input type="text" v-model="input_customer" />
        <input type="submit" style="display: none" />
      </form>
      <ul class="selector" v-if="selector_customer.length != 0">
        <li v-for="cus in selector_customer" :key="cus.id">
          <pre style="font-size: 24px;" @click="select_cus(cus)"
            >{{ phone_number_layout(cus.phone_number) }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;{{cus.nick_name}}</pre>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { api_customer } from "../../api/api_customer";
export default {
  props: ["show"],
  data() {
    return {
      input_customer: "",
      selector_customer: [],
    };
  },
  methods: {
    phone_number_layout(phone) {
      return (
        phone.substr(0, 3) + "-" + phone.substr(3, 3) + "-" + phone.substr(6, 4)
      );
    },
    select_cus(cus) {
      this.input_customer = cus.phone_number;
      this.$emit("submit", { tel: this.input_customer, customer: cus });
    },
    enter() {
      this.$emit("submit", { tel: this.input_customer, customer: null });
    },
  },
  watch: {
    input_customer(newTel) {
      if (newTel != "") {
        api_customer
          .get("get-customer-by-phone-number/" + newTel)
          .then((response) => {
            this.selector_customer = response.data;
          });
      } else {
        this.selector_customer = [];
      }
    },
  },
};
</script>

<style scoped>
.dark {
  background-color: #00000099;
  width: 100%;
  height: 100%;
  top: 0px;
  left: 0px;
  position: fixed;
  display: block;
}
.input {
  top: 10.5%;
  left: 23%;
  position: absolute;
  background-color: #303344;
  min-width: 320px;
  min-height: 40px;
  border-radius: 10px;
}
input {
  width: 100%;
  height: 40px;
  border-radius: 10px;
}
.selector {
  margin-top: 10px;
  background-color: #303344;
  position: absolute;
  list-style-type: none;
  border-radius: 0px 0px 10px 10px;
  text-align: left;
  padding-left: 10px;
  min-width: 320px;
  color: #fff;
  font-size: 20px;
  font-weight: 400;
  padding-bottom: 10px;
}
li {
  height: 45px;
  line-height: 45px;
}
pre {
  font-family: "Sarabun", sans-serif !important;
  font-size: 27px;
}
</style>