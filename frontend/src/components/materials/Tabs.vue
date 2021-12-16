<template>
  <!-- Tabs -->
  <div>
    <div class="tab">
      <button
        v-for="(cate, idx) in categories"
        :key="idx"
        @click="select_cate(cate)"
        class="tab-item"
      >
        {{ cate }}
      </button>
    <button class="tab-item" v-if="categories.length < 5">></button>
  </div>
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


<style>

.tab {
  overflow: hidden;
  width: 90%;
  height: 46px;
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
  padding: 5px;
  padding-top: 6px;
  transition: 0.3s;
  font-size: 26.5px;
  /* font-weight: 700; */
  font-style: normal;
  border-radius: 15px 15px 0px 0px;
  margin-top: 0px;
  margin: 3px;
  margin-bottom: 1em;
  height: 46px;
  width: fit-content;
  block-size: fit-content;
  text-decoration: none;
  line-height: 31px;
}

/* Change background color of buttons on hover */
.tab,
.tab-item:hover {
  color: white;
}
</style>