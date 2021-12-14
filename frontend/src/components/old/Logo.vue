<template>
  <a class="navbar-brand" @click="EZzone()"
    ><h4 class="link fromLeft">EZzone</h4></a
  >
</template>

<script>
export default {
  methods: {
    EZzone() {
      this.$store.state.product.select_app = "";
      this.$router.push({ name: "Home" });
    },
  },
};
</script>

<style>
.link {
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
}
</style>