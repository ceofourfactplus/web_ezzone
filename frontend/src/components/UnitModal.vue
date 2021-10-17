<template>
  <div
    class="modal fade"
    id="unit-modal"
    tabindex="-1"
    aria-labelledby="unit-label"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="unit-label">Unit</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
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
                  <div>please write the form properly</div>
                </div>
              </div>
              <table class="table">
                <tbody>
                  <tr>
                    <th colspan="2">
                      <input
                        id="unit"
                        class="form-control"
                        type="text"
                        placeholder="unit"
                        v-model="unit"
                      />
                    </th>
                    <th>
                      <button class="btn btn-primary" @click="addUnit()">
                        Add
                      </button>
                    </th>
                  </tr>
                </tbody>
              </table>
              <div style="overflow-y: auto; height: 25vw">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">unit</th>
                      <th scope="col">delete</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="(item, index) in $store.state.unit_data"
                      :key="item.id"
                    >
                      <th scope="row">{{ index+1 }}</th>
                      <td scope="row">{{ item.unit }}</td>
                      <td scope="row">
                        <button
                          class="btn btn-danger btn-sm"
                          @click="deleteUnit(item.id)"
                        >
                          delete
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
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
      unit: "",
    };
  },
  computed:mapState(['unit_data','auth']),
  methods: {
    addUnit() {
      if (this.unit != "" && this.unit.length <= 30) {
        this.error = false;
        const config = {
          headers: { Authorization: `Bearer ${this.$store.state.auth.accessToken}` },
        };
        const data = {
          unit: this.unit,
        };
        apiStock.post("unit/", data, config).then(() => {
          this.$store.dispatch("refreshModels",{models:"unit"});
        });
        this.unit = "";
      } else {
        this.error = true;
      }
    },
    deleteUnit(id) {
      const config = {
        headers: { Authorization: `Bearer ${this.$store.state.auth.accessToken}` },
      };
      apiStock.delete("unit/" + id + "/", config).then(() => {
        this.$store.dispatch("refreshModels",{models:"unit"});
      });
    },
  },
};
</script>

<style>
</style>