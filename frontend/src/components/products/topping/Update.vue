<template>
  <!-- Create Category Modal -->
  <div
    class="modal fade"
    id="UpdateTopping"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Update Topping</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit="save_topping()">
            <div class="alert alert-danger" role="alert" v-if="err.status">
              {{ err.data }}
            </div>

            <div class="col-12">
              <div class="row">
                <label
                  for="product_name"
                  class="col-form-label col-sm-2 text-uppercase"
                  >PRODUCT NAME</label
                >

                <div class="col-sm-10">
                  <input
                    v-model="form.name"
                    type="text"
                    class="form-control"
                    id="product_name"
                  />
                </div>
              </div>
            </div>

            <!-- code -->
            <div class="col-12 mt-2 mb-2">
              <div class="row">
                <label for="code" class="col-form-label col-sm-2 text-uppercase"
                  >CODE</label
                >
                <div class="col-sm-10">
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
            <h5>Price For Sale Channel</h5>
            <div class="col-12 mb-2">
              <div class="row">
                <div
                  class="col-4"
                  v-for="item in price_topping"
                  :key="item"
                >
                  <div class="row">
                    <label
                      for="sale_channel_id"
                      class="col-form-label col-sm-6 text-uppercase"
                      >{{ item.sale_channel.sale_channel }}</label
                    >

                    <div class="col-sm-6">
                      <input
                        class="form-control"
                        v-model="item.price"
                        type="nmber"
                        placeholder="price"
                        id="sale_channel_id"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <button
              type="submit"
              data-bs-dismiss="modal"
              class="btn btn-primary"
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
  name: "UpdateCategory",
  computed: mapState(["auth", "product"]),
  props: ["get_topping"],
  data() {
    return {
      price_topping: [],
      form: {
        name: "",
        img: null,
        code: "",
      },
      err: {
        status: false,
        data: "",
      },
    };
  },
  methods: {
    save_topping() {
      if (this.form.img != null) {
        const f = this.form;
        const fb = new FormData();
        fb.append("name", f.product_name);
        fb.append("img", f.img, f.img.name);
        fb.append("code", f.code);
        fb.append("create_by", this.$store.state.auth.userInfo.id);
        fb.append("update_by", this.$store.state.auth.userInfo.id);
        axios
          .put("http://127.0.0.1:8000/product/topping/", fb)
          .then((response) => {
            for (const sale_channel of this.price_topping) {
              if (sale_channel.price != null) {
                const sc = new FormData();
                sc.append("topping_id", response.data["id"]);
                sc.append("price", sale_channel.price);
                sc.append("sale_channel_id", sale_channel.id);
                sc.append("update_by", this.$store.state.auth.userInfo.id);
                axios.post("http://127.0.0.1:8000/product/price-topping/", sc);
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
      this.form.img = e.target.files[0];
      console.log(this.form.img.name);
    },
  },
  watch: {
    get_topping(newTopping) {
      this.form.name = newTopping.name;
      this.form.code = newTopping.code;
      this.price_topping = newTopping.price_topping;
    },
  },
};
</script>

<style>
</style>