<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <logo />
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
        <ul class="navbar-nav">
          <li class="nav-item me-2" style="width:100px">
            <div class="row">
              <a class="nav-link fw-bold active" href="#">see order</a>
            </div>
            <div class="row">
              <a class="nav-link fw-bold active" href="#">clear category</a>
            </div>
          </li>
          <li class="nav-item" id="categories_nav" style="width: 800px">
            <div class="scrollmenu">
              <button
                v-for="category in categories"
                :key="category.id"
                class="m-2 fs-5 fw-bold btn btn-warning"
              >
                {{ category.category }}
              </button>
            </div>

            <!-- <div
              id="category_nav"
              v-for="category in categories"
              :key="category.id"{{ category.category }}
            >{{ category.category }}
              <button class="btn-warning btn" style="display: inline-block">
                {{ category.category }}
              </button>
            </div> -->
          </li>
        </ul>
        <form class="d-flex ms-2">
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
import Logo from "./Logo";

export default {
  components: { Logo },
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
/* div#category_nav button {
  display: inline-block;
  color: white;
  text-align: center;
  padding: 14px;
  text-decoration: none;
}

#category_nav {
  background-color: #333;
  overflow: auto;
  white-space: nowrap;
 } */

div.scrollmenu {
  /* background-color: #333; */
  overflow: auto;
  white-space: nowrap;
}

div.scrollmenu a {
  display: inline-block;
  /* color: white; */
  text-align: center;
  padding: 14px;
  text-decoration: none;
}

div.scrollmenu a:hover {
  background-color: #777;
}
</style>