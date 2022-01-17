<template>
    <div>
        <nav-app :reward_menu="true">Consigner Product</nav-app>
    <!-- SearchBlock -->
        <div class="row" style="max-width:672px;">
            <div class="col-10 w-100 BlockSearch"><SearchBar @search="search" /></div>
            <div class="col-2 w-100 BlockNew"><b>+ New</b></div>
        </div>
    
    <!-- Category -->
        <div class="row AreaCategory">
            <div class="table-item BlockCategory">All</div>
            <div class="table-item BlockCategory">Drink</div>
            <div class="table-item BlockCategory">ของหวาน</div>
            <div class="table-item BlockCategory">ของคาว</div>

        </div>

    <!-- Header -->
        <div class="table-header Header">
            <div class="row" 
            style="width: 672px;
            height:50px;
            margin: 0px;">
                <div class="BlockProduct" >Product Name</div>
                <div class="BlockQty" >Qty</div>
                <div class="BlockPrice" >Price</div>
                <div class="BlockNotPaid" >Not Paid</div>
                <div>Status</div>
            </div>

        </div>
    <!-- Itme -->
            <div class="row table-item BlockItem" style="line-height:50px;">
                <div class="BlockProduct" style="text-align:left;">พายสับปะรดไส้เสาวรส</div>
                <div class="BlockQty" >20</div>
                <div class="BlockPrice" >60</div>
                <div class="BlockNotPaid" >54,101</div>
                <div class="BlockIcon" ><img src="../../assets/icon/check-mark.png" style="height:50;margin-top:-7px;"></div>
                <div class="BlockIcon" ><img src="../../assets/icon/bath-coin.png"  style="height:50;margin-top:-7px;"></div>
                <div class="BlockIcon" ><img src="../../assets/icon/edit-icon.png"  style="height:50;margin-top:-7px;"></div>
            </div>
    </div>
</template>

<script>
export default {  
  name: "ConsignerProduct",
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

.BlockNew {
    position: relative;
    left: 35px;
    top: 10px;
    border:1px solid #65B0F6;
    color: #65B0F6;
    border-radius: 10px;
    height:45px; 
    width: 145px;
    line-height:40px;
    font-size: 26px;

}

.AreaCategory {
    width: 672px;
    height: 45px;
    margin-left: 24px;
    margin-right: 24px;
    position: relative;
    padding:0px;
}

.BlockCategory {
    color: #ffffff;
    width: 95px;
    height: 100%;
    font-size:22px;
    line-height:45px;
    margin: 0px;
    margin-right: 5px;
    padding:0px;
    border-top-left-radius:  10px;
    border-top-right-radius: 10px;
    border-bottom-left-radius:  0px;
    border-bottom-right-radius: 0px;
}

.Header {
    width: 672px;
    height: 50px;
    margin-left: 24px;
    margin-right: 24px;
    margin-bottom: 20px;
    color: #ffffff;
    position: relative;
    line-height:45px;
    font-size:24px;
    padding:0px;
}

.BlockItem {
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

.BlockProduct {
    width: 260px;
    

}
.BlockQty {
    width: 63px;

}
.BlockPrice {
    width: 80px;

}
.BlockNotPaid {
    width: 122px;

}
.BlockIcon {
    width: 45px;
    padding:0px;
    padding-left: 5px;

}

</style>