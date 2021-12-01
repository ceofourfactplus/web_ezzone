<template>
  <div
    class="modal fade"
    id="UpdateSaleChannel"
    tabindex="-1"
    aria-labelledby="create_product"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="create_product">Update Sale Channel</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="alert alert-danger" role="alert" v-if="err">
            some thing went wrong
          </div>
          <form class="row g-3" @submit="update_sale_channel()">
            <div class="col-8">
              <div class="row">
                <label for="sale_channel" class="form-label col-4"
                  >Sale Channel Name</label
                >
                <div class="col-8">
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
            <div class="col-4">
              <div class="row">
                <label for="exampleColorInput" class="col-7 form-label"
                  >Color picker</label
                >
                <div class="col-5">
                  <input
                    type="color"
                    v-model="form.color"
                    class="form-control form-control-color"
                    id="exampleColorInput"
                    title="Choose your color"
                    opacity
                  />
                </div>
              </div>
            </div>
            <div class="col-12">
              <div class="row">
                <label for="formFileLg" class="col-form-label col-sm-2"
                  >Images</label
                >

                <div class="col-sm-10">
                  <input
                    class="form-control"
                    id="formFileLg"
                    type="file"
                    @change="onFileChange"
                  />
                </div>
              </div>
            </div>
            <div class="row mt-1">
              <hr class="m-3 mt-1" />
              <h5 class="text-center">Product Price</h5>
            </div>
            <div class="row">
              <div
                class="col-4"
                v-for="product in form.products"
                :key="product.id"
              >
                <div class="row">
                  <label :for="product.id" class="col-sm-4 col-form-label">{{
                    product.name
                  }}</label>

                  <div
                    class="col-sm-8"
                    v-for="price in product.price"
                    :key="price"
                  >
                    <input
                      v-if="price.sale_channel_id == form.sale_channel_id"
                      type="number"
                      v-model="price.price"
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
                class="col-4"
                v-for="topping in form.toppings"
                :key="topping.id"
              >
                <div class="row">
                  <label :for="topping.id" class="col-sm-4 col-form-label">{{
                    topping.name
                  }}</label>

                  <div
                    class="col-sm-8"
                    v-for="price in topping.price_topping"
                    :key="price"
                  >
                    <input
                      v-if="price.sale_channel_id == form.sale_channel_id"
                      type="number"
                      v-model="price.price"
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
                Update Product
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
  props: ["select_sale_channel"],
  data() {
    return {
      form: {
        sale_channel_id: null,
        sale_channel: "",
        products: [],
        toppings: [],
        img: null,
        color: null,
      },
      err: false,
    };
  },
  methods: {
    onFileChange(e) {
      if (this.form.img == null) {
        this.form.img = e.target.files[0];
      }
    },
    update_sale_channel() {
      var can_save = true;
      this.form.products.forEach((element) => {
        element.sale_channel_edit = this.form.sale_channel_id;
        element.update_by = this.$store.state.auth.userInfo.id;
        element.price.forEach((price) => {
          if (price.price == "") {
            can_save = false;
            this.err = true;
          }
        });
      });
      this.form.toppings.forEach((element) => {
        element.sale_channel_edit = this.form.sale_channel_id;
        element.update_by = this.$store.state.auth.userInfo.id;
        element.price_topping.forEach((price) => {
          if (price.price == "") {
            can_save = false;
            this.err = true;
          }
        });
      });

      console.log("1");
      if (this.form.sale_channel != "" && can_save && this.form.img != null) {
        console.log("2");
        const f = this.form;
        const fb = new FormData();
        fb.append("sale_channel", f.sale_channel);
        fb.append("img", f.img, f.img.name);
        fb.append("color", f.color + "ff");
        fb.append("create_by", this.$store.state.auth.userInfo.id);
        fb.append("update_by", this.$store.state.auth.userInfo.id);
        axios
          .put("http://127.0.0.1:8000/product/sale-channel/" + f.sale_channel_id + "/", fb)
          .then(() => {
            axios.put(
              "http://127.0.0.1:8000/product/many-price-product/",
              f.products
            );
            axios.put(
              "http://127.0.0.1:8000/product/many-price-topping/",
              f.toppings
            );
            this.$emit("reload");
          })
          .catch(() => {
            this.err = true;
          });
      } else {
        this.err = true;
      }
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
  watch: {
    select_sale_channel(newData) {
      this.form.sale_channel_id = newData.id;
      this.form.sale_channel = newData.sale_channel;
      this.form.color = newData.color.slice(0, 7);
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