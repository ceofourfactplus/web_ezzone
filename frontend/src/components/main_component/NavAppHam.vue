<template>
  <div>
    <nav class="nav">
      <div class="row">
        <div class="col-3">
          <img
            src="../../assets/icon/btn-back.png"
            class="back inline ms-4"
            @click="$router.go(-1)"
          />
        </div>
        <div class="col-6">
          <p id="login" class="header-text"><slot></slot></p>
        </div>
        <div class="col-3">
          <img @click="ham_status = !ham_status" class="hamburger" src="../../assets/icon/Menu-icon.png" />
        </div>
      </div>
    </nav>

    <div class="side-bar" v-if="ham_status">
        <p 
          class="txt" 
          v-for="page in pages" 
          @click="select_page(page)"
          :key="page.name"
          :class="{'selected': ham_val == page.name}"
          >
          {{ page.name }}
        </p>
      </div>
  </div>
</template>

<script>
export default {
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
      ham_val: '',
    };
  },
  methods: {
    select_page(page) {
      this.ham_val = page.name
      console.log(page.name)
    }
  }
};
</script>

<style scoped>
.selected {
  color: #EA7C69;
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
.header-text {
  font-style: normal;
  font-weight: 800;
  font-size: 48px;
  top: 0px;
  right: 80px;
  margin-bottom: 100px;
  color: #fafafa;
  display: inline;
  position: fixed;
  width: 80%;

  line-height: 80px;
  margin-left: 20%;
}
</style>
