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
  line-height: 10px;
  font-size: 30px;
  background-size: 40px;
  background-repeat: no-repeat;
  background-color: #3a3d49;
  text-indent: 60px;
  padding-left: 10px;
  border-radius: 10px;
  width: 100%;
  height: 45px;
  background-image: url("../../assets/icon/search.png");
  background-position: 2% 50%;
  /* Extra Styling */
}
::placeholder{
  text-indent: 60px;
}
</style>