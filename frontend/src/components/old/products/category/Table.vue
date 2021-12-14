<template>
  <table class="table table-dark fw-bold fs-5">
    <thead>
      <tr>
        <th>#</th>
        <th>Color</th>
        <th>Category</th>
        <th>Able</th>
        <th>edit/delete</th>
      </tr>
    </thead>
    <tbody class="scroll">
      <tr v-for="(category, index) in categories" :key="category.id">
        <td>
          {{ index + 1 }}
        </td><td>
          <div class="color">
            <div style="width:100%;height:100%;" :style="{'background-color':category.color}"></div>
          </div>
        </td>
        <td>{{ category.category }}</td>
        <td>
          <Switch :value="category.status" :id="category.id" @input="Switch" />
        </td>
        <td>
          <div class="btn-group">
            <button
              class="btn btn-warning"
              @click="$emit('select_category',category)"
              data-bs-toggle="modal"
              data-bs-target="#UpdateCategory"
            >
              <i class="fas fa-arrow-alt-circle-up"></i>update
            </button>
            <button class="btn btn-danger" @click="DeleteCategory(category.id)">
              <i class="fas fa-trash-alt"></i>delete
            </button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import Switch from "../../switch.vue";
import axios from "axios";
export default {
  name: "TabelCategory",
  components: { Switch },
  props: ["categories"],
  methods: {
    Switch(value, id) {
      axios
        .put(
          "http://127.0.0.1:8000/product/category/status/" +
            id +
            '/',{
              update_by: this.$store.state.auth.userInfo.id,
              status:value
            }
           
        )
        .then((data) => {
          this.$emit("reload");
          console.log(data.data);
        });
    },
    DeleteCategory(id) {
      axios
        .delete("http://127.0.0.1:8000/product/category/" + id + "/")
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
.color {
  width: 50px;
  height: 50px;
  border: 5px solid white;
  margin:auto;
  border-radius: 20%;
}
</style>