<template>
    <div>
        <nav-app :reward_menu="true">Record Product</nav-app>
    <!-- SearchBlock -->
        <div class="row" style="width: 770px;">
            <div class="BlockSearch"><SearchBar @search="search" /></div>
            <div class="BlockNew" style="border:1px solid #50D1AA;color: #50D1AA;"><b>Add</b></div>
            <div class="BlockNew" style="border:1px solid #FF7CA3;color: #FF7CA3;"><b>Out</b></div>
            <div class="BlockNew" style="border:1px solid #FFB572;color: #FFB572;"><b>Pay</b></div>
        </div>

    <!-- Header -->
        <div class="table-header Header">
            <div class="row" 
            style="width: 770px;
            height:60px;
            margin: 0px;">
                <div class="BlockDate" >Date</div>
                <div class="BlockAdd" >Add</div>
                <div class="BlockSold" >Sold</div>
                <div class="BlockOut" >Out</div>
                <div class="BlockShare">Share</div>
                <div class="BlockStatus">Status</div>
            </div>

        </div>
    <!-- Itme -->
            <div class="row table-item BlockItem" style="line-height:55px;">

                <div class="BlockDate" style="text-align:left;">
                    <!-- CheckBok -->
                    <div class="checkbox-white" style="display:inline-block;">
                        <input
                        type="checkbox"
                        :value="true"
                        style=""
                        @input="selectAllItem"/>
                    </div>

                    <!-- Date -->
                    <div class="Date">11/12/64</div>

                </div>
                <div class="BlockAdd" >20</div>
                <div class="BlockSold" >60</div>
                <div class="BlockOut" >0</div>
                <div class="BlockShare">300</div>
                <div class="BlockStatus"><img src="../../assets/icon/bath-coin.png"  style="height:45;width:45px;margin-top:-5px;"></div>
            </div>
    </div>
</template>

<script>
export default {  
  name: "RecordProduct",
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
    width: 450px;
    height: 60px;
    margin-left: 20px;
    margin-right: 0px;
    margin-top: 10px;
    margin-bottom: 20px;

}

.BlockNew {
    position: relative;
    top: 10px;
    border-radius: 10px;
    height:60px; 
    width: 106px;
    line-height:53px;
    margin-right: 10px;
    font-size: 34px;

}

.Header {
    width: 770px;
    height: 60px;
    margin-left: 24px;
    margin-right: 24px;
    margin-bottom: 20px;
    color: #ffffff;
    position: relative;
    line-height:55px;
    font-size:32px;
    padding:0px;
}

.BlockItem {
    width: 770px;
    height: 60px;
    margin-left: 24px;
    margin-right: 24px;
    margin-top: 10px;
    position: relative;
    font-size: 30px;
    text-align: center;
    padding:0px;
}

.BlockDate {
    width: 230px;
    

}

.BlockAdd {
    width: 100px;

}

.BlockSold {
    width: 100px;

}

.BlockOut {
    width: 100px;

}

.BlockShare {
    width: 120px;

}

.BlockStatus {
    width: 120px;

}

/* CheckBox */
.checkbox-white input:checked::after {
  font-size: 20px;
  line-height: 23px;
  top: -1px;
  left: 2px;
  height: 30px;
  width: 30px;
}
.checkbox-white input::before {
  height: 30px;
  width: 30px;
  margin-top:0px;
  margin-left:5px;
  border: 3px solid #EA7C69;
}

.Date {
    display: inline-block;
    margin-left:20px;

}
</style>