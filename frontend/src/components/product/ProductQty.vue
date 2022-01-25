<template>
    <div class="dark">
        <div class="AreaPopup">
        <!-- Head Name Page -->
            <div class="row Header">
                <div class="col-1 w-100" style="padding-left:10%;"></div>
                <div class="col-10 w-100" style="line-height: 160%;"><b>Add Consignment</b></div>
                <div class="col-1 w-100" style="padding-left:10%;"><img src="../../assets/img/btn-close.png" style="height:60%"></div>
            </div>
        <!-- MainArea -->
            <div class="MainArea">
                <!-- Image Qty Reason -->
                <div class="row AreaImg">
                    <!-- Img Block -->
                    <div class="col-5 BlockImg">
                        <div class="EditImg">
                            <img src="../../assets/icon/el_camera.png" style="position:relative;top:-2.9px;left:-5px;">
                            <b>Edit</b>
                        </div>
                        <img src="" style="height:100%; width:100%; position:absolute; left:0%; border-radius:10%">
                    </div>
                    
                    <div class="col-7 AreaRowInput">
                        <!-- Qty Input -->
                        <div class="row RowBlockInput" style="margin-top:0%;">
                            <div class="col-3 BlockDetail">Name</div>
                            <div class="col-1 BlockColon">:</div>
                            <div class="col-8 BlockInput" style="text-align:left;">ทาร์ตไข่</div>
                            
                        </div>
                        <!-- Qty Input -->
                        <div class="row RowBlockInput" style="line-height:100%;">
                            <div class="col-3 BlockDetail">+ QTY</div>
                            <div class="col-1 BlockColon">:</div>
                            <div class="col-5 BlockInput">
                                <input type="text" v-model="input_customer" 
                                style="background: #717171;
                                border-radius: 10px;
                                width: 100%;
                                height: 100%;
                                font-size: 100%;"/>
                            </div>
                            <div class="col-3 BlockDetail" style="text-align:right;">กล่อง</div>
                        </div>

                        <!-- EXP -->
                        <div class="row RowBlockInput" style="margin-top:15%;line-height:100%;">
                            <div class="col-3 BlockDetail">EXP</div>
                            <div class="col-1 BlockColon">:</div>
                            <div class="col-7 BlockInput">
                                <input type="date" v-model="input_customer" 
                                style="background: #717171;
                                border-radius: 10px;
                                width: 100%;
                                height: 100%;
                                font-size: 100%;"/>
                            </div>
                        </div>
                        

                    </div>

                </div>
                <!-- Confirm Button -->
                <div class="AreaConfirmButton">
                    <div class="ConfirmButton">Confirm</div>
                </div>

            </div>
            

        </div>
    </div>
        
</template>

<script>
export default {  
  name: "ProductQty",
  components : {
     

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

</script>

<style scoped>

/* AreaPopup */
.AreaPopup {
    height: 590px;
    width: 90%;
    margin-left: 5%;
    margin-right: 5%;
    margin-top: 15%;
    border-radius: 20px;
    background-color: #252836;
    position: absolute;

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

/* MainArea */
.MainArea {
    height: 460px;
    width: 96%;
    margin-left: 2%;
    margin-right: 2%;
    margin-top: 5%;
    padding-top: 0.5%;
    border-radius: 20px;
    background-color: #303344;
}

/* AreaImg */
.AreaImg {
    height: 68%;
    width: 96%;
    margin-top: 3%;
    margin-left: 2%;
    margin-right: 2%;
    padding-top: 2%;
    padding: 0%;

}

.BlockImg {
    background-color: #717171;
    width: 100%;
    height: 100%;
    position: relative;
    text-align: center;
    padding:0px;
    margin:0px;
    border-radius: 25px;

}

.EditImg {
    color: #000000;
    position: absolute;
    text-align: right;
    font-size: 18px;
    padding-right: 8px;
    border-radius: 5px;
    top: 83%;
    left: 9%;
    height: 30px;
    width: 80px;
    line-height: 30px;
    background-color: #C4C4C4;
}

.AreaRowInput {
    width: 100%;
    height: 100%;
    padding-right: 0%;
    padding-left: 5%;

}
 
/* Input And Sign */
.AreaInputAndSign {
    height: 300px;
    width: 96%;
    margin-top: 0%;
    margin-left: 2%;
    margin-right: 2%;
    padding-top: 2%;
    padding: 0%;

}

.RowBlockInput {
    height: 20%;
    width: 100%;
    margin: 0%;
    margin-top: 12%;
    color:#fff;
    font-size: 200%;
     
}

.BlockInput {
    width: 100%;
    padding: 0%;
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

.AreaConfirmButton {
    height: 18%;
    width: 96%;
    margin-top: 5%;
    margin-left: 2%;
    margin-right: 2%;
    padding-top: 2%;
    padding: 0%;

}

.ConfirmButton {
    height: 80%;
    width: 30%;
    margin-left:  35%;
    margin-right: 35%;
    border: 2px solid #50D1AA;
    border-radius: 10px;
    color: #50D1AA;
    font-size: 200%;
}
</style>