<template>
  <div>

    <div class="row Header">
        <div class="col-1 w-100" style="padding-left:0px;"><img src="../../assets/icon/save.png" style="height:60px"></div>
        <div class="col-10 w-100" style="line-height: 105px;"><b>New Consignment</b></div>
        <div class="col-1 w-100" style="padding-right:0px;"><img src="../../assets/img/btn-close.png" style="height:60px"></div>
    </div>
    <!-- CustommerPhone Block -->
    <div class="row Area Name">
      <div class="BlockName">Name :</div>
      <div class="BlockInputName">
        <input type="text" v-model="input_customer" 
        style="background: #717171;
        border-radius: 10px;
        width: 585px;
        height: 60px;
        margin-top: 15px;
        font-size: 32px;" />
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
    <div class="row Area Img">
        <!-- Img Block -->
        <div class="RedeemImg" style="background-color: #717171;width: 293px;left:0px;">
            <div class="EditImg">
                <img src="../../assets/icon/el_camera.png" style="position:relative;top:-2.9px;left:-5px;">
                <b>Edit</b>
            </div>
            <img src="" style="height:300px;width:293px;position: absolute;left:0px; border-radius:10%">
        </div>
        <!-- Detail Block -->
        <div class="RedeemImg" style="margin-left:10px; width:100%;padding-right:20px">
            <!-- Code -->
            <div class="row AreaDetail">
                <div class="BlockSubject">Code</div>
                <div class="BlockColon">:</div>
                <div class="BlockInputCode"><input type="text" 
                    style="background: #717171;
                    border-radius: 10px;
                    width: 280px;
                    height: 60px;
                    font-size: 38px;
                    ">
                </div>
 
            </div>
            <!-- Status -->
            <div class="row AreaDetail">
                <div class="BlockSubject">Status</div>
                <div class="BlockColon">:</div>
                <div class="BlockInputCode" style="line-height: 50px;">
                    <div class="IconStatus"><b>Minimum</b></div>
                    <img src="../../assets/icon/btn-alert-icon.png" style="display:inline-block; height:35px;margin-bottom:3px;">
                </div>
            </div>
            <!-- Active -->
            <div class="row AreaDetail">
                <div class="BlockSubject">Active</div>
                <div class="BlockColon">:</div>
                <div class="BlockInputCode" style="padding-top:8px;"><Switch style="width:65px;"></Switch></div>
 
            </div>
            <!-- Consigner -->
            <div class="row AreaDetail">
                <div class="BlockSubject" style="width:150px;">Consigner</div>
                <div class="BlockColon">:</div>
                <div class="BlockSelect">
                    <select
                    name="category"
                    id="category"
                    v-model="category_id"
                    style="background:#717171;height:55px;width:170px;"
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
                    width: 255px;
                    height: 60px;">
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
                    style="background:#717171;height:60px;width:255px;"
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
                    width: 185px;
                    height: 60px;
                    font-size: 32px;">
                </div>
            </div>
            <!-- Qty Max -->
            <div class="row QtyHalf">
                <div class="BlockSubjectQtyM">Qty Max</div>
                <div class="BlockColonQty">:</div>
                <div class="BlockInputQty"><input type="text" 
                    style="background: #717171;
                    border-radius: 10px;
                    width: 185px;
                    height: 60px;
                    font-size: 32px;">
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
                    width: 255px;
                    height: 60px;
                    font-size: 32px;">
                </div>
            </div>
            <!-- Type Topping -->
            <div class="row QtyHalf">
                <div class="BlockSubjectQty" style="width:196px;">Type Topping</div>
                <div class="BlockColonQty">:</div>
                <div class="BlockSelect">
                    <select
                    name="category"
                    id="category"
                    v-model="category_id"
                    style="background:#717171;height:60px;width:134px;"
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
                    width: 185px;
                    height: 60px;
                    font-size: 32px;">
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
                    style="background:#717171;height:60px;width:185px;"
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
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import SavePopup from "../../components/main_component/SavePopup.vue"


export default {
  name: "NewConsignment",
  components: {
    NavApp,
    Switch,
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
    border-radius: 10px;
    background-color: #303344;
    margin-left: 24px;
    margin-right: 24px;
    margin-top: 20px;
    margin-bottom: 20px;
    
}
.Header {
    color:#fff;
    font-size: 62px;
    text-align: center;
    position: relative;
    height: 90px;
    margin-left: 24px;
    margin-right: 24px;
    margin-bottom: 50px;  
    margin-top: 10px;  
}

.Name {
    padding-top: 10px;
    line-height: 80px;
    height: 110px;
}

.BlockName {
    color: #ffffff;
    font-size: 38px;
    padding: 0px;
    text-align: right;
    display: inline-block;
    width: 145px;
    
}

.BlockInputName {
    width: 535px;
    height: 60px;
    display: inline-block;

}

.Img {
    height:360px;
    padding: 20px;
    padding-top:30px;
    padding-bottom:30px;

}

.EditImg {
    color: #000000;
    position: absolute;
    text-align: right;
    font-size: 18px;
    padding-right: 8px;
    border-radius: 5px;
    top: 235px;
    left: 30px;
    height: 30px;
    width: 80px;
    line-height: 30px;
    background-color: #C4C4C4;
}

.RedeemImg {
    height: 300px;
    position: relative;
    font-size: 23px;
    text-align: center;
    padding:0px;
    border-radius: 25px;
    margin:0px;

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
    height: 60px;
    padding-left:10px ;
    font-size: 38px;
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
    width: 75px;
    text-align: left;
    padding: 0px;
    margin-left:15px;
    

}

.BlockSubjectQtyM {
    
    display: inline-block;
    width: 140px;
    height: 60px;
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
    height: 41px;
    width: 120px;
    font-size: 26px;
    border-radius: 10px;
    text-align: center;
    line-height: 35px;
    display:inline-block;
    margin-right: 10px;

}

.AddButton {
    display:inline-block;
    font-size: 45px;
    line-height: 37px;
    color: #50D1AA;
    border-radius: 10px;
    border: 2px solid #50D1AA;
    height: 55px;
    width: 55px;
    margin-left:25px;
    padding: 0px;

}

.QtyBlock {
    height: 220px;
    color: #fff;
    font-size: 34px;
    padding-top: 20px;

}

.QtyHalf {
    margin-top: 15px;
    margin-bottom: 35px;
    height: 60px;
}
</style>