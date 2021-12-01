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
          <li class="nav-item ms-3 me-3" style="width: 110px">
            <div class="row mb-1 mt-1">
              <a
                class="fw-bold active btn btn-sm btn-primary"
                @click="$emit('see_order')"
                >see order</a
              >
            </div>
            <div class="row">
              <a
                class="fw-bold active btn btn-sm btn-primary"
                @click="$emit('clear_category')"
                >clear category</a
              >
            </div>
          </li>
          <li class="nav-item" id="categories_nav" style="width: 800px">
            <div class="scrollmenu">
              <button
                v-for="category in categories"
                :key="category.id"
                class="m-2 fs-5 fw-bold btn"
                @click="select_category(category.id)"
                :class="{
                  'btn-danger': select_category_id == category.id,
                  'btn-warning': select_category_id != category.id,
                }"
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
import Logo from "../Logo";

export default {
  components: { Logo },
  props: ["categories",'select_category_id'],
  name: "NavbarPOS",
  methods:{
    select_category(id){
      this.$emit('select_category', id)
    }
  }
};
</script>

<style>
div.scrollmenu {
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