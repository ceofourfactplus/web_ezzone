<template>
  <nav class="nav">
    <div class="row">
      <div class="col-3">
        <img
          src="../../assets/icon/btn-back.png"
          class="back inline ms-4"
          @click="$router.go(-1)"
        />
      </div>
      <div class="col-9">
        <p id="login" class="header-text"><slot></slot></p>
      </div>
    </div>
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
  font-style: normal;
  font-weight: 800;
  font-size: 48px;
  top: 0px;
  right: 80px;
  margin-bottom: 100px;
  color: #fafafa;
  display: inline;
  position: fixed;
  width:80%;
  
  line-height: 80px;
  margin-left:20%;
}
.inline {
  display: inline;
}
</style>
