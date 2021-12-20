<template>
  <div>
    <nav class="nav">
      <div class="row w-100">
        <div class="col-2">
          <img
            src="../../assets/icon/btn-back.png"
            class="back inline ms-4"
            @click="$router.go(-1)"
          />
        </div>
        <div class="col-9 w-100">
          <h1 id="login" class="header-text"><slot></slot></h1>
        </div>
        <div class="col-2" v-if="save">
          <img
          @click="$emit('save')"
            src="../../assets/icon/save.png"
            style="align-item: right"
            class="save"
            alt=""
          />
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  props: ["save"],
  data() {
    return {
      pages: [
        { name: "Raw Materials" },
        { name: "Suppliers" },
        { name: "PO for Suppliers" },
        { name: "Add Raw Materials" },
        { name: "Pickup Raw Materials" },
      ],
      ham_status: false,
      ham_val: "",
    };
  },
  methods: {
    select_page(page) {
      this.ham_val = page.name;
      console.log(page.name);
    },
  },
};
</script>

<style scoped>
.selected {
  color: #ea7c69;
}
.txt {
  margin-top: 20px;
}
.side-bar {
  width: 292px;
  height: 880px;
  color: #889898;
  background-color: #2f414e;
  position: absolute;
  margin-left: 60%;
  float: right;
  font-size: 24px;
}
.hamburger {
  top: 2px;
  right: 25px;
  position: absolute;
}
.back {
  margin: auto;
  margin-left: 25px;
  margin-top: 25px;
  position: fixed;
}
.nav {
  height: 90px;
}
.save {
  right: 40px;
  top: 25px;
  position: fixed;
}
.header-text {
  font-style: normal;
  font-weight: 800;
  font-size: 48px;
  color: #fafafa;
  display: inline;
  line-height: 80px;
}
</style>
