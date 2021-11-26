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
          <h5 class="modal-title ms-3" id="create_product">Create Product</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form class="row g-3" @submit="create_product()">
            <div class="alert alert-danger" role="alert" v-if="err.status">
              {{ err.data }}
            </div>
            <div class="col-md-8">
              <div class="row">
                <label
                  for="product_name"
                  class="col-form-label col-sm-3 text-uppercase"
                  >PRODUCT NAME</label
                >

                <div class="col-sm-9">
                  <input
                    v-model="form.product_name"
                    type="text"
                    class="form-control"
                    id="product_name"
                  />
                </div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="row">
                <label for="code" class="col-form-label col-sm-4 text-uppercase"
                  >CODE</label
                >
                <div class="col-sm-8">
                  <input
                    v-model="form.code"
                    type="text"
                    class="form-control"
                    id="code"
                  />
                </div>
              </div>
            </div>

            <div class="col-12">
              <div class="row">
                <label
                  for="category"
                  class="col-form-label col-sm-2 text-uppercase"
                  >Category</label
                >
                <div class="col-sm-10">
                  <select
                    id="category"
                    v-model="form.category"
                    class="form-select"
                  >
                    <option
                      v-for="category in categories"
                      :key="category.id"
                      :value="category.id"
                    >
                      {{ category.category }}
                    </option>
                  </select>
                </div>
              </div>
            </div>

            <div class="col-12">
              <div class="row">
                <label
                  for="topping_set"
                  class="col-form-label col-sm-2 text-uppercase"
                  >Topping Set</label
                >
                <div class="col-sm-10">
                  <select
                    id="topping_set"
                    v-model="form.type_topping"
                    class="form-select"
                  >
                    <option
                      v-for="item in type_topping"
                      :key="item.id"
                      :value="item.id"
                    >
                      {{ item.type_topping }}
                    </option>
                  </select>
                </div>
              </div>
            </div>

            <div class="col-12">
              <div class="row">
                <label
                  for="formFileLg"
                  class="col-form-label col-sm-2 text-uppercase"
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

            <hr />

            <h5>Price For Each Sale Channel</h5>
            <div class="col-12">
              <div class="row">
                <div
                  class="col-6"
                  v-for="sale_channel in sale_channels"
                  :key="sale_channel"
                >
                  <div class="row">
                    <label
                      :for="sale_channel.id"
                      class="col-form-label col-sm-4 text-uppercase"
                      >{{ sale_channel.sale_channel }}</label
                    >

                    <div class="col-sm-8">
                      <input
                        class="form-control"
                        v-model="sale_channel.price"
                        type="nmber"
                        placeholder="price"
                        :id="sale_channel.id"
                        @change="onFileChange"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-12 d-grid gap-2">
              <button
                type="submit"
                data-bs-dismiss="modal"
                class="btn btn-primary"
              >
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
      categories: [],
      type_topping: [],
      sale_channels: [],
      form: {
        img: null,
        category: "",
        type_topping: "",
        product_name: "",
        code: "",
      },
      err: {
        status: false,
        data: "",
      },
    };
  },
  methods: {
    create_product() {
      if (this.form.img != null) {
        const f = this.form;
        const fb = new FormData();
        fb.append("category_id", f.category);
        fb.append("type_topping_id", f.type_topping);
        fb.append("name", f.product_name);
        fb.append("img", f.img, f.img.name);
        fb.append("code", f.code);
        fb.append("create_by", this.$store.state.auth.userInfo.id);
        fb.append("update_by", this.$store.state.auth.userInfo.id);
        axios
          .post("http://127.0.0.1:8000/product/product/", fb)
          .then((response) => {
            for (const sale_channel of this.sale_channels) {
              if (sale_channel.price != null) {
                const sc = new FormData();
                sc.append("product", response.data["id"]);
                sc.append("price", sale_channel.price);
                sc.append("sale_channel_id", sale_channel.id);
                sc.append("create_by", this.$store.state.auth.userInfo.id);
                sc.append("update_by", this.$store.state.auth.userInfo.id);
                axios.post("http://127.0.0.1:8000/product/price-product/", sc);
              } else {
                this.err.status = true;
                this.err.data = "price is require";
              }
            }
            this.$emit("reload");
            this.err.status = false;
            this.clearForm;
          })
          .catch((err) => {
            this.err.status = true;
            this.err.data = err.response.data;
            this.clearForm();
          });
      } else {
        this.err.status = true;
        this.err.data = "your image is require";
      }
    },
    onFileChange(e) {
      if (this.form.img == null) {
        this.form.img = e.target.files[0];
      }
    },
    clearForm() {
      this.form = {
        img: null,
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
    axios.get("http://127.0.0.1:8000/product/category/").then((response) => {
      this.categories = response.data;
    });
    axios
      .get("http://127.0.0.1:8000/product/type-topping/")
      .then((response) => {
        this.type_topping = response.data;
      });
    axios
      .get("http://127.0.0.1:8000/product/sale-channel/")
      .then((response) => {
        this.sale_channels = response.data;
      });
  },
};
</script>

<style>
</style>