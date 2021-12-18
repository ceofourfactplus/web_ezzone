<template>
  <div>
    <input
      type="text"
      class="search-bar"
      placeholder="Search"
      v-model="texts"
    />
  </div>
</template>


<script>
export default {
  name: "SearchBar",
  props: {
    value: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      texts: "",
    };
  },
  watch: {
    texts: function (val) {
      this.texts = val;
      this.$emit("search", val);
    },
  },
  mounted() {
    this.texts = this.value;
  },
};
</script>

<style scoped>
.search-bar {
  background-size: contain;
  background-repeat: no-repeat;
  background-color: #3a3d49;
  text-indent: 60px;
  padding-left: 10px;
  margin-left: 3px;
  border-radius: 20px;
  width: 90%;
  height: 45px;
  background-image: url("../../assets/icon/Search-19x18-1.png");
  background-position: 2% 50%;
  /* Extra Styling */
}
</style>