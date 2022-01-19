<template>
  <div>
    <!-- Head Name Page -->
    <div class="row Header">
        <div class="col-1 w-100" style="padding-left:0%;"><img src="../../assets/icon/save.png" style="height:55%"></div>
        <div class="col-10 w-100" style="line-height: 105px;"><b>New Consigner</b></div>
        <div class="col-1 w-100" style="padding-right:0%;"><img src="../../assets/img/btn-close.png" style="height:55%"></div>
    </div>
    
    <!-- Row 1 -->
    <div class="row Area ImgAndAmount">
        <!-- Picture -->
        <div class="col-3 w-100 ColArea"><img src="../../assets/icon/User.png" style="width:100%"></div>
        <!-- Amount Sales -->
        <div class="col-3 w-100 ColArea">
            <div class="BlockAmount">Amount Sales</div>
            <div class="BlockTotal"><b>999,999</b></div>
        </div>
        <!-- Share Received -->
        <div class="col-3 w-100 ColArea">
            <div class="BlockAmount">Share Received</div>
            <div class="BlockTotal"><b>999,999</b></div>
        </div>
        <!-- Share Not Received -->
        <div class="col-3 w-100 ColArea">
            <div class="BlockAmount">Share Not Received</div>
            <div class="BlockTotal"><b>999,999</b></div>
        </div>

    </div>
    <!-- Edit Name -->
    <div class="row Area InputDetail">
        <div class="col-2 w-100 BlockDetail"><b>Name</b></div>
        <div class="col-1 w-100"><b>:</b></div>
        <div class="col-9 w-100 BlockInput">
            <input type="text" v-model="input_customer" 
            style="background: #717171;
            border-radius: 10px;
            width: 100%;
            height: 100%;
            font-size: 100%;"/>
        </div>

    </div>
    <!-- Edit ID Card -->
    <div class="row Area InputDetail">
        <div class="col-2 w-100 BlockDetail"><b>ID Card</b></div>
        <div class="col-1 w-100"><b>:</b></div>
        <div class="col-9 w-100 BlockInput">
            <input type="text" v-model="input_customer" 
            style="background: #717171;
            border-radius: 10px;
            width: 100%;
            height: 100%;
            font-size: 100%;"/>
        </div>
        
    </div>
    <!-- Edit Email -->
    <div class="row Area InputDetail">
        <div class="col-2 w-100 BlockDetail"><b>Email</b></div>
        <div class="col-1 w-100"><b>:</b></div>
        <div class="col-9 w-100 BlockInput">
            <input type="text" v-model="input_customer" 
            style="background: #717171;
            border-radius: 10px;
            width: 100%;
            height: 100%;
            font-size: 100%;"/>
        </div>

    </div>
    <!-- Edit Line -->
    <div class="row Area InputDetail">
        <div class="col-2 w-100 BlockDetail"><b>Line</b></div>
        <div class="col-1 w-100"><b>:</b></div>
        <div class="col-9 w-100 BlockInput">
            <input type="text" v-model="input_customer" 
            style="background: #717171;
            border-radius: 10px;
            width: 100%;
            height: 100%;
            font-size: 100%;"/>
        </div>

    </div>
    <!-- Edit Phone -->
    <div class="row Area InputDetail">
        <div class="col-2 w-100 BlockDetail"><b>Phone</b></div>
        <div class="col-1 w-100"><b>:</b></div>
        <div class="col-9 w-100 BlockInput">
            <input type="text" v-model="input_customer" 
            style="background: #717171;
            border-radius: 10px;
            width: 100%;
            height: 100%;
            font-size: 100%;"/>
        </div>

    </div>
    <!-- Edit Address -->
    <div class="row Area InputDetailAddress">
        <div class="col-2 w-100 BlockDetail"><b>Address</b></div>
        <div class="col-1 w-100"><b>:</b></div>
        <div class="col-9 w-100 BlockInput">
            <textarea type="text" v-model="input_customer" 
            style="background: #717171;
            border-radius: 10px;
            width: 100%;
            height: 100%;
            font-size: 100%;"/>
        </div>

    </div>
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import SavePopup from "../../components/main_component/SavePopup.vue"

export default {
  name: "NewConsigner",
  components: {
      SavePopup,
  },
  data() {
    return {
        alert: false,
        CustommerPhone: null,
        input_customer: "",
        temp_date: null,
        selector_status: false,
        selector_customer: [],
        customer_point: [],
    };
  },
  
};
</script>

<style scoped>
.Area {
    width: 95%;
    margin-left: 2.5%;
    margin-right: 2.5%;
}

.Header {
    color:#fff;
    font-size: 410%;
    text-align: center;
    position: relative;
    height: 7.6%;
    margin-left: 2%;
    margin-right: 2%;
    margin-bottom: 10px;  
    margin-top: 1%;  
}

.ImgAndAmount {
    margin-top: 5%;
    height: 180px;
}

.InputDetail{
    margin-top: 6.5%;
    margin-bottom: 10px;
    height: 60px;
    font-size: 230%;
    color: #fff;

}

.InputDetailAddress{
    margin-top: 6.5%;
    margin-bottom: 10px;
    height: 195px;
    font-size: 230%;
    color: #fff;

}

.ColArea {
    padding: 0%;
    height: 100%;
    /* background-color: blueviolet; */
}

.BlockAmount {
    margin-left: 10%;
    margin-right: 0%;
    margin-top: 2.5%;
    margin-bottom: 2.5%;
    height: 45%;
    line-height: 125%;
    font-size: 200%;
    color: #fff;
}

.BlockTotal {
    margin-left: 10%;
    margin-right: 0%;
    margin-top: 5%;
    margin-bottom: 2.5%;
    height: 40%;
    border-radius: 10px;
    line-height: 170%;
    font-size: 250%;
    color: #fff;
    background-color: #BD523F;
}

.BlockDetail {
    text-align: left;
    padding: 0%;

}

.BlockInput {
    padding: 0%;

}
</style>