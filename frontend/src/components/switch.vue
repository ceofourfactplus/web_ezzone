<template>
  <div class="m-2">
    <span
      class="toggle-wrapper"
      role="checkbox"
      :aria-checked="value.toString()"
      tabindex="0"
      @click="toggle"
      @keydown.space.prevent="toggle"
    >
      <span class="toggle-background" :class="backgroundStyles" />
      <span class="toggle-indicator" :style="indicatorStyles" />
    </span>
    <span class="ms-2"> {{ able() }}</span>
    
  </div>
</template>

<script>
export default {
  name: "switch",
  props: ["value", "index"],
  computed: {
    backgroundStyles() {
      return {
        "gold-mid": this.value,
        "gray-lighter": !this.value,
      };
    },
    indicatorStyles() {
      return { transform: this.value ? "translateX(17px)" : "translateX(-7px)" };
    },
  },
  methods: {
    toggle() {
      this.$emit("input", !this.value, this.index);
    },
    able() {
      if (this.value == true)return 'ABLE'
      if (this.value == false)return 'DISABLE'
    }
  },
};
</script>

<style scoped>
.gold-mid {
  background-color: #48da60;
}

.gray-lighter {
  background-color: #ff5e5e;
}

.toggle-wrapper {
  display: inline-block;
  position: relative;
  cursor: pointer;
  width: 50px;
  height: 25px;
  border-radius: 9999px;
}

.toggle-wrapper:focus {
  outline: 0;
}

.toggle-background {
  display: inline-block;
  border-radius: 9999px;
  height: 100%;
  width: 100%;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: background-color 0.4s ease;
}

.toggle-indicator {
  position: absolute;
  height: 20px;
  width: 20px;
  left: 10px;
  bottom: 2.75px;
  background-color: #ffffff;
  border-radius: 9999px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.4s ease;
}
</style>
