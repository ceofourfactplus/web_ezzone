<template>
  <div id="list-category">
    <category-table :categories="categories" @reload="reloadCategories()"/> 
    <category-create @reload="reloadCategories()" />
    <cate-update :category="select_category" @save="reloadCategories()" />
  </div>
</template>

<script>
import axios from "axios";
import CategoryCreate from "../../components/products/category/Create.vue";
import CateUpdate from "../../components/products/category/Update.vue";
import CategoryTable from "../../components/products/category/Table.vue"

export default {
  components: { CategoryCreate, CateUpdate, CategoryTable },
  name: "Category",
  data() {
    return {
      categories: [],
      load: false,
      select_category: "",
    };
  },
  mounted() {
    this.reloadCategories();
  },
  methods: {
    reloadCategories() {
      axios.get("http://127.0.0.1:8000/product/category/").then((response) => {
        this.categories = response.data;
      });
    },
    DeleteCategory(id) {
      axios.delete("http://127.0.0.1:8000/product/category/"+id+ "/").then(()=>{this.reloadCategories()})
    },
    // showModal() {
    //   var myModal = bootstrap.Modal(document.getElementById("createModal"));
    //   myModal.show();
    // },
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