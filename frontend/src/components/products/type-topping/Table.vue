<template>
  <table class="table table-dark fw-bold fs-5">
    <thead>
      <tr>
        <th>#</th>
        <th>type topping</th>
        <th>topping</th>
        <th>edit/delete</th>
      </tr>
    </thead>
    <tbody class="scroll">
      <tr v-for="(type, index) in type_toppings" :key="type.id">
        <td>{{ index+1 }}</td>
        <td>{{ type.type_topping }}</td>
        <td>
          <div v-for="tabletopping in type.tabletopping_set" :key="tabletopping.id">
            {{ tabletopping.topping_set.name }}<br />
          </div>
        </td>
        <td>
          <div class="btn-group">
            <button
              class="btn btn-warning"
              @click="$emit('select-type',type)"
              data-bs-toggle="modal"
              data-bs-target="#Updateproduct"
            >
              <i class="fas fa-arrow-alt-circle-up"></i>update
            </button>
            <button class="btn btn-danger" @click="Delete(type.id)">
              <i class="fas fa-trash-alt"></i>delete
            </button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";
export default {
  name: "TypeToppingTable",
  props: ["type_toppings"],
  methods: {
    Switch(value, id) {
      axios
        .put("http://127.0.0.1:8000/product/type-topping/status/" + id + "/", {
          status: value,
          update_by: this.$store.state.auth.userInfo.id,
        })
        .then((data) => {
          this.$emit("reload");
          console.log(data.data);
        });
    },
    Delete(id) {
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