<template>
  <!-- Create Category Modal -->
  <div
    class="modal fade"
    id="createModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Create SaleChannel</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit="save_category()">
            <div class="alert alert-danger" v-show="err" role="alert">
              this caetgory name is already in use
            </div>
            <div class="mb-3">
              <label for="Category" class="form-label">Category</label>
              <input
                type="text"
                class="form-control"
                v-model="category"
                id="Category"
                placeholder="Drink"
              />
            </div>
            <button
              type="submit"
              class="btn btn-primary"
              data-bs-dismiss="modal"
              style="width: 100%"
            >
              save
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

export default {
  name: "CategoryCreate",
  computed: mapState(["auth", "product"]),
  data() {
    return {
      category: "",
      err: false,
    };
  },
  methods: {
    save_category() {
      axios
        .post("http://127.0.0.1:8000/product/category/", {
          category: this.category,
          create_by: this.$store.state.auth.userInfo.id,
          update_by: this.$store.state.auth.userInfo.id,
        })
        .then((response) => {
          this.$store.state.product.category = response.data;
          this.$emit("reload");
          this.category = "";
          // myModal.hide();
        })
        .catch(() => {
          this.err = true;
          // var myModal = new bootstrap.Modal(
          //   document.getElementById("createModal")
          // );
          // myModal.show();
        });
    },
  },
  watch: {
    category() {
      this.err = false;
    },
  },
};
</script>

<style>
</style>