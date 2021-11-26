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
        <!-- header modal -->
        <div class="modal-header">
          <h5 class="modal-title" id="create_product">Create Topping</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>

        <div class="modal-body">
          <form class="row g-3" @submit="create_topping()">
            <!-- topping name -->

            <div class="alert alert-danger" role="alert" v-show="err.status">
              {{ err.massage }}
            </div>
            <div class="col-md-8">
              <div class="row">
                <label for="product_name" class="form-label col-3"
                  >topping name</label
                >
                <div class="col-9">
                  <input
                    v-model="topping_name"
                    type="text"
                    class="form-control"
                    id="product_name"
                  />
                </div>
              </div>
            </div>

            <!-- code -->
            <div class="col-md-4">
              <div class="row">
                <label for="code" class="form-label col-3">code</label>
                <div class="col-9">
                  <input
                    v-model="code"
                    type="text"
                    class="form-control"
                    id="code"
                  />
                </div>
              </div>
            </div>

            <!-- select img -->
            <div class="col-12">
              <div class="row">
                <label for="formFileLg" class="form-label col-2"
                  >image here</label
                >

                <div class="col-10">
                  <input
                    class="form-control"
                    id="formFileLg"
                    type="file"
                    @change="onFileChange"
                  />
                </div>
              </div>
            </div>

            <div class="col-12">
              <hr />
              Price For Sale Channel
              <div class="row">
                <div
                  class="col-6 mt-1"
                  v-for="sale_channel in sale_channels"
                  :key="sale_channel"
                >
                  <div class="row">
                    <label
                      :for="sale_channel.id"
                      class="col-sm-4 col-form-label"
                      >{{ sale_channel.sale_channel }}</label
                    >

                    <div class="col-sm-8">
                      <input
                        type="number"
                        v-model="sale_channel.price"
                        placeholder="Price"
                        class="form-control"
                        :id="sale_channel.id"
                      />
                    </div>
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
      sale_channels: [],
      img: null,
      topping_name: "",
      code: "",
      err: {
        status: false,
        massage: "",
      },
    };
  },
  methods: {
    create_topping() {
      const fb = new FormData();
      fb.append("name", this.topping_name);
      fb.append("img", this.img, this.img.name);
      fb.append("code", this.code);
      fb.append("create_by", this.$store.state.auth.userInfo.id);
      fb.append("update_by", this.$store.state.auth.userInfo.id);
      axios
        .post("http://127.0.0.1:8000/product/topping/", fb)
        .then((response) => {
          for (var channel of this.sale_channels) {
            const SH = new FormData();
            SH.append("topping_id", response.data.id);
            SH.append("sale_channel_id", parseInt(channel.id));
            SH.append("price", parseInt(channel.price));
            SH.append("create_by", this.$store.state.auth.userInfo.id);
            SH.append("update_by", this.$store.state.auth.userInfo.id);
            axios.post("http://127.0.0.1:8000/product/price-topping/", SH);
          }
          this.$emit("reload");
        })
        .catch((err) => {
          this.err.massage = err.response.data;
          this.err.status = true;
        });
    },
    onFileChange(e) {
      this.img = e.target.files[0];
      console.log(this.img.name);
    },
    clearForm() {
      this.img = null;
      this.topping_name = "";
      this.code = "";
    },
  },
  watch: {
    code() {
      this.err.status = false;
    },
  },
  mounted() {
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