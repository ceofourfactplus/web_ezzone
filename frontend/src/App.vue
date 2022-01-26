<template><router-view /></template>

<script>
import { api_product } from './api/api_product';
export default {
  mounted(){
    api_product.get('sale-channel/ezzone').then((response)=>{
      this.$store.state.ezzone_id = response.data.id;
    })
  }
}
</script>

<style>

#app {
  font-family: "Sarabun", sans-serif !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
@import "~bootstrap/dist/css/bootstrap.css";
</style>
