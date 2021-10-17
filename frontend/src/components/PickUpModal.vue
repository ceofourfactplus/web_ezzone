<template>
  <div
    class="modal fade"
    id="pick-up"
    tabindex="-1"
    aria-labelledby="pickuplabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="pickup">
            {{ $store.getters.stock_select}}
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="btn-group" style="height: 200px; width: 300px">
            <button id="minus" class="btn btn-warning" @click="amount--">
              <span style="font-size: 50px"> - </span>
            </button>
            <button class="btn btn-warning">
              <span style="font-size: 50px">{{ amount }}</span>
            </button>
            <button id="plus" class="btn btn-warning" @click="amount++">
              <span style="font-size: 50px"> + </span>
            </button>
          </div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-primary"
            data-bs-dismiss="modal"
            @click="pick_up()"
          >
            Pick Up
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState,mapGetters } from "vuex";
import { apiStock } from "../api/ApiStock";
export default {
  props: ["stock"],
  name: "PickUp",
  data() {
    return {
      amount: 1,
      btn_plus: false,
    };
  },
  computed:{ 
    ...mapState(["stock_select", "auth"]),
    ...mapGetters(["stock_select"])
  },
  methods: {
    pick_up() {
      const config = {
        headers: { Authorization: `Bearer ${this.$store.state.auth.accessToken}` },
      };
      const data = {
        amount: parseInt(this.amount),
        create_by: this.$store.state.auth.userInfo.id,
        stock_id: this.$store.state.stock_select.id,
      };
      apiStock.post("stock-trance/", data, config).then(() => {
        this.$store.dispatch("refreshModels", { models: "stock" });
      });
    },
  },
};
</script>

<style>
#plus:hover {
  background-color: #dc3545;
}
#minus:hover {
  background-color: #dc3545;
}
</style>