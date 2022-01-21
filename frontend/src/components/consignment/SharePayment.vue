<template>
    <div class="MainArea">
    <!-- Head Name Page -->
        <div class="row Header">
            <div class="col-1 w-100" style="padding-left:10%;"><img src="../../assets/img/btn-close.png" style="height:50%"></div>
            <div class="col-10 w-100" style="line-height: 160%;"><b>Share Payment</b></div>
        </div>
    <!-- Checkbox Row -->
        <div class="row RowCheckBox">
            <!-- Pay By -->
            <div class="col-2 BlockPayBy">Pay By :</div>
            <!-- CheckBox -->
            <div class="col-1 BlockCheckBox">
                <div class="checkbox-white" style="display:inline-block;">
                        <input
                        type="checkbox"
                        :value="true"
                        style="background-color:rgba(250, 250, 250, 0);"
                        @input="selectAllItem"/>
                </div>
            </div>
            <!-- Cash -->
            <div class="col-2 BlockTextCheckbox">Cash</div>
            <!-- CheckBox -->
            <div class="col-1 BlockCheckBox">
                <div class="checkbox-white" style="display:inline-block;">
                    <input
                    type="checkbox"
                    :value="true"
                    style="background-color:rgba(250, 250, 250, 0);"
                    @input="selectAllItem"/>
                </div>
            </div>
            <!-- Transfer -->
            <div class="col-2 BlockTextCheckbox">Transfer</div>
            <!-- Confirm -->
            <div class="col-4 w-100 BlockConfirm">
                <div class="BtnConfirm"><b>Confirm</b></div>
            </div>

        </div>

    <!-- Share To Paid Row -->
        <div class="row RowShareToPaid">
            <div class="col-4 BlockSTP">Share to paid</div>
            <div class="col-7 BlockInput">
                <input type="text" v-model="input_customer" 
                    style="background: ##717171;
                    border-radius: 10px;
                    width: 100%;
                    height: 100%;
                    font-size: 100%;"/>
            </div>
            <div class="col-1 BlockIconBath"><b>฿</b></div>

        </div>

    <!-- Header Item -->
        <div class="row table-header HeaderNameItem">
                <div class="col-3 w-100" >Date</div>
                <div class="col-4 w-100" >Prod Name</div>
                <div class="col-1 w-100" >Qty</div>
                <div class="col-2 w-100" >Sales</div>
                <div class="col-2 w-100" >Share</div>

        </div>

    <!-- Item -->
        <div class="AreaBlockItem">
            <div class="row RowItem">
                <div class="col-3 BlockDate" >11/12/64</div>
                <div class="col-4 BlockProdName" >โยเกิร์ตสตอเบอรี่</div>
                <div class="col-1 BlockQty" >30</div>
                <div class="col-2 BlockSales" >3,000</div>
                <div class="col-2 BlockShare" >2,000</div>
            </div>

        </div>

    <!-- Input & Sign -->
        <div class="AreaInputAndSign">
            <!-- Received by -->
            <div class="row RowBlockInput">
                <div class="col-3 BlockDetail">Received by</div>
                <div class="col-1 BlockColon">:</div>
                <div class="col-8 BlockInput">
                    <input type="text" v-model="input_customer" 
                    style="background: ##717171;
                    border-radius: 10px;
                    width: 100%;
                    height: 100%;
                    font-size: 100%;"/>
                </div>
            </div>
            
            <!-- Phone No -->
            <div class="row RowBlockInput">
                <div class="col-3 BlockDetail">Phone No</div>
                <div class="col-1 BlockColon">:</div>
                <div class="col-8 BlockInput">
                    <input type="text" v-model="input_customer" 
                    style="background: ##717171;
                    border-radius: 10px;
                    width: 100%;
                    height: 100%;
                    font-size: 100%;"/>
                </div>
            </div>
            
            <!-- Sign Here -->
            <div class="row RowBlockSignHere">
                <div class="col-4"></div>
                <div class="col-8 BlockSignHere">
                    <input type="text" v-model="input_customer" 
                    style="background: ##717171;
                    border-radius: 10px;
                    width: 100%;
                    height: 100%;
                    font-size: 100%;"/>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
export default {  
  name: "SharePayment",
  components : {
      NavApp,

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
</script>

<style scoped>

/* MainArea */
.MainArea {
    height: 925px;
    width: 90%;
    margin-left: 5%;
    margin-right: 5%;
    margin-top: 15%;
    background-color: #252836;
    position: absolute;
    border-radius: 20px;

}

.AreaRow {
    width: 96%;
    margin-left: 2%;
    margin-right: 2%;
}

/* Header */
.Header {
    color:#fff;
    font-size: 310%;
    text-align: center;
    position: relative;
    height: 70px;
    margin-left: 2%;
    margin-right: 2%;
    margin-bottom: 10px;  
    margin-top: 1%;  
}

/* Row CheckBox */
.RowCheckBox {
    height: 60px;
    width: 96%;
    margin-left: 2%;
    margin-right: 2%;
    margin-top: 2%;
    color:#fff;
    font-size: 220%;

}

.BlockPayBy {
    width: 100%;
    padding:0%;

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

.BlockTextCheckbox {
    width: 100%;
    text-align: left;
    padding:0%;
    font-size:80%;
    padding-top: 7%;
    padding-left: 3%;
}

.BlockCheckBox {
    width: 100%;

}

.BlockConfirm {
    padding-left:30%;

}

.BtnConfirm {
    height: 90%;
    width: 100%;
    border:3px solid #65B0F6;
    border-radius: 10px;
    color: #65B0F6;
    font-size: 90%;
    margin-right:0%;
    line-height: 120%;
    position:relative;


}

/* Share to paid */
.RowShareToPaid {
    height: 60px;
    width: 96%;
    margin-left: 2%;
    margin-right: 2%;
    margin-top: 2%;
    color:#fff;
    font-size: 220%;

}

.BlockSTP {
    width: 100%;
    height: 100%;
    padding:0%;
    text-align: left;

}

.BlockInput {
    width: 100%;
    height: 100%;
    padding: 0%;
}

.BlockIconBath {
    width: 100%;
    height: 100%;
    
}


/* HeaderNameItem */
.HeaderNameItem {
    height: 60px;
    width: 96%;
    margin-top: 1%;
    margin-left: 2%;
    margin-right: 2%;
    color: #ffffff;
    position: relative;
    line-height:55px;
    font-size:170%;
    padding:0%;
}

/* Item */
.AreaBlockItem {
    height: 300px;
    width: 96%;
    margin-left: 2%;
    margin-right: 2%;

}

.RowItem {
    height: 19%;
    width: 100%;
    margin: 0%;
    margin-top: 2%;
    position: relative;
    color: #fff;
    font-size: 160%;
    text-align: center;
    line-height: 200%;
    padding: 0%;
    background-color: #303344;
    border-radius: 10px;
}

.BlockDate {
    width: 100%;
    height: 100%;

}
.BlockProdName {
    width: 100%;
    height: 100%;
    text-align: left;
    padding-left:0%;

}
.BlockQty {
    width: 100%;
    height: 100%;
    padding:0%;

}
.BlockSales {
    width: 100%;
    height: 100%;

}
.BlockShare {
    width: 100%;
    height: 100%;

}

/* Input And Sign */
.AreaInputAndSign {
    height: 300px;
    width: 96%;
    margin-left: 2%;
    margin-right: 2%;
    margin-top: 0%;
    padding-top: 2%;
    padding: 0%;

}

.RowBlockInput {
    height: 20%;
    width: 100%;
    margin: 0%;
    margin-top: 2%;
    color:#fff;
    font-size: 210%;
    
    
}

.RowBlockSignHere {
    height: 46%;
    width: 100%;
    margin: 0%;
    margin-top: 2%;
    color:#fff;
    font-size: 210%;
    
    
}

.BlockDetail {
    width: 100%;
    height: 100%;
    line-height: 155%;
    text-align: left;
    padding: 0%;
    
}

.BlockColon {
    width: 100%;
    height: 100%;
    line-height: 155%;
    
}

.BlockSignHere {
    width: 100%;
    height: 100%;
    padding: 0%;

}

</style>