<template>
  <table class="table table-dark fw-bold fs-5">
    <thead>
      <tr>
        <th>img</th>
        <th>code</th>
        <th>product</th>
        <th>category</th>
        <th>topping set</th>
        <th>price</th>
        <th>status</th>
        <th>edit/delete</th>
      </tr>
    </thead>
    <tbody class="scroll">
      <tr v-for="product in all_product" :key="product.id">
        <td>
          <img
            id="image"
            :src="product.img"
            style="width:60px;height:60px;border"
            :alt="product"
          />
        </td>
        <td>{{ product.code }}</td>
        <td>{{ product.name }}</td>
        <td>{{ product.category.category }}</td>
        <td>{{ product.type_topping.type_topping }}</td>
        <td>
          <button
            class="btn btn-primary fw-bold"
            type="button"
            data-bs-toggle="offcanvas"
            data-bs-target="#price-detail"
            aria-controls="offcanvasRight"
            @click="$emit('select_product',product)"
          >
            see price detail
          </button>
        </td>
        <td>
          <Switch :value="product.status" :id="product.id" @input="Switch" />
        </td>
        <td>
          <div class="btn-group">
            <button
              class="btn btn-warning"
              @click="$emit('select_product',product)"
              data-bs-toggle="modal"
              data-bs-target="#UpdateProduct"
            >
              <i class="fas fa-arrow-alt-circle-up"></i>update
            </button>
            <button class="btn btn-danger" @click="DeleteProduct(product.id)">
              <i class="fas fa-trash-alt"></i>delete
            </button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import Switch from "../../../components/switch";
import axios from "axios";
export default {
  components: { Switch },
  props: ["all_product"],
  methods: {
    Switch(value,id) {
      axios
        .put(
          "http://127.0.0.1:8000/product/product/status/" + id + "/",
          {
            status: value,
            update_by: this.$store.state.auth.userInfo.id,
          }
        )
        .then((data) => {
          this.$emit("reload");
          console.log(data.data);
        });
    },
    DeleteProduct(id) {
      axios
        .delete("http://127.0.0.1:8000/product/product/" + id + "/")
        .then(() => {
          this.$emit("reload");
        });
    },
  },
};
</script>

<style scoped>
#image {
  width: 40px;
  height: 40px;
  border-radius: 20%;
}
</style>