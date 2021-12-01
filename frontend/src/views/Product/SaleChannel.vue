<template>
  <div id="sale-channel">
      <sale-channel-table :sales_channels="sales_channels" @reload="reloadSaleChannel" @select_channel="SelectChannel" />
      <sale-channel-update @reload="reloadSaleChannel" :select_sale_channel="select_channel"></sale-channel-update>
      <sale-channel-create @reload="reloadSaleChannel"/>
  </div>
</template>

<script>
import axios from 'axios'
import SaleChannelTable from '../../components/products/sale-channel/Table.vue'
import SaleChannelUpdate from '../../components/products/sale-channel/Update.vue'
import SaleChannelCreate from '../../components/products/sale-channel/Create.vue'
export default {
  components: { SaleChannelTable,SaleChannelUpdate,SaleChannelCreate },
  data(){
    return{ 
      sales_channels:[],
      select_channel:null
    }
  },
  methods: {
    reloadSaleChannel(){
      axios.get("http://127.0.0.1:8000/product/sale-channel/").then((response)=>{
        this.sales_channels = response.data 
      })
    },
    SelectChannel(channel){
      this.select_channel = channel
    }
  },
  mounted() {
    this.reloadSaleChannel();
  }
}
</script>

<style>

</style>