<template>
  <!-- Tabs -->
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
  width: 95%;
  margin-right: 1%;
  margin-left: 3%;
  margin-top: 3%;
}

.tab-item {
  background-color: #2f3446;
  color: gray;
  /* float: left; */
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  transition: 0.3s;
  font-size: 19px;
  font-weight: 400;
  border-radius: 15px 15px 0px 0px;
  margin-top: 0px;
  margin: 3px;
  height: 46px;
  width: fit-content;
  text-decoration: none;
}

/* Change background color of buttons on hover */
.tab,
.tab-item:hover {
  color: white;
}
</style>