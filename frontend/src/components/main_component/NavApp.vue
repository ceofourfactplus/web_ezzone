<template>
  <div>
    <nav class="nav">
      <div class="row w-100">
        <div class="col-1">
          <img
            src="../../assets/icon/btn-back.png"
            class="back inline ms-4"
            @click="$router.push({ name: url_name })"
          />
        </div>
        <div class="col-10 w-100">
          <h1 id="login" class="header-text"><slot></slot></h1>
        </div>
        <div class="col-1" v-if="save">
          <img
            @click="$emit('save')"
            src="../../assets/icon/save.png"
            style="align-item: right"
            class="save"
            alt=""
          />
        </div>
        <div class="col-1" v-else-if="rm_menu">
          <img
            src="../../assets/icon/Menu-icon.png"
            style="top: 0px; right: 25px; position: absolute; height: 100px;"
            @click="open_slide"
          />
        </div>
        <div class="col-1" v-else-if="reward_menu">
          <img
            src="../../assets/icon/Menu-icon.png"
            style="top: 0px; right: 25px; position: absolute; height: 100px;"
            @click="open_slide"
          />
        </div>
        <div class="col-1" v-else-if="product_menu">
          <img
            src="../../assets/icon/Menu-icon.png"
            style="top: 10px; right: 25px; position: absolute; height: 80px"
            @click="open_slide"
          />
        </div>
        <div
          class="col-1 w-100"
          style="padding: 0px; margin-top: 20px; margin-right: 20px"
          v-else-if="cart"
        >
          <img
            v-if="amount == 0"
            src="../../assets/icon/cart-o.png"
            @click="$router.push({ name: 'OrderReceipt' })"
            style="width: 35px"
          />
          <div v-else style="display: flex; text-align: right">
            <div class="noti me-1">
              {{ amount }}
            </div>
            <img
              src="../../assets/icon/cart-g.png"
              @click="$router.push({ name: 'OrderReceipt' })"
              style="width: 35px;height: 35px; display: inline"
            />
          </div>
        </div>
        <div class="col-1" v-else-if="trash">
          <img
            src="../../assets/icon/bin.png"
            style="top: 2.5%; right: 25px; position: absolute; height: 34px"
            @click="$emit('trash')"
            alt=""
          />
        </div>
      </div>
    </nav>
    <!-- RM Side Nav -->
    <div id="mySidenav" class="sidenav" v-if="rm_menu">
      <a href="javascript:void(0)" class="closebtn" @click="close_slide"
        >&times;</a
      >
      <div
        style="margin-top: 30px; color: #889898; margin-left: 0px"
        v-for="item in $store.state.raw_material.side_nav"
        :key="item"
      >
        <img
          :src="item.img"
          :style="item.img_style"
          style="margin-top: -10px; display: inline"
        />
        <div
          style="
            display: inline;
            text-align: left;
            font-size: 30px;
            margin-left: -20px;
          "
          :style="item.style"
          @click="select_page(item)"
          :class="{
            'rm-link-clicked': item.url_name == $store.state.raw_material.page,
          }"
        >
          {{ item.name }}
        </div>
      </div>
    </div>

    <!-- Reward Side Nav -->
    <div id="mySidenav" class="sidenav" v-else-if="reward_menu">
      <a href="javascript:void(0)" class="closebtn" @click="close_slide"
        >&times;</a
      >
      <div
        style="margin-top: 30px; color: #889898; margin-left: 0px"
        v-for="item in $store.state.promotion.side_nav"
        :key="item"
      >
        <div
          style="
            display: inline;
            text-align: left;
            font-size: 30px;
            font-weight: bold;
            margin-left: -20px;
          "
          :style="item.style"
          @click="select_promotion_page(item)"
          :class="{
            'rm-link-clicked': item.url_name == $store.state.promotion.page,
          }"
        >
          {{ item.name }}
        </div>
      </div>
    </div>

    <!-- PRODUCT Side Nav -->
    <div id="mySidenav" class="sidenav" v-else-if="product_menu">
      <a href="javascript:void(0)" class="closebtn" @click="close_slide"
        >&times;</a
      >
      <div
        style="margin-top: 30px; color: #889898; margin-left: 0px"
        v-for="item in $store.state.product.side_nav"
        :key="item"
      >
        <img
          :src="item.img"
          :style="item.img_style"
          style="margin-top: -10px; display: inline"
        />
        <div
          style="
            display: inline;
            text-align: left;
            font-size: 30px;
            margin-left: -20px;
            white-space: nowrap;
          "
          :style="item.style"
          @click="select_product_page(item)"
          :class="{
            'rm-link-clicked': item.url_name == $store.state.product.active_page,
          }"
        >
          {{ item.name }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: [
    "save",
    "rm_menu",
    "reward_menu",
    "cart",
    "amount",
    "trash",
    "url_name",
    "product_menu",
  ],
  data() {
    return {
      page: "",
    };
  },
  mounted() {
    this.$store.state.raw_material.page = this.$route.name;
  },
  methods: {
    select_product_page(item) {
      this.$store.state.product.active_page = item.url_name;
      this.$router.push({ name: item.url_name });
    },
    select_promotion_page(item) {
      this.$store.state.promotion.page = item.url_name;
      this.$router.push({ name: item.url_name });
    },
    select_page(item) {
      this.$router.push({ name: item.url_name, query: { page: item.name } });
      this.page = item.url_name;
      this.$store.state.raw_material.page = item.url_name;
    },
    open_slide() {
      document.getElementById("mySidenav").style.width = "310px";
    },
    close_slide() {
      document.getElementById("mySidenav").style.width = "0";
    },
  },
};
</script>

<style scoped>
.rm-link-clicked {
  color: #ea7c69;
}
.rm-link {
  text-decoration: none;
  margin-left: 15px;
}
.selected {
  color: #889898;
}
.txt {
  margin-top: 20px;
}
.hamburger {
  width: 40px;
  height: 80px;
  top: 2px;
  right: 25px;
  position: absolute;
}
.back {
  margin: auto;
  margin-left: 25px;
  margin-top: 25px;
  transform: rotate(90deg);
}
.nav {
  height: 90px;
}
.save {
  right: 55px;
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
.sidenav {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 1;
  top: 0;
  right: 0;
  background-color: #2f3344;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 20px;
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.5);
  border-radius: 20px 0px 0px 20px;
}

.sidenav div {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 25px;
  /* color: #818181; */
  display: block;
  text-align: left;
  transition: 0.3s;
}

.closebtn {
  text-decoration: none;
  color: #818181;
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
}

@media screen and (max-height: 450px) {
  .sidenav {
    padding-top: 15px;
  }
  .sidenav a {
    font-size: 18px;
  }
}
.noti {
  background-color: #9ef0d7;
  color: #000;
  margin: auto -3px;
  height: 35px;
  width: 35px;
  text-align: center;
  border-radius: 50%;
  font-size: 22px;
}
</style>
