<template>
  <!-- Tabs -->
  <div>
    <div class="tab" v-if="status == 'category'">
      <button
        v-for="(item, idx) in elements"
        :key="idx"
        @click="select_item(item)"
        class="tab-item"
      >
        {{ item.category }}
      </button>
    <button class="tab-item" v-if="elements.length > 5">></button>
  </div>
  <div class="tab" v-else>
      <button
        v-for="(item, idx) in elements"
        :key="idx"
        @click="select_item(item)"
        class="tab-item"
      >
        {{ item.name }}
      </button>
    <button class="tab-item" v-if="elements.length > 5">></button>
  </div>
  </div>
</template>


<script>
export default {
  name: "Tabs",
  props: ['elements', 'status'],
  data() {
    return {
      //   materials: [],
    };
  },
  methods: {
    select_item(item) {
      this.$emit("select_item", item.id);
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
  text-align: left !important;
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