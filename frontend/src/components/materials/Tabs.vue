<template>
  <!-- Tabs -->
  <div class="tab">
      <button
        v-for="(cate, idx) in categories"
        :key="idx"
        @click="select_cate(cate)"
        class="tab-item"
      >
        <p class="txt">{{ cate }}</p>
      </button>
    <button class="tab-item" v-if="categories.length < 5">></button>
  </div>
</template>


<script>
export default {
  name: "Tabs",
  props: [],
  data() {
    return {
      //   materials: [],
      categories: [
        "All",
        "Fresh Food",
        "Dried Food",
        "Garnish",
        "Package",
        "ETC.",
        '>'
      ],
    };
  },
  methods: {
    select_cate(cate) {
      this.$emit("select_cate", cate);
    },
  },
};
</script>


<style scoped>

.tab {
  overflow: hidden;
  width: 90%;
  margin-right: 1%;
  margin-left: 5%;
  margin-top: 10px;
}

.tab-item {
  background-color: #2f3446;
  color: gray;
  /* float: left; */
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  padding-top: 6px;
  transition: 0.3s;
  font-size: 18px;
  font-size: height 10px;
  font-weight: 700;
  font-style: normal;
  border-radius: 15px 15px 0px 0px;
  margin-top: 0px;
  margin: 3px;
  height: 46px;
  width: fit-content;
  text-decoration: none;
  line-height: 31px;
}

/* Change background color of buttons on hover */
.tab,
.tab-item:hover {
  color: white;
}
</style>