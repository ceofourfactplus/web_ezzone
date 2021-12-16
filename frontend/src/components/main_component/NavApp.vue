<template>
  <nav class="nav">
    <img
      src="../../assets/icon/btn-back.png"
      class="back inline ms-4"
    />

    <p id="login" class="header-text" @click="$router.go(-1)"><slot></slot></p>
  </nav>
</template>

<script>
export default {};
</script>

<style scoped>
.back {
  margin: auto;
  margin-left: 25px;
  margin-top: 25px;
  position: fixed;
}
.nav {
  height: 90px;
}
.header-text {
  width: 100%;
  font-style: normal;
  font-weight: 800;
  font-size: 48px;
  top: 0px;
  margin: auto;
  margin-bottom: 100px;
  color: #fafafa;
  display: inline;
  position: fixed;
  line-height: 80px;
}
.inline {
  display: inline;
}
</style>
