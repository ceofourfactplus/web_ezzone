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
          <h5 class="modal-title" id="create_product">Create Sale Channel</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form class="row g-3" @submit="create_sale_channel()">
            <div class="col-md">
              <div class="row m-1">
                <label for="sale_channel" class="form-label col-sm-3"
                  >Sale Channel Name</label
                >
                <div class="col-sm-5">
                  <input
                    v-model="form.sale_channel"
                    type="text"
                    placeholder="sale channel name"
                    class="form-control"
                    id="sale_channel"
                  />
                </div>
                <!-- <div class="col-sm-4">
                  <Switch :value="form.status" :object="form" @input="Switch" />
                </div> -->
              </div>
            </div>
            <div class="row mt-1">
              <hr class="m-3 mt-1" />
              <h5 class="text-center">Product Price</h5>
            </div>
            <div class="row">
              <div
                class="col"
                v-for="product in form.products"
                :key="product.id"
              >
                <div class="row">
                  <label :for="product.id" class="col-sm-4 col-form-label">{{
                    product.name
                  }}</label>

                  <div class="col-sm-8">
                    <input
                      type="number"
                      v-model="product.price"
                      placeholder="Price"
                      class="form-control"
                      :id="product.id"
                    />
                  </div>
                </div>
              </div>
            </div>

            <div class="row mt-1">
              <hr class="m-3 mt-1" />
              <h5 class="text-center">Topping Price</h5>
            </div>

            <div class="row">
              <div
                class="col"
                v-for="topping in form.toppings"
                :key="topping.id"
              >
                <div class="row">
                  <label :for="topping.id" class="col-sm-4 col-form-label">{{
                    topping.name
                  }}</label>

                  <div class="col-sm-8">
                    <input
                      type="number"
                      v-model="topping.price"
                      placeholder="Price"
                      class="form-control"
                      :id="topping.id"
                    />
                  </div>
                </div>
              </div>
            </div>

            <div class="col">
              <hr class="m-3" />
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
// import Switch from "../switch.vue";

export default {
  // components: { Switch },
  name: "SaleChannelCreate",
  computed: mapState(["auth", "product"]),
  data() {
    return {
      form: {
        sale_channel: "",
        products: [],
        toppings: [],
      },
      err: false,
    };
  },
  methods: {
    async create_sale_channel() {
      const f = this.form;
      const fb = new FormData();
      fb.append("sale_channel", f.sale_channel);
      fb.append("create_by", this.$store.state.auth.userInfo.id);
      fb.append("update_by", this.$store.state.auth.userInfo.id);
      axios
        .post("http://127.0.0.1:8000/product/sale-channel/", fb)
        .then((response) => {
          this.categories = response.data;
          console.log("1");
          for (const item of f.product) {
            setTimeout(() => {
              const form = new FormData();
              form.append("price", item.price);
              form.append("product", item.id);
              form.append("sale_channel_id", response.data.id);
              form.append("status", item.status);
              form.append("create_by", this.$store.state.auth.userInfo.id);
              form.append("update_by", this.$store.state.auth.userInfo.id);

              axios.post("http://127.0.0.1:8000/product/price-product/", form);
            }, 1000);
          }
          for (const item of f.topping) {
            setTimeout(() => {
              const form = new FormData();
              form.append("price", item.price);
              form.append("topping_id", item.id);
              form.append("sale_channel_id", response.data.id);
              form.append("status", item.status);
              form.append("create_by", this.$store.state.auth.userInfo.id);
              form.append("update_by", this.$store.state.auth.userInfo.id);

              axios.post("http://127.0.0.1:8000/product/price-topping/", form);
            }, 1000);
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
        sale_channel: "",
        product: [],
        status: true,
      };
    },
    Switch(value, obj) {
      this.form.status = value;
      console.log(obj);
    },
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/product/product/").then((response) => {
      this.form.products = response.data;
    });
    axios.get("http://127.0.0.1:8000/product/topping/").then((response) => {
      this.form.toppings = response.data;
    });
  },
};
</script>

<style>
</style>