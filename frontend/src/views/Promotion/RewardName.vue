<template>
    <div>
        <nav-app :url_name="'AllReward'">{{ $store.state.promotion.reward_detail.reward }}</nav-app>

        <!-- AreaBlockItem -->
        <div class="table-item"
            style="margin-left: 24px;
            margin-right: 24px;
            margin-top: 20px;
            margin-bottom: 20px;
            border-radius:20px;
            height: 820px;
            width: 672px;">

            <!-- Select Bar -->
            <div class="row BlockItem">
                
                <div class="col-6 w-100">
                    <input type="text" style="background:#717171; height:50px; width:282px; font-size: 28px;" readonly value="Pre-order" v-if="$store.state.promotion.reward_detail.is_per_order">
                    <input type="text" style="background:#717171; height:50px; width:282px; font-size: 28px;" readonly value="รับสินค้าเลย" v-else>
                </div>
                <div class="col-6 w-100" style="padding:0px;">
                    <div class="RedeemItem"><b>Redeem</b></div>
                </div>
            </div>
            <div class="row BlockImg">
                
                <div class="col-6 w-100">
                <img :src="require(`../../../../backend${$store.state.promotion.reward_detail.img}`)" alt="" style="width:282px;height: 298px; border-radius: 20px;">
                </div>
                <div class="col-6 w-100 BlockRedeemPoint" style="padding:0px;">
                    <div class="RedeemPointItem">
                        <dir style="height:60px;margin:0px;padding:0px;line-height:55px;" @click="popup_status = true"><b>Redeem Point</b></dir>
                        <div class="table-item BlockPoint"><b>{{ $store.state.promotion.reward_detail.point }}</b></div>
                        <dir style="height:60px;margin:0px;padding:0px;line-height:55px;font-size:28px;">Value {{ $store.state.promotion.reward_detail.value }}B.</dir>
                    </div>
                </div>
            </div>
            <div class="row AreaDescription">
                <div  class="col-12 w-100" style="height:50px;"><b>Description :</b></div>
                <div  class="col-12 w-100 BlockDescription" >
                    {{ $store.state.promotion.reward_detail.description }}
                </div>

            </div>
        
        
        </div>
        <!-- Popup -->
        <div class="AreaPopup" v-if="popup_status">
            <div class="HeadPopup" style="left:20px">
                <b>Redeem</b>
                <img src="../../assets/img/btn-close.png" alt="" style="right:-176px;position:relative;" @click="popup_status = false">
            </div>
            <div class="table-item AreaRedeemPopup">
                <div class="row">
                    <div class="col-6 StatusBlock"><b>Confirm Redeem</b></div>
                    <div class="col-6 RedeemNamePhone" style="margin-bottom:5px;">ป้าวราภรณ์แสงโสภา</div>
                </div>
                <div class="row" style="height:250px;padding-top:10px;">
                    <div class="col-6 RedeemImg" style="background-color: #717171;"><img src="../../assets/img/BG.png" style="height:245px;width:243px;"></div>
                    <div class="col-6 RedeemImg">
                        <div class="RedeemNamePhone" style="margin:0px;margin-bottom:15px;">095-161-7171</div>
                        <div class="RedeemNameReward" style="margin:0px;margin-bottom:15px"><b>Specail Set1</b></div>
                        <div class="row RedeemPoint" style="margin:0px;margin-bottom:15px;">
                            <div class="col-6 w-100 DetailPoint" style="background-color:#303344;"><b>200</b></div>
                            <div class="col-6 w-100 DetailPoint"><b>Point</b></div>
                            
                        </div>
                        <div class="RedeemNamePhone" style="margin:0px;">
                            <select
                            name="category"
                            id="category"
                            v-model="category_id"
                            style="background:#717171;height:50px;width:233px;"
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
                <!-- Sign Here -->
                <div class="AreaSign">Sign Here
                    <img src="../../assets/icon/eraser.png" alt="" style="position:absolute;height:50px;padding:0px;right:5px;">
                </div>
            </div>



        </div>
        <p style="font-size: 50px; color: white;" @click="save()">Save</p>
        <div class="flex-row">
            <div class="wrapper">
                <canvas id="signature-pad" width="400" height="200"></canvas>
            </div>
            <div class="clear-btn">
                <button id="clear"><span>Clear</span></button>
            </div>
        </div>
    </div>

</template>

<script>
export default {  
  name: "RewardName",
  components : {
      NavApp,
      SearchBar
      
  },
  mounted() {
      this.signature_pad()
  },
  data() {
      return{
        popup_status: false,
        reward_status: '',
      }
  },
  methods: {
      signature_pad() {
          var canvas = document.getElementById("signature-pad")
          function resizeCanvas() {
             var ratio = Math.max(window.devicePixelRatio || 1, 1)
            canvas.width = canvas.offsetWidth * ratio
            canvas.height = canvas.offsetHeight * ratio
            canvas.getContext("2d").scale(ratio, ratio) 
          }
          window.onresize = resizeCanvas
          resizeCanvas()
          
          var signaturePad = new SignaturePad(canvas, {
              backgroundColor: 'rgb(250,250,250)'
          })
          document.getElementById("clear").addEventListener('click',function(){
              signaturePad.clear()
          })
          console.log(canvas, 'canvas')
      },
      save() {
        var canvas = document.getElementById("signature-pad")
        canvas.toBlob(blob => {
            const data = new FormData();
            data.append("img", blob, 'filename.png')

            console.log(data, "data")
        })
      },
      search(val) {
          console.log(val)
      }
  },

};

import NavApp from "../../components/main_component/NavApp.vue"
import SearchBar from "../../components/materials/SearchBar.vue"

</script>

<style scoped>
#clear {
    height: 100%;
    background: green;
    border: 1px solid transparent;
    color: white;
    font-weight: 600;
}
canvas#signature-pad {
    background: white;
    width: 100%;
    height: 100%;
    cursor: crosshair;
}
.wrapper {
    border: 1px solid black;
    border-right: 0;
}
.flex-row {
    display: flex;
}

img {
    border-radius: 20px;
}

.BlockItem {
    width: 672px;
    position: relative;
    font-size: 23px;
    text-align: center;
    padding:0px;
    margin:0px;
    top: 30px;
}

.RedeemItem {
    color: #EA7C69;
    font-size: 30px;
    height: 50px;
    width: 308px;
    padding: 10px;
    border-radius: 10px;
    border: 2px solid #EA7C69;
    line-height: 20px;
    margin-left:0px;
    margin-right:20px;
}

.BlockImg {
    width: 672px;
    position: relative;
    font-size: 23px;
    text-align: center;
    padding:0px;
    margin:0px;
    top: 60px;
    
}

.RedeemPointItem {
    color: #fff;
    font-size: 30px;
    height: 298px;
    width: 308px;
    padding-left:  2px;
    padding-right: 2px;
    border-radius: 30px;
    background-color:  #EA7C69;
    line-height: 20px;
    margin-left:0px;
    margin-right:20px;
}

.BlockPoint {
    height: 178px;
    margin: 0px;
    border-radius: 0px;
    font-size: 106px;
    line-height:160px;

}

.AreaDescription {
    margin: 20px;
    color: aliceblue;
    width: 615px;
    position: relative;
    font-size: 30px;
    text-align: left;
    padding:0px;
    margin-left:27px;
    top: 70px;

}

.BlockDescription {
    width: 100%;
    height: 305px;
    border-radius: 20px;
    position: relative;
    font-size: 24px;
    text-align: left;
    padding:0px;
    margin-left: 14px;
}

.AreaPopup {
    color: #fff;
    position:absolute;
    border-radius: 20px;
    width: 590px;
    height: 586px;
    background-color: #252836;
    top: 140px;
    left: 65px;
}

.HeadPopup {
    color: #fff;
    width: 590px;
    position: relative;
    font-size: 37px;
    text-align: center;
    padding:0px;
    margin:0px;
}

.AreaRedeemPopup {
    margin-left:20px;
    margin-right:20px;
    margin-bottom:20px;
    width: 550px;
    height: 85%;
    padding: 20px;

}

.RedeemNamePhone {
    width: 243px;
    height: 50px;
    background-color: #717171;
    position: relative;
    font-size: 23px;
    padding:0px;
    padding-left:10px;
    margin-left:12px;
    border-radius: 10px;
    line-height: 45px;
    text-align:left;
}

.RedeemImg {
    width: 243px;
    height: 100%;
    position: relative;
    font-size: 23px;
    text-align: center;
    padding:0px;
    margin-left:12px;
    border-radius: 25px;

}

.StatusBlock {
    color: #50D1AA;
    width: 243px;
    height: 50px;
    border-radius: 20px;
    border: 3px solid #50D1AA;
    width: 243px;
    height: 50px;
    position: relative;
    font-size: 23px;
    text-align: center;
    padding:0px;
    margin-left:12px;
}

.RedeemNameReward {
    width: 243px;
    height: 50px;
    position: relative;
    font-size: 30px;
    padding:0px;
    margin-left:12px;
    border-radius: 10px;
    line-height: 45px;
    padding-left:10px;
    text-align:left;
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
    line-height: 45px;
}

.DetailPoint {

    height: 100%;
    padding:0px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
}

.AreaSign {

    position: relative;
    text-align: left;
    background-color: #717171;
    border-radius: 15px;
    padding-left: 12px;
    padding-top: 5px;
    width: 510px;
    height: 130px;
    left: 12px;
    top: 20px;
    font-size: 28px;
}
</style>