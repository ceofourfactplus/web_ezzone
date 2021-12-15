<template>
  <div>
    <!-- Head -->
    <NavRM :header="'Raw Material'" />
    <SearchBar @search="serch_by_typing" />

    <Tabs @select_cate="query_category" />

    <!-- Table -->
    <div class="table-head">
      <div class="row" style="padding-right: 10px">
        <div class="col-6 items-in-row">Items</div>
        <div class="col-2 items-in-row">Qty</div>
        <div class="col-2 items-in-row">Unit</div>
        <div class="col-2 items-in-row">Status</div>
      </div>
    </div>
    <div class="my-table">
      <div class="my-row my-table" v-for="(item, idx) in raw_materials" :key="idx">
        <div class="col-6 items-in-row item-field">{{ item.item }}</div>
        <div class="col-2 items-in-row">{{ item.qty }}</div>
        <div class="col-2 items-in-row">{{ item.unit }}</div>
        <div class="col-2 items-in-row"><img src="../../assets/icon/Group95.png" alt="img"></div>
      </div>
    </div>

    <!-- <RawMaterial :materials=materials /> -->
  </div>
</template>

<script>
// import RawMaterial from '../../components/materials/RawMaterial.vue'
// import api_raw_material from "../../api/api_raw_material";
import Tabs from "../../components/materials/Tabs.vue"
import SearchBar from "../../components/materials/SearchBar.vue"
import NavRM from "../../components/materials/NavRM.vue"

export default {
  components: {
      // RawMaterial,
      Tabs,
      SearchBar,
      NavRM,
  },
  // mounted: {

  // },
  data() {
    return {
      category: "",
      materials: [],
      raw_materials: [
          {'item': 'นมข้นหวาน', 'qty': 2, 'unit': 'pack', 'status': '../../assets/icon/Group95.png'},
          {'item': 'นมข้นจืด', 'qty': 2, 'unit': 'pack', 'status': '../../assets/icon/Group95.png'},
          {'item': 'โซดา', 'qty': 20, 'unit': 'bag', 'status': '../../assets/icon/Group95.png'},
          {'item': 'สไปรท์', 'qty': 10, 'unit': 'bag', 'status': '../../assets/icon/Group95.png'},
      ],
    };
  },
  methods: {
    query_category(cate){
      console.log(cate)
      // api_raw_material.get(`query_category/${cate}`).then((response) => {
      //   this.materials = response.data;
      // });
    },
    select_category(cate) {
      this.category = cate;
      console.log(this.category);
    },
    serch_by_typing(val) {
      this.texts = val;
      console.log(val, 'views')
      // api_raw_material.get(`serch_by_typing/${val}`).then((response) => {
      //   this.materials = response.data
      //   console.log(response.data);
      // });
    },
  },
};
</script>

<style>
.my-table{
    background-color: #2f3446;
    color: white;
  }
  
  .table-head{
    background-color: #BD523F;
    color: white;
    
  }

  .table-head, .my-table{
    width: 90%;
    height: 55px;
    border-radius: 7px;
    text-align: center;
    font-size: 28px;
    font-weight: 200;
    margin-top: 10px;
    margin-left: 5.5%;
    margin-right: 5.5%;
  }
  
  .my-row{
    width: 100%;
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    counter-reset: div;
  }
  
  .my-row.my-table{
    margin-left: 0%;
  }

  .item-field{
    text-align: left;
  }

  .items-in-row{
    width: 100%;
    padding-top: 5px;
    padding-left: 15px;
  }
  
  .header {
    font-style: normal;
    font-weight: 600;
    font-size: 56px;
    /* line-height: 94px; */
    color: #fafafa;
    margin-top: 5%;
    /* left:55px; */
    /* position: fixed; */
  }
  .hamburger {
    top: 45px;
    right: 55px;
    position: fixed;
  }

</style>