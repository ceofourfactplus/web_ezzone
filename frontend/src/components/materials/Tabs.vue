<template>
  <!-- Tabs -->
  <div>
    <!-- <div class="tab" v-if="status == 'category'">
      <button
        @click="select_all()"
        :class="{'tab-selected': 'All' == tab_selected}"
        class="tab-item"
      >
        All
      </button>
      <button
        v-for="(item, idx) in elements"
        :key="idx"
        @click="select_item(item)"
        :class="{'tab-selected': item.name == tab_selected}"
        class="tab-item"
      >
        {{ item.category }}
      </button>
    <button class="tab-item" v-if="elements.length > 5">></button>
  </div> -->

  <div class="tab">
    <button
        @click="select_all()"
        class="tab-item"
      >
        <p :class="{'tab-selected': 'All' == $store.state.raw_material.tab}">All</p>
      </button>
      <button
        v-for="(item, idx) in elements"
        :key="idx"
        @click="select_item(item)"
        class="tab-item"
        style="height:50px"
      >
      <p :class="{'tab-selected': item.name == $store.state.raw_material.tab}">{{ item.name }}</p>
        
      </button>
      <button class="tab-item" v-if="elements.length > 5">></button>
    </div>

  </div>
</template>


<script>
export default {
  name: "Tabs",
  props: ["elements", "status"],
  data() {
    return {
    };
  },
  methods: {
    select_all() {
      this.$store.state.raw_material.tab = "All"
      this.$emit('all_category')
    },
    select_item(item) {
      console.log(this.$store.state.raw_material.tab, 'tab1')
      this.$store.state.raw_material.tab = item.name
      console.log(this.$store.state.raw_material.tab, 'tab2')
      this.$emit("select_item", item.id);
    },
  },
};
</script>


<style>
.tab-selected {
  color: white;
}
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
  border: none;
  outline: none;
  cursor: pointer;
  padding: 10px;
  padding-top: 6px;
  transition: 0.3s;
  font-size: 26.5px;
  font-style: normal;
  border-radius: 15px 15px 0px 0px;
  margin-top: 0px;
  margin: 5px;
  margin-bottom: 1em;
  height: 46px;
  width: fit-content;
  block-size: fit-content;
  text-decoration: none;
  line-height: 31px;
}
</style>