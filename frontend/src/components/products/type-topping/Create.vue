<template>
  <div
    class="modal fade"
    id="createModal"
    tabindex="-1"
    aria-labelledby="create_product"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="create_product">Create Type Topping</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form class="row g-3" @submit="create_type_topping()">
            <div class="col">
              <div class="row">
                <label for="product_name" class="form-label col-3"
                  >Type Topping</label
                >
                <div class="col-9">
                  <input
                    v-model="form.product_name"
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
                <div class="col" v-for="topping in toppings" :key="topping.id">
                  <div class="form-check">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      v-model="form.select_topping"
                      :value="topping.id"
                      :id="topping.id"
                    />
                    <label class="form-check-label" :for="topping.id">
                      {{topping.name}}
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
  name: "CategoryCreate",
  computed: mapState(["auth", "product"]),
  data() {
    return {
      toppings: [],
      form: {
        type_topping:'',
        topping:[],
      },
      err: {
        status:false,
        data:''
      },
    };
  },
  methods: {
    create_product() {
      const f = this.form;
      const fb = new FormData();
      fb.append("type_topping", f.type_topping);
      fb.append("create_by", this.$store.state.auth.userInfo.id);
      fb.append("update_by", this.$store.state.auth.userInfo.id);
      axios
        .post("http://127.0.0.1:8000/product/type-topping/", fb)
        .then((response) => {
          for(const topping of f.topping){
            axios.post("http://127.0.0.1:8000/product/table-topping/",{
              type_topping_id:response.data.id,
              topping_id:topping,
              create_by:this.$store.state.auth.userInfo.id,
              update_by:this.$store.state.auth.userInfo.id
            })
          }
          this.$emit("reload");
        })
        .catch(() => {
          this.err = true;
        });
    },
    onFileChange(e) {
      this.form.img = e.target.files[0];
      console.log(this.form.img.name);
    },
    clearForm() {
      this.form = {
        status: true,
        img: null,
        able: true,
        category: "",
        type_topping: "",
        product_name: "",
        code: "",
      };
    },
  },
  watch: {
    category() {
      this.err = false;
    },
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/product/topping/")
      .then((response) => {
        this.type_topping = response.data;
      });
  },
};
</script>

<style>
</style>