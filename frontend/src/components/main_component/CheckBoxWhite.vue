<template>
  <div class="checkbox">
    <div class="row">
      <div class="col-4">
        <input
          type="radio"
          class="me-3 mt-2"
          v-model="gender"
          value="Male"
          id="Male"
        />
      </div>
      <div class="col-8">
        <label class="ms-3" for="Male"><slot></slot></label>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.checkbox label {
  font-size: 24px;
  display: inline;
}
.checkbox input {
  position: relative;
  appearance: none;
  height: 20px;
  width: 20px;
  justify-content: center;
  align-content: center;
  display: flex;
  text-indent: 3px;
}
.checkbox input::before {
  position: absolute;
  content: "";
  height: 20px;
  width: 20px;
  background-color: #252836;
  border: 2px solid #ffffff80;
  border-radius: 3px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  cursor: pointer;
  transition: 0.3s all ease;
}
.checkbox input:checked::before {
  background-color: #ffffff80;
  border: 0px solid #ffffff80;
}
.checkbox input:checked::after {
  position: absolute;
  content: "\f00c";
  font-family: "FontAwesome";
  color: #252836;
  font-size: 13px;
  top: 0px;
  left: 0px;
  display: flex;
}
</style>