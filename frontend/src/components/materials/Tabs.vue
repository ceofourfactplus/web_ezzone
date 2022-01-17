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
        class="btn-gray"
        style="min-width: 65px; line-height: 50px"
        :class="{
          active: $store.state.raw_material.tab == 'All',
        }"
      >
        <!-- <p :class="{ 'tab-selected': 'All' == $store.state.raw_material.tab }">
          All
        </p> -->
        All
      </button>
      <button
        v-for="(item, idx) in elements"
        :key="idx"
        @click="select_item(item)"
        class="btn-gray"
        style="height: 50px"
        :class="{
          active: $store.state.raw_material.tab == item.name,
        }"
      >
        <!-- <p :class="{'tab-selected': item.name == $store.state.raw_material.tab}"></p> -->
        {{ item.name }}
      </button>
      <!-- <button class="tab-item" v-if="elements.length > 5">></button> -->
    </div>
  </div>
</template>


<script>
export default {
  name: "Tabs",
  props: ["elements", "status"],
  data() {
    return {};
  },
  methods: {
    select_all() {
      this.$store.state.raw_material.tab = "All";
      this.$emit("all_category");
    },
    select_item(item) {
      console.log(this.$store.state.raw_material.tab, "tab1");
      this.$store.state.raw_material.tab = item.name;
      console.log(this.$store.state.raw_material.tab, "tab2");
      this.$emit("select_item", item.id);
    },
  },
};
</script>


<style scoped>
.tab-selected {
  color: white;
}
.tab {
  overflow: hidden;
  width: 90%;
  height: 46px;
  margin: auto;
  text-align: left !important;
}

.btn-gray {
  opacity: 0.5;
  display: inline;
  height:100%;
}
.active {
  opacity: 1;
  color:#fff;
}
</style>