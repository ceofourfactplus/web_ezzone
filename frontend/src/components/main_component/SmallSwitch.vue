<template>
  <label class="switch">
    <input type="checkbox" v-model="input"  @click="$emit('switch')"/>
    <span class="sm-slider sm-round" v-if="value"></span>
    <span class="false-slider false-round" v-else></span>
  </label>
</template>

<script>
export default {
  name: "SmallSwitch",
  props: {
    value: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      input: true,
    };
  },
  watch: {
    input: function (val) {
      this.input = val;
    },
    value(val){
      this.input = val
    }
  },
  mounted() {
    this.input = this.value;
  },
};
</script>

<style scoped>
/* The slider */
.false-slider {
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

.false-slider.false-round {
  border-radius: 34px;
}

.false-slider.false-round:before {
  border-radius: 34px;
}

.false-slider:before {
    position: absolute;
    content: "";
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 1px;
    background-color: #ccc;
    transition: 0.4s;
}





.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 28px;
  margin-top: -3px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.sm-slider {
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

.sm-slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 1px;
  background-color: #ccc;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

input:checked + .sm-slider {
  background-color: #c5ffed;
}

input:focus + .sm-slider {
  box-shadow: 0 0 1px #c5ffed;
}

input:checked + .sm-slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
  background-color: #50d1aa;
}
/* Rounded sm-sliders */
.sm-slider.sm-round {
  border-radius: 34px;
}

.sm-slider.sm-round:before {
  border-radius: 50%;
}
</style>