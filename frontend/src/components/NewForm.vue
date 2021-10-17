<template>
  <div class="input-group mb-3">
    <button
      class="btn btn-secondary dropdown-toggle"
      type="button"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      Query Data
    </button>
    <ul class="dropdown-menu">
      <li v-for="data in qury" :key="data.id">
        <a class="dropdown-item" @click="change_input(data[query_name])">
          <div class="row">
            <div class="col-10 text-start">
              <span>{{ data[query_name] }}</span>
            </div>
            <div class="col-2 text-end">
              <span @click="delete_query(data.id)"
                ><i class="bi bi-x-lg"></i
              ></span>
            </div>
          </div>
        </a>
      </li>
    </ul>
    <input
      type="text"
      class="form-control"
      aria-label="Text input with dropdown button"
    />
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";
export default {
  props: ["query", "query_name", "delete_path",'models'],
  compute: mapState(["auth"]),
  data() {
    return {
      input: "",
    };
  },
  methods: {
    change_input(data) {
      this.input = data;
    },
    delete_query(id) {
      const config = {
        headers: { Authorization: `Bearer ${this.$store.state.auth.accessToken}` },
      };
      axios
        .delete(
          "http://127.0.0.1:8000/" + this.path_models + "/" + id + "/",
          config
        )
        .then(() => {
          this.$store.dispatch("refreshQueryModels", { models: this.models });
        });
    },
  },
};
</script>

<style>
</style>