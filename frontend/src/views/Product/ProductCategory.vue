<template>
  <div>
    <nav-app @back="back">Product Category</nav-app>
    <div class="row" v-if="is_staff">
      <div class="col-11 wrap-search">
        <SearchBar @search="serch_by_typing" />
      </div>
      <div style="padding-left: 0px">
        <button class="btn-ghost">+ New</button>
      </div>
    </div>
    <SearchBar v-else @search="serch_by_typing" />
    <Table :head1="'Name'" :head2="'Product'" :head3="'Amount'" :head4="''" />
    <div class="category-popup">
      <h2>Create Category</h2>
      <label for="category" style="color: white;">Name : &nbsp;</label>
      <input type="text" name="category" class="for-category" />
      <div class="btn btn_red"><span class="icon"></span><a href="#">Save</a><span></span></div>
    </div>
  </div>
</template>

<script>
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavAppHam.vue";
import Table from "../../components/main_component/Table.vue";
// import {apiProduct} from "../../api/apiProduct"

export default {
  components: {
    SearchBar,
    NavApp,
    Table,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
  },
  data() {
    return {
      is_staff: false,
    };
  },
  //   methods: {

  //   },
};
</script>

<style scoped>
.btn span.icon {
    background: url('../../assets/icon/correct.png') no-repeat;
    display: block;
    float: left;
    width: 10px;
    height: 40px;
}
.for-category {
    margin: 40px 0px 0px 0px;
    width: 300px;
    height: 50px;
}
h2 {
  width: 100%;
  height: 39px;
  margin: auto;
  top: 10px;
  color: #ea7c69;
}
.category-popup {
  position: absolute;
  top: 100px;
  left: 50px;
  font-weight: bold;
  font-size: 30px;
  width: 542px;
  height: 262px;
  background: #252836;
  border: 2px solid #ea7c69;
  box-sizing: border-box;
  border-radius: 10px;
}
.btn-ghost {
  border-color: #65b0f6;
  color: #65b0f6;
  width: 119px;
  height: 45px;
  margin: 0px 30px 0px 0px;
}
.wrap-search {
  min-width: 520px;
  width: fit-content;
  padding: 0px;
  margin-left: 45px;
}
</style>