<template>
  <div>

    <div class="row Header">
        <div class="col-1 w-100" style="padding-left:0px;"><img src="../../assets/icon/save.png" style="height:45px"></div>
        <div class="col-10 w-100" style="line-height: 85px;"><b>New Consignment</b></div>
        <div class="col-1 w-100" style="padding-right:0px;"><img src="../../assets/img/btn-close.png" style="height:45px"></div>
    </div>
    <!-- CustommerPhone Block -->
    <div class="row Area Name">
      <div class="col-2 w-100"
      style="font-size: 30px;
      padding: 0px;
      text-align: right;
      color: #ffffff"
      >Name :</div>
      <div class="input col-10">
        <input type="text" v-model="input_customer" 
        style="background: #717171;
        border-radius: 10px;
        width: 535px;
        height: 50px;
        margin-top: 10px;" />
        <ul class="selector" v-if="selector_status">
          <li v-for="cus in selector_customer" :key="cus.id">
            <pre @click="select_customer(cus)"
              >{{ phone_number_layout(cus.phone_number) }}  :{{
                cus.first_name
              }}</pre
            >
          </li>
        </ul>
      </div>
    </div>

    <!-- Img Detail -->
    <div class="row Area Img" style="height:305px;padding-top:25px;padding-bottom:15px;">
        <!-- Img Block -->
        <div class="col-5 RedeemImg" style="background-color: #717171;">
            <div class="EditImg">
                <img src="../../assets/icon/el_camera.png" style="position:relative;top:-2.9px;left:-5px;">
                <b>Edit</b>
            </div>
            <img src="" style="height:260px;width:253px;position: absolute;left:0px; border-radius:10%">
        </div>
        <!-- Detail Block -->
        <div class="col-7 RedeemImg" style="margin:0px; width:100%;">
            <!-- Code -->
            <div class="row AreaDetail">
                <div class="BlockSubject">Code</div>
                <div class="BlockColon">:</div>
                <div class="BlockInputCode"><input type="text" 
                    style="background: #717171;
                    border-radius: 10px;
                    width: 230px;
                    height: 50px;
                    ">
                </div>
 
            </div>
            <!-- Status -->
            <div class="row AreaDetail">
                <div class="BlockSubject">Status</div>
                <div class="BlockColon">:</div>
                <div class="BlockInputCode">
                    <div class="IconStatus"><b>Minimum</b></div>
                    <img src="../../assets/icon/btn-alert-icon.png" style="display:inline-block; height:29px;margin-bottom:3px;">
                </div>
            </div>
            <!-- Active -->
            <div class="row AreaDetail">
                <div class="BlockSubject">Active</div>
                <div class="BlockColon">:</div>
                <div class="BlockInputCode" style="padding-top:7px;"><Switch></Switch></div>
 
            </div>
            <!-- Consigner -->
            <div class="row AreaDetail">
                <div class="BlockSubject" style="width:120px;">Consigner</div>
                <div class="BlockColon">:</div>
                <div class="BlockSelect">
                    <select
                    name="category"
                    id="category"
                    v-model="category_id"
                    style="background:#717171;height:50px;width:160px;"
                    >
                    <!-- <option
                        v-for="category in categories"
                        :key="category.id"
                        :value="category.id"
                    >
                        {{ category.name }}
                    </option> -->
                    </select>
                </div>
                <div class="AddButton" >+</div>
            </div>
            
        </div>

    </div>
    <!-- Area 1 -->
    <div class="row Area QtyBlock">
        <div class="col-6 w-100">
            <!-- Qty -->
            <div class="row QtyHalf">
                <div class="BlockSubjectQty">Qty</div>
                <div class="BlockColonQty">:</div>
                <div class="BlockInputQty"><input type="text" 
                    style="background: #717171;
                    border-radius: 10px;
                    width: 220px;
                    height: 50px;">
                </div>
            </div>
            <!-- Unit -->
            <div class="row QtyHalf">
                <div class="BlockSubjectQty">Unit</div>
                <div class="BlockColonQty">:</div>
                <div class="BlockSelect">
                    <select
                    name="category"
                    id="category"
                    v-model="category_id"
                    style="background:#717171;height:50px;width:220px;"
                    >
                    <!-- <option
                        v-for="category in categories"
                        :key="category.id"
                        :value="category.id"
                    >
                        {{ category.name }}
                    </option> -->
                    </select>
                </div>
            </div>
        </div>
        <!-- Area QTY Max-Min -->
        <div class="col-6 w-100">
            <!-- Qty Min -->
            <div class="row QtyHalf">
                <div class="BlockSubjectQtyM">Qty Min</div>
                <div class="BlockColonQty">:</div>
                <div class="BlockInputQty"><input type="text" 
                    style="background: #717171;
                    border-radius: 10px;
                    width: 170px;
                    height: 50px;">
                </div>
            </div>
            <!-- Qty Max -->
            <div class="row QtyHalf">
                <div class="BlockSubjectQtyM">Qty Max</div>
                <div class="BlockColonQty">:</div>
                <div class="BlockInputQty"><input type="text" 
                    style="background: #717171;
                    border-radius: 10px;
                    width: 170px;
                    height: 50px;">
                </div>
            </div>
        </div>
    </div>

    <!-- Area 2 -->
    <div class="row Area QtyBlock">
        <div class="col-6 w-100">
            <!-- Price -->
            <div class="row QtyHalf">
                <div class="BlockSubjectQty">Price</div>
                <div class="BlockColonQty">:</div>
                <div class="BlockInputQty"><input type="text" 
                    style="background: #717171;
                    border-radius: 10px;
                    width: 220px;
                    height: 50px;">
                </div>
            </div>
            <!-- Type Topping -->
            <div class="row QtyHalf">
                <div class="BlockSubjectQty" style="width:165px;">Type Topping</div>
                <div class="BlockColonQty">:</div>
                <div class="BlockSelect">
                    <select
                    name="category"
                    id="category"
                    v-model="category_id"
                    style="background:#717171;height:50px;width:115px;"
                    >
                    <!-- <option
                        v-for="category in categories"
                        :key="category.id"
                        :value="category.id"
                    >
                        {{ category.name }}
                    </option> -->
                    </select>
                </div>
            </div>
        </div>
        <!-- Area Share , Stock -->
        <div class="col-6 w-100">
            <!-- Share % -->
            <div class="row QtyHalf">
                <div class="BlockSubjectQtyM">Share(%)</div>
                <div class="BlockColonQty">:</div>
                <div class="BlockInputQty"><input type="text" 
                    style="background: #717171;
                    border-radius: 10px;
                    width: 170px;
                    height: 50px;">
                </div>
            </div>
            <!-- Stock -->
            <div class="row QtyHalf">
                <div class="BlockSubjectQtyM">Stock</div>
                <div class="BlockColonQty">:</div>
                <div class="BlockSelect">
                    <select
                    name="category"
                    id="category"
                    v-model="category_id"
                    style="background:#717171;height:50px;width:170px;"
                    >
                    <!-- <option
                        v-for="category in categories"
                        :key="category.id"
                        :value="category.id"
                    >
                        {{ category.name }}
                    </option> -->
                    </select>
                </div>
            </div>
        </div>
    </div>
    
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";


export default {
  name: "NewConsignment",
  components: {
    NavApp,
    Switch,

  },
  data() {
    return {
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
    border-radius: 10px;
    background-color: #303344;
    margin-left: 24px;
    margin-right: 24px;
    margin-top: 20px;
    margin-bottom: 20px;
    
}
.Header {
    color:#fff;
    font-size: 48px;
    text-align: center;
    position: relative;
    height: 70px;
    margin-left: 24px;
    margin-right: 24px;
    margin-bottom: 50px;  
}

.Name {
    padding-top: 10px;
    line-height: 65px;
    height: 90px;
}
.Img {
    padding: 5px;
}

.EditImg {
    color: #000000;
    position: absolute;
    text-align: right;
    font-size: 18px;
    padding-right: 8px;
    border-radius: 5px;
    top: 205px;
    left: 25px;
    height: 30px;
    width: 80px;
    line-height: 30px;
    background-color: #C4C4C4;
}

.RedeemImg {
    width: 253px;
    height: 260px;
    position: relative;
    font-size: 23px;
    text-align: center;
    padding:0px;
    margin-left:12px;
    border-radius: 25px;

}
.RedeemPoint {
    width: 243px;
    height: 50px;
    background-color: #EA7C69;
    position: relative;
    font-size: 26px;
    text-align: center;
    padding:2px;
    margin-left:12px;
    border-radius: 10px;
    line-height: 55px;
}

.AreaDetail {
    color: #fff;
    width:380px;
    height: 50px;
    padding-left:10px ;
    font-size: 30px;
    line-height: 40px;
    margin-bottom: 20px;

}

.BlockSubject {
    
    display: inline-block;
    width: 100px;
    text-align: left;
    

}

.BlockSubjectQty {
    
    display: inline-block;
    width: 60px;
    text-align: left;
    padding: 0px;
    margin-left:15px;
    

}

.BlockSubjectQtyM {
    
    display: inline-block;
    width: 110px;
    height: 50px;
    text-align: left;
    padding: 0px;
    margin-left:10px;
    

}

.BlockColonQty {

    display: inline-block;
    margin: 0px;
    
}
.BlockColon {

    display: inline-block;
    margin-left:8px;
    margin-right:8px;
    
}

.BlockInputCode {
    width: 243px;
    height: 50px;
    position: relative;
    font-size: 23px;
    padding:0px;
    border-radius: 10px;
    line-height: 45px;
    text-align:left;
    display: inline-block;
}

.BlockInputQty {
    width: 100%;
    height: 50px;
    position: relative;
    font-size: 23px;
    padding:0px;
    border-radius: 10px;
    line-height: 45px;
    text-align:left;
    display: inline-block;
}

.BlockSelect {
    width: 160px;
    height: 50px;
    position: relative;
    font-size: 23px;
    padding:0px;
    border-radius: 10px;
    line-height: 45px;
    text-align:left;
    display: inline-block;
}

.IconStatus {
    color: black;
    background-color: #FFB572;
    height: 35px;
    width: 120px;
    font-size: 22px;
    border-radius: 10px;
    text-align: center;
    line-height: 33px;
    display:inline-block;
    margin-right: 10px;

}

.AddButton {
    display:inline-block;
    line-height: 27px;
    color: #50D1AA;
    border-radius: 10px;
    border: 2px solid #50D1AA;
    height: 40px;
    width: 40px;
    margin-left:10px;
    margin-top:5.5px;
    padding: 0px;

}

.QtyBlock {
    height: 180px;
    color: #fff;
    font-size: 28px;
    padding-top: 20px;

}

.QtyHalf {
    margin-top: 5px;
    margin-bottom: 25px;
}
</style>