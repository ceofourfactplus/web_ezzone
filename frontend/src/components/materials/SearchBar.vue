<template>
  <div>
      <input
      type="text"
      class="search-bar"
      placeholder="Search"
      v-model="texts"
    />
<<<<<<< HEAD
    <img class="img-float" src="../../assets/icon/868282.png">
=======
    <img class="img-float" src="../../assets/icon/search-orange.png">
>>>>>>> 547f0d42ea438cec64d2bac35e35f52a83200ba6
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
<<<<<<< HEAD
      width: 43px;
      left: 48px;
      top: 9.5%;
=======
      /* width: 50px; */
      left: 50px;
      top: 105px;
>>>>>>> 547f0d42ea438cec64d2bac35e35f52a83200ba6
      position: fixed;
  }
</style>