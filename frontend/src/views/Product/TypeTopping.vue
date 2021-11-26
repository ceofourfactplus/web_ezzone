<template>
  <div id="type-topping">
      <type-topping-table :type_toppings="type_toppings" @reload="reloadTypeTopping" @select_type="SelectType" />
      <type-topping-update @reload="reloadTypeTopping" :select_type="select_type" />
      <type-topping-create @reload="reloadTypeTopping"/>
  </div>
</template>

<script>
import axios from 'axios'
import TypeToppingTable from '../../components/products/type-topping/Table.vue'
import TypeToppingUpdate from '../../components/products/type-topping/Update.vue'
import TypeToppingCreate from '../../components/products/type-topping/Create.vue'
export default {
  components: { TypeToppingTable,TypeToppingUpdate,TypeToppingCreate },
  data(){
    return{ 
      type_toppings:[],
      select_type:null
    }
  },
  methods: {
    reloadTypeTopping(){
      axios.get("http://127.0.0.1:8000/product/type-topping/").then((response)=>{
        this.type_toppings = response.data 
      })
    },
    SelectType(type){
      this.select_type = type
    }
  },
  mounted() {
    this.reloadTypeTopping();
  }
}
</script>

<style>

</style>