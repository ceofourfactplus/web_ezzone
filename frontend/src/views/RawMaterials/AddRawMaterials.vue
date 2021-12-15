<template>
  <div>
    <!-- Head -->
    <NavRM :header="'Add Raw Material'" />
    <div class="row">
      <div style="width: 1px"></div>
      <div class="col-9" style="width: 415px; padding: 0px">
        <input
          type="text"
          class="search-barinadd"
          placeholder="Search"
          v-model="texts"
        />
        <img class="img-floating" src="../../assets/icon/Search.png" />
      </div>
      <button
        class="tab-item"
        style="margin: 6px; width: 150px; font-size: 22px"
      >
        Add RM
      </button>
      <button
        class="tab-item"
        style="margin: 6px; width: 150px; font-size: 22px"
      >
        All Added
      </button>
    </div>
    <div class="wrap-tabs">
      <Tabs />
    </div>
  </div>
</template>

<script>
// import RawMaterial from '../../components/materials/RawMaterial.vue'
// import api_raw_material from "../../api/api_raw_material";
import Tabs from "../../components/materials/Tabs.vue"
import NavRM from "../../components/materials/NavRM.vue";

export default {
  components: {
    // RawMaterial,
      Tabs,
    NavRM,
  },
  // mounted: {

  // },
  data() {
    return {
      category_name: "",
      categories: [
          'All',
          'Fresh Food',
          'Dried Food',
          'Garnish',
          'Package',
          'ETC.',
          '+',
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

<style>
.search-barinadd {
  background-size: contain;
  background-repeat: no-repeat;
  background-color: #3E4444;
  text-indent: 60px;
  padding-left: 10px;
  margin-left: 5px;
  border-radius: 60px;
  width: 94%;
  height: 50px;
  margin-top: 2%;
  /* Extra Styling */
}

.img-floating{
    width: 50px;
    left: 40px;
    top: 15%;
    position: fixed;
}
</style>