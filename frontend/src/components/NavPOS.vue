<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">EZ zone</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" href="#">see order</a>
          </li>
          <li class="nav-item ms-2" id="categories_nav" style="width: 200px">
            <div
              data-bs-spy="scroll"
              data-bs-offset="0"
              class="scrollspy-example"
              tabindex="0"
              id="category_nav"
              v-for="category in categories"
              :key="category.id"
            >
              <button class="btn-warning btn">{{ category.category }}</button>
            </div>
          </li>
        </ul>
        <form class="d-flex">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Search"
            aria-label="Search"
          />
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
import axios from "axios";

export default {
  name: "NavbarPOS",
  data() {
    return {
      categories: [],
    };
  },
  methods: {
    getCategory() {
      axios.get("http://127.0.0.1:8000/product/category/").then((response) => {
        this.categories = response.data;
      });
    },
  },
  mounted() {
    this.getCategory();
  },
};
</script>

<style>
#category_nav {
  overflow-y: auto;
  overflow-x: hidden;
  background-color: rgb(253, 255, 151,0.5);
  border-radius: 3px;
}
</style>