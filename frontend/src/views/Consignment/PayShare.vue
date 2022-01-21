<template>
    <div>
        <nav-app :reward_menu="true">Pay Share</nav-app>

    <!-- Date -->
        <div class="row RowDate">
            <div class="col-9 w-100">Date :</div>
            <div class="col-3 w-100">12/12/2564</div>
        </div>

    <!-- Header -->
        <div class="row table-header Header">
                <div class="col-9 w-100" >List</div>
                <div class="col-3 w-100" >Bath</div>

        </div>

    <!-- Area Itme -->
        <div class="AreaBlockItem">
            
            <!-- Item -->
            <div class="row table-item BlockItem">
                <!-- List -->
                <div class="col-9 BlockList">เกี้ยวปู</div>
                <!-- Bath -->
                <div class="col-3 BlockBath">234,999</div>
            </div>            

        </div>

    <!-- Share -->
        <div class="AreaShare">
            <!-- Row Share -->
            <div class="row RowShare">

                <!-- Detil -->
                <div class="col-2 BlockDetil">Share</div>
                <!-- Colon -->
                <div class="col-1 BlockColon">:</div>
                <!-- Input Block -->
                <div class="col-6 BlockInput">
                    <input type="text" v-model="input_customer" 
                    style="background: #717171;
                    border-radius: 10px;
                    width: 100%;
                    height: 100%;
                    font-size: 100%;"/>
                </div>
                <!-- Icon Bath -->
                <div class="col-1 IconBath">
                    <img src="../../assets/icon/Bath.png" style="position:relative;top:-10%">
                </div>
                <!-- COnfirm Button -->
                <div class="col-2 BlockButtonConfirm">Confirm</div>

            </div>

            <!-- Row ผู้รับเงิน -->
            <div class="row RowShare">

                <!-- Detil -->
                <div class="col-2 BlockDetil">ผู้รับเงิน</div>
                <!-- Colon -->
                <div class="col-1 BlockColon">:</div>
                <!-- Input Block -->
                <div class="col-9 BlockInput">
                    <input type="text" v-model="input_customer" 
                    style="background: #717171;
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
  name: "PayShare",
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

/* Row Date */
.RowDate {
    height: 60px;
    width: 94%;
    margin-left: 3%;
    margin-right: 3%;
    margin-top: 5%;
    margin-bottom: 1%;
    color: #EA7C69;
    text-align: right;
    font-size: 200%;

}

/* Header */
.Header {
    height: 60px;
    width: 94%;
    margin-left: 3%;
    margin-right: 3%;
    color: #ffffff;
    position: relative;
    line-height:55px;
    font-size:220%;
    padding:0%;
}

/* Item */
.AreaBlockItem {
    height: 680px;
    width: 94%;
    margin-left: 3%;
    margin-right: 3%;
}

.BlockItem {
    height: 60px;
    width: 100%;
    margin: 0%;
    margin-top: 2%;
    position: relative;
    font-size: 185%;
    text-align: center;
    line-height: 200%;
    padding: 0%;
}

.BlockList {
    text-align: left;
    padding-left: 3%;
    height: 100%;
    width: 100%;
}

.BlockBath {
    height: 100%;
    width: 100%;

}

/* Share */
.AreaShare {
    height: 200px;
    width: 94%;
    margin-left: 3%;
    margin-right: 3%;
    padding-top: 5%;
    color: #ffffff;
    line-height:55px;
    font-size:200%;

}

.RowShare {
    height:34.5%;
    width: 100%;
    margin: 0%;
    margin-bottom: 3%;
    padding: 0%;
    padding-left: 2.5%;
    padding-right: 2.5%;
}

.BlockDetil {
    width: 100%;
    height: 100%;
    line-height: 125%;
    text-align: left;
    padding: 0%;
    
}
.BlockColon {
    width: 100%;
    height: 100%;
    line-height: 125%;
    
}
.BlockInput {
    width: 100%;
    height: 100%;
    padding: 0%;
}
.IconBath {
    width: 100%;
    height: 100%;
    
}
.BlockButtonConfirm { 
    width: 100%;
    height: 100%;
    border-radius: 10px;
    border: 1px solid #65B0F6;
    color: #65B0F6;
    font-size: 95%;
    padding: 0%;
    line-height: 155%;
}

</style>