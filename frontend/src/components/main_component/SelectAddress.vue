<template>
  <div v-if="show">
    <div class="dark" @click="$emit('hide')"></div>
    <div class="table-select">
      <div class="row" style="margin: 0px">
        <div
          class="col-12 mb-4"
          style="
            display: flex;
            font-weight: bold;
            font-size: 36px;
            line-height: 23px;
            justify-content: space-between;
          "
        >
          <img
            @click="$emit('save', address_select)"
            src="../../assets/icon/save.png"
            style="height: 29.5px"
            alt=""
          />
          Customer Address
          <img
            @click="$emit('hide')"
            src="../../assets/icon/delete.png"
            style="height: 29.5px"
            alt=""
          />
        </div>
        <div class="col-4 h-40">Name</div>
        <div class="col-8 h-40">:&#160;{{ customer.nick_name }}</div>
        <div class="col-4 h-40">Tel</div>
        <div class="col-8 h-40">
          :&#160;{{ phone_number_layout(customer.phone_number) }}
        </div>
        <div class="col-12 line"></div>
        <div class="col-12" style="padding: 0px">
          <div
            v-for="(address, index) in customer.addresscustomer_set"
            :key="address.id"
            class="row"
          >
            <div class="col-4 h-40">
              <label class="container-radio"
                >Address {{ index + 1 }}
                <input
                  type="radio"
                  checked="checked"
                  :value="address.address"
                  v-model="address_select"
                  name="radio"
                />
                <span class="checkmark"></span>
              </label>
            </div>
            <div
              class="col-8"
              style="
                white-space: normal;
                padding: 0px;
                text-align: left;
                padding-left: 13px;
                display: flex;
              "
            >
              <span>: </span>
              <span style="padding-left: 5px">{{ address.address }}</span>
            </div>
            <div class="col-12 mt-2 mb-2 line w-100" style="margin: auto"></div>
          </div>
        </div>
        <div class="col-4 h-40" style="padding: 0px">
          <label class="container-radio"
            >Address {{ customer.addresscustomer_set.length + 1 }}
            <input
              type="radio"
              checked="checked"
              :value="new_address"
              v-model="address_select"
              name="radio"
              style="z-index: 1"
            />
            <span class="checkmark"></span>
          </label>
        </div>
        <div class="col-8 w-100" style="padding: 0px">
          <textarea
            style="
              z-index: 5;
              width: 100%;
              height: 135px;
              background: #717171;
              font-size: 20px;
            "
            v-model="new_address"
          ></textarea>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["customer",'show'],
  methods: {
    phone_number_layout(phone) {
      if (phone != undefined) {
        return (
          phone.substr(0, 3) +
          "-" +
          phone.substr(3, 3) +
          "-" +
          phone.substr(6, 4)
        );
      }
    },
  },
  data() {
    return {
      address_select: "",
      new_address: "",
    };
  },
  watch: {
    new_address(add) {
      this.address_select = add;
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
.table-select {
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
  background-color: #303344;
  width: 470px;
  padding: 16px;
  border: 1.13592px solid #ea7c69;
  border-radius: 10px;
  display: flex;
  color: #ffffff;
  font-size: 20px;
}
.h-40 {
  height: 40px;
  text-align: left;
}
.col-4,
label {
  color: #ea7c69;
  font-weight: 700;
}
.line {
  height: 1.5px;
  background-color: #ea7c69;
}
input[type="radio"] {
  width: 0px;
  height: 0px;
}
</style>