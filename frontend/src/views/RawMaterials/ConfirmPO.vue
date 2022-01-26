<template>
  <div>
    <!-- nav bar -->
    <nav-app :url_name="'PO'">Confirm&#160;PO</nav-app>
    <img src="../../assets/icon/save.png" class="image-save" @click="save" />
    <div v-for="po in this.$store.state.raw_material.all_po_selected" :key="po">
      <!-- Head Page -->
      <div class="row head-page">
        <!-- Left -->
        <div class="col-6 w-100" style="margin-left: 30px">
          <!-- Supplier -->
          <div class="col-12 w-100 line-col">
            Supplier&nbsp;&nbsp;:&nbsp;{{ po.supplier.company_name }}
          </div>
        </div>
        <!-- Right -->
        <div class="col-6 w-100" style="margin-right: 30px">
          <!-- Payment -->
          <div class="col-12 w-100 line-col">
            Payment&nbsp;:&nbsp;
            <select
              v-model="
                this.$store.state.raw_material.all_receipt[
                  this.$store.state.raw_material.all_po_selected.indexOf(po)
                ].payment
              "
              class="input-payment"
            >
              <option value="" selected disabled style="color: white">
                payment
              </option>
              <option
                v-for="payment in payments"
                :key="payment.id"
                :value="payment.payment"
              >
                {{ payment.payment }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <!-- Table -->
      <div class="table">
        <!-- Table Header -->
        <div class="table-header">
          <div
            class="row"
            style="
              color: white;
              text-align: left;
              margin-top: 10px;
            "
          >
            <div class="col-6 w-100" style="padding-left: 30px">Name</div>
            <div class="col-1 w-100">Qty</div>
            <div class="col-1 w-100">Unit</div>
            <div class="col-2 w-100" style="text-align: center">Price</div>
            <div class="col-2 w-100" style="margin-left: -10px">Amount</div>
          </div>
        </div>
        <!-- Table Item loop -->
        <div
          class="row table-item"
          style="margin-left: 0px; line-height: 20px;"
          v-for="recept_detail in po.recept_detail"
          :key="recept_detail"
        >
          <div
            class="col-6 w-100 line-item"
            style="padding-left: 30px; text-align: left; white-space: nowrap; overflow-x:auto;"
          >
            {{ recept_detail.raw_material_set.name }}
          </div>
          <div class="col-1 w-100 line-item" style="margin-left: -5px">
            {{ recept_detail.raw_material_set.must_buy }}
          </div>
          <div class="col-1 w-100 line-item" style="margin-right: -10px">
            {{ recept_detail.unit_set.unit }}
          </div>
          <div
            class="col-2 w-100 line-item"
            style="text-align: center; margin-left: 10px"
          >
            {{ recept_detail.last_price }}
          </div>
          <div class="col-2 w-100 line-item">{{ calc(recept_detail) }}</div>
        </div>
        <!-- Discount -->
        <div class="row table-item" style="margin-left: 0px; line-height: 20px;">
          <div class="col-12 w-100" style="margin-top: 10px">
            Discount&nbsp;<span style="width: 200px">{{
              po.recept_detail[0].discount
            }}</span
            >&nbsp;บาท/%
          </div>
        </div>
        <!-- Total Price -->
        <div class="row table-item" style="margin-left: 0px; line-height: 20px;">
          <div class="col-12 w-100" style="margin-top: 10px">
            Total Price&nbsp;<span style="width: 200px">{{
              calc_total_price(po)
            }}</span
            >&nbsp;บาท
          </div>
        </div>
      </div>
      <hr style="background-color: white; height: 5px" />
    </div>
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import { api_raw_material } from "../../api/api_raw_material";
import SavePopup from "../../components/main_component/SavePopup.vue"
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";
import Table from "../../components/main_component/Table.vue";
import CheckBoxWhite from "../../components/main_component/CheckBoxWhite.vue";

export default {
  components: {
    SavePopup,
    SearchBar,
    NavApp,
    Table,
    CheckBoxWhite,
  },
  mounted() {
    api_raw_material.get("category").then((response) => {
      console.log(response.data, "categories");
      this.categories = response.data;
    });
    api_raw_material.get("unit").then((response) => {
      this.all_unit = response.data;
    });
    api_raw_material.get("raw-material/").then((response) => {
      this.all_raw_material = response.data;
    });
    console.log(this.$store.state.raw_material.all_receipt, "all receipt");
    console.log(
      this.$store.state.raw_material.all_po_selected,
      "all_po_selected"
    );
    console.log(
      this.$store.state.raw_material.all_receipt_detail,
      "all receipt detail"
    );
  },

  data() {
    return {
      alert: false,
      all_raw_material: [],
      all_unit: [],
      categories: [],
      payments: [
        { id: 1, payment: "cash" },
        { id: 2, payment: "transfer" },
      ],
      payment_id: null,
    };
  },
  methods: {
    calc(item) {
      item.total_price = item.last_price * item.raw_material_set.must_buy;
      return item.total_price;
    },
    calc_total_price(item) {
      var sum = 0;
      item.recept_detail.forEach((el) => {
        sum += el.total_price;
      });
      item.total_price = sum;
      return sum;
    },
    select_payment(item) {
      console.log(item);
    },
    async save() {
      if (this.$store.state.raw_material.all_receipt.some(item => item.payment != null)) {
        this.$store.state.raw_material.all_receipt.forEach((receipt) => {
          api_raw_material.post("/receipt/", receipt).then((res) => {
            console.log(res.data, "receipt data");
            this.$store.state.raw_material.all_receipt_detail.forEach((receipt_detail) => {
                if (res.data.supplier_id == receipt_detail.supplier_id) {
                  receipt_detail.receipt_raw_material_id = res.data.id;
                  setTimeout(() => {
                    api_raw_material.post("/receipt-detail/", receipt_detail).then((res) => {
                      this.alert = true
                      setTimeout(() => {
                        this.alert = false
                        this.$router.push({ name: "Promotion"})
                      }, 2000)
                      console.log(res.data, 'receipt_detail');
                    });
                  }, 1000)
                }
              }
            );
          });
        });
      } else {
        alert('Warning')
      }
      
    },
  },
  computed: {},
};
</script>

<style scoped>
.image-save {
  position: absolute;
  top: 20px;
  right: 25px;
}
.line-item {
  margin-top: 10px;
}
.line-col {
  text-align: left;
}
.input-payment {
  width: 162px;
  height: 36px;
  background: #717171;
  border-radius: 10px;
}
.head-page {
  width: 672px;
  margin-left: 15px;
  font-size: 28px;
  color: white;
}
</style>