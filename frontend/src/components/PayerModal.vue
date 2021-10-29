<template>
  <div
    class="modal fade"
    id="payer"
    tabindex="-1"
    aria-labelledby="payer-label"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="payer-label">Create Payer</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
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
          <div class="row">
            <div class="col-md">
              <div class="form-floating mb-3">
                <input
                  type="text"
                  class="form-control"
                  placeholder="name@example.com"
                  v-model="name"
                />
                <label for="name">Name</label>
              </div>
            </div>
          </div>
          <div class="row mb-2">
            <div class="col-md">
              <div class="form-floating">
                <select
                  class="form-select"
                  id="floatingSelect"
                  v-model="gender"
                  aria-label="Floating label select example"
                >
                  <option selected disabled>select gender</option>
                  <option value="female">female</option>
                  <option value="male">male</option>
                </select>
                <label for="floatingSelect">Gender</label>
              </div>
            </div>
          </div>
          <div class="row m-1">
            <button class="btn-block btn btn-primary" @click="createPayer()">
              Create Payer
            </button>
          </div>
          <div style="overflow-y: auto; height: 20vw">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">unit</th>
                  <th scope="col">gender</th>
                  <th scope="col">delete</th>
                </tr>
              </thead>
              <tbody style="height: 20vw">
                <tr
                  v-for="(item, index) in $store.state.payer_data"
                  :key="item.id"
                >
                  <th>{{ index + 1 }}</th>
                  <td>{{ item.name }}</td>
                  <td>{{ item.gender }}</td>
                  <td>
                    <button
                      class="btn btn-danger btn-sm"
                      @click="deletePayer(item.id)"
                    >
                      delete
                      <h2 style="color: #dc3545;">how are you </h2> 
                        
                     
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
            data-bs-dismiss="modal"
            class="btn btn-secondary"
          >
            Close
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
  data() {
    return {
      error: false,
      name: "",
      gender: "",
    };
  },
  computed: mapState(["auth"]),
  methods: {
    createPayer() {
      if (this.name != "" && this.gender != "") {
        this.error = false;
        const config = {
          headers: { Authorization: `Bearer ${this.$store.state.auth.accessToken}` },
        };
        const data = {
          name: this.name,
          gender: this.gender,
        };
        apiStock.post("payer/", data, config).then(() => {
          this.$store.dispatch("refreshModels", { models: "payer" });
        });
        this.name = "";
        this.gender = "";
      } else {
        this.error = true;
      }
    },
    deletePayer(id) {
      const config = {
        headers: { Authorization: `Bearer ${this.$store.state.auth.accessToken}` },
      };
      apiStock.delete("payer/" + id + "/", config).then(() => {
        this.$store.dispatch("refreshModels", { models: "payer" });
      });
    },
  },
};
</script>

<style>
</style>