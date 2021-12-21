<template>
  <label class="switch">
    <input type="checkbox" v-model="input" />
    <span class="slider round"></span>
  </label>
</template>

<script>
export default {
  name: "Switch",
  props: {
    value: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      input: "",
    };
  },
  watch: {
    input: function (val) {
      this.input = val;
      this.$emit("switch", val);
    },
  },
  mounted() {
    this.input = this.value;
  },
};
</script>

<style scoped>
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #fff;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: #ccc;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

input:checked + .slider {
  background-color: #c5ffed;
}

input:focus + .slider {
  box-shadow: 0 0 1px #c5ffed;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
  background-color: #50d1aa;
}
/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>