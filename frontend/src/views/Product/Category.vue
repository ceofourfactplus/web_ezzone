<template>
  <div id="list-category">
    <table class="table table-dark fw-bold fs-5">
      <thead>
        <tr>
          <th>#</th>
          <th>Category</th>
          <th>able</th>
          <th>edit/delete</th>
        </tr>
      </thead>
      <tbody class="scroll">
        <tr v-for="(category, index) in categories" :key="category.id">
          <td>{{ index + 1 }}</td>
          <td>{{ category.category }}</td>
          <td>
            <Switch :value="category.status" :index="index" @input="Switch" />
          </td>
          <td>
            <div class="btn-group">
              <button class="btn btn-warning">
                <i class="fas fa-arrow-alt-circle-up"></i>update
              </button>
              <button class="btn btn-danger">
                <i class="fas fa-trash-alt"></i>delete
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <category-create />
  </div>
</template>

<script>
import axios from "axios";
import CategoryCreate from "../../components/CategoryCreate.vue";
import Switch from "../../components/switch.vue";
export default {
  components: { CategoryCreate, Switch },
  name: "Category",
  data() {
    return {
      categories: [],
    };
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/product/category/").then((response) => {
      this.categories = response.data;
    });
  },
  methods: {
    Switch(value, index) {
      this.categories[index].status = value;
      console.log(value);
    },
  },
};
</script>

<style>
.scroll {
  scroll-behavior: smooth;
}
.center {
  margin-left: auto;
  margin-right: auto;
  display: block;
}
</style>