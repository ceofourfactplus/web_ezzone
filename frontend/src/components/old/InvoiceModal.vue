<template>
  <div
    class="modal fade"
    id="add-invoice"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="invoice-label"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-xl">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="invoice-label">Create Invoice</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>

        <div class="modal-body">
          <div class="row g-2">
            <!-- supplier -->
            <div class="col-md">
              <div class="form-floating">
                <select
                  class="form-select"
                  v-model="Invoice.supplier_id"
                  id="supplier"
                >
                  <option selected>Supplier</option>
                  <option
                    v-for="item in $store.state.supplier_data"
                    :key="item.id"
                    :value="item.id"
                  >
                    {{ item.com_name }}
                  </option>
                </select>
                <label for="supplier">Supplier</label>
              </div>
            </div>
            <!-- payer -->
            <div class="col-md">
              <div class="form-floating">
                <select
                  class="form-select"
                  v-model="Invoice.payer_id"
                  id="supplier"
                >
                  <option selected>Payer</option>
                  <option
                    v-for="payer in $store.state.payer_data"
                    :key="payer.id"
                    :value="payer.id"
                  >
                    {{ payer.name }}
                  </option>
                </select>
                <label for="supplier">Payer</label>
              </div>
            </div>
            <!-- payment -->
            <div class="col-md mb-3">
              <div class="form-floating">
                <select
                  class="form-select"
                  v-model="Invoice.payment"
                  id="supplier"
                >
                  <option selected>Payment</option>
                  <option value="cash">Cash</option>
                  <option value="tranceform">Trancefer</option>
                </select>
                <label for="supplier">Payment</label>
              </div>
            </div>
          </div>
          <!-- error -->
          <div class="row g-3">
            <div class="col">
              <div id="error" v-show="error">
                <svg xmlns="http://www.w3.org/2000/svg" style="display: none">
                  <symbol
                    id="exclamation-triangle-fill"
                    fill="currentColor"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"
                    />
                  </symbol>
                </svg>
                <div
                  class="
                    alert alert-danger
                    d-flex
                    align-items-center
                    text-center
                  "
                  role="alert"
                >
                  <svg
                    class="bi flex-shrink-0 me-2"
                    width="24"
                    height="24"
                    role="img"
                    aria-label="Danger:"
                  >
                    <use xlink:href="#exclamation-triangle-fill" />
                  </svg>
                  <div>your username have already</div>
                </div>
              </div>
            </div>
          </div>
          <!-- table -->
          <table class="table table-bordered border border-4 rounded">
            <!-- form -->
            <thead>
              <tr>
                <th>
                  <div class="form-floating">
                    <select
                      id="stock"
                      class="form-select"
                      aria-label="create inventory"
                      v-model="newInvoice.stock"
                      placeholder="stock"
                      required
                    >
                      <option
                        v-for="stock in $store.state.stock_data"
                        :key="stock.id"
                        :value="stock"
                      >
                        {{ stock.name }}
                      </option>
                    </select>
                    <label for="stock">Stock</label>
                  </div>
                </th>
                <th colspan="2">
                  <div class="form-floating">
                    <input
                      id="price-sub"
                      class="form-control"
                      type="number"
                      v-model="newInvoice.price"
                      placeholder="Price"
                      required
                    />
                    <label for="price-sub">Price</label>
                  </div>
                </th>
                <th>
                  <div class="form-floating">
                    <input
                      class="form-control"
                      type="number"
                      v-model="newInvoice.amount"
                      placeholder="Amount"
                      id="amount"
                      required
                    />
                    <label for="amount">Amount</label>
                  </div>
                </th>
                <th>
                  <div class="form-floating">
                    <input
                      class="form-control"
                      type="number"
                      placeholder="Discount"
                      id="discount"
                      v-model="newInvoice.discount"
                    />
                    <label for="discount">Discount</label>
                  </div>
                </th>
                <th>
                  <div class="form-floating">
                    <input
                      id="remark"
                      class="form-control"
                      type="text"
                      placeholder="remark"
                      v-model="newInvoice.remark"
                    />
                    <label for="remark">Remark</label>
                  </div>
                </th>
                <th>
                  <button class="btn btn-danger" @click="addInvoiceDetail()">
                    Add
                  </button>
                </th>
              </tr>
              <tr>
                <th>Stock</th>
                <th>price</th>
                <th>amount</th>
                <th>discount</th>
                <th>total price</th>
                <th>remark</th>
                <th>delete</th>
              </tr>
            </thead>
            <!-- data -->
            <tbody style="height: 20vw; overflow: scroll">
              <tr v-for="item in Invoice.detail" :key="item.id">
                <td>{{ item.stock.name }}</td>
                <td>{{ item.price }}</td>
                <td>{{ item.amount }}</td>
                <td>{{ item.discount }}</td>
                <td>{{ item.total_price }}</td>
                <td>{{ item.remark }}</td>
                <td><button class="btn btn-danger">delete</button></td>
              </tr>
            </tbody>
            <!-- total -->
            <tfoot>
              <tr>
                <td colspan="3"></td>
                <th>total amount :{{ Invoice.total_amount }}</th>
                <th>total price :{{ Invoice.total_price }}</th>
                <td></td>
              </tr>
            </tfoot>
          </table>
        </div>

        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-primary"
            @click="createInvoice()"
            data-bs-dismiss="modal"
          >
            Save
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { apiStock } from "../api/ApiStock";

export default {
  name: "InvoiceModal",
  data() {
    return {
      isEdit: false,
      newInvoice: {
        stock: 0,
        price: null,
        total_price: null,
        discount: 0,
        amount: null,
        remark: "",
      },
      Invoice: {
        detail: [],
        supplier_id: 0,
        payer_id: 0,
        payment: 0,
        total_price: 0,
        total_amount: 0,
      },
      error: false,
    };
  },
  computed: mapState([
    "auth",
    "supplier_data",
    "payer_data",
  ]),
  methods: {
    addInvoiceDetail() {
      const n = this.newInvoice;
      if (n.price != null && n.amount != null && n.stock != null) {
        n.total_price = n.price * n.amount - n.discount;

        const clone = Object.assign({}, n);
        this.Invoice.detail.push(clone);

        this.error = false;
        n.price = null;
        n.amount = null;
        n.stock = null;
        n.total_price = null;
        n.discount = null;
        this.calculateTotal();
      } else {
        this.error = true;
      }
    },
    calculateTotal() {
      for (const item of this.Invoice.detail) {
        this.Invoice.total_price = item.total_price;
        this.Invoice.total_amount = item.amount;
      }
    },
    createInvoice() {
      if (
        (this.Invoice.supplier_id != null,
        this.Invoice.payer_id != null,
        this.Invoice.payment != null,
        this.Invoice.total_amount != 0,
        this.Invoice.detail.length != 0)
      ) {
        const config = {
          headers: { Authorization: `Bearer ${this.$store.state.auth.accessToken}` },
        };
        const data = {
          supplier_id: this.Invoice.supplier_id,
          payer_id: this.Invoice.payer_id,
          payment: this.Invoice.payment,
          total_price: this.Invoice.total_price,
          total_amount: this.Invoice.total_amount,
          create_by_id: this.$store.state.auth.userInfo.id,
          update_by_id: this.$store.state.auth.userInfo.id,
        };
        apiStock.post("invoice/", data, config).then((response) => {
          console.log(response.data.id);
          for (const detail of this.Invoice.detail) {
            const data_detail = {
              invoice_id: response.data.id,
              stock_id: detail.stock.id,
              price: detail.price,
              total_price: detail.total_price,
              avg_price: detail.price,
              amount: detail.amount,
              remark: detail.remark,
              discount: detail.discount,
              create_by_id: this.$store.state.auth.userInfo.id,
              update_by_id: this.$store.state.auth.userInfo.id,
            };
            apiStock.post("invoice-detail/", data_detail, config);
          }
          this.Invoice.supplier_id = null;
          this.Invoice.payer_id = null;
          this.Invoice.payment = null;
          this.Invoice.total_amount = 0;
          this.error = false;
          this.Invoice.total_price = 0;
          this.$store.dispatch("refreshModels", { models: "stock" });
        });
      }
    },
  },
};
</script>

<style>
</style>