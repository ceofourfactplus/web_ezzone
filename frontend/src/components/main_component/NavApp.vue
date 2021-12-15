<template>
  <nav class="nav">
    <img
      src="../../assets/icon/btn-back.png"
      class="back inline ms-4"
      @click="$emit('back')"
    />
    <p id="login" class="header-text"><slot></slot></p>

  </nav>
</template>

<script>
export default {
  props:{

  }
};
</script>

<style scoped>

.back {
  margin:auto;
  margin-left: 25px;
  margin-top:25px;
  position: fixed;
}
.nav{
height: 120px;
}
.header-text{
  width:100%;
  font-style: normal;
  font-weight: 800;
  font-size: 48px;
  top: 0px;
  margin:auto;
  margin-bottom: 100px;
  color: #fafafa;
  display: inline;
  position: fixed;
  line-height: 80px;
}
.inline{
  display :inline;
}
</style>
