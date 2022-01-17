<template>
    <div>
        <nav-app :reward_menu="true">Consigner</nav-app>
    <!-- SearchBlock -->
        <div class="row" style="max-width:672px;">
            <div class="col-10 w-100 BlockSearch"><SearchBar @search="search" /></div>
            <div class="col-2 w-100 BlockSelect"><b>+ New</b></div>
        </div>
            
    <!-- Header -->
        <div class="table-header" id="Header">
            <div class="row" 
            style="width: 672px;
            height:50px;
            margin: 0px;">
                <div class="col-5 w-100 BlockRow" >Consigner Name</div>
                <div class="col-2 w-100 BlockRow" >Prod</div>
                <div class="col-2 w-100 BlockRow" >Prod Qty</div>
                <div class="col-2 w-100 BlockRow" >Status</div>
                <div class="col-1 w-100 BlockRow" ></div>
            </div>

        </div>
    <!-- Itme -->
            <div class="row table-item" id="BlockItem" style="line-height:50px;">
                <div class="col-5 w-100 BlockRow" style="text-align:left;padding-left:15px;">4!+</div>
                <div class="col-2 w-100 BlockRow" >20</div>
                <div class="col-2 w-100 BlockRow" >60</div>
                <div class="col-1 w-100 BlockRow" ><img src="../../assets/icon/check-mark.png" style="height:50;margin-top:-7px;"></div>
                <div class="col-1 w-100 BlockRow" ><img src="../../assets/icon/bath-coin.png"  style="height:50;margin-top:-7px;"></div>
                <div class="col-1 w-100 BlockRow" ><img src="../../assets/icon/edit-icon.png"  style="height:50;margin-top:-7px;"></div>
            </div>
    </div>
</template>

<script>
export default {  
  name: "Consigner",
  components : {
      NavApp,
      SearchBar,

  },
  data() {
      return{
        
      }
  },
  methods: {
      search(val) {
          console.log(val)
      }
  }

};
import NavApp from "../../components/main_component/NavApp.vue"
import SearchBar from "../../components/materials/SearchBar.vue"
</script>

<style scoped>
.BlockSearch {

    height: 45px;
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 10px;
    margin-bottom: 20px;

}

.BlockSelect {

    position: relative;
    left: 25px;
    top: 10px;
    border:1px solid #65B0F6;
    color: #65B0F6;
    border-radius: 10px;
    height:45px; 
    width: 137px;
    line-height:40px;
    font-size: 26px;

}

.BlockRow {

    padding: 0px;

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