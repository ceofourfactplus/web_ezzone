<template>
  <!-- Card Popup -->
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img src="../../assets/icon/btn-pass.png" alt="" />
      </div>
      <div class="main-text">Saved successfully</div>
    </div>
</template>

<script>
export default {
    name: "SavePopup",
    props: ["alert"]

}
</script>

<style>
.card {
  left: 25%;
  top: 15%;
  width: 390px;
  height: 500px;
  position: fixed;
  background: #303344;
  border: 2px solid #ea7c69;
  box-sizing: border-box;
  border-radius: 10px;
  visibility: hidden;
  opacity: 0;
  transition: visibility 0s, opacity 0.5s linear;
}

.card-active {
  visibility: visible;
  opacity: 1;
}

.card .icon {
  margin: 0;
  position: relative;
  top: 26%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.card .main-text {
  margin: 0;
  position: absolute;
  width: 100%;
  top: 55%;
  font-weight: bold;
  color: #fff;
  font-size: 50px;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.card .second {
  margin: 0;
  position: absolute;
  width: 100%;
  top: 75%;
  font-weight: bold;
  color: #ffb572;
  font-size: 28px;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
</style>