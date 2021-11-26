<template>
   <div id="list-topping">
    <table-topping :all_topping="all_topping" @reload="reloadTopping()" @select_topping="selectTopping"/>
    <create-topping @reload="reloadTopping()" />
    <price-detail-topping :all_price="select_topping.price_topping"/>
    <update-topping :get_topping="select_topping" @save="reloadTopping()" />
  </div>
</template>

<script>
import PriceDetailTopping from '../../components/products/topping/PriceDetail.vue'
import TableTopping from "../../components/products/topping/Table.vue";
import CreateTopping from "../../components/products/topping/Create.vue";
import UpdateTopping from "../../components/products/topping/Update.vue";
import axios from 'axios';
export default {
  components: { TableTopping, CreateTopping, UpdateTopping, PriceDetailTopping},
  data() {
    return {
      all_topping:[],
      select_topping:{},
    };
  },
  methods:{
    reloadTopping(){
      axios.get('http://127.0.0.1:8000/product/topping/').then((response) => {
        this.all_topping = response.data
      })
    },
    selectTopping(topping){
      this.select_topping = topping
    },
  },
  mounted() {
    this.reloadTopping()
  }
};
</script>

<style>
</style>