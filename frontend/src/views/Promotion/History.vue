<template>
    <div>
        <nav-app>History</nav-app>
    <!-- SearchBlock -->
        <div class="BlockSearch">
            <SearchBar @search="search" /> 
        </div>   
    
    <!-- Header -->
        <div class="table-header" id="Header">
            <div class="row" 
            style="width: 672px;
            height:50px;
            margin: 0px;">
                <div class="col-1 w-100"></div>
                <div class="col-4 w-100" style="padding-left:30px;">Reward Name</div>
                <div class="col-2 w-100">Qty</div>
                <div class="col-3 w-100">Date</div>
                <div class="col-2 w-100">Status</div>
            </div>

        </div>
    <!-- Item -->
        <div class="row table-item" id="BlockItem" style="line-height:50px;">
            <div class="col-1" style="background-color:#717171;
            border-radius: 10px;
            width: 40px;
            height:40px;
            margin:5px;
            left:3px;
            position:relative;
            ">
            <img src="../../assets/img/delivery.png" alt="" style=";height: 40px;width: 40px;left:-11px;top:-9px;position:relative;"></div>
            <div class="col-4 w-100" style="text-align:left;">Item</div>
            <div class="col-2 w-100">14</div>
            <div class="col-3 w-100">12/12/2564</div>
            <div class="col-2 w-100" style="padding:0px;" v-if="eh.is_pre_order"><img src="../../assets/icon/cooking-status.png" alt="" style="height:38px;width:100px;top:-4px;position:relative;"></div>
            <div class="col-2 w-100" style="padding:0px;" v-else><img src="../../assets/icon/cooking-status.png" alt="" style="height:38px;width:100px;top:-4px;position:relative;"></div>
        </div>
    </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue"
import SearchBar from "../../components/materials/SearchBar.vue"
import { api_promotion } from "../../api/api_promotion";

export default {  
  name: "History",
  components : {
      NavApp,
      SearchBar,

  },
  data() {
      return{
        exchange_histories: [],
      }
  },
  methods: {
      fetchExchangeHistory() {
          api_promotion.get('exchange-history/').then(response => {
              console.log(response.data, 'history')
              this.exchange_histories = response.data
          })
      },
      search(val) {
          console.log(val)
      },
  },
  beforeMount() {
      this.fetchExchangeHistory()
  }

};

</script>

<style scoped>
.BlockSearch {
    width: 672px;
    height: 45px;
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 10px;
    margin-bottom: 20px;

}

#Header {
    width: 672px;
    height: 50px;
    margin-left: 24px;
    margin-right: 24px;
    margin-top: 10px;
    margin-bottom: 20px;
    color: #ffffff;
    position: relative;
    line-height:45px;
    font-size:26px;
    padding:0px;
}

#BlockItem {
    width: 672px;
    height: 50px;
    margin-left: 24px;
    margin-right: 24px;
    margin-top: 10px;
    position: relative;
    font-size: 23px;
    text-align: center;
    padding:0px;
}

</style>