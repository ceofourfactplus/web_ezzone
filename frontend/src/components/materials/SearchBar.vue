<template>
  <div>
      <input
      type="text"
      class="search-bar"
      placeholder="Search"
      v-model="texts"
    />
    <img class="img-float" src="../../assets/icon/868282.png">
  </div>
</template>


<script>
export default {
  name: "SearchBar",
  props: [],
  data() {
      return {
        texts: '',
      }
  },
//   methods: {
//     select_cate(cate) {
//         this.$emit('select_cate', cate)
//     },
//   },
  watch: {
    texts: function (val) {
      this.texts = val;
      this.$emit('search', val)
    },
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
    /* Extra Styling */
  }

  .img-float{
      width: 43px;
      left: 48px;
      top: 9.5%;
      position: fixed;
  }
</style>