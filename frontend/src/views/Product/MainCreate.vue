<template>
  <div id="main-create" class="container">
    <!-- navbar create -->
    <nav-product>product</nav-product>

    <router-view></router-view>
  </div>
</template>

<script>
import NavProduct from '../../components/NavProduct.vue';
export default {
  components: { NavProduct },
  name: "MainCreate",
};
</script>

<style>
</style>