 <template>
  <div
    class="modal fade"
    id="UpdateTypeTopping"
    tabindex="-1"
    aria-labelledby="update_type_topping"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="update_type_topping">
            Update Type Topping
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form class="row g-3" @submit="update_type_topping()">
            <div class="col">
              <div class="row">
                <label for="product_name" class="form-label col-3"
                  >Type Topping</label
                >
                <div class="col-9">
                  <input
                    v-model="form.type_topping"
                    type="text"
                    class="form-control"
                    id="product_name"
                  />
                </div>
              </div>
            </div>
            <hr />
            <h5>Select Topping</h5>
            <div class="col-12">
              <div class="row">
                <div
                  class="col-3"
                  v-for="topping in toppings"
                  :key="topping.id"
                >
                  <div class="form-check">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      v-model="form.topping"
                      :value="{ topping_id: topping.id, table_id: null }"
                      :id="topping.id"
                    />
                    <label class="form-check-label" :for="topping.id">
                      {{ topping.name }}
                    </label>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-12">
              <button type="submit" class="btn btn-primary">
                Create Product
              </button>
            </div>
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
  name: "UpdateTypeTopping",
  computed: mapState(["auth", "product"]),
  props: ["select_type_topping"],
  data() {
    return {
      toppings: [],
      old_topping: [],
      form: {
        topping: [],
      },
      err: {
        status: false,
        data: "",
      },
    };
  },
  methods: {
    update_type_topping() {
      for (const old of this.old_topping) {
        if (
          this.form.topping.find((item) => {
            item.topping_id == old.topping_id;
          }) != undefined
        ) {
          const index = this.form.topping.findIndex((item) => {
            item.topping_id == old.topping_id;
          });
          this.form.topping.splice(index, index + 1);
        } else {
          axios.delete(
            "http://127.0.0.1:8000/product/table-topping/" + old.table_id + "/"
          );
        }
      }
      const f = this.form;
      const fb = new FormData();
      fb.append("type_topping", f.type_topping);
      fb.append("create_by", this.$store.state.auth.userInfo.id);
      fb.append("update_by", this.$store.state.auth.userInfo.id);
      axios
        .put("http://127.0.0.1:8000/product/type-topping/" + f.id + "/", fb)
        .then((response) => {
          for (const topping of f.topping) {
            axios.post("http://127.0.0.1:8000/product/table-topping/", {
              type_topping_id: response.data.id,
              topping_id: topping.topping_id,
              create_by: this.$store.state.auth.userInfo.id,
              update_by: this.$store.state.auth.userInfo.id,
            });
          }
          this.$emit("reload");
          this.clearForm();
        })
        .catch((error) => {
          this.err.status = true;
          this.err.data = error.response.data;
        });
    },
    clearForm() {
      this.form = {
        topping: [],
      };
      this.old_topping = [];
    },
  },
  watch: {
    select_type_topping(newData) {
      this.clearForm();
      const f = this.form;
      f.type_topping = newData.type_topping;
      f.id = newData.id;
      f.create_by = newData.create_by;
      f.update_by = newData.update_by;
      for (const tabletopping of newData.tabletopping_set) {
        f.topping.push({
          topping_id: tabletopping.topping_id,
          table_id: null,
        });
        this.old_topping.push({
          topping_id: tabletopping.topping_id,
          table_id: tabletopping.id,
        });
      }
    },
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/product/topping/").then((response) => {
      this.toppings = response.data;
    });
  },
};
</script>

<style>
</style>