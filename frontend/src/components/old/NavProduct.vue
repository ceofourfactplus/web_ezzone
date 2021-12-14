<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <Logo/>
      <a class="navbar-brand"
        ><h4
          class="link fromLeft"
          style="color: rgba(255, 156, 88, 1)"
          @click="Product()"
        >
          Product
        </h4>
        >
        <h4 class="link fromLeft" style="color: rgba(255, 215, 88, 1)">
          <slot></slot></h4
      ></a>
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
            <a
              class="nav-link btn btn-primary fw-bold"
              data-bs-toggle="modal"
              style="color: #ffff"
              data-bs-target="#createModal"
              >Create</a
            >
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <form class="d-flex">
              <input
                class="form-control me-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />
              <button class="btn btn-outline-success" type="submit">
                Search
              </button>
            </form>
          </li>
          <nav-user />
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import Logo from "./Logo";
import NavUser from "./NavUser.vue";
export default {
  components: { NavUser, Logo },
  methods: {
    EZzone() {
      this.$store.state.product.select_app = "";
      this.$router.push({ name: "Home" });
    },
    Product() {
      this.$store.state.product.select_app = "";
      this.$router.push({ name: "SelectApp" });
    },
  },
};
</script>

<style>
/*.link {
  color: rgba(255, 88, 88, 1);
  display: inline-block;
  margin: 0;
}
.link:after {
  display: block;
  content: "";
  border-bottom: solid 3px #ffb938;
  transform: scaleX(0);
  transition: transform 250ms ease-in-out;
}
.fromLeft:after {
  transform-origin: 100% 50%;
}
.fromRight:after {
  transform-origin: 0% 50%;
}
.fromLeft:hover:after {
  transform: scaleX(1);
  transform-origin: 0% 50%;
}
.fromRight:hover:after {
  transform: scaleX(1);
  transform-origin: 100% 50%;
}*/
</style>