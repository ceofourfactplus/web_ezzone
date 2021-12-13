<template>
  <div></div>
</template>

<script>
export default {
  name: "Logout",
  created() {
    this.$store.dispatch("auth/userLogout").then(() => {
      this.$router.push({ name: "Login" });
    });
  },
  BeforeUnmout() {
    const vuex = JSON.parse(localStorage.getItem("vuex"));
    localStorage.removeItem(vuex);
  },
};
</script>

<style>
</style>
