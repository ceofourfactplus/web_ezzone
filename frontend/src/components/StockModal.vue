<template>
  <div
    class="modal fade"
    id="create-stock"
    tabindex="-1"
    aria-labelledby="inventory-label"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="inventory-label">Create Stock</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>

        <div class="modal-body">
          <!-- error -->
          <div v-show="error_b">
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
              class="alert alert-danger d-flex align-items-center text-center"
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
              <div>{{ error_t }}</div>
            </div>
          </div>

          <!-- category fil -->
          <div class="row m-1">
            <div class="col">
              <div class="input-group mb-3">
                <input
                  type="text"
                  class="form-control"
                  aria-label="Text input with dropdown button"
                  placeholder="category"
                  v-model="category"
                  @input="category_input()"
                />
                <button
                  class="btn btn-secondary dropdown-toggle"
                  type="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Query Data
                </button>
                <ul class="dropdown-menu dropdown-menu-end">
                  <li v-for="data in query_category" :key="data.id">
                    <a class="dropdown-item" @click="category = data.name">
                      <div class="row">
                        <div class="col-10 text-start">
                          <span>{{ data.name }}</span>
                        </div>
                        <div class="col-2 text-end">
                          <!-- <span @click="delete_query_category(data.id)"
                            ><i class="bi bi-x-lg"></i
                          ></span> -->
                        </div>
                      </div>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <!-- code name -->

          <div class="row m-1">
            <div class="col-md">
              <div class="form-floating mb-2">
                <input
                  type="text"
                  class="form-control"
                  id="code"
                  placeholder="name@example.com"
                  v-model="code"
                />
                <label class="fw-bold" for="code">Code</label>
              </div>
            </div>
            <div class="col-md">
              <div class="form-floating mb-2">
                <input
                  type="text"
                  class="form-control"
                  id="name"
                  placeholder="name@example.com"
                  v-model="name"
                />
                <label class="fw-bold" for="name">Name</label>
              </div>
            </div>
          </div>
          <!-- balance unit min-stock -->
          <div class="row m-1 mb-2">
            <div class="col-md">
              <div class="form-floating">
                <input
                  type="text"
                  class="form-control"
                  id="balance"
                  placeholder="name@example.com"
                  v-model="balance"
                />
                <label class="fw-bold" for="name">balance</label>
              </div>
            </div>
          </div>

          <!-- unit -->
          <div class="row m-1">
            <div class="col">
              <div class="input-group mb-3">
                <input
                  type="text"
                  class="form-control"
                  aria-label="Text input with dropdown button"
                  v-model="unit"
                  placeholder="unit"
                  @input="unit_input()"
                />
                <button
                  class="btn btn-secondary dropdown-toggle"
                  type="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Query Data
                </button>
                <ul class="dropdown-menu dropdown-menu-end">
                  <li v-for="data in query_unit" :key="data.id">
                    <a class="dropdown-item" @click="unit = data.unit">
                      <div class="row">
                        <div class="col-10 text-start">
                          <span>{{ data.unit }}</span>
                        </div>
                        <div class="col-2 text-end">
                          <!-- <span @click="delete_query_unit(data.id)"
                            ><i class="bi bi-x-lg"></i
                          ></span> -->
                        </div>
                      </div>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div class="row m-1 mb-2">
            <div class="col-md">
              <div class="form-floating">
                <input
                  type="text"
                  class="form-control"
                  id="min_stock"
                  placeholder="name@example.com"
                  v-model="min_stock"
                />
                <label class="fw-bold" for="min_stock">Min stock</label>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            @click="createInventory()"
            class="btn btn-primary"
            data-bs-toggle="modal"
            data-bs-target="#checkpass"
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
  name: "StockModal",
  data() {
    return {
      error_b: false,
      error_t: "",
      code: "",
      name: "",
      balance: null,
      unit: "",
      min_stock: null,
      category: "",
      query_category: [],
      query_unit: [],
    };
  },
  computed: mapState(["auth",'modal_id']),
  mounted() {
    this.category_input();
    this.unit_input();
  },
  onIdle() {
    this.$store.dispatch("userLogout").then(() => {
      this.$router.push({ name: "Login" });
    });
  },
  methods: {
    async createInventory() {
      if (
        this.unit != null &&
        this.min_stock != null &&
        this.balance != null &&
        this.name != "" &&
        this.code != "" &&
        this.category != ""
      ) {
        this.$store.state.modal_id = 'create-stock'
        if (this.$store.state.auth.confirm_pass) {
          this.error = false;
          const config = {
            headers: {
              Authorization: `Bearer ${this.$store.state.auth.accessToken}`,
            },
          };
          const data = {
            unit: this.unit,
            minstock: this.min_stock,
            balance: this.balance,
            name: this.name,
            code: this.code,
            category: this.category,
            unit_id: 0,
            category_id: 0,
            avg_price: 0,
            min_price: 0,
            max_price: 0,
            create_by: this.$store.state.userInfo.id,
            update_by: this.$store.state.userInfo.id,
          };
          apiStock
            .post("stock/", data, config)
            .then(() => {
              this.$store.dispatch("refreshModels", { models: "stock" });
              this.unit = null;
              this.min_stock = null;
              this.balance = null;
              this.name = "";
              this.code = "";
              this.error_b = true;
            })
            .catch(() => {
              this.error_b = true;
              this.error_t = "code or name has been taked";
            });
        }
      } else {
        this.error_b = true;
        this.error_t = "please write the form properly";
      }
    },
    category_input() {
      if (this.category == "") {
        apiStock.get("category/").then((response) => {
          this.query_category = response.data;
        });
      } else {
        apiStock.get("category-fil/" + this.category).then((response) => {
          this.query_category = response.data;
        });
      }
    },
    unit_input() {
      const config = {
        headers: { Authorization: `Bearer ${this.$store.state.auth.accessToken}` },
      };
      if (this.unit == "") {
        apiStock.get("unit/", config).then((response) => {
          this.query_unit = response.data;
        });
      } else {
        apiStock.get("unit-fil/" + this.unit).then((response) => {
          this.query_unit = response.data;
        });
      }
      console.log(this.category);
    },
  },
};
</script>

<style>
</style>