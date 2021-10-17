<template>
  <div id="inventory">
    <navbar-stock />
    <div class="container">
      <!-- if have stock-data -->
      <div v-if="stock_data.length != 0" class="row mt-2">
        <div
          class="col-3"
          v-for="data in stock_data"
          :key="data.id"
        >
          <card-stock :item="data" />
        </div>
      </div>
      <!-- if don`t have stock-data -->
      <div v-else class="position-absolute top-50 start-50 translate-middle">
        <h1 class="text-center text-light">don`t have stock</h1>
      </div>
    </div>
    <modal-invoice />
    <modal-inventory />
    <modal-supplier />
    <modal-payer />
    <unit-modal />
    <pick-up-modal/>
    <check-pass/>
  </div>
</template>

<script>
import { apiStock } from "../../api/ApiStock";
import { mapState } from "vuex";
import NavbarStock from "../../components/NavbarStock.vue";
import CardStock from "../../components/CardStock.vue";
import ModalInvoice from "../../components/InvoiceModal.vue";
import ModalInventory from "../../components/StockModal.vue";
import ModalSupplier from "../../components/SupplierModal.vue";
import ModalPayer from "../../components/PayerModal.vue";
import UnitModal from "../../components/UnitModal.vue";
import PickUpModal from '../../components/PickUpModal.vue';
import CheckPass from '../../components/CheckPass.vue';
export default {
  components: {
    NavbarStock,
    CardStock,
    ModalInvoice,
    ModalInventory,
    ModalSupplier,
    ModalPayer,
    UnitModal,
    PickUpModal,
    CheckPass,
  },
  data() {
    return {};
  },
  computed: mapState(["stock_data","auth"]),
  created() {
    apiStock
      .get("/supplier/", {
        headers: { Authorization: `Bearer ${this.$store.state.auth.accessToken}` },
      })
      .then((response) => {
        this.$store.state.supplier_data = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
</style>