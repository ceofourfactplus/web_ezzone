<template>
  <div id="inventory">
    <navbar-stock />
    <router-view/>
  </div>
</template>

<script>
import { apiStock } from "../../api/ApiStock";
import { mapState } from "vuex";
import NavbarStock from "../../components/NavStock.vue";
export default {
  name: "MainStock",
  components: {
    NavbarStock,
  },
  computed: mapState(["auth"]),
  created() {
    apiStock
      .get("/supplier/", {
        headers: {
          Authorization: `Bearer ${this.auth.accessToken}`,
        },
      })
      .then((response) => {
        this.supplier_data = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
</style>