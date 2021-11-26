<template>
  <!-- Create Category Modal -->
  <div
    class="modal fade"
    id="UpdateSaleChannel"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Update Sale Channel</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit="save_sale_channel()">
            <div class="mb-3">
              <label for="Category" class="form-label">Sale Channel</label>
              <input
                type="text"
                class="form-control"
                v-model="sale_channel_name"
                id="Category"
                placeholder="Drink"
              />
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
  name: "SaleChannelUpdate",
  computed: mapState(["auth", "product"]),
  props: ["select_channel"],
  data() {
    return {
      sale_channel_name: "",
    };
  },
  methods: {
    save_sale_channel() {
      axios
        .put(
          "http://127.0.0.1:8000/product/sale-channel/" + this.select_channel.id + "/",
          {
            sale_channal: this.select_channel_name,
            create_by: this.select_channel.create_by,
            update_by: this.$store.state.auth.userInfo.id,
          }
        )
        .then(() => {
          this.$emit("save");
        });
    },
  },
  watch:{
    select_channel(newSaleChannel) {
     this.sale_channel_name = newSaleChannel.sale_channel   
    }
  }
};
</script>

<style>
</style>