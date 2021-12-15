<template>
  <div>
    <nav-app @back="back">Add Raw Material</nav-app>
    <div class="row">
      <div class="col-10 wrap-search">
        <SearchBar />
      </div>
      <button class="btn-ghost">Confirm Add</button>
    </div>
    <div class="table-head">
        <div class="row" style="padding-right: 10px">
          <div class="col-6 items-in-row">Items</div>
          <div class="col-2 items-in-row">+ Qty</div>
          <div class="col-2 items-in-row">Unit</div>
          <div class="col-2 items-in-row">Price/Unit</div>
          <div class="col-2 items-in-row">Total Price</div>
        </div>
      </div>
    <table class="table table-add-rm" style="color: white;">
      <tr class="parent-tr" width="676px">
        <th width="276px">Item</th>
        <th>+ Qty</th>
        <th>Unit</th>
        <th>Price/Unit</th>
        <th>Total Price</th>
      </tr>
      <tr class="child-tr">
        <td class="table-item" width="76px"><input type="checkbox" name="" id=""></td>
        <td class="table-item" width="200px">Item</td>
        <td class="table-item" style="background-color: #889898;">9999</td>
        <td class="table-item" style=""></td>
        <td class="table-item" style=""></td>
        <td class="table-item" style=""></td>
      </tr>
    </table>
  </div>
</template>

<script>
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";

export default {
  components: {
    NavApp,
    SearchBar,
  },
  // mounted() {

  // },
  data() {
    return {
      category_name: "",
      categories: [
        "All",
        "Fresh Food",
        "Dried Food",
        "Garnish",
        "Package",
        "ETC.",
        "+",
      ],
      // id: Null,
      // img: NullNull,
      // status: Null,
      // name: Null,
      // balance: Null,
      // minimum: Null,
      // avg_price: Null,
      // max_price: Null,
      // min_price: Null,
      // max_price_supplier_id: Null,
      // min_price_supplier_id: Null,
      // in_refrigerator: Null,
      // create_by_id: Null,
      // update_by_id: Null,
      // category_id: Null,
      // unit_id: Null,
    };
  },
  methods: {
    // createCategory() {
    //   const data = {'name': this.category_name}
    //   axios.post('create_category/', data).then(response => {
    //     console.log(response.data)
    //   })
    // },
  },
};
</script>

<style scoped>
.table-add-rm {
  color: white;
  width: 676px;
  height: 45px;
  font-size: 24px;
  border-radius: 200px;
  border: none;
  margin-left: 20px;
  border-collapse: separate;
  border-spacing: 0 10px;
}
.parent-tr {
  background-color: #bd523f;
  border: none;
}
.child-tr {
  margin-top: 10px;
  border: none;
}
th {
  border: none;
}
.table-item {
  height: 45px;
  margin-top: 20px;
  background-color: #2f3446;
  border: none;
}
.head-section {
  /* width: 676px; */
  height: 60px;
  color: white;
  background-color: #bd523f;
  border-radius: 10px;
  margin-top: 10px;
  margin-left: 20px;
  font-weight: bold;
  font-size: 24px;
  line-height: 31px;
}

.head-section-item.head,
.head-section-item {
  margin: 0px;
  display: inline;
  color: white;
}

.head-section-item.head {
  width: 276px;
  font-size: 24px;
  text-align: center;
}

.head-section-item {
  width: 100px;
}

.btn-ghost {
  border-color: #65b0f6;
  color: #65b0f6;
  width: 242px;
  height: 45px;
}
.btn-beside-search {
  margin: 3px;
  margin-left: 0px;
  width: 120px;
  font-size: 22px;
}
.wrap-search {
  min-width: 424px;
  width: fit-content;
  padding: 0px;
  margin-left: 0px;
}
</style>