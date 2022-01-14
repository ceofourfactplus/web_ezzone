<template>
  <div v-if="show">
    <div class="dark" @click="close()"></div>
    <div class="main-pop-up" style="width: 400px">
      <div class="row" style="width: 90%; margin: auto">
        <div class="col-12 mt-3 mb-3">Cancel Order</div>
        <div class="col-12 m-2">
          <div class="checkbox-orange" style="padding-left: 25%">
            <input
              type="radio"
              v-model="cancel_order_status"
              value=1
              id="re-order"
            />
            <label for="re-order">Re-order</label>
          </div>
        </div>
        <div class="col-12 m-2">
          <div class="checkbox-orange" style="padding-left: 25%">
            <input
              type="radio"
              id="permanently"
              v-model="cancel_order_status"
              value=0
            />
            <label for="permanently">Permanently</label>
          </div>
        </div>
        <div class="col-12">
          <div class="row reason">
            <div class="col-12" style="font-size: 20px; font-weight: bold">
              Reason to Cancel
            </div>
            <div
              class="col-12"
              v-for="text in reason"
              :key="text"
              style="height: 30px"
            >
              <div class="checkbox-orange">
                <input
                  type="checkbox"
                  v-model="selected_reason"
                  :value="text"
                  :id="text"
                />
                <label :for="text">{{ text }}</label>
              </div>
            </div>
            <div class="col-12">
              <textarea
                v-model="reason_detail"
                placeholder="Description"
              ></textarea>
            </div>
          </div>
        </div>
        <div class="col-6 mt-3 w-100" style="padding: 0px; margin: auto">
          <button
            class="btn-ghost-r"
            @click="close()"
            style="width: 175px; height: 56px; line-height: 100%"
          >
            <img
              src="../../assets/icon/cancel.png"
              style="width: 30px; height: 30px"
              alt=""
            />
          </button>
        </div>
        <div class="col-6 mt-3 w-100" style="padding: 0px; margin: auto">
          <button
            @click="submit()"
            class="btn-ghost-g"
            style="width: 175px; height: 56px; line-height: 100%"
          >
            <img
              src="../../assets/icon/correct-bold.png"
              style="width: 30px; height: 30px"
              alt=""
            />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["show"],
  data() {
    return {
      reason: [
        "Payment issue",
        "Change of mind",
        "Employee error",
        "Wait for too long",
        "Product out of stock",
        "Promo code not applied",
      ],
      selected_reason: [],
      reason_detail: "",
      cancel_order_status: 0,
    };
  },
  methods: {
    close() {
      this.selected_reason = [];
      this.reason_detail = "";
      this.$emit("close");
    },
    submit() {
      var reason = "";
      for (var i of this.selected_reason) {
        reason += i + " ";
      }
      reason += this.reason_detail;
      if (parseInt(this.cancel_order_status)) {
        this.$emit("re_order", reason);
      } else {
        this.$emit("cancel_order",reason);
      }
    },
  },
};
</script>

<style scoped>
.checkbox-orange {
  line-height: 20px;
  display: flex;
}
.main-pop-up {
  padding-bottom: 20px;
}
.reason {
  margin-top: 10px;
  padding-top: 10px;
  border-radius: 10px;
  border: 2px solid#ea7c69;
  height: 370px;
}
textarea {
  width: 330px;
  background-color: #717171;
  height: 80px;
  text-indent: 0px;
  padding-left: 5px;
}
label {
  font-size: 20px !important;
}
input {
  margin-right: 15px;
}
</style>