<template>
  <div
    class="modal fade"
    id="add-supplier"
    tabindex="-1"
    aria-labelledby="supplier-label"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="supplier-label">Add Supplier</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <!-- company neme -->
          <div class="mb-3 row">
            <!-- company name -->
            <div class="col-md">
              <div class="form-floating">
                <input
                  type="text"
                  class="form-control"
                  id="company_name"
                  placeholder=" "
                  v-model="company"
                />
                <label for="company_name">Company Name</label>
              </div>
            </div>
          </div>
          <!-- contact phone -->
          <div class="mb-3 row">
            <!-- contact name -->
            <div class="col-md">
              <div class="form-floating">
                <input
                  type="text"
                  class="form-control"
                  id="contact_name"
                  placeholder=" "
                  v-model="contact"
                />
                <label for="contact_name">Contact Name</label>
              </div>
            </div>

            <!-- Phone Number -->
            <div class="col-md">
              <div class="form-floating">
                <input
                  type="number"
                  class="form-control"
                  id="phone_number"
                  placeholder=" "
                  v-model="phone"
                />
                <label for="phone_number">Phone Number</label>
              </div>
            </div>
          </div>
          <!-- address discriptions -->
          <div class="mb-2 row">
            <div class="col-md">
              <div class="form-floating">
                <textarea
                  class="form-control"
                  placeholder="Leave a comment here"
                  id="address"
                  style="height: 100px"
                  v-model="address"
                ></textarea>
                <label for="address">Address</label>
              </div>
            </div>
            <div class="col-md mb-3">
              <div class="form-floating">
                <textarea
                  class="form-control"
                  placeholder="Leave a comment here"
                  id="descriptions"
                  style="height: 100px"
                  v-model="descriptions"
                ></textarea>
                <label for="descriptions">Descriptions</label>
              </div>
            </div>
            <!-- error -->
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
                <div>please write the form properly</div>
              </div>
            </div>
          </div>
          <div class="row m-1">
            <button
              type="button"
              class="btn btn-block btn-primary"
              @click="createSupplier()"
            >
              Create supplier
            </button>
          </div>

          <!-- table -->
          <div style="overflow-y: auto; height: 15vw">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">company</th>
                  <th scope="col">contact</th>
                  <th scope="col">phone number</th>
                  <th scope="col">address</th>
                  <th scope="col">descriptions</th>
                  <th scope="col">delete</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="(item, index) in $store.state.supplier_data"
                  :key="item.id"
                >
                  <th scope="row">{{ index + 1 }}</th>
                  <td scope="row">{{ item.com_name }}</td>
                  <td scope="row">{{ item.contact }}</td>
                  <td scope="row">{{ item.phone }}</td>
                  <td scope="row">{{ item.address }}</td>
                  <td v-if="item.descriptions.length != 0" scope="row">
                    {{ item.descriptions }}
                  </td>
                  <td v-else scope="row">-</td>
                  <td scope="row">
                    <button
                      class="btn btn-danger btn-sm"
                      @click="deleteSupplier(item.id)"
                    >
                      delete
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import { apiStock } from "../api/ApiStock";
export default {
  data() {
    return {
      error: false,
      company: "",
      contact: "",
      phone: "",
      address: "",
      descriptions: "",
    };
  },
  computed:mapState(['supplier_data','auth']),
  methods: {
    createSupplier() {
      if (
        this.company != "" &&
        this.contact != "" &&
        this.phone != "" &&
        this.address != ""
      ) {
        this.error = false;

        const config = {
          headers: { Authorization: `Bearer ${this.$store.state.auth.accessToken}` },
        };

        const bodyParameters = {
          com_name: this.company,
          contact: this.contact,
          phone: this.phone,
          address: this.address,
          descriptions: this.descriptions,
          create_by: this.$store.state.auth.userInfo.id,
          update_by: this.$store.state.auth.userInfo.id,
        };

        apiStock.post("supplier/", bodyParameters, config).then(() => {
          this.$store.dispatch("refreshModels", { models: "supplier" });
        });
        this.company = "";
        this.contact = "";
        this.phone = "";
        this.address = "";
        this.descriptions = "";
      } else {
        this.error = true;
      }
    },
    deleteSupplier(id) {
      const config = {
        headers: { Authorization: `Bearer ${this.$store.state.auth.accessToken}` },
      };
      apiStock.delete("supplier/" + id + "/", config).then(() => {
        this.$store.dispatch("refreshModels", { models: "supplier" });
      });
    },
  },
};
</script>

<style>
</style>